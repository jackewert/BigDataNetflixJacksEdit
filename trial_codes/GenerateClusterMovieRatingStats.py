'''
Name        : Generate_Movies_Cluster_Stats.py
Version     : 1.0b
Author      : Alpaca (Rebecca & Yuchen)


Input: MovieClusterLabel
Intermediates: Generate_Movie_Single_Stats_Beta.py
Output:is Rating Statistics: Mean, Minimum, Maximum, Standard Deviation, (other stuff to added later) for
all movies in the cluster

Details:
1. This function will return statistics for all movies' (in a cluster) ratings for all users
2. It will identify the movies from each cluster.
3. It will call Generate_Movie_Single_Stats_Beta.py to obtain the statistics for a single user.
4. Its output will generate the same statistics but the whole population of movies in a given cluster.
'''