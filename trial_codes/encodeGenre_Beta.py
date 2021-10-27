'''

Name        : encodeGenre.py
Version     : 1.0b
Author      : Alpaca
Requirements: Add additionalData_*****.csv file in data folder

'''

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import LabelEncoder

# Define the headers are the first line of the datefile.

# Read in the CSV file and convert "?" to NaN
df = pd.read_csv('../src_plots/data/additionalData',
                  header='infer',sep='\t')
# # Displaying the top lines of 'df'
# df.head()
#
# # The final check we want to do is see what data types we have:
# df.dtypes