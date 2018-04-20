import arcpy
import pandas
#from arcpy import env

#from arcpy.sa import *

arcpy.env.overwriteOutput = "TRUE"

# Define workspace
mywspace = "C:\ArcMap_SSD_Workspace\Blank_Workspace.gdb"

print mywspace

# Set the workspace for the ListFeatureClass function
arcpy.env.workspace = mywspace

dataframe = "TN_OGdb_6_17_TOPS"

def topselect(table,top1,top2,top3,top4):
    try:
        #if the field TOPGEO is greater than zero, make the field BEST_PICK equal to the value of TOPGEO
        #If it's less than zero, check if the field TOPLOGS is greater than zero, and if so use that for BEST_PICK
        table['BEST_PICK'][table['TOPSGEO'] > 0 ] = table['TOPSGEO']

       if !TOPGEO!
             print fc
             arcpy.AddField_management(fc, "LINE", "TEXT", "", "", "7")
             lineexpression= 'KEN'
             arcpy.CalculateField_management(fc, field="LINE", expression='"KEN"', expression_type="PYTHON", code_block="")


        except:
            print "It's not working"
            print arcpy.GetMessages()

        else:
            print "It Works!"  # -*- coding: utf-8 -*-



"""gdb2gdf.py
gdb feature class to geopandas dataframe.

@author: Garin Wally / Windfall Spatial
@license: MIT
@date: October 28, 2015

This work will likely be released as a part of an add-on series by
Windfall Spatial.
"""

import arcpy
import geopandas as gp


def gdb2gdf(fc):
    """Opens an ESRI File GDB feature class (or table) as a geopandas
        GeoDataFrame.

    Args:
        fc (str): path to feature class (can be contained in dataset)

    Returns:
        df (geopandas.GeoDataFrame)

    Usage:
        my_data = fc2df(r"\\path\to\your\data.gdb\dataset\featureclass")

    Notes:
        ESRI's arcpy (Python 2.7) is exceptionally slow, please forgive them
        for the speed of this function. The output dataframe will be quicker.
    """

    # Insure input feature class exists
    assert arcpy.Exists(fc), "There is a problem with your path."

    # Print a happy remark
    print("Creating GeoDataFrame, please wait...")
    print("(If your data is big, you should go make a sandwich.)")
    print("(...and if your data is real big, make me one!)")

    # Get field names from feature class
    field_names = [c.name.replace(" ", "_") for c in arcpy.ListFields(fc)]

    # Create a blank GeoDataFrame; set geo_df column names from fc field names
    gdb_df = gp.GeoDataFrame(columns=field_names)

    # Load the rows of the input feature class as a cursor
    with arcpy.da.SearchCursor(fc, ["*"]) as cur:
        # Iterate over each row in the cursor
        for row in cur:
            # Get the next index in gdb_df (the length of the GeoDataFrame)
            insert_position = len(gdb_df)
            # Load each column value in the row into the GeoDataFrame
            gdb_df.loc[insert_position] = [col for col in row]

    return gdb_df



#The pandas DataFrame provides a nice querying ability.

#What you are trying to do can be done simply with:

# Set a default value
df['Age_Group'] = '<40'
# Set Age_Group value for all row indexes which Age are greater than 40
df['Age_Group'][df['Age'] > 40] = '>40'
# Set Age_Group value for all row indexes which Age are greater than 18 and < 40
df['Age_Group'][(df['Age'] > 18) & (df['Age'] < 40)] = '>18'
# Set Age_Group value for all row indexes which Age are less than 18
df['Age_Group'][df['Age'] < 18] = '<18'

The querying here is a powerful tool of the dataframe and will allow you to manipulate the DataFrame as you need.

For more complex conditionals, you can specify multiple conditions by encapsulating each condition in parenthesis and separating them with a boolean operator ( eg. '&' or '|')

You can see this in work here for the second conditional statement for setting >18.