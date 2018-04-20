import pandas as pd

welldatashpfile = pd.read_csv('E:\Users\Ken\Documents\GIS Files\AL_SHP.csv')

welldataaddition = pd.read_csv('C:\Users\Ken\Google Drive\ArcGIS_Python_Code\Well data\\all well data.csv')

print welldatashpfile.head()
print welldataaddition.head()

joineddf = pd.merge(welldatashpfile, welldataaddition, how='outer', on='API')

print joineddf