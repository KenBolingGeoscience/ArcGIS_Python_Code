# Import system modules
import arcpy

# Set the current workspace
arcpy.env.workspace = "C:\ArcMap_SSD_Workspace\Test_Workspace.gdb"

featureClassList_arc = arcpy.ListFeatureClasses("*_arc")


try:
     for fc in featureClassList_arc:
            print fc

            Infeatures = fc
            combofield = "Combo_Units"
            #Geo1 = "GEO"
            #Geo2 = "GEO_1"
            ComboFieldsExpression = "!GEO! + '-' + !GEO_1!"
            arcpy.AddField_management(Infeatures, combofield, "TEXT","","","20")
            arcpy.CalculateField_management(Infeatures, combofield, ComboFieldsExpression, "PYTHON")


except:
     print "It's not working"
     print arcpy.GetMessages()

else:
    print "It Works!"
