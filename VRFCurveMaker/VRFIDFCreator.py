__author__ = 'claytonmiller'

from VRF_IDFObjectsTemplates import *

ThermalZoneList = ['OS:ThermalZone 1','OS:ThermalZone 2', 'OS:ThermalZone 3',
                   'OS:ThermalZone 4','OS:ThermalZone 5','OS:ThermalZone 6','OS:ThermalZone 7','OS:ThermalZone 8',
                   'OS:ThermalZone 9','OS:ThermalZone 10', 'OS:ThermalZone 11']

#Create Terminal Unit Names
UnitList = []
for zone in ThermalZoneList:
    UnitList.append(zone + ' TU')

VRFObjectFile = open("CentralVRFObjects.txt","w")

#Create the main VRF Object
CoolingRatedCOP = 3.02
HeatingRatedCOP = 3.69
MasterThermostatZone = 'OS:ThermalZone 1'
ZoneTerminalUnitList = 'VRF Heat Pump TU List'
VRFInputArray = [CoolingRatedCOP,HeatingRatedCOP,MasterThermostatZone,ZoneTerminalUnitList]

VRFACObject = AirConditionerVariableRefrigerantFlow(VRFInputArray)
VRFObjectFile.write(VRFACObject)

#Add OA Nodes
VRFObjectFile.write(OutdoorAirNodeList())
VRFObjectFile.write(OutdoorAirNodes(ThermalZoneList))

#Add VRF Condenser Avail Schedule
VRFObjectFile.write(VRFCondAvailSchedule())

#Add TU List
VRFObjectFile.write(TerminalUnits(UnitList))

#Create Objects for each Terminal Unit
TUCount = 0
for TU in UnitList:
    Zone = ThermalZoneList[TUCount]
    TUCount+=1
    VRFObjectFile.write(VRFZoneTerminalUnitObject(TU,Zone,TUCount))

#Create curves and schedules necessary for the terminal units
VRFObjectFile.write(VRFZoneTerminalUnitMiscObjects())