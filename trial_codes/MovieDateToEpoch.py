'''
Name        : MovieDateToEpoch.py
Version     : 1.0b
Author      : Alpaca

Input: Movie Date (YYYY-MM-DD) in string
Output: 0 or 1 (successful or failed run)

Libraries: time

Details: this movie will convert dates to time (epoch), which can be used for time-series analysis.
'''
import time

def MovieDateToEpoch(DateRated):
    for CurrentItem in DateRated:
        DateRatedFormat = '%Y-%m-%d'
        DateRatedEpoch = int(time.mktime(time.strptime(CurrentItem, DateRatedFormat)))
    return DateRatedEpoch

