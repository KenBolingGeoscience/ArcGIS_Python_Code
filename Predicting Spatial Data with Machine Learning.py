import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
from shapely import geometry
import seaborn as sns
%matplotlib inline

mag_data = pd.read_csv('C:\Users\Ken\Google Drive\TN Structure\Geophysical_data\Magnetic\KY_TN_TVA_formatted.csv', index_col=0)
mag_data['geometry'] = [geometry.Point(x, y) for x, y in zip(mag_data['long_wgs84'], mag_data['lat_wgs84'])]
mag_data = gpd.GeoDataFrame(mag_data, geometry='geometry', crs="+init=epsg:4326")

mag_data.head()