from sklearn.cluster import KMeans
import numpy as np

# Sample NumPy array
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

# 2 clusters of k-means
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)



results1 = kmeans.labels_
print(results1, '\n')
# array([0, 0, 0, 1, 1, 1], dtype=int32)

results2 = kmeans.predict([[0, 0], [4, 4]])
print(results2, '\n')
# array([0, 1], dtype=int32)

#
results3 = kmeans.cluster_centers_
print(results3, '\n')
# # array([[1., 2.],
# #        [4., 2.]])