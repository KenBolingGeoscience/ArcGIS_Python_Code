


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


arcpy.env.workspace = "C:\ArcMap_SSD_Workspace\Test_Workspace.gdb"


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

gdb2gdf(TN_OGdb_6_17_TOPS)