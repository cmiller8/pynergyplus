#!/usr/bin/env python
# encoding: utf-8
"""
IDFObjectCounter.py

Created by Clayton Miller on 2011-05-17.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
import re
import string

def main():
  
  # Define input path for IDF File and Output path for report
  fInIDF = open('in.idf','r')
  
  # Create and IDF Object List and add all lines where the first char is NOT a ' '
  IDFObjectList = []
  Lines = fInIDF.readlines()
  for line in Lines:
    firstchar = line[0]
    if not firstchar.isspace() and not firstchar == '!':
      line = line.replace(',','')
      IDFObjectList.append(line)
      
  # Sort the List and create a dictionary with the number of occurences
  IDFObjectList.sort()
  
  IDFObjects = {}
  for object in IDFObjectList:
    if not object in IDFObjects:
      IDFObjects[object] = 1
    else:
      IDFObjects[object] = IDFObjects[object] + 1
      
  # Prints the dictionary when in.idf is in the same folder 
  for object in IDFObjects:
    print object + str(IDFObjects[object])

if __name__ == '__main__':
  main()

