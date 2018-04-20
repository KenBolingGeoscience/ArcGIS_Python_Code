import arcpy

#from arcpy import env

#from arcpy.sa import *

arcpy.env.overwriteOutput = "TRUE"

# Define workspace
mywspace = "C:\ArcMap_SSD_Workspace\Blank_Workspace.gdb"

print mywspace

# Set the workspace for the ListFeatureClass function
arcpy.env.workspace = mywspace


try:
     for fc in arcpy.ListFeatureClasses("","all",""):
             print fc

             map_name = fc
             map_name = map_name.replace('_polygon', '')
             map_name = map_name.replace('_label', '')
             map_name = map_name.replace('_arc', '')
             map_name = map_name.replace('_tic', '')

             print map_name

             arcpy.AddField_management(fc, "map_name", "TEXT","","","30")

             arcpy.CalculateField_management(fc, "map_name","\"" + map_name + "\"", "PYTHON")

except:
     print "It's not working"
     print arcpy.GetMessages()

else:
    print "It Works!"
