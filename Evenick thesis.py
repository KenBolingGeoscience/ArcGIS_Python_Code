import pandas as pd
import numpy as np
import os

wd = 'C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\TN\Evenick'
print(os.getcwd())
os.chdir(wd)
print(os.getcwd())

evnk1 = pd.read_csv('Evenick_Dissertation_Appendix_from_BM.csv')
evnk2 = pd.read_csv('Evenick_Dissertation_Appendix_TN_Only.csv')

evnkmerged = pd.merge(
    evnk1,
    evnk2,
    how='outer',
    on='API')

print(evnkmerged)

