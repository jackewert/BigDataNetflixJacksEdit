#https://github.com/mGalarnyk/Python_Tutorials/blob/master/Python_Basics/Linear_Regression/Linear_Regression_Python.ipynb
#link above with original code and what each line means more specifically
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
%pylab inline
import matplotlib.pyplot as plt

#filtered_data = pd.read_csv("linear.csv")
#this is the data input type which is the same as we used so if We change the x and y we should be good.
npMatrix = np.matrix(filtered_data)
X, Y = npMatrix[:,0], npMatrix[:,1]
mdl = LinearRegression().fit(X,Y) # either this or the next line
#mdl = LinearRegression().fit(filtered_data[['x']],filtered_data.y)
m = mdl.coef_[0]
b = mdl.intercept_

plt.scatter(X,Y, color='blue')
plt.plot([0,100],[b,m*100+b],'r')
plt.title('Linear Regression Example', fontsize = 20)
plt.xlabel('X', fontsize = 15)
plt.ylabel('Y', fontsize = 15)
plt.show()