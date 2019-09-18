
#Set the destination folder for sensitive files
Location = r'\\127.0.0.1\quarantine'
QuarentineMsg = 'Content has been removed please contact administrator'
DaysKeepActiveFiles = 0


#---------------------------------------------------------------------
#DO NOT MODIFYSCRIPT PAST THIS LINE
import sys
from DiscoveryIncidentProcessing import MoveDiscoveryIncident


MoveDiscoveryIncident(sys.argv[1],Location,True,DaysKeepActiveFiles,QuarentineMsg)