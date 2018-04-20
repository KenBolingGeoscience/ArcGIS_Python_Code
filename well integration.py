import pandas as pd

from simpledbf import Dbf5

kydbf = Dbf5('C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\KY\kyog_dd.dbf')
kyogloc = kydbf.to_dataframe()

kyogtop = pd.read_csv('C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\KY\KY_TOPS\KY_FM_Tops_Data_csv.csv')


kylocdup = kyogloc.drop(['Letter',
                      'Number',
                      'Section',
                      'FNS',
                      'NS',
                      'FEW',
                      'EW',
                      'Org_Farm',
                      'tdfm',
                      'Deepst_Pay',
                      'Org_WClass',
                      'Plug_Date',
                      'Plug_Afdvt',
                      'Core',
                      'Cuttings',
                      'images',
                      'IOF_IP',
                      'PlotSymbol',
                      'ELog'], axis=1)
kylocdup.drop_duplicates(subset=['KGS_Recno', 'Rec_Lat83', 'Rec_Lng83'],inplace=True)

kylocdup.rename(columns={"KGS_Recno": "record_number"},inplace=True)


#drop duplicate rows from mistakes made in putting the original files together in excel

kytopdup = kyogtop.drop_duplicates(subset=['record_number',
                                           'pick_fm_name',
                                           'fm_top_depth_ft',
                                           'comments',
                                           'source'
                                           ])

kygroup = kytopdup.groupby(['record_number','pick_fm_name']).mean().reset_index()

kymerge = pd.merge(kytopdup, kygroup, how='inner', on=['record_number', 'pick_fm_name'])

kymerge['pick_delta'] = abs(kymerge.fm_top_depth_ft_x - kymerge.fm_top_depth_ft_y)

kymask = kymerge['pick_delta'] <= 20

kymasked = kymerge[kymask]

kymaskedgroup = kymasked.drop_duplicates(subset=['record_number',
                                           'pick_fm_name',
                                           'fm_top_depth_ft_y'])



kymaskedgroup.rename(columns={"fm_top_depth_ft_y": "top_depth_avg"},inplace=True)

kytopfinal = kymaskedgroup.drop(['datum_ft_y',
                                 'fm_bottom_depth_ft_y',
                                 'pick_stratcode_y',
                                 'secondary_lithology',
                                 'primary_lithology',
                                 'type'], axis=1)

kyogwells = pd.merge(kylocdup, kytopfinal, how='inner', on=['record_number'])


kyogwells.to_csv('C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\KY\KY_well_output.csv')



#kygroup =  kygroup.mean()
#kymask= (kytopdup.duplicated(['record_number','pick_fm_name','fm_top_depth_ft'], keep='first'))

#kytopdup2 = kytopdup[kymask]


#print kytopdup2


#selects all the rows with more than one entry for each formation top


# create list
#booleans = []

# loop
#for records in kytopdup2:
 #   if kytopdup2.comments  == 'PETRA TOPS FROM 2011 MRCSP PROJECT'
  #      booleans.append(True)
   # else:
    #    booleans.append(False)


#            & [kytopdup.comments == 'PETRA TOPS FROM 2011 MRCSP PROJECT']
 #                    [kytopdup.comments == 'PETRA TOPS FROM 2009 L PENN COAL PROJECT']]
#drop duplicate rows from mistakes made in putting the original files together in excel

#kygroup = kytopdup.groupby(['record_number','pick_fm_name'])

#kytopdup['mean_fm_depth']= kytopdup['fm_top_depth_ft'].groupby(kytopdup['record_number','pick_fm_name']).transform('mean')

#print kytopdup
#kymask= (kytopdup.duplicated(['record_number','pick_fm_name','fm_top_depth_ft'], keep='first'))

#kytopdup2 = kytopdup[kymask]


#print kytopdup2

#use this to rename columns:
# df.rename({'$a':'a', '$b':'b', '$c':'c', '$d':'d', '$e':'e'}, axis=1)

