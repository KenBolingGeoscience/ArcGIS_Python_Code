import arcpy
import numpy

# Set overwrite option
#arcpy.env.overwriteOutput = True


arcpy.env.workspace = "C:/Users/Ken/Google Drive/TN Structure/Test_Workspace_1.gdb"

arcpy.gp.RasterCalculator_sa('"C:/Users/Ken/Google Drive/TN Structure/Test_Workspace_1/_FINAL_Subtraction_layer" - "C:/Users/Ken/Google Drive/TN Structure/Test_Workspace_1/_FINAL_CLIPPED_BASE_SHALE_Spline_with_barriers_Clipped"',
                             "C:/Users/Ken/Google Drive/TN Structure/Test_Workspace_1.gdb/_FINAL_Flattened_Base_Shale")