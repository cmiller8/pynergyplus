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

def CoolingLengthCorrectionFactor():
    return "  Curve:Biquadratic,\n\
    CoolingLengthCorrectionFactor,  !- Name\n\
    1.0693794,               !- Coefficient1 Constant\n\
    -0.0014951,              !- Coefficient2 x\n\
    2.56E-06,                !- Coefficient3 x**2\n\
    -0.1151104,              !- Coefficient4 y\n\
    0.0511169,               !- Coefficient5 y**2\n\
    -0.0004369,              !- Coefficient6 x*y\n\
    8,                       !- Minimum Value of x\n\
    175,                     !- Maximum Value of x\n\
    0.5,                     !- Minimum Value of y\n\
    1.5,                     !- Maximum Value of y\n\
    ,                        !- Minimum Curve Output\n\
    ,                        !- Maximum Curve Output\n\
    Temperature,             !- Input Unit Type for X\n\
    Temperature,             !- Input Unit Type for Y\n\
    Dimensionless;           !- Output Unit Type\n\
    \n"

def AirConditionerVariableRefrigerantFlow(VRFInputArray):
    return  "  AirConditioner:VariableRefrigerantFlow,\n\
    VRF Heat Pump,           !- Heat Pump Name\n\
    VRFCondAvailSched,       !- Availability Schedule Name\n\
    autosize,                !- Rated Total Cooling Capacity {W}\n\
    " + str(VRFInputArray[0]) + ",                  !- Rated Cooling COP {W/W}\n\
    -5,                      !- Minimum Outdoor Temperature in Cooling Mode {C}\n\
    43,                      !- Maximum Outdoor Temperature in Cooling Mode {C}\n\
    VRFCoolCapFT,            !- Cooling Capacity Ratio Modifier Function of Low Temperature Curve Name\n\
    ,                        !- Cooling Capacity Ratio Boundary Curve Name\n\
    ,                        !- Cooling Capacity Ratio Modifier Function of High Temperature Curve Name\n\
    VRFCoolEIRFT,            !- Cooling Energy Input Ratio Modifier Function of Low Temperature Curve Name\n\
    ,                        !- Cooling Energy Input Ratio Boundary Curve Name\n\
    ,                        !- Cooling Energy Input Ratio Modifier Function of High Temperature Curve Name\n\
    CoolingEIRLowPLR,        !- Cooling Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name\n\
    CoolingEIRHiPLR,         !- Cooling Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name\n\
    CoolingCombRatio,        !- Cooling Combination Ratio Correction Factor Curve Name\n\
    VRFCPLFFPLR,             !- Cooling Part-Load Fraction Correlation Curve Name\n\
    autosize,                !- Rated Total Heating Capacity {W}\n\
    " + str(VRFInputArray[1]) + ",                  !- Rated Heating COP {W/W}\n\
    -20,                     !- Minimum Outdoor Temperature in Heating Mode {C}\n\
    20,                      !- Maximum Outdoor Temperature in Heating Mode {C}\n\
    VRFHeatCapFT,            !- Heating Capacity Ratio Modifier Function of Low Temperature Curve Name\n\
    ,                        !- Heating Capacity Ratio Boundary Curve Name\n\
    ,                        !- Heating Capacity Ratio Modifier Function of High Temperature Curve Name\n\
    VRFHeatEIRFT,            !- Heating Energy Input Ratio Modifier Function of Low Temperature Curve Name\n\
    ,                        !- Heating Energy Input Ratio Boundary Curve Name\n\
    ,                        !- Heating Energy Input Ratio Modifier Function of High Temperature Curve Name\n\
    WetBulbTemperature,      !- Heating Performance Curve Outdoor Temperature Type\n\
    HeatingEIRLowPLR,        !- Heating Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name\n\
    HeatingEIRHiPLR,         !- Heating Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name\n\
    HeatingCombRatio,        !- Heating Combination Ratio Correction Factor Curve Name\n\
    VRFCPLFFPLR,             !- Heating Part-Load Fraction Correlation Curve Name\n\
    0.25,                    !- Minimum Heat Pump Part-Load Ratio\n\
    " + VRFInputArray[2] + ",               !- Zone Name for Master Thermostat Location\n\
    LoadPriority,            !- Master Thermostat Priority Control Type\n\
    ,                        !- Thermostat Priority Schedule Name\n\
    " + VRFInputArray[3] + ",   !- Zone Terminal Unit List Name\n\
    No,                      !- Heat Pump Waste Heat Recovery\n\
    30,                      !- Equivalent Piping Length used for Piping Correction Factor in Cooling Mode {m}\n\
    10,                      !- Vertical Height used for Piping Correction Factor {m}\n\
    CoolingLengthCorrectionFactor,  !- Piping Correction Factor for Length in Cooling Mode Curve Name\n\
    -0.000386,               !- Piping Correction Factor for Height in Cooling Mode Coefficient\n\
    30,                      !- Equivalent Piping Length used for Piping Correction Factor in Heating Mode {m}\n\
    ,                        !- Piping Correction Factor for Length in Heating Mode Curve Name\n\
    ,                        !- Piping Correction Factor for Height in Heating Mode Coefficient\n\
    15,                      !- Crankcase Heater Power per Compressor {W}\n\
    3,                       !- Number of Compressors\n\
    0.33,                    !- Ratio of Compressor Size to Total Compressor Capacity\n\
    7,                       !- Maximum Outdoor Dry-bulb Temperature for Crankcase Heater {C}\n\
    Resistive,               !- Defrost Strategy\n\
    Timed,                   !- Defrost Control\n\
    ,                        !- Defrost Energy Input Ratio Modifier Function of Temperature Curve Name\n\
    ,                        !- Defrost Time Period Fraction\n\
    0.0000001,               !- Resistive Defrost Heater Capacity {W}\n\
    7,                       !- Maximum Outdoor Dry-bulb Temperature for Defrost Operation {C}\n\
    AirCooled,               !- Condenser Type\n\
    MyVRFOANode,             !- Condenser Node Name\n\
    ,                        !- Evaporative Condenser Effectiveness {dimensionless}\n\
    ,                        !- Evaporative Condenser Air Flow Rate {m3/s}\n\
    0,                       !- Evaporative Condenser Pump Rated Power Consumption {W}\n\
    ,                        !- Supply Water Storage Tank Name\n\
    0,                       !- Basin Heater Capacity {W/K}\n\
    ,                        !- Basin Heater Setpoint Temperature {C}\n\
    ,                        !- Basin Heater Operating Schedule Name\n\
    Electric;                !- Fuel Type\n\
    \n"

def OutdoorAirNodeList():
    return "  OutdoorAir:NodeList,\n\
    OutsideAirInletNodes;    !- Node or NodeList Name 1\n\
    \n"

def OutdoorAirNodes(Zonelist):
    OAList = "  NodeList,\n\
    OutsideAirInletNodes,    !- Name\n"

    counter = 0
    while counter < len(Zonelist):
        OAList += "    Outside Air Inlet Node " + str(counter+1) + ",\n"
        counter+=1

    OAList += "    MyVRFOANode;\n\
    \n"

    return OAList

def VRFCondAvailSchedule():
    return "  Schedule:Compact,\n\
    VRFCondAvailSched,       !- Name\n\
    Fraction,                !- Schedule Type Limits Name\n\
    Through: 12/31,          !- Field 1\n\
    For: AllDays,            !- Field 2\n\
    Until: 12:00,1.0,        !- Field 3\n\
    Until: 13:00,1.0,        !- Field 5\n\
    Until: 24:00,1.0;        !- Field 7\n\
    \n"

def TerminalUnits(TUList):
    TUListObj = "  ZoneTerminalUnitList,\n\
    VRF Heat Pump TU List,   !- Zone Terminal Unit List Name\n"

    counter=0
    while counter <= len(TUList):
        if counter < (len(TUList)-1):
            TUListObj += "    " + TUList[counter] + ",                    !- Zone Terminal Unit Name\n"
        elif counter == (len(TUList)-1):
            TUListObj += "    " + TUList[counter] + ";                    !- Zone Terminal Unit Name\n\
            \n"
        counter+=1

    return TUListObj

def VRFZoneTerminalUnitObject(TU,Zone,TUCount):
    return "  ZoneHVAC:TerminalUnit:VariableRefrigerantFlow,\n\
    "+ TU +",                     !- Zone Terminal Unit Name\n\
    VRFAvailSched,           !- Terminal Unit Availability schedule\n\
    " + TU + " Inlet Node,          !- Terminal Unit Air Inlet Node Name\n\
    " + TU + " Outlet Node,         !- Terminal Unit Air Outlet Node Name\n\
    autosize,                !- Supply Air Flow Rate During Cooling Operation {m3/s}\n\
    autosize,                !- Supply Air Flow Rate When No Cooling is Needed {m3/s}\n\
    autosize,                !- Supply Air Flow Rate During Heating Operation {m3/s}\n\
    autosize,                !- Supply Air Flow Rate When No Heating is Needed {m3/s}\n\
    autosize,                !- Outdoor Air Flow Rate During Cooling Operation {m3/s}\n\
    autosize,                !- Outdoor Air Flow Rate During Heating Operation {m3/s}\n\
    autosize,                !- Outdoor Air Flow Rate When No Cooling or Heating is Needed {m3/s}\n\
    VRFFanSchedule,          !- Supply Air Fan Operating Mode Schedule Name\n\
    drawthrough,             !- Supply Air Fan placement\n\
    Fan:ConstantVolume,      !- Supply Air Fan Object Type\n\
    " + TU + " VRF Supply Fan,      !- Supply Air Fan Object Name\n\
    OutdoorAir:Mixer,        !- Outside Air Mixer Object Type\n\
    " + TU + " OA Mixer,            !- Outside Air Mixer Object Name\n\
    COIL:Cooling:DX:VariableRefrigerantFlow,  !- Cooling Coil Object Type\n\
    " + TU + " VRF DX Cooling Coil, !- Cooling Coil Object Name\n\
    COIL:Heating:DX:VariableRefrigerantFlow,  !- Heating Coil Object Type\n\
    " + TU + " VRF DX Heating Coil, !- Heating Coil Object Name\n\
    30,                      !- Zone Terminal Unit On Parasitic Electric Energy Use {W}\n\
    20;                      !- Zone Terminal Unit Off Parasitic Electric Energy Use {W}\n\
    \n\
  ZoneHVAC:EquipmentList,\n\
    " + Zone + " Eq,             !- Name\n\
    ZoneHVAC:TerminalUnit:VariableRefrigerantFlow,  !- Zone Equipment 1 Object Type\n\
    " + TU + ",                     !- Zone Equipment 1 Name\n\
    1,                       !- Zone Equipment 1 Cooling Sequence\n\
    1;                       !- Zone Equipment 1 Heating or No-Load Sequence\n\
\n\
  ZoneHVAC:EquipmentConnections,\n\
    " + Zone + ",                !- Zone Name\n\
    " + Zone + " Eq,             !- Zone Conditioning Equipment List Name\n\
    " + Zone + " In Nodes,       !- Zone Air Inlet Node or NodeList Name\n\
    " + Zone + " Out Nodes,      !- Zone Air Exhaust Node or NodeList Name\n\
    " + Zone + " Node,           !- Zone Air Node Name\n\
    " + Zone + " Out Node;       !- Zone Return Air Node Name\n\
\n\
  NodeList,\n\
    " + Zone + " In Nodes,       !- Name\n\
    " + TU + " Outlet Node;         !- Node 1 Name\n\
\n\
  NodeList,\n\
    " + Zone + " Out Nodes,      !- Name\n\
    " + TU + " Inlet Node;          !- Node 1 Name\n\
\n\
  OutdoorAir:Mixer,\n\
    " + TU + " OA Mixer,            !- Name\n\
    " + TU + " VRF DX CCoil Inlet Node,  !- Mixed Air Node Name\n\
    Outside Air Inlet Node " + str(TUCount) + ",!- Outdoor Air Stream Node Name\n\
    Relief Air Outlet Node " + str(TUCount) + ",!- Relief Air Stream Node Name\n\
    " + TU + " Inlet Node;          !- Return Air Stream Node Name\n\
\n\
  Fan:ConstantVolume,\n\
    " + TU + " VRF Supply Fan,      !- Name\n\
    VRFAvailSched,           !- Availability Schedule Name\n\
    0.7,                     !- Fan Efficiency\n\
    600.0,                   !- Pressure Rise {Pa}\n\
    autosize,                !- Maximum Flow Rate {m3/s}\n\
    0.9,                     !- Motor Efficiency\n\
    1.0,                     !- Motor In Airstream Fraction\n\
    " + TU + " VRF DX HCoil Outlet Node,  !- Air Inlet Node Name\n\
    " + TU + " Outlet Node;         !- Air Outlet Node Name\n\
\n\
  COIL:Heating:DX:VariableRefrigerantFlow,\n\
    " + TU + " VRF DX Heating Coil, !- Name\n\
    VRFAvailSched,           !- Availability Schedule\n\
    autosize,                !- Rated Total Heating Capacity {W}\n\
    autosize,                !- Rated Air Flow Rate {m3/s}\n\
    " + TU + " VRF DX CCoil Outlet Node,  !- Coil Air Inlet Node\n\
    " + TU + " VRF DX HCoil Outlet Node,  !- Coil Air Outlet Node\n\
    VRFTUHeatCapFT,          !- Heating Capacity Ratio Modifier Function of Temperature Curve Name\n\
    VRFACCoolCapFFF;         !- Heating Capacity Modifier Function of Flow Fraction Curve Name\n\
\n\
  COIL:Cooling:DX:VariableRefrigerantFlow,\n\
    " + TU + " VRF DX Cooling Coil, !- Name\n\
    VRFAvailSched,           !- Availability Schedule Name\n\
    autosize,                !- Rated Total Cooling Capacity {W}\n\
    autosize,                !- Rated Sensible Heat Ratio\n\
    autosize,                !- Rated Air Flow Rate {m3/s}\n\
    VRFTUCoolCapFT,          !- Cooling Capacity Ratio Modifier Function of Temperature Curve Name\n\
    VRFACCoolCapFFF,         !- Cooling Capacity Modifier Curve Function of Flow Fraction Name\n\
    " + TU + " VRF DX CCoil Inlet Node,  !- Coil Air Inlet Node\n\
    " + TU + " VRF DX CCoil Outlet Node,  !- Coil Air Outlet Node\n\
    ;                        !- Name of Water Storage Tank for Condensate Collection\n\
\n"

def VRFZoneTerminalUnitMiscObjects():
    return "  Curve:Cubic,\n\
    VRFTUHeatCapFT,          !- Name\n\
    -0.390708928227928,      !- Coefficient1 Constant\n\
    0.261815023760162,       !- Coefficient2 x\n\
    -0.0130431603151873,     !- Coefficient3 x**2\n\
    0.000178131745997821,    !- Coefficient4 x**3\n\
    0.0,                     !- Minimum Value of x\n\
    50.0,                    !- Maximum Value of x\n\
    0.5,                     !- Minimum Curve Output\n\
    1.5,                     !- Maximum Curve Output\n\
    Temperature,             !- Input Unit Type for X\n\
    Dimensionless;           !- Output Unit Type\n\
\n\
  Curve:Cubic,\n\
    VRFTUCoolCapFT,          !- Name\n\
    0.504547273506488,       !- Coefficient1 Constant\n\
    0.0288891279198444,      !- Coefficient2 x\n\
    -0.000010819418650677,   !- Coefficient3 x**2\n\
    0.0000101359395177008,   !- Coefficient4 x**3\n\
    0.0,                     !- Minimum Value of x\n\
    50.0,                    !- Maximum Value of x\n\
    0.5,                     !- Minimum Curve Output\n\
    1.5,                     !- Maximum Curve Output\n\
    Temperature,             !- Input Unit Type for X\n\
    Dimensionless;           !- Output Unit Type\n\
\n\
  Curve:Quadratic,\n\
    VRFACCoolCapFFF,         !- Name\n\
    0.8,                     !- Coefficient1 Constant\n\
    0.2,                     !- Coefficient2 x\n\
    0.0,                     !- Coefficient3 x**2\n\
    0.5,                     !- Minimum Value of x\n\
    1.5;                     !- Maximum Value of x\n\
\n\
  Schedule:Compact,\n\
    VRFFanSchedule,          !- Name\n\
    Any Number,              !- Schedule Type Limits Name\n\
    Through: 12/31,          !- Field 1\n\
    For: AllDays,            !- Field 2\n\
    Until: 7:00,1.0,         !- Field 3\n\
    Until: 18:00,1.0,        !- Field 5\n\
    Until: 24:00,1.0;        !- Field 7\n\
\n\
  Schedule:Compact,\n\
    VRFAvailSched,           !- Name\n\
    Fraction,                !- Schedule Type Limits Name\n\
    Through: 3/31,           !- Field 1\n\
    For: AllDays,            !- Field 2\n\
    Until: 24:00,1.0,        !- Field 3\n\
    Through: 9/30,           !- Field 5\n\
    For: WeekDays,           !- Field 6\n\
    Until: 7:00,1.0,         !- Field 7\n\
    Until: 17:00,1.0,        !- Field 9\n\
    Until: 24:00,1.0,        !- Field 11\n\
    For: SummerDesignDay WinterDesignDay, !- Field 13\n\
    Until: 24:00,1.0,        !- Field 14\n\
    For: AllOtherDays,       !- Field 16\n\
    Until: 24:00,1.0,        !- Field 17\n\
    Through: 12/31,          !- Field 19\n\
    For: AllDays,            !- Field 20\n\
    Until: 24:00,1.0;        !- Field 21\n\
\n"