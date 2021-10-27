#reservoir sampling

import pandas as pd

import random

import numpy as np

#First select k random indices between 0 and length of the array

arr=[0]
k=8
indices = np.random.randint(0,arr.shape[0],k)

#then subsample data using these indices
random_sample = arr[indices]

