
# Import system modules
import arcpy
import numpy

# Set overwrite option
#arcpy.env.overwriteOutput = True


targetfc = "C:\ArcMap_SSD_Workspace\Test_Workspace.gdb\KYContacts_Spatial_Join_1_to_1_line_segment"
targetfield = "gq_number"
fieldlist = [f.name for f in arcpy.ListFields(targetfc)]

print fieldlist

def unique_values(fc, field):
    data = arcpy.da.TableToNumPyArray(fc, [field])
    return numpy.unique(data[field])

uniquefieldvalues = unique_values(targetfc, targetfield)

print uniquefieldvalues


try:
     for quadselect in uniquefieldvalues:
         #sql_exp = """{0} > {1}""".format(arcpy.AddFieldDelimiters(dissBuffs, "sumPoint_2"), int(1))
         #'"Parcel"' + " = '" + str(ID) + "'"
         where = "KYContacts_Spatial_Join_1_to_1_line_segment.gq_number = '" + quadselect + "'"
         #where = '"gq_number"' + "='" + quadselect"'"
         print where

         arcpy.MakeFeatureLayer_management(targetfc, "selected_quad_layer")
         arcpy.SelectLayerByAttribute_management("selected_quad_layer", "NEW_SELECTION", where_clause=where)
         print quadselect

         Contourlines = "C:/ArcMap_SSD_Workspace/TN_KY_24K_Elevation_contours.gdb/TN_KY_24k_Elevation"
         InputFeatures = ["selected_quad_layer", Contourlines]
         OutputFeatures = str(quadselect) + '_elvpts'
         clusterTolerance = 0
         arcpy.MakeFeatureLayer_management(
         arcpy.Intersect_analysis(InputFeatures, OutputFeatures, "ALL", clusterTolerance, "POINT")


except:
     print "It's not working"
     print arcpy.GetMessages()

else:
    print "It Works!"

# Put in error trapping in case an error occurs when running tool

   # Make a layer from the feature class

   # Select all cities that overlap the chihuahua polygon
   #arcpy.SelectLayerByLocation_management("cities_lyr", "INTERSECT", "c:/data/mexico.gdb/chihuahua", "", "NEW_SELECTION")

   # Within the selection (done above) further select only those cities that have a population >10,000
   #arcpy.SelectLayerByAttribute_management("cities_lyr", "SUBSET_SELECTION", "POPULATION > 10000")

   # Write the selected features to a new featureclass
   #arcpy.CopyFeatures_management("cities_lyr", "c:/data/mexico.gdb/chihuahua_10000plus")

#except:
#   print(arcpy.GetMessages())
