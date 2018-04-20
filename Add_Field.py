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
             arcpy.AddField_management(fc, "LINE", "TEXT", "", "", "7")
             lineexpression= 'KEN'
             arcpy.CalculateField_management(fc, field="LINE", expression='"KEN"', expression_type="PYTHON", code_block="")


except:
     print "It's not working"
     print arcpy.GetMessages()

else:
    print "It Works!"

