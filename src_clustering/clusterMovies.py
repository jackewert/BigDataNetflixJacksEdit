'''
Name        : clusterMovies.py
Versiojn    : 1.0a
Author      : Alpaca

'''

#================================================================================================================================================
# https://stackabuse.com/hierarchical-clustering-with-python-and-scikit-learn/ was used for this
import matplotlib.pyplot as plt
import pandas as pd
# matplotlib inline
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#================================================================================================================================================
def writeMovieClusterLabels(fileNames, movieClusterLabels):
    print('Writing labels started.')
    fileHandles = open(fileNames, 'w')
    count = 0
    for currentLabel in movieClusterLabels:
        count += 1
        fileHandles.write(str(count)+','+str(currentLabel)+'\n')
    fileHandles.close()
    print('Writing labels done.')


#================================================================================================================================================
def plotMovieClusters(principleDataFrames, movieClustersLabels, numMovieClusters, plotTitle='', xlabel='', ylabel=''):

    colors = ['r', 'b', 'g', 'y', 'm', ]
    principleDataFramesValues = principleDataFrames.values

    #vals = df
    print(len(principleDataFramesValues))
    print(len(colors))
    print('Plotting started')

    #plt.xlim((-250, 250))
    #plt.ylim((-250, 250))

    plt.title(plotTitle)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    PC1data = [[] for _ in range(numMovieClusters)]
    PC2data = [[] for _ in range(numMovieClusters)]

    print('Labels sorting started...')
    for index in range(0, len(principleDataFramesValues)):
        PC1data[movieClustersLabels[index]].append(principleDataFramesValues[index][0])
        PC2data[movieClustersLabels[index]].append(principleDataFramesValues[index][1])
    print('Labels sorting ended ... now plotting...')

    for index in range(0, len(PC1data)):
        plt.scatter(PC1data[index], PC2data[index], s=3)
        print('Index is : %d' % index)
    print('Plotting done')

    plt.savefig('../plots/movieCluster.png')
#================================================================================================================================================
def main():
    # Import data as pandas csv DataFrame. skip 'NA' or empty items.
    movie_data = pd.read_csv('../data/additionalData.csv', skip_blank_lines=True).dropna()
    print(movie_data)

    # Specify the number of clusters desired here.
    numMovieClusters = 10

    # Defining movie features selected
    movieFeatures = ['year', 'runtime', 'Action', 'Adventure',
                 'Animation', 'Biography', 'Comedy', 'Crime',
                 'Documentary', 'Drama', 'Family', 'Fantasy',
                'Film Noir', 'Game Show', 'History', 'Horror',
                'Music', 'Musical', 'Mystery', 'Romance',
                'Sci-Fi', 'Short', 'Sport', 'Superhero',
                'Thriller', 'War', 'Western']

    #features = ['year', 'runtime']

    # Separating out the values of the features by labels (loc)
    movie_data_features = movie_data.loc[:, movieFeatures].values

    ## **** NOTE: no MovieID are listed in "additionalData.csv"????

    # Conducting Agglomerative clustering for the movies.
    #X = StandardScaler().fit_transform(x)
    movieClusters = AgglomerativeClustering(affinity='euclidean', compute_full_tree='auto',
                connectivity=None, linkage='ward', memory=None, n_clusters=numMovieClusters,
                pooling_func='deprecated')
    movieClusters.fit(movie_data_features)

    # Using Principle component Analysis (PCA) to two dimensions to see how the movies will fall into clusters.
    PCA_results = PCA(n_components=2)
    principalComponentsMovies = PCA_results.fit_transform(movie_data_features)

    # Redefining the movies based on the clusters and their labels along the new PCs.
    principleDataFrame = pd.DataFrame(data=principalComponentsMovies, columns=['principal component 1', 'principal component 2'])
    movieClusterLabels = movieClusters.labels_

    # Write labels to data file (Optional)
    #writeMovieClusterLabels('../data/movieIDClusters.csv', movieClusterLabels)

    # Plotting the clusters along the newfound PCA axes.
    plotMovieClusters(principleDataFrame, movieClusterLabels, numMovieClusters,
                      'Visualizing Clustered Movies Clustered in ' + str(numMovieClusters) + ' Clusters',
                      'PCA Component 1', 'PCA Component 2')


if __name__ == "__main__":
    main()


