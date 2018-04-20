import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

#try:
#    import pycpt
#    cmap = pycpt.load.cmap_from_cptcity_url('ukmo/wow/temp-c.cpt')
#except:
#    cmap = 'Spectral_r'

column_names = 'line_no direction longitude latitude year jul_day fiducial radar barom totmag resmag'.split(' ')
print column_names

mag_data = pd.read_csv('C:\Users\Ken\Google Drive\TN Structure\Geophysical\Magnetic\KY_TN_TVA.csv',
                       delim_whitespace=True, names=column_names) #usecols=['latitude', 'longitud', 'totmag'])

print mag_data.head() # This shows the first 5 entries of the DF.\

mag_data.to_csv('C:\Users\Ken\Google Drive\TN Structure\Geophysical\Magnetic\KY_TN_TVA_formatted.csv')