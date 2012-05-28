__author__ = 'claytonmiller'

import csv
import os
import glob
from xlwt import Workbook

def getRawData(file,book):
    RoomScheduleRaw = csv.reader(open(file, 'rb'), delimiter='\t')
    ScheduleRawData=[]
    PositionX,PositionY = [],[]
    for row in RoomScheduleRaw:
        ScheduleRawData.append([row[2],row[3],row[4]])
        PositionX.append(row[3])
        PositionY.append(row[4])
    #print ScheduleRawData

    ScheduleRawData.pop(0)

    PositionX.pop(0)
    PositionX.sort()
    PositionX=list(set(PositionX))
    #print PositionX
    #print len(PositionX)

    PositionY.pop(0)
    PositionY.sort()
    PositionY=list(set(PositionY))

    ProcessedData=[]
    for row in ScheduleRawData:
        ProcessedData.append([PositionX.index(row[1]),PositionY.index(row[2]),row[0]])

    n=0
    CSVoutput=[]
    while n <= len(PositionY):
        rowlist=[]
        for row in ProcessedData:
            if row[1]==n:
                rowlist.append(row)
        rowlist.sort()
        CSVrow=[]
        for item in rowlist:
            CSVrow.append(item[2])
        CSVoutput.append(CSVrow)
        n+=1

    shortfilename = file[:-15]
    sheet = book.add_sheet(shortfilename)
    for row_index, row_contents in enumerate(CSVoutput):
        for column_index, cell_value in enumerate(row_contents):
            sheet.write(row_index, column_index, cell_value)

    #for row in CSVoutput:
    #    for item in row:
    #        print item
    #outs = csv.writer(open("10thFloorScheduleRefined.csv", "wb"))
    #for row in CSVoutput:
    #    outs.writerow(row)

path = '/Users/claytonmiller/Dropbox/05-CODE/autocadscripts/RoomScheduleExtraction'
book = Workbook(encoding='utf-8')
for infile in glob.glob( os.path.join(path, '*.txt') ):
    head,tail= os.path.split(infile)
    print tail
    getRawData(tail,book)

book.save('AllFloorplansSchedules.xls')


