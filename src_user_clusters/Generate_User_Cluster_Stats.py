'''
Name        : Generate_User_Cluster_Stats.py
Version     : 1.0b
Author      : Alpaca (Rebecca & Yuchen)


Input: UserClusterLabel
Intermediates: Generate_User_Single_Stats.py
Output: is Rating Statistics: Mean, Minimum, Maximum, Standard Deviation, (other stuff to added later) for
all users in the cluster

Details:
1. This function will return statistics for all Users' (in a cluster) ratings for all movies
2. It will identify the users from each cluster.
3. It will call Generate_User_Single_Stats.py to obtain the statistics for a single user.
4. Its output will generate the same statistics but the whole population of users in a given cluster.
'''