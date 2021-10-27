'''
Name        : RMSE_Ratings.py
Version     : 1.0b
Author      : Alpaca (Waddah & Jack)

Input: MovieClusterLabel
Intermediates:
    MovieIDRatings.py to find Known Movie Ratings
    GenerateClusterMovieRatingStats.py to find Predicted Movie Ratings
Output Ratings RMSE (Root Mean Square Error)

Details:
1. This function will read known Ratings from a given Movie Cluster Label (based on their Cluster Label) using MovieIDRatings.py
2. This function will read predicted Ratings from a given Movie Cluster Label (based on their Cluster Label) using GenerateClusterMovieRatingStats.py
3. This function will output RMSE between Known/Actual ratings vs. Predicted Ratings
'''


from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np

# ================================================================================================================================================
def RMSE_Ratings(KnownRatings, PredictedRatings):

    RMSE = sqrt(mean_squared_error(KnownRatings, PredictedRatings))
    return RMSE