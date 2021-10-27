'''
Name        : Mine_Dict_User_Ratings.py
Version     : 1.0b
Author      : Alpaca (Nick)


Input: (UserID from Dictionary)
Output: Array of UserIDs & Ratings from combined_data*

Details:
1. This function will return the ratings for all the UserIDs that watched a MovieID as given by combined_data*
2. This will be done by using the UserID from the UserID dictionary output
'''

import matplotlib.pyplot as plt
import pandas as pd
# matplotlib inline
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def main():
    with open('../Data/combined_data_1.txt', 'r') as myfile:
        data = myfile.read().replace('\n', '')

    data.split(",")
    print(data)

if __name__ == "__main__":
    main()