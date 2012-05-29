__author__ = 'claytonmiller'

def CoolingCapModifierFunction(CoeffArray):
    return "  Curve:Biquadratic,\n\
    VRFCoolCapFT,               !- Name\n\
    " + str("%.7G" % CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str("%.7G" % CoeffArray[1]) + ",             !- Coefficient2 x\n\
    " + str("%.7G" % CoeffArray[2]) + ",             !- Coefficient3 x**2\n\
    " + str("%.7G" % CoeffArray[3]) + ",             !- Coefficient3 y\n\
    " + str("%.7G" % CoeffArray[4]) + ",             !- Coefficient5 y**2\n\
    " + str("%.7G" % CoeffArray[5]) + ",             !- Coefficient6 x*y\n\
    15,                      !- Minimum Value of x\n\
    24,                      !- Maximum Value of x\n\
    -5,                      !- Minimum Value of y\n\
    43,                      !- Maximum Value of y\n\
    ,                        !- Minimum Curve Output\n\
    ,                        !- Maximum Curve Output\n\
    Temperature,             !- Input Unit Type for X\n\
    Temperature,             !- Input Unit Type for Y\n\
    Dimensionless;           !- Output Unit Type\n\
      \n"

def EnergyInputRatioModifierFunction(CoeffArray):
    return "  Curve:Biquadratic,\n\
    VRFCoolEIRFT,               !- Name\n\
    " + str("%.7G" % CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str("%.7G" % CoeffArray[1]) + ",             !- Coefficient2 x\n\
    " + str("%.7G" % CoeffArray[2]) + ",             !- Coefficient3 x**2\n\
    " + str("%.7G" % CoeffArray[3]) + ",             !- Coefficient3 y\n\
    " + str("%.7G" % CoeffArray[4]) + ",             !- Coefficient5 y**2\n\
    " + str("%.7G" % CoeffArray[5]) + ",             !- Coefficient6 x*y\n\
    15,                      !- Minimum Value of x\n\
    24,                      !- Maximum Value of x\n\
    -5,                      !- Minimum Value of y\n\
    43,                      !- Maximum Value of y\n\
    ,                        !- Minimum Curve Output\n\
    ,                        !- Maximum Curve Output\n\
    Temperature,             !- Input Unit Type for X\n\
    Temperature,             !- Input Unit Type for Y\n\
    Dimensionless;           !- Output Unit Type\n\
      \n"

def EnergyInputRatioModifierPartLoadLow(CoeffArray):
    return "  Curve:Cubic,\n\
    CoolingEIRLowPLR,        !- Name\n\
    " + str("%.7G" % CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str("%.7G" % CoeffArray[1]) + ",             !- Coefficient2 x\n\
    " + str("%.7G" % CoeffArray[2]) + ",             !- Coefficient3 x**2\n\
    " + str("%.7G" % CoeffArray[3]) + ",             !- Coefficient4 x**3\n\
    0,                      !- Minimum Value of x\n\
    1,                      !- Maximum Value of x\n\
    ,                        !- Minimum Curve Output\n\
    ,                        !- Maximum Curve Output\n\
    Temperature,             !- Input Unit Type for X\n\
    Temperature;             !- Output Unit Type\n\
      \n"

def EnergyInputRatioModifierPartLoadHigh(CoeffArray):
    return "  Curve:Quadratic,\n\
    CoolingEIRHiPLR,        !- Name\n\
    " + str("%.7G" % CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str("%.7G" % CoeffArray[1]) + ",             !- Coefficient2 x\n\
    " + str("%.7G" % CoeffArray[2]) + ",             !- Coefficient3 x**2\n\
    1.0,                      !- Minimum Value of x\n\
    1.5,                      !- Maximum Value of x\n\
    ,                        !- Minimum Curve Output\n\
    ,                        !- Maximum Curve Output\n\
    Dimensionless,             !- Input Unit Type for X\n\
    Dimensionless;             !- Output Unit Type\n\
     \n "

def CoolingCombinationRatioCorrectionFactor(CoeffArray):
    return "  Curve:Linear,\n\
    CoolingCombRatio,        !- Name\n\
    " + str("%.7G" % CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str("%.7G" % CoeffArray[1]) + ",             !- Coefficient2 x\n\
    1.0,                      !- Minimum Value of x\n\
    1.5,                      !- Maximum Value of x\n\
    1.0,                        !- Minimum Curve Output\n\
    1.2,                        !- Maximum Curve Output\n\
    Dimensionless,             !- Input Unit Type for X\n\
    Dimensionless;             !- Output Unit Type\n\
      \n"

def CPLFFPLR():
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
    Dimensionless;           !- Output Unit Type\n\
      \n"

def HeatCapModifierFunction(CoeffArray):
    return "  Curve:Biquadratic,\n\
    VRFHeatCapFT,               !- Name\n\
    " + str("%.7G" % CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str("%.7G" % CoeffArray[1]) + ",             !- Coefficient2 x\n\
    " + str("%.7G" % CoeffArray[2]) + ",             !- Coefficient3 x**2\n\
    " + str("%.7G" % CoeffArray[3]) + ",             !- Coefficient3 y\n\
    " + str("%.7G" % CoeffArray[4]) + ",             !- Coefficient5 y**2\n\
    " + str("%.7G" % CoeffArray[5]) + ",             !- Coefficient6 x*y\n\
    15,                      !- Minimum Value of x\n\
    27,                      !- Maximum Value of x\n\
    -20,                      !- Minimum Value of y\n\
    15,                      !- Maximum Value of y\n\
    ,                        !- Minimum Curve Output\n\
    ,                        !- Maximum Curve Output\n\
    Temperature,             !- Input Unit Type for X\n\
    Temperature,             !- Input Unit Type for Y\n\
    Dimensionless;           !- Output Unit Type\n\
      \n"

def HeatEnergyInputRatioModifierFunction(CoeffArray):
    return "  Curve:Biquadratic,\n\
    VRFHeatEIRFT,               !- Name\n\
    " + str("%.7G" % CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str("%.7G" % CoeffArray[1]) + ",             !- Coefficient2 x\n\
    " + str("%.7G" % CoeffArray[2]) + ",             !- Coefficient3 x**2\n\
    " + str("%.7G" % CoeffArray[3]) + ",             !- Coefficient3 y\n\
    " + str("%.7G" % CoeffArray[4]) + ",             !- Coefficient5 y**2\n\
    " + str("%.7G" % CoeffArray[5]) + ",             !- Coefficient6 x*y\n\
    15,                      !- Minimum Value of x\n\
    27,                      !- Maximum Value of x\n\
    -20,                      !- Minimum Value of y\n\
    15,                      !- Maximum Value of y\n\
    ,                        !- Minimum Curve Output\n\
    ,                        !- Maximum Curve Output\n\
    Temperature,             !- Input Unit Type for X\n\
    Temperature,             !- Input Unit Type for Y\n\
    Dimensionless;           !- Output Unit Type\n\
      \n"

def HeatEnergyInputRatioModifierPartLoadLow(CoeffArray):
    return "  Curve:Cubic,\n\
    HeatEIRLowPLR,        !- Name\n\
    " + str("%.7G" % CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str("%.7G" % CoeffArray[1]) + ",             !- Coefficient2 x\n\
    " + str("%.7G" % CoeffArray[2]) + ",             !- Coefficient3 x**2\n\
    " + str("%.7G" % CoeffArray[3]) + ",             !- Coefficient4 x**3\n\
    0,                      !- Minimum Value of x\n\
    1,                      !- Maximum Value of x\n\
    ,                        !- Minimum Curve Output\n\
    ,                        !- Maximum Curve Output\n\
    Temperature,             !- Input Unit Type for X\n\
    Temperature;             !- Output Unit Type\n\
      \n"

def HeatEnergyInputRatioModifierPartLoadHigh(CoeffArray):
    return "  Curve:Quadratic,\n\
    HeatEIRHiPLR,        !- Name\n\
    " + str("%.7G" % CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str("%.7G" % CoeffArray[1]) + ",             !- Coefficient2 x\n\
    " + str("%.7G" % CoeffArray[2]) + ",             !- Coefficient3 x**2\n\
    1.0,                      !- Minimum Value of x\n\
    1.5,                      !- Maximum Value of x\n\
    ,                        !- Minimum Curve Output\n\
    ,                        !- Maximum Curve Output\n\
    Dimensionless,             !- Input Unit Type for X\n\
    Dimensionless;             !- Output Unit Type\n\
      \n"

def HeatCombinationRatioCorrectionFactor(CoeffArray):
    return "  Curve:Linear,\n\
    HeatingCombRatio,        !- Name\n\
    " + str("%.7G" % CoeffArray[0]) + ",             !- Coefficient1 Constant\n\
    " + str("%.7G" % CoeffArray[1]) + ",             !- Coefficient2 x\n\
    1.0,                      !- Minimum Value of x\n\
    1.5,                      !- Maximum Value of x\n\
    1.0,                        !- Minimum Curve Output\n\
    1.023,                        !- Maximum Curve Output\n\
    Dimensionless,             !- Input Unit Type for X\n\
    Dimensionless;             !- Output Unit Type\n\
      \n"
