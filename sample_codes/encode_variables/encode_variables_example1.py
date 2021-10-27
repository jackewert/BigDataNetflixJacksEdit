# The following codes were copied from
# http://pbpython.com/categorical-encoding.html

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import LabelEncoder

# Define the headers since the data does not have any

headers = ["symboling", "normalized_losses", "make", "fuel_type", "aspiration",
           "num_doors", "body_style", "drive_wheels", "engine_location",
           "wheel_base", "length", "width", "height", "curb_weight",
           "engine_type", "num_cylinders", "engine_size", "fuel_system",
           "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",
           "city_mpg", "highway_mpg", "price"]

# Read in the CSV file and convert "?" to NaN
df = pd.read_csv("http://mlr.cs.umass.edu/ml/machine-learning-databases/autos/imports-85.data",
                  header=None, names=headers, na_values="?" )
# Displaying the top lines of 'df'
df.head()

# The final check we want to do is see what data types we have:
df.dtypes

#----------------------------------------------------------------------------------------------------------------------------------------------
'''
Since this article will only focus on encoding the categorical variables, we are going to include only the object columns in our dataframe. 
Pandas has a helpful select_dtypes function which we can use to build a new dataframe containing only the object columns.
'''

# See how they encoded the car makes.




obj_df = df.select_dtypes(include=['object']).copy()
obj_df["num_doors"].value_counts()
obj_df.head()

# # # Before going any further, there are a couple of null values in the data that we need to clean up.

obj_df[obj_df.isnull().any(axis=1)]

obj_df["num_doors"].value_counts()

obj_df = obj_df.fillna({"num_doors": "four"})

#
# #----------------------------------------------------------------------------------------------------------------------------------------------
#
# ''' Approach 1: Find & Replace'''    # VERY LAME APPROACH AND NEEDS YOU TO KNOW WHAT THE CATEOGRIES ARE
#
# obj_df["num_cylinders"].value_counts()
#
# cleanup_nums = {"num_doors":     {"four": 4, "two": 2},
#                 "num_cylinders": {"four": 4, "six": 6, "five": 5, "eight": 8,
#                                   "two": 2, "twelve": 12, "three":3 }}
#
# obj_df.replace(cleanup_nums, inplace=True)
# obj_df.head()
#
# obj_df.dtypes
#
# #----------------------------------------------------------------------------------------------------------------------------------------------
# ''' #2 Label Encoding'''
# obj_df["body_style"] = obj_df["body_style"].astype('category')
# obj_df.dtypes
#
# obj_df["body_style_cat"] = obj_df["body_style"].cat.codes
# obj_df.head()
#
#
# #----------------------------------------------------------------------------------------------------------------------------------------------
# # A few other approaches are possible.
#
#
# #----------------------------------------------------------------------------------------------------------------------------------------------
# '''
# Using scikit-learn
#
#

# Using Label Encoder()


lb_make = LabelEncoder()
obj_df["make_code"] = lb_make.fit_transform(obj_df["make"])
obj_df[["make", "make_code"]].head(11)


# Using Label Binarizer()

lb_style = LabelBinarizer()
lb_results = lb_style.fit_transform(obj_df["body_style"])
pd.DataFrame(lb_results, columns=lb_style.classes_).head()

