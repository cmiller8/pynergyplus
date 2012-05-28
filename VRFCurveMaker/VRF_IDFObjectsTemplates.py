__author__ = 'claytonmiller'

def CoolingCapModifierFunction(CoeffArray):
    return "  Curve:Biquadratic,\n\
    VRFCoolCapFT,               !- Name\n\
    " + str(CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str(CoeffArray[1]) + ",             !- Coefficient2 x\n\
    " + str(CoeffArray[2]) + ",             !- Coefficient3 x**2\n\
    " + str(CoeffArray[3]) + ",             !- Coefficient3 y\n\
    " + str(CoeffArray[4]) + ",             !- Coefficient5 y**2\n\
    " + str(CoeffArray[5]) + ",             !- Coefficient6 x*y\n\
    15,                      !- Minimum Value of x\n\
    24,                      !- Maximum Value of x\n\
    -5,                      !- Minimum Value of y\n\
    43,                      !- Maximum Value of y\n\
    ,                        !- Minimum Curve Output\n\
    ,                        !- Maximum Curve Output\n\
    Temperature,             !- Input Unit Type for X\n\
    Temperature,             !- Input Unit Type for Y\n\
    Dimensionless;           !- Output Unit Type"

def EnergyInputRatioModifierFunction(CoeffArray):
    return "  Curve:Biquadratic,\n\
    VRFCoolEIRFT,               !- Name\n\
    " + str(CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str(CoeffArray[1]) + ",             !- Coefficient2 x\n\
    " + str(CoeffArray[2]) + ",             !- Coefficient3 x**2\n\
    " + str(CoeffArray[3]) + ",             !- Coefficient3 y\n\
    " + str(CoeffArray[4]) + ",             !- Coefficient5 y**2\n\
    " + str(CoeffArray[5]) + ",             !- Coefficient6 x*y\n\
    15,                      !- Minimum Value of x\n\
    24,                      !- Maximum Value of x\n\
    -5,                      !- Minimum Value of y\n\
    43,                      !- Maximum Value of y\n\
    ,                        !- Minimum Curve Output\n\
    ,                        !- Maximum Curve Output\n\
    Temperature,             !- Input Unit Type for X\n\
    Temperature,             !- Input Unit Type for Y\n\
    Dimensionless;           !- Output Unit Type"

def EnergyInputRatioModifierPartLoadLow(CoeffArray):
    return "  Curve:Cubic,\n\
    CoolingEIRLowPLR,        !- Name\n\
    " + str(CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str(CoeffArray[1]) + ",             !- Coefficient2 x\n\
    " + str(CoeffArray[2]) + ",             !- Coefficient3 x**2\n\
    " + str(CoeffArray[3]) + ",             !- Coefficient4 x**3\n\
    0,                      !- Minimum Value of x\n\
    1,                      !- Maximum Value of x\n\
    ,                        !- Minimum Curve Output\n\
    ,                        !- Maximum Curve Output\n\
    Temperature,             !- Input Unit Type for X\n\
    Temperature;             !- Output Unit Type"

def EnergyInputRatioModifierPartLoadHigh(CoeffArray):
    return "  Curve:Quadratic,\n\
    CoolingEIRHiPLR,        !- Name\n\
    " + str(CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str(CoeffArray[1]) + ",             !- Coefficient2 x\n\
    " + str(CoeffArray[2]) + ",             !- Coefficient3 x**2\n\
    1.0,                      !- Minimum Value of x\n\
    1.5,                      !- Maximum Value of x\n\
    ,                        !- Minimum Curve Output\n\
    ,                        !- Maximum Curve Output\n\
    Dimensionless,             !- Input Unit Type for X\n\
    Dimensionless;             !- Output Unit Type"

def CoolingCombinationRatioCorrectionFactor(CoeffArray):
    return "  Curve:Linear,\n\
    CoolingCombRatio,        !- Name\n\
    " + str(CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str(CoeffArray[1]) + ",             !- Coefficient2 x\n\
    1.0,                      !- Minimum Value of x\n\
    1.5,                      !- Maximum Value of x\n\
    1.0,                        !- Minimum Curve Output\n\
    1.2,                        !- Maximum Curve Output\n\
    Dimensionless,             !- Input Unit Type for X\n\
    Dimensionless;             !- Output Unit Type"

def CoolingCombinationRatioCorrectionFactor():
  return "  CURVE:QUADRATIC,\n\
  VRFCPLFFPLR,             !- Name\n\
    0.85,                    !- Coefficient1 Constant\n\
    0.15,                    !- Coefficient2 x\n\
    0.0,                     !- Coefficient3 x**2\n\
    0.0,                     !- Minimum Value of x\n\
    1.0,                     !- Maximum Value of x\n\
    0.85,                    !- Minimum Curve Output\n\
    1.0,                     !- Maximum Curve Output\n\
    Dimensionless,           !- Input Unit Type for X\n\
    Dimensionless;           !- Output Unit Type"

def HeatCapModifierFunction(CoeffArray):
    return "  Curve:Biquadratic,\n\
    VRFHeatCapFT,               !- Name\n\
    " + str(CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str(CoeffArray[1]) + ",             !- Coefficient2 x\n\
    " + str(CoeffArray[2]) + ",             !- Coefficient3 x**2\n\
    " + str(CoeffArray[3]) + ",             !- Coefficient3 y\n\
    " + str(CoeffArray[4]) + ",             !- Coefficient5 y**2\n\
    " + str(CoeffArray[5]) + ",             !- Coefficient6 x*y\n\
    15,                      !- Minimum Value of x\n\
    24,                      !- Maximum Value of x\n\
    -5,                      !- Minimum Value of y\n\
    43,                      !- Maximum Value of y\n\
    ,                        !- Minimum Curve Output\n\
    ,                        !- Maximum Curve Output\n\
    Temperature,             !- Input Unit Type for X\n\
    Temperature,             !- Input Unit Type for Y\n\
    Dimensionless;           !- Output Unit Type"

def EnergyInputRatioModifierFunction(CoeffArray):
    return "  Curve:Biquadratic,\n\
    VRFHeatEIRFT,               !- Name\n\
    " + str(CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str(CoeffArray[1]) + ",             !- Coefficient2 x\n\
    " + str(CoeffArray[2]) + ",             !- Coefficient3 x**2\n\
    " + str(CoeffArray[3]) + ",             !- Coefficient3 y\n\
    " + str(CoeffArray[4]) + ",             !- Coefficient5 y**2\n\
    " + str(CoeffArray[5]) + ",             !- Coefficient6 x*y\n\
    15,                      !- Minimum Value of x\n\
    24,                      !- Maximum Value of x\n\
    -5,                      !- Minimum Value of y\n\
    43,                      !- Maximum Value of y\n\
    ,                        !- Minimum Curve Output\n\
    ,                        !- Maximum Curve Output\n\
    Temperature,             !- Input Unit Type for X\n\
    Temperature,             !- Input Unit Type for Y\n\
    Dimensionless;           !- Output Unit Type"

def EnergyInputRatioModifierPartLoadLow(CoeffArray):
    return "  Curve:Cubic,\n\
    HeatEIRLowPLR,        !- Name\n\
    " + str(CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str(CoeffArray[1]) + ",             !- Coefficient2 x\n\
    " + str(CoeffArray[2]) + ",             !- Coefficient3 x**2\n\
    " + str(CoeffArray[3]) + ",             !- Coefficient4 x**3\n\
    0,                      !- Minimum Value of x\n\
    1,                      !- Maximum Value of x\n\
    ,                        !- Minimum Curve Output\n\
    ,                        !- Maximum Curve Output\n\
    Temperature,             !- Input Unit Type for X\n\
    Temperature;             !- Output Unit Type"

def HeatEnergyInputRatioModifierPartLoadHigh(CoeffArray):
    return "  Curve:Quadratic,\n\
    HeatingEIRHiPLR,        !- Name\n\
    " + str(CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str(CoeffArray[1]) + ",             !- Coefficient2 x\n\
    " + str(CoeffArray[2]) + ",             !- Coefficient3 x**2\n\
    1.0,                      !- Minimum Value of x\n\
    1.5,                      !- Maximum Value of x\n\
    ,                        !- Minimum Curve Output\n\
    ,                        !- Maximum Curve Output\n\
    Dimensionless,             !- Input Unit Type for X\n\
    Dimensionless;             !- Output Unit Type"

def HeatingCombinationRatioCorrectionFactor(CoeffArray):
    return "  Curve:Linear,\n\
    HeatingCombRatio,        !- Name\n\
    " + str(CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str(CoeffArray[1]) + ",             !- Coefficient2 x\n\
    1.0,                      !- Minimum Value of x\n\
    1.5,                      !- Maximum Value of x\n\
    1.0,                        !- Minimum Curve Output\n\
    1.2,                        !- Maximum Curve Output\n\
    Dimensionless,             !- Input Unit Type for X\n\
    Dimensionless;             !- Output Unit Type"
