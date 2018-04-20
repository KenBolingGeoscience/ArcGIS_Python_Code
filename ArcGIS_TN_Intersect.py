
# Import system modules
import arcpy

# Set the current workspace
arcpy.env.workspace = "C:\ArcMap_SSD_Workspace\Blank_Workspace.gdb"
arcpy.env.overwriteOutput = "TRUE"


featureClassList_arc = arcpy.ListFeatureClasses("*_arc")

try:
     for fc in featureClassList_arc:
         print fc
         Contourlines = "C:/ArcMap_SSD_Workspace/TN_KY_24K_Elevation_contours.gdb/TN_KY_24k_Elevation"
         InputFeatures = [fc, Contourlines]
         OutputFeatures = fc.replace('_arc', '_elvpts')
         clusterTolerance = 0
         arcpy.Intersect_analysis(InputFeatures, OutputFeatures, "ALL", clusterTolerance, "POINT")
         # Create field name with the proper delimiters
         #fieldname = "LINE"
         #field = arcpy.AddFieldDelimiters(OutputFeatures, fieldname)
         # Create a search cursor using an SQL expression
         #
         #rows = arcpy.SearchCursor(fc, field + " = 2")
         #for row in rows:
         # do something
         #del rows




except:
     print "It's not working"
     print arcpy.GetMessages()

else:
    print "It Works!"


#arcpy.Intersect_analysis(in_features="C:/ArcMap_SSD_Workspace/Test_Workspace.gdb/ne_10_arc #;C:/ArcMap_SSD_Workspace/TN_KY_24K_Elevation_contours.gdb/TN_KY_24k_Elevation #", out_feature_class="C:/ArcMap_SSD_Workspace/Test_Workspace.gdb/ne_10_elvpts", join_attributes="ALL", cluster_tolerance="0 Feet", output_type="POINT")