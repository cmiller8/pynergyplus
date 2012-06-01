__author__ = 'claytonmiller'

from VRF_IDFObjectsTemplates import *

ThermalZoneListGroup1 = ['OS:ThermalZone 4','OS:ThermalZone 5','OS:ThermalZone 6','OS:ThermalZone 7',
                         'OS:ThermalZone 8','OS:ThermalZone 11']

ThermalZoneListGroup2 = ['OS:ThermalZone 1','OS:ThermalZone 2', 'OS:ThermalZone 3',
                         'OS:ThermalZone 9','OS:ThermalZone 10']

ThermalZoneListTotal = ['OS:ThermalZone 4','OS:ThermalZone 5','OS:ThermalZone 6','OS:ThermalZone 7',
                         'OS:ThermalZone 8','OS:ThermalZone 11','OS:ThermalZone 1','OS:ThermalZone 2', 'OS:ThermalZone 3',
                         'OS:ThermalZone 9','OS:ThermalZone 10']

#Create Terminal Unit Names
UnitListGroup1 = []
for zone in ThermalZoneListGroup1:
    UnitListGroup1.append(zone + ' TU')

UnitListGroup2 = []
for zone in ThermalZoneListGroup2:
    UnitListGroup2.append(zone + ' TU')

VRFObjectFile = open("CentralVRFObjects.txt","w")

#Create the main VRF Objects
CoolingRatedCOP = 3.02
HeatingRatedCOP = 3.69
MasterThermostatZone = 'OS:ThermalZone 1'
ZoneTerminalUnitList = 'VRF Heat Pump TU List Group 1'
VRFCondenserName = 'VRF Heat Pump Group 1'
VRFInputArray = [CoolingRatedCOP,HeatingRatedCOP,MasterThermostatZone,ZoneTerminalUnitList,VRFCondenserName]
VRFObjectFile.write(AirConditionerVariableRefrigerantFlow(VRFInputArray))

CoolingRatedCOP = 3.02
HeatingRatedCOP = 3.69
MasterThermostatZone = 'OS:ThermalZone 7'
ZoneTerminalUnitList = 'VRF Heat Pump TU List Group 2'
VRFCondenserName = 'VRF Heat Pump Group 2'
VRFInputArray = [CoolingRatedCOP,HeatingRatedCOP,MasterThermostatZone,ZoneTerminalUnitList,VRFCondenserName]
VRFObjectFile.write(AirConditionerVariableRefrigerantFlow(VRFInputArray))

#Add OA Nodes
VRFObjectFile.write(OutdoorAirNodeList())
VRFObjectFile.write(OutdoorAirNodes(ThermalZoneListTotal))

#Add VRF Condenser Avail Schedule
VRFObjectFile.write(VRFCondAvailSchedule())

#Add TU List
VRFObjectFile.write(TerminalUnits(UnitListGroup1,"VRF Heat Pump TU List Group 1"))
VRFObjectFile.write(TerminalUnits(UnitListGroup2,"VRF Heat Pump TU List Group 2"))

#Create Objects for each Terminal Unit
TUCount = 0
for TU in UnitListGroup1:
    Zone = ThermalZoneListGroup1[TUCount]
    TUCount+=1
    VRFObjectFile.write(VRFZoneTerminalUnitObject(TU,Zone,TUCount))

TUCount = 0
for TU in UnitListGroup2:
    Zone = ThermalZoneListGroup2[TUCount]
    TUCount+=1
    VRFObjectFile.write(VRFZoneTerminalUnitObject(TU,Zone,TUCount))

#Create curves and schedules necessary for the terminal units
VRFObjectFile.write(VRFZoneTerminalUnitMiscObjects())