'''
Name        : customerIDPlot.py
Version     : 1.0a
Author      : Alpaca

'''

from matplotlib import pyplot as plt
import datetime
import time

#================================================================================================================================================
def readCombinedDataForCustomerIDRatings():
    customerIDRatings = dict()
    # data files
    combinedDataFileNames = ['../data/combined_data_1.txt','../data/combined_data_2.txt',
                '../data/combined_data_3.txt','../data/combined_data_4.txt']
    for currentFileName in combinedDataFileNames:
        fileHandle = open(currentFileName,'r')
        line = fileHandle.readline()
        movieId = ''
        while line:
            if ':' in line:
                movieTitle = line.split(':')[0]
                print(movieTitle)
            else:
                data = line.split(',')
                if data[0] in customerIDRatings:
                    customerIDRatings[data[0]] += ','+str(movieTitle+'|'+data[2].strip('\r').strip('\n').strip('\r').strip('\n')+'|'+data[1])
                else:
                    customerIDRatings[data[0]] = str(movieTitle+'|'+data[2].strip('\r').strip('\n').strip('\r').strip('\n')+'|'+data[1])
            line = fileHandle.readline()
        fileHandle.close()
    return customerIDRatings

#================================================================================================================================================
def readCombinedDataForMovieIDRatings():
    movieIDRatings = dict()
    # data files
    combinedDataFiles = ['../data/combined_data_1.txt', '../data/combined_data_2.txt',
                '../data/combined_data_3.txt', '../data/combined_data_4.txt']
    for CurrentFileName in combinedDataFiles:
        CurrentFileHandle = open(CurrentFileName,'r')
        currentLine = CurrentFileHandle.readline()
        movieId = ''
        while currentLine:
            if ':' in currentLine:
                movieTitle = currentLine.split(':')[0]
                print(movieTitle)
            else:
                data = currentLine.split(',')
                if movieTitle in movieIDRatings:
                    movieIDRatings[movieTitle] += ','+str(data[0]+'|'+data[2].strip('\r').strip('\n').strip('\r').strip('\n')+'|'+data[1])
                else:
                    movieIDRatings[movieTitle] = str(data[0]+'|'+data[2].strip('\r').strip('\n').strip('\r').strip('\n')+'|'+data[1])

            currentLine = CurrentFileHandle.readline()
        CurrentFileHandle.close()
    return movieIDRatings

#================================================================================================================================================
def writeMovieIDDictDataFiles(DictionaryKeys, fileName):
    fileHandle = open(fileName, 'w')
    count = 0
    for currentKey in DictionaryKeys:
        fileHandle.write(currentKey +':' + DictionaryKeys[currentKey] + '\n')
        count += 1
        if count % 1000 == 0:
            print(count)
    fileHandle.close()

#================================================================================================================================================
def readCustomerIDDictDataFile(UserID, fileName):
    fileName = '../data/customerIDDict.csv'
    fileHandle = open(fileName, 'r')
    line = fileHandle.readline()
    i = 0
    while i < UserID and line:
        line = fileHandle.readline()
        i += 1
    print(line)
    return line

#================================================================================================================================================
def plotTrendTimeline(dictEntry):
    # Extract Ratings for UserID (index is 1)
    UserIDdata = dictEntry.split(':')[1].split(',')
    RatingData = dict()
    finalDict = dict()
    for currentUserData in UserIDdata:
        CurrentRating = int(currentUserData.split('|')[2].strip('\r').strip('\n').strip('\r').strip('\n'))

        DateRated = currentUserData.split('|')[1]          # date in YYYY-MM-DD format
        DateRatedFormat='%Y-%m-%d'
        DateRatedEpoch = int(time.mktime(time.strptime(DateRated,DateRatedFormat)))
        RatingData[DateRatedEpoch] = CurrentRating
    sortedKeys = sorted(RatingData)
    print(RatingData)
    index = 1
    X = []
    Y = []
    for s in sortedKeys:
        X.append(s)
        Y.append(RatingData[s])
        index += 1
    plt.plot(X, Y)
    plt.xlim(sortedKeys[0],sortedKeys[-1])
    plt.ylim(0,5.5)
    plt.title('CustomerID (Ratings vs time)')
    plt.xlabel('Time in epoch')
    plt.ylabel('Rating (1-5)')
    plt.show()

#================================================================================================================================================
def main():
    #customerIDRatings = readDataFiles()
    #writeDataFiles(customerIDRatings,'../data/customerIDDict.csv')
    #plotTrendTimeline(readFile(10,'../data/customerIDDict.csv'))
    movieIDRatings = readCombinedDataForMovieIDRatings()
    writeMovieIDDictDataFiles(movieIDRatings, '../data/movieIDDict.csv')
    #plotTrendTimeline(readFile(10,'../data/movieIDDict.csv'))


if __name__ == "__main__":
    main()
