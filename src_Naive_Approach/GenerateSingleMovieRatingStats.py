'''
Name        : Generate_Movie_Single_Stats_Beta.py
Version     : 1.0b
Author      : Alpaca


Input: MovieID
Output is Rating Statistics: Mean, Minimum, Maximum, Standard Deviation, (other stuff to added later)

Details:
1. This function will return statistics for a single User ratings for all movies that that user watches
2. It will call Mine_Movie_Rating.py to get all the movie ratings for a particular user.
3. Its output will be pass to Generate_User_Cluster_Stat.py
'''
import numpy as np
np.set_printoptions(threshold=np.inf)    # to print entire output of numpy array

from Mine_Dict_Movie_Ratings import *
#================================================================================================================================================
def GenerateSingleMovieRatingStats(MovieID):
    # Caling all the Ratings for MovieID
    MovieRatings = np.array(Mine_Dict_Movie_Ratings(MovieID)[1])

    # Evaluating all the movie statistics

    MeanRating = np.nanmean(MovieRatings)
    MaxRating = np.nanargmax(MovieRatings)
    MinRating = np.nanargmin(MovieRatings)
    MovieStdDev = np.nanstd(MovieRatings)
    #
    return MovieID, MeanRating, MaxRating, MinRating, MovieStdDev