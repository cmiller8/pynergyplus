__author__ = 'claytonmiller'

from pylab import *
from scipy.optimize import leastsq
from xlrd import open_workbook
import re
import matplotlib.pyplot as plt
from VRFfunctions import *

def GetData(sheetind):

    sheet = book.sheet_by_index(sheetind)

    # Retrieve Combination % from First Column
    CombPerList = []
    for row in sheet.col(0):
        if type(row.value) is float:
            CombPerList.append(row.value)

    # Retrieve Capacity Ind from First Column
    CapIndList = []
    for row in sheet.col(1):
        if type(row.value) is float:
            CapIndList.append(row.value/100)

    # Retrieve the Interior Web Bulb Temps (IWBdegC) from Line 2
    IWBdegC = []
    for col in sheet.row(1):
        if type(col.value) is float:
            IWBdegC.append(col.value/10)

    # Retrieve ODB from Col
    ODB = sheet.cell(4,2).value
    ODBlist = CellParse(ODB)

    #Column numbers that have 'TC' kW values
    TCColumns = [3,5,7,9,11,13,15]
    PIColumns = [4,6,8,10,12,14,16]
    DataRows = [4,5,6,7]

    DataMatrix = []

    DataMatrixItemlist = []
    TClist = []
    PIlist = []
    for row in DataRows:
        for col in TCColumns:
            RowInd = DataRows.index(row)
            ColInd = TCColumns.index(col)
            TCCell = sheet.cell(row,col).value
            PICell = sheet.cell(row,col+1).value

            TClist = CellParse(TCCell)
            PIlist = CellParse(PICell)

            TCind = 0
            while TCind < len(TClist):
                DataMatrixItemlist = [CombPerList[RowInd],CapIndList[RowInd],IWBdegC[ColInd],ODBlist[TCind],
                                      TClist[TCind],PIlist[TCind]]
                DataMatrix.append(DataMatrixItemlist)
                TCind += 1
    return DataMatrix

#Pulls Data out of a spreadsheet
def calcerror(infodict,xdata):
    ss_err=(infodict['fvec']**2).sum()
    ss_tot=((xdata-xdata.mean())**2).sum()
    rsquared=1-(ss_err/ss_tot)
    return (rsquared)

#LeastSq R^2 Calc
def FTCurves(TotalData,RatEnergy):
#Create the CAPFT and EIRFT Curves
#Start by aggregating the IWB, ODB, and CapRatio
    IWB,ODB,CapRatio,PowerRatio=[],[],[],[]
    for measurement in TotalData:
        if measurement[0] == 100.0:
            IWB.append(measurement[2])
            ODB.append(measurement[3])
            CapRatio.append(measurement[4]/measurement[1])
            PowerRatio.append(measurement[5]/RatEnergy)

    npIWB=np.array(IWB)
    npODB=np.array(ODB)
    npCapRatio=np.array(CapRatio)
    npPowerRatio=np.array(PowerRatio)
    #    print npPowerRatio
    #    print npCapRatio

    p0=[0,0,0,0,0,0] # initial guesses

    #Least Square Optimization to find parameters
    CAPFT,cov,infodict,mesg,ier = leastsq(residualsTwoDimBiquadratic,p0,args=(npCapRatio,npIWB,npODB),full_output=1)
    CAPFTerr = calcerror(infodict,npCapRatio)
    #print CAPFT
    #print CAPFTerr
    EIRFT,cov,infodict,mesg,ier = leastsq(residualsTwoDimBiquadratic,p0,args=(npPowerRatio,npIWB,npODB),full_output=1)
    #print EIRFT
    EIRFTerr = calcerror(infodict,npPowerRatio)
    #print EIRFTerr

    #Can Plot to Compare Fit
    #    EIRPredict = FT(npIWB,npODB,EIRFT)
    #    plotcurve(npIWB,npODB,npPowerRatio,EIRPredict)

    return CAPFT,EIRFT,CAPFTerr,EIRFTerr

#Creates EIRFT and CAPFT
def CellParse(cell):
#Parse the Cells with multiple values and convert to a list of floats
    numbers = re.findall(r"[+-]? *(?:\d+(?:\,\d*)?|\,\d+)(?:[eE][+-]?\d+)?", cell)

    kWnumlist = []
    for kWvalstr in numbers:
        kWnum = float(kWvalstr.replace(",","."))
        kWnumlist.append(kWnum)
    return kWnumlist

#Creates EIRModFunctions - Modifies EIRRatio as a function of CombRatio
def EIRModifier(TotalData,RatedIWB,RatedODB,RatEnergy):
    CombRatioHi,CapRatioHi,PowerRatioHi=[],[],[]
    CombRatioLo,CapRatioLo,PowerRatioLo=[],[],[]
    for measurement in TotalData:
        if measurement[2] == RatedIWB and measurement[3] == RatedODB:
            if measurement[0] > 100.0:
                CapRatioHi.append(measurement[4]/measurement[1])
                PowerRatioHi.append(measurement[5]/RatEnergy)
                CombRatioHi.append(measurement[0])
            elif measurement[0]<= 100.0:
                CapRatioLo.append(measurement[4]/measurement[1])
                PowerRatioLo.append(measurement[5]/RatEnergy)
                CombRatioLo.append(measurement[0])

    #print CapRatio,PowerRatio,CombRatio

    npCombRatioHi = np.array(CombRatioHi)
    npPowerRatioHi = np.array(PowerRatioHi)
    npCombRatioLo = np.array(CombRatioLo)
    npPowerRatioLo = np.array(PowerRatioLo)

    #Calc EIRHiModFunction
    p0=[0,0,0] # initial guesses
    #Least Square Optimization to find parameters
    EIRModFTHi,cov,infodict,mesg,ier = leastsq(residualsOneDimQuadratic,p0,
                                             args=(npPowerRatioHi,npCombRatioHi),full_output=1)
    EIRModFTHierr = calcerror(infodict,npPowerRatioHi)
    #print EIRModFT
    #print EIRModFTerr

     #Calc EIRHiModFunction
    p0=[0,0,0,0] # initial guesses
    #Least Square Optimization to find parameters
    EIRModFTLo,cov,infodict,mesg,ier = leastsq(residualsOneDimCubic,p0,
                                             args=(npPowerRatioLo,npCombRatioLo),full_output=1)
    EIRModFTLoerr = calcerror(infodict,npPowerRatioLo)
    #print EIRModFT
    #print EIRModFTerr

    return EIRModFTHi,EIRModFTHierr,EIRModFTLo,EIRModFTLoerr

#Creates Cooling Combination Ratio Correction Factor - Modifies Capacity as a function of CombRatio
#Only applies to Comb Ratios above 100%
def CCRCF(TotalData,RatedIWB,RatedODB):
    CapRatio,CombRatio=[],[]
    CombDivisor = float(100)
    for measurement in TotalData:
        if measurement[2] == RatedIWB and measurement[3] == RatedODB and measurement[0] > 100:
            CombRatio.append(measurement[0]/CombDivisor)
            CapRatio.append(measurement[4]/measurement[1])

    npCapRatio=np.array(CapRatio)
    npCombRatio=np.array(CombRatio)

    #Calc Linear Cooling Combination Ratio Correction Factor
    p0=[0,0] # initial guesses
    #Least Square Optimization to find parameters
    CCRCFactor,cov,infodict,mesg,ier = leastsq(residualsOneDimLinear,p0,args=(npCapRatio,npCombRatio),full_output=1)
    CCRCFactorErr = calcerror(infodict,npCapRatio)

    return CCRCFactor,CCRCFactorErr

def plotcurve(X,Y,Z,Z2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X, Y, Z)
    ax.scatter(X,Y,Z2)
    plt.show()

#Open Workbook
book = open_workbook('RXYQ18Cool.xls')

TotalData = []
TotalData.append(['CombPer','Cap','IWB','ODB','TotCap','Power'])

SheetData = []
sheetcount = 0

#print book.nsheets

#Create array with all data from sheet
#Excel sheets in the example files are created by uploading the Daikin Performance Data PDF
#to http://www.pdftoexcelonline.com/ The excel file is parsed and laoded in to a python list
while book.nsheets > sheetcount:
    SheetData = GetData(sheetcount)
    for row in SheetData:
        TotalData.append(row)
    sheetcount += 1

#Find Cooling Cooling Capacity Ratio Modifier Function (CAPFT)
# and Energy Input Ratio Modifier Function (EIRFT)
#This script is designed to simplify the process described in:
#https://securedb.fsec.ucf.edu/pub/pub_show_detail?v_pub_id=4588 by neglecting to created a High AND Low
#Performance curves.
RatedCoolingEnergy = 16.2
CAPFT,EIRFT,CAPFTerr,EIRFTerr = FTCurves(TotalData,RatedCoolingEnergy)
print CAPFT,EIRFT,CAPFTerr,EIRFTerr

#Find Cooling Energy Input Ratio Modifier Functions -
#Hi = CombRatio >100, Lo = CombRatio <= 100
RatedIWB = 19
RatedODB = 35

EIRModFT,EIRFTerr,EIRModFTLo,EIRModFTLoerr = EIRModifier(TotalData,RatedIWB,RatedODB,RatedCoolingEnergy)

print EIRModFT,EIRFTerr,EIRModFTLo,EIRModFTLoerr

#Find Cooling Combination Ratio Correction Factor
RatedCap = 49

CCRCFactor, CCRCFactorErr = CCRCF(TotalData,RatedIWB,RatedODB)
print CCRCFactor, CCRCFactorErr










