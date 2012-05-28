__author__ = 'claytonmiller'

import re
from xlrd import open_workbook
import csv

#Pulls Data out of a spreadsheet
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

#Parses Cells
def CellParse(cell):
#Parse the Cells with multiple values and convert to a list of floats
    numbers = re.findall(r"[+-]? *(?:\d+(?:\,\d*)?|\,\d+)(?:[eE][+-]?\d+)?", cell)

    kWnumlist = []
    for kWvalstr in numbers:
        kWnum = float(kWvalstr.replace(",","."))
        kWnumlist.append(kWnum)
    return kWnumlist

Workbookname = 'RXYQ18Heat.xls'

#Open Workbook
book = open_workbook(Workbookname)

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

#Create a txt file with the total data array. This text file is loaded in the CurveFitter script
csvwriter = csv.writer(file(Workbookname+".csv", "w"),quoting=csv.QUOTE_NONNUMERIC)
for row in TotalData:
    csvwriter.writerow(row)

