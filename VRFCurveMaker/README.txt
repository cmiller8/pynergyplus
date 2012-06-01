This set of scripts automates the process of creating VRF System Objects. The input is the PDF files from Daikin which
are translated into excel using http://www.pdftoexcelonline.com/

The main steps:
1) Unpack the excel files into csv using the 'CellParser.py' script
2) Create the CoolingCurveObjects.txt and HeatingCurveObjects.txt using the CoolingCurveFitter.py and
HeatingCurveFitter.py scripts
3) Create the VRF Objects (CentralVRFObjects.txt) using the VRFIDFCreator.py
4) OutputOption.txt contains the outputs that are desired
5) IDFJoiner.py is then used to tie everything together into one file which can then be renamed to a idf and run in
Energyplus. Spits out "TypicalFloorComplete.txt" 
