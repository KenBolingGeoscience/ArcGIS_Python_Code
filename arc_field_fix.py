# PermanentJoin.py
# Purpose: Join two fields from a table to a feature class

# Import system modules
import arcpy

# Set the current workspace
arcpy.env.workspace = "C:\ArcMap_SSD_Workspace\Test_Workspace.gdb"

map_name = fc

arcpy.AddField_management(fc, "ref_ID", "LONG", 9, "", "", "refcode", "NULLABLE", "REQUIRED")
arcpy.AddField_management(fc, "map_name", "TEXT", "", "", "30")
arcpy.CalculateField_management(fc, "map_name", "\"" + map_name + "\"", "PYTHON")
arcpy.AlterField_management(fc, field, new_name, new_alias, new_type, new_length, new_is_nullable, clear_alias)