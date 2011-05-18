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
#  fInIDD = open('Energy+.idd','r')

#calls readlines which puts every line of the IDD into a list
#  Lines = fInIDD.readlines()
#  for line in Lines:
#    print line,
  
  IDFObjectList = []

  Lines = fInIDF.readlines()
  for line in Lines:
    firstchar = line[0]
    if not firstchar.isspace() and not firstchar == '!':
      IDFObjectList.append(line)
  
  IDFObjectList.sort()
  IDFObjects = {}
  



if __name__ == '__main__':
  main()

