# PermanentJoin.py
# Purpose: Join two fields from a table to a feature class

# Import system modules
import arcpy

# Set the current workspace
arcpy.env.workspace = "C:\ArcMap_SSD_Workspace\Blank_Workspace.gdb"
# Set local variables
outLocation = "C:\ArcMap_SSD_Workspace\Test_Workspace.gdb"

outName_elvpts = "C:\ArcMap_SSD_Workspace\Test_Workspace.gdb\Appended_Elvpts"
outName_arc = "C:\ArcMap_SSD_Workspace\Test_Workspace.gdb\Appended_Arcs"
outName_elvpts_MTS = "C:\ArcMap_SSD_Workspace\Test_Workspace.gdb\Appended_Elvpts_MultipartToS"
outName_polygon = "C:\ArcMap_SSD_Workspace\Test_Workspace.gdb\Appended_Polygons"

schemaType = "NO_TEST"

#fieldMappings = ""
#subtype = ""
#arcpy.CreateFeatureclass_management(outLocation, outName, geometry_type="MULTIPOINT", template="ne_10_elvpts", )

featureClassList_elvpts = arcpy.ListFeatureClasses("*_elvpts")
featureClassList_arc = arcpy.ListFeatureClasses("*_arc")
featureClassList_elvpts_MTS = arcpy.ListFeatureClasses("*_elvpts_MTS")
featureClassList_polygon = arcpy.ListFeatureClasses("*_polygon")

try:
     for fc1 in featureClassList_arc:
            print fc1
            arcpy.Append_management([fc1], outName_arc, schemaType,"", "")

except:
     print "It's not working"
     print arcpy.GetMessages()

else:
    print "It ARCS!"



try:
     for fc2 in featureClassList_elvpts:
            print fc2
            arcpy.Append_management([fc2], outName_elvpts, schemaType,"", "")

except:
     print "It's not working"
     print arcpy.GetMessages()

else:
    print "It POINTS!"




try:
    for fc3 in featureClassList_elvpts_MTS:
            print fc3
            arcpy.Append_management([fc3], outName_elvpts_MTS, schemaType, "", "")

except:
        print "It's not working"
        print arcpy.GetMessages()

else:
        print "It MULTIPOINTS!"



try:
    for fc4 in featureClassList_polygon:
            print fc4
            arcpy.Append_management([fc4], outName_polygon, schemaType, "", "")

except:
            print "It's not working"
            print arcpy.GetMessages()

else:
            print "It POLYGONS!"




            #emptyFC = arcpy.CreateFeatureclass_management(outLocation, outName, "POLYLINE", "ne_10_arc")