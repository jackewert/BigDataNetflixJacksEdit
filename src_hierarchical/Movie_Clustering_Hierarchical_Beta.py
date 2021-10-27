import matplotlib.pyplot as plt
import pandas as pd

import numpy as np
def writeLabels(fn, labels):
    print('Writing labels started.')
    fh = open(fn, 'w')
    count = 0
    for l in labels:
        count += 1
        fh.write(str(count)+','+str(l)+'\n')
    fh.close()
    print('Writing labels done.')

customer_data = pd.read_csv('../Data/movieStats.csv')
print(customer_data.head())
data = customer_data.iloc[:, 1:6].values
import scipy.cluster.hierarchy as shc

plt.figure(figsize=(10, 7))
plt.title("Customer Dendograms")

dend = shc.dendrogram(shc.linkage(data, method='ward'))
from sklearn.cluster import AgglomerativeClustering

cluster = AgglomerativeClustering(n_clusters=100, affinity='Euclidean', linkage='average')
cluster.fit_predict(data)
plt.figure(figsize=(10, 7))
plt.scatter(data[:,1], data[:,3], c=cluster.labels_)
movieCluster = cluster.labels_
writeLabels('../Data/clusterTrial.csv', movieCluster)

plt.show()