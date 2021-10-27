'''
Similar to AgglomerativeClustering, but recursively merges features instead of samples.
http://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration
''''

# INCOMPLETE

import numpy as np
from sklearn import datasets, cluster

digits = datasets.load_digits()
images = digits.images
X = np.reshape(images, (len(images), -1))
agglo = cluster.FeatureAgglomeration(n_clusters=32)
agglo.fit(X) 
FeatureAgglomeration(affinity='euclidean', compute_full_tree='auto',
           connectivity=None, linkage='ward', memory=None, n_clusters=32,
           pooling_func=...)
X_reduced = agglo.transform(X)
X_reduced.shape