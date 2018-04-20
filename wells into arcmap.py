# Import system modules
import arcpy
import os

# Set environment settings
arcpy.env.workspace = "C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\intermediate files\intermediate well files.gdb"
arcpy.env.overwriteOutput = True
#arcpy.env.scratchWorkspace = "C:\ArcMap_SSD_Workspace\SSD_SCRATCH_WORKSPACE.gdb"
#input feature class
out_location = "C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\intermediate files\intermediate well files.gdb"


# MakeXYLayer.py
# Description: Creates an XY layer and exports it to a layer file

# import system modules 

# Set environment settings

try:
    # Set the local variables
    tnogwells = "C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\intermediate files\\tnogwells.csv"
    tnx_coords = "TSPEAST27"
    tny_coords =  "TSPNRTH27"
    tnout_Layer = "tnogwells"
    tnsaved_Layer = "C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\intermediate files\\tnogwells.lyr"

    # Set the spatial reference
    tnspRef = r"Coordinate Systems\Projected Coordinate Systems\NAD 1927 StatePlane Tennessee FIPS 4100.prj"

    # Make the XY event layer for tnogwells
    arcpy.MakeXYEventLayer_management(tnogwells, tnx_coords, tny_coords, tnout_Layer, tnspRef)

    # Print the total rows
    print(arcpy.GetCount_management(tnout_Layer))

    # Save to a layer file
    arcpy.SaveToLayerFile_management(tnout_Layer, tnsaved_Layer)

    #convert to feature class
    arcpy.FeatureClassToFeatureClass_conversion(tnsaved_Layer, out_location, tnout_Layer)

except Exception as err:
    print(err.args[0])


try:
    # Set the local variables
    kyogwells = "C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\intermediate files\\kyogwells.csv"
    kyx_coords = "Rec_Lng83"
    kyy_coords =  "Rec_Lat83"
    kyout_Layer = "kyogwells"
    kysaved_Layer = "C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\intermediate files\\kyogwells.lyr"

    # Set the spatial reference
    kyspRef = r"Coordinate Systems\Projected Coordinate Systems\NAD 1983.prj"

    # Make the XY event layer for tnogwells
    arcpy.MakeXYEventLayer_management(kyogwells, kyx_coords, kyy_coords, kyout_Layer, kyspRef)

    # Print the total rows
    print(arcpy.GetCount_management(kyout_Layer))

    # Save to a layer file
    arcpy.SaveToLayerFile_management(kyout_Layer, kysaved_Layer)

    #convert to feature class
    arcpy.FeatureClassToFeatureClass_conversion(kysaved_Layer, out_location, kyout_Layer)

except Exception as err:
    print(err.args[0])
