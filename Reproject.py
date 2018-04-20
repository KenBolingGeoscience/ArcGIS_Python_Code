# Import system modules
import arcpy
import os

# Set environment settings
arcpy.env.workspace = "C:\Users\Ken\Google Drive\TN Structure\Faults\Faults.gdb"
arcpy.env.overwriteOutput = True
arcpy.env.scratchWorkspace = "C:\ArcMap_SSD_Workspace\SSD_SCRATCH_WORKSPACE.gdb"
#input feature class

fcin = 'E:\Users\Ken\Documents\GIS Files\AL_GIS\GISdata\Digital_Geologic_Map_of_Alabama_faults.shp'

out_location = "C:\Users\Ken\Google Drive\TN Structure\Faults\Faults.gdb"


#output feature class
fcout ='AL_faults_250k'


# Set output coordinate system
outCS = arcpy.SpatialReference('NAD 1983')

# run project tool

arcpy.Project_management(fcin, fcout, outCS)


