# PermanentJoin.py
# Purpose: Join two fields from a table to a feature class

# Import system modules
import arcpy

# Set the current workspace
arcpy.env.workspace = "C:\ArcMap_SSD_Workspace\Nashville_Files.gdb"

featureClassList_arc = arcpy.ListFeatureClasses("*_repaired_arc")
#featureClassList_polygon = arcpy.ListFeatureClasses("*_polygon")

try:
     for fc in featureClassList_arc:
             print fc
             polygonfeatures = fc.replace('_repaired_arc', '_polygon')
             #quadname_ = fc.replace('arc', '')

             inFeatures = fc
             joinFieldL = "LEFT_FID"
             joinFieldR = "RIGHT_FID"
             joinField2 = "OBJECTID"
             joinTable = polygonfeatures
             fieldList = ["Geology"]
             arcpy.JoinField_management(inFeatures, joinFieldL, joinTable, joinField2, fieldList)
             arcpy.JoinField_management(inFeatures, joinFieldR, joinTable, joinField2, fieldList)
             combofield = "Combo_Units"
             # Geo1 = "GEO"
             # Geo2 = "GEO_1"
             ComboFieldsExpression = "!Geology! + '-' + !Geology_1!"
             arcpy.AddField_management(inFeatures, combofield, "TEXT", "", "", "20")
             arcpy.CalculateField_management(inFeatures, combofield, ComboFieldsExpression, "PYTHON")



             #arcpy.AddField_management(fc, "Combo_Units", "TEXT","","","20")

             #arcpy.CalculateField_management(fc, "Combo_Units",'GEO' + 'GEO1', "PYTHON")


except:
     print "It's not working"
     print arcpy.GetMessages()

else:
    print "It Works!"


# Join two feature classes by the zonecode field and only carry
# over the land use and land cover fields

