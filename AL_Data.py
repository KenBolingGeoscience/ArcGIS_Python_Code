import pandas as pd
import numpy as np
import os

alogmypicks = pd.read_csv('C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\AL\\AL_TOPS_KSB.csv')
alogloc = pd.read_csv('E:\Users\Ken\Documents\GIS Files\AL_SHP.csv')
alogtop = pd.read_csv('C:\Users\Ken\Google Drive\ArcGIS_Python_Code\Well data\\all well data.csv')
aldata = pd.read_csv('C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\AL\\AL_TOPS_KSB.csv')

aloglocsan = alogloc.drop_duplicates(subset=['API', 'WellName', 'Permit', 'Operator'])
alogtopsan1 = alogtop.drop_duplicates(subset=['API', 'WellName', 'Permit', 'Operator'])

alogtopsan = alogtopsan1.drop(alogtopsan1.columns[43], axis=1)


print aloglocsan
print alogtopsan

joineddf = pd.merge(aloglocsan, alogtopsan, how='inner', on=['Permit', 'API', 'WellName', 'Operator'])

alfinal = pd.merge(joineddf, aldata, how='inner', on=['API', 'WellName'])
#joineddf = welldatashpfilesanitized.merge(welldataadditionsanitized, how='inner', on= ['Permit', 'API', 'WellName', 'Operator', 'FieldKey'])

# asign best pick for TN top pick GEO<LOG<SAMP<WELL HISTORY
conditions = [
    (alfinal['GRElev'] > 0),
    (alfinal['GRElev'] == 0) & (alfinal['DFElev'] > 0),
    (alfinal['GRElev'] == 0) & (alfinal['DFElev'] == 0) & (alfinal['KBElev'] > 0)]
choices = [alfinal['GRElev'], alfinal['DFElev'], alfinal['KBElev']]
alfinal['Elevation'] = np.select(conditions, choices)


print alfinal

alout = alfinal[['API',
                 'Longitude',
                 'Latitude',
                 'Elevation',
                 'WellName',
                 'FORMATION',
                 'bestpick']]

print alout
alout.to_csv('C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\intermediate files\\alogwells.csv')