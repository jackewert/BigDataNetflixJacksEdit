#https://www.kdnuggets.com/2016/10/beginners-guide-neural-networks-python-scikit-learn.html/2
#https://stackoverflow.com/questions/20485592/how-do-i-create-a-sklearn-datasets-base-bunch-object-in-scikit-learn-from-my-own
#https://github.com/mGalarnyk/Python_Tutorials/blob/master/Sklearn/PCA/PCA_Data_Visualization_Iris_Dataset_Blog.ipynb
import pandas as pd



movie_data = pd.read_csv('../../Data/additionalData.csv', skip_blank_lines=True).dropna()
train = pd.read_csv('../../Data/additionalData.csv',names=['title','year','runtime','Action','Adventure','Animation','Biography','Comedy','Crime','Documentary','Drama','Family','Fantasy','Film Noir','Game Show','History','Horror','Music','Musical','Mystery','Romance','Sci-Fi','Short', 'Sport','Superhero','Thriller','War','Western'])
print(train.head())
feature_cols = ['year','runtime','Action','Adventure','Animation','Biography','Comedy','Crime','Documentary','Drama','Family','Fantasy','Film Noir','Game Show','History','Horror','Music','Musical','Mystery','Romance','Sci-Fi','Short', 'Sport','Superhero','Thriller','War','Western'])
X = train.loc[:, feature_cols]
X.shape
y = train.Survived
y.shape
