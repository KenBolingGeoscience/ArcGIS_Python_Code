import pandas as pd

tnogloc = pd.read_excel('C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\TN\TNOG0617_A.xls')
tnogtop = pd.read_excel('C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\TN\Tops_A.xls')
tnogmypicks = ()
kyogloc = 'C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\KY\kyog_dd.dbf'
kyogtop = 'C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\KY\KY_TOPS\KY_FM_Tops_Data.xlsx'
alogloc = pd.read_csv('E:\Users\Ken\Documents\GIS Files\AL_SHP.csv')
alogtop = pd.read_csv('C:\Users\Ken\Google Drive\ArcGIS_Python_Code\Well data\\all well data.csv')




aloglocsan = alogloc.drop_duplicates(subset=['API', 'WellName', 'Permit', 'Operator'])
alogtopsan = alogtop.drop_duplicates(subset=['API', 'WellName', 'Permit', 'Operator'])

alogtopsan.drop(alogtopsan.columns[43], axis=1, inplace=True)


print aloglocsan
print alogtopsan

joineddf = pd.merge(aloglocsan, alogtopsan, how='inner', on=['Permit', 'API', 'WellName', 'Operator'])

#joineddf = welldatashpfilesanitized.merge(welldataadditionsanitized, how='inner', on= ['Permit', 'API', 'WellName', 'Operator', 'FieldKey'])

print joineddf

joineddf.to_csv('C:\Users\Ken\Google Drive\ArcGIS_Python_Code\Well data\AL_Joined.csv')

