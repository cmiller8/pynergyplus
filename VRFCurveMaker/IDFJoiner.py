__author__ = 'claytonmiller'

#Splice together the Cooling and Heating Curves and the VRFObjects into the Base IDF File

content = " "
fullidffile = content + '\n' + open("TypicalFloorwithVRF-Base.txt").read() + open("CentralVRFObjects.txt").read() + \
              open("HeatingCurveObjects.txt").read() + open("CoolingCurveObjects.txt").read()

open('TypicalFloorComplete.txt','wb').write(fullidffile)
  