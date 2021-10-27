'''
Name        : RMSE_Ratings.py
Version     : 1.0b
Author      : Alpaca (Waddah & Jack)

Input: UserClusterLabel
Intermediates:
    Mine_Dict_User_Ratings.py to find Known Movie Ratings
    Generate_User_Cluster_Stats.py to find Predicted Movie Ratings
Output Ratings RMSE (Root Mean Square Error)

Details:
1. This function will read known Ratings from a given User Cluster Label (based on their Cluster Label) using Mine_Dict_User_Ratings.py
2. This function will read predicted Ratings from a given User Cluster Label (based on their Cluster Label) using Generate_User_Cluster_Stats.py
3. This function will output RMSE between Known/Actual ratings vs. Predicted Ratings
'''