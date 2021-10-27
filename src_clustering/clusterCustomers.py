'''
Name        : clusterMovies.py
Versiojn    : 1.0a
Author      : Alpaca

'''

# https://stackabuse.com/hierarchical-clustering-with-python-and-scikit-learn/ was used for this
import matplotlib.pyplot as plt
# matplotlib inline
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

#Write cluster labels to file
def writeUserClusterLabels(fileNames, movieClusterLabels, cidList):
    print('Writing labels started.')
    fileHandles = open(fileNames, 'w')
    count = 0
    for index in range(0, len(movieClusterLabels)):
        fileHandles.write(str(cidList[index])+','+str(movieClusterLabels[index])+'\n')
    fileHandles.close()
    print('Writing labels done.')

#================================================================================================================================================
def read_customer_features(fileName):
    print('Reading file start...')
    dataFrames = []
    fileHandle = open(fileName, 'r', encoding='latin1')
    line = fileHandle.readline()
    count = 0
    cidList = []
    while line:
        count += 1
        features = []
        data = line.split(',')
        cidList.append(data[0])
        for d in data[1:]:
            features.append(int(d))
        if count % 1000 == 0:
            print('Reading index is : %d' % count)
        dataFrames.append(features)
        line = fileHandle.readline()
    print('Reading file completed...')
    return dataFrames, cidList

#================================================================================================================================================
def clusterUsers(dataFile, numUserClusters):
    print('Clustering user started...')
    clustering = KMeans(n_clusters=numUserClusters, random_state=0)
    # clustering = AgglomerativeClustering(affinity='euclidean', compute_full_tree='auto',
    #                                      connectivity=None, linkage='ward', memory=None, n_clusters=numUserClusters,
    #                                      pooling_func='deprecated')
    clustering.fit(dataFile)
    print('Fitting completed...PCA analysis started...')

    pcaComponents = PCA(n_components=2)
    principalComponents = pcaComponents.fit_transform(dataFile)
    principalDataFrames = pd.DataFrame(data=principalComponents,
                               columns=['principal component 1', 'principal component 2'])
    print('PCA Completed...En route to plot the clustered data...')

    userClusterLabels = clustering.labels_
    plotUserClusters(principalDataFrames, userClusterLabels, numUserClusters, 'Visualization (Clustered Users)', 'PCA Comp 1', 'PCA Comp 2')

    return userClusterLabels

#================================================================================================================================================
def plotUserClusters(principleDataFrames, userClusterLabels, numUserClusters, plotLabel='', xlabel='', ylabel=''):
    vals = principleDataFrames.values
    print(len(vals))
    print('Plotting started')
    #plt.xlim((-250, 250))
    #plt.ylim((-250, 250))
    plt.title(plotLabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    PC1Comp = [[] for _ in range(numUserClusters)]
    PC2Comp = [[] for _ in range(numUserClusters)]
    print('Labels sorting started...')
    for index in range(0, len(vals)):
        PC1Comp[userClusterLabels[index]].append(vals[index][0])
        PC2Comp[userClusterLabels[index]].append(vals[index][1])
    print('Labels sorting ended ... now plotting...')
    for index in range(0, len(PC1Comp)):
        plt.scatter(PC1Comp[index], PC2Comp[index], s=3)
        print('Index is : %d' % index)
    print('Plotting done')
    plt.savefig('../plots/userClusters.png')
    return 0


#================================================================================================================================================
def main():
    dataFile,cidList = read_customer_features('../data/userfeatures.csv')
    labels = clusterUsers(dataFile, 10)
    # Write labels to data file (Optional)
    writeUserClusterLabels('../data/userIDClusters.csv', labels, cidList)

if __name__ == "__main__":
    main()


