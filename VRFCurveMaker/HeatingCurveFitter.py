__author__ = 'claytonmiller'

from pylab import *
from scipy.optimize import leastsq
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
from VRFfunctions import *
from VRF_IDFObjectsTemplates import *

#LeastSq R^2 Calc
def calcerror(infodict,xdata):
    ss_err=(infodict['fvec']**2).sum()
    ss_tot=((xdata-xdata.mean())**2).sum()
    rsquared=1-(ss_err/ss_tot)
    return (rsquared)

def plotcurve(X,Y,Z,Z2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X, Y, Z,color='r')
    ax.scatter(X,Y,Z2)
    plt.show()

#Creates EIRFT and CAPFT
def FTCurves(TotalData,RatEnergy):
#Create the CAPFT and EIRFT Curves
#Start by aggregating the IWB, ODB, and CapRatio
    IWB,ODB,CapRatio,PowerRatio=[],[],[],[]
    for measurement in TotalData:
        if measurement[0]==100.0:
            IWB.append(measurement[2])
            ODB.append(measurement[3])
            CapRatio.append(measurement[4]/measurement[1])
            PowerRatio.append(measurement[5]/RatEnergy)

    npIWB=np.array(IWB)
    IWBmax,IWBmin = max(npIWB),min(npIWB)
    npODB=np.array(ODB)
    ODBmax,ODBmin = max(npODB),min(npODB)
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

#    Can Plot to Compare Fit
    EIRPredict = TwoDimBiquadratic(npIWB,npODB,EIRFT)
    plotcurve(npIWB,npODB,npPowerRatio,EIRPredict)

    return CAPFT,EIRFT,CAPFTerr,EIRFTerr,IWBmax,IWBmin,ODBmax,ODBmin

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

#Creates Heating Combination Ratio Correction Factor - Modifies Capacity as a function of CombRatio
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

    #Calc Linear Heating Combination Ratio Correction Factor
    p0=[0,0] # initial guesses
    #Least Square Optimization to find parameters
    CCRCFactor,cov,infodict,mesg,ier = leastsq(residualsOneDimLinear,p0,args=(npCapRatio,npCombRatio),full_output=1)
    CCRCFactorErr = calcerror(infodict,npCapRatio)

    return CCRCFactor,CCRCFactorErr

#Load TotalData Array from Text file output of CellParser.py
TotalData = []
csvreader = csv.reader(file("RXYQ18Heat.xls.csv"),quoting=csv.QUOTE_NONNUMERIC)
for row in csvreader:
    TotalData.append(row)
for row in TotalData[1:]:
    for item in row[1:]:
        item=float(item)
    for item in row[:0]:
        item=int(item)

#Find Heating Capacity Ratio Modifier Function (CAPFT)
# and Energy Input Ratio Modifier Function (EIRFT)
#This script is designed to simplify the process described in:
#https://securedb.fsec.ucf.edu/pub/pub_show_detail?v_pub_id=4588 

#Creating a Hi and Low EIR Curve is required for heating (unlike Heating)
RatedHeatingEnergy = 15.3
CAPFT,EIRFT,CAPFTerr,EIRFTerr,IWBmax,IWBmin,ODBmax,ODBmin = FTCurves(TotalData,RatedHeatingEnergy)

#Convert Numpy arrays back to lists for output
CAPFTlist = (CAPFT.tolist())
EIRFTlist = (EIRFT.tolist())

#Find Heating Energy Input Ratio Modifier Functions -
#Hi = CombRatio >100, Lo = CombRatio <= 100
RatedIWB = 20
RatedODB = 6

EIRModFTHi,EIRFTHierr,EIRModFTLo,EIRModFTLoerr = EIRModifier(TotalData,RatedIWB,RatedODB,RatedHeatingEnergy)

#print EIRModFT,EIRFTerr,EIRModFTLo,EIRModFTLoerr

EIRModFTHi = (EIRModFTHi.tolist())
EIRModFTLo = (EIRModFTLo.tolist())

#Find Heating Combination Ratio Correction Factor
RatedCap = 56.5

CCRCFactor, CCRCFactorErr = CCRCF(TotalData,RatedIWB,RatedODB)
#print CCRCFactor, CCRCFactorErr

VRFHeatCapFT = HeatCapModifierFunction(CAPFTlist)
VRFHeatEIRFT = HeatEnergyInputRatioModifierFunction(EIRFTlist)
HeatEIRLowPLR = HeatEnergyInputRatioModifierPartLoadLow(EIRModFTLo)
HeatEIRHiPLR = HeatEnergyInputRatioModifierPartLoadHigh(EIRModFTHi)
HeatingCombCorrFactor = HeatCombinationRatioCorrectionFactor(CCRCFactor)
CPLFFPLR = CPLFFPLR()

#print VRFCoolCapFT
#print EIRCoolCapFT
#print EIRCoolModLowFT
#print EIRCoolModHiFT
#print HeatingCombCorrFactor

#Print Errors
print CAPFTerr, EIRFTerr, EIRModFTLoerr, EIRFTHierr, CCRCFactorErr

CurveObjectFile = open("HeatingCurveObjects.txt","w")
CurveObjectFile.write(VRFHeatCapFT)
CurveObjectFile.write(VRFHeatEIRFT)
CurveObjectFile.write(HeatEIRLowPLR)
CurveObjectFile.write(HeatEIRHiPLR)
CurveObjectFile.write(HeatingCombCorrFactor)









