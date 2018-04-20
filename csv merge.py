import csv
import os
import pandas as pd

filedirectory = 'C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\KY\KY_TOPS\county downloads'

#creates a list of files in the filedirectory
filelist = os.listdir(filedirectory)

pathlist = []
appendeddf = []

print filelist

#creates a list of paths to .csv files in the filelist
for files in filelist:
    if files.endswith(".xls"):
       pathlist.append (os.path.join(filedirectory, files))

print type(pathlist)
print pathlist

#reads each .csv file on the filelist into a pandas dataframe and adds each dataframe together
for paths in pathlist:
    xlscontents = pd.read_xls(paths)
    appendeddf.append(csvcontents)

#concatinates the dataframes into one single dataframe
outputdf = pd.concat(appendeddf)

outputdf.to_csv(filedirectory + '\output.csv')
#for paths in pathlist:



#def csv_reader(file_obj)
#    with open(file_obj, 'r') as userfile:
#        userFileReader = csv.reader(userfile)
#        for row in userFileReader:
#            print row