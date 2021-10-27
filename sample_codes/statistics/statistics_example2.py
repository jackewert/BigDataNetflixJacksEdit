# Using Numpy statistical libraries to exclude NAs
import numpy as np

#  1. NA median

a = np.array([[10.0, 7, 4], [3, 2, 1]])
a[0, 1] = np.nan
a
#array([[ 10.,  nan,   4.],   [  3.,   2.,   1.]])
np.median(a)
#nan


np.nanmedian(a, axis=0)

np.median(a, axis=1)

b = a.copy()
np.nanmedian(b, axis=1, overwrite_input=True)

assert not np.all(a==b)

b = a.copy()
np.nanmedian(b, axis=None, overwrite_input=True)

assert not np.all(a==b)


#=============================
#2. NA mean

a = np.array([[1, np.nan], [3, 4]])
np.nanmean(a)
np.nanmean(a, axis=0)
np.nanmean(a, axis=1)

#=============================
#https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.nanstd.html#numpy.nanstd
# 3. NA Std

a = np.array([[1, np.nan], [3, 4]])
np.nanstd(a)
#1.247219128924647
np.nanstd(a, axis=0)
#array([ 1.,  0.])
np.nanstd(a, axis=1)
#array([ 0.,  0.5])

