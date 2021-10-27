#https://github.com/mGalarnyk/Python_Tutorials/blob/master/Sklearn/PCA/PCA_Data_Visualization_Iris_Dataset_Blog.ipynb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


movie_data = pd.read_csv('../../Data/additionalData.csv', skip_blank_lines=True).dropna()
df = pd.read_csv('../../Data/additionalData.csv',names=['title','year','runtime','Action','Adventure','Animation','Biography','Comedy','Crime','Documentary','Drama','Family','Fantasy','Film Noir','Game Show','History','Horror','Music','Musical','Mystery','Romance','Sci-Fi','Short', 'Sport','Superhero','Thriller','War','Western'])

#have to remove all string variabels for standardscaler
del df['title']
df=df.iloc[1:] #removing row 0 which is collumn names

target1='Action'  #assigns lines 15 25 28  35 36 it's the comparable feature used in pca later

#removed title from featurese as its not longer in table not string
features = ['year','runtime','Action','Adventure','Animation','Biography','Comedy','Crime','Documentary','Drama','Family','Fantasy','Film Noir','Game Show','History','Horror','Music','Musical','Mystery','Romance','Sci-Fi','Short', 'Sport','Superhero','Thriller','War','Western']

x = df.loc[:, features].values
y = df.loc[:,[target1]].values #where runtime is  I think is what they compare it to has to be from data set title
x = StandardScaler().fit_transform(x)

pd.DataFrame(data = x, columns = features).head()    #this line should have  a graph output
print(type(df))

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])

collumnNumber = 27   #array collumns number? not certain what this number should be
principalDf.head(collumnNumber)
df[[target1]].head()
finalDf = pd.concat([principalDf, df[[target1]]], axis = 1)   #target1
finalDf.head(collumnNumber)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 Component PCA', fontsize = 20)


targets = ['1','0','-1']
colors = ['r', 'g', 'b']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf[target1] == 1
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
print(ax.grid())

print(pca.explained_variance_ratio_)

print(type(df))
