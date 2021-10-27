'''
Name        : generateDicts.py
Version     : 1.0a
Author      : Alpaca

'''

#================================================================================================================================================
from matplotlib import pyplot as plt
import datetime
import time

#================================================================================================================================================
def readDataFiles():
    customerIDRatingsDict = dict()
    # data files
    dataFileNames = ['../data/combined_data_1.txt','../data/combined_data_2.txt',
                '../data/combined_data_3.txt','../data/combined_data_4.txt']
    # Lopping through all 'combined_data_*.txt
    for FileName in dataFileNames:
        FileHeader = open(FileName,'r')
        currentLineRead = FileHeader.readline()
        movieId = ''
        while currentLineRead:
            # MovieID is followed by ":"
            if ':' in currentLineRead:
                movieTitle = currentLineRead.split(':')[0]
                print(movieTitle)
            else:
                # what follows will be "UserID, Rating, Date of Rating (YYYY-MM-DD)
                data = currentLineRead.split(',')
                if data[0] in customerIDRatingsDict:
                    customerIDRatingsDict[data[0]] += ',' +str(movieTitle+'|'+ data[2].strip('\r').strip('\n').strip('\r').strip('\n')+'|'+data[1])
                else:
                    customerIDRatingsDict[data[0]] = str(movieTitle+'|'+data[2].strip('\r').strip('\n').strip('\r').strip('\n')+'|'+data[1])
            currentLineRead = FileHeader.readline()
        FileHeader.close()
    return customerIDRatingsDict


#================================================================================================================================================
def readMovieWiseDataFiles():
    movieIDRatings = dict()
    # data files
    dataFns = ['../data/combined_data_1.txt','../data/combined_data_2.txt',
                '../data/combined_data_3.txt','../data/combined_data_4.txt']
    for fn in dataFns:
        fh = open(fn,'r')
        line = fh.readline()
        movieTitle = ''
        title = 0
        count = 0
        while line:
            if ':' in line:
                movieTitle = line.split(':')[0]
                count += 1
                if count == 101:
                    break
                print(movieTitle)
                title = 1
            else:
                data = line.split(',')
                if title == 0:
                    movieIDRatings[movieTitle] += ','+str(data[0]+'|'+data[2].strip('\r').strip('\n').strip('\r').strip('\n')+'|'+data[1])
                else:
                    movieIDRatings[movieTitle] = str(data[0]+'|'+data[2].strip('\r').strip('\n').strip('\r').strip('\n')+'|'+data[1])
                    title = 0
            line = fh.readline()
        fh.close()
    print(movieIDRatings)
    return movieIDRatings

#================================================================================================================================================
def writeDataFiles(dictn,fn):
    fh = open(fn,'w')
    count = 0
    for key in dictn:
        fh.write(key+':'+dictn[key]+'\n')
        count += 1
        if count % 1000 == 0:
            print(count)
    fh.close()

#================================================================================================================================================
def readFile(str,fn):
    fh = open(fn,'r')
    line = fh.readline()
    i = 0
    while line:
        if str == line.split(':')[0]:
            break
        line = fh.readline()
        i += 1
    print(line)
    return line

#================================================================================================================================================
def plotTrendTimeline(dictEntry, movie):
    data = dictEntry.split(':')[1].split(',')
    dataDict = dict()
    finalDict = dict()
    for d in data:
        rating = int(d.split('|')[2].strip('\r').strip('\n').strip('\r').strip('\n'))
        dateInfo = d.split('|')[1]
        p='%Y-%m-%d'
        epoch = int(time.mktime(time.strptime(dateInfo,p)))
        dataDict[epoch] = rating
    sortedKeys = sorted(dataDict)
    print(dataDict)
    index = 1
    X = []
    Y = []
    for s in sortedKeys:
        X.append(s)
        Y.append(dataDict[s])
        index += 1
    plt.plot(X, Y)
    plt.xlim(sortedKeys[0],sortedKeys[-1])
    plt.ylim(0,5.5)
    if movie == 0:
        plt.title('CustomerID (Ratings vs time)')
        plt.xlabel('Time in epoch')
        plt.ylabel('Rating (1-5)')
        plt.savefig('../plots/customerIDPlot.png')
        plt.clf()
    else:
        plt.title('MovieID (Ratings vs time)')
        plt.xlabel('Time in epoch')
        plt.ylabel('Rating (1-5)')
        plt.savefig('../plots/movieIDPlot.png')
        plt.clf()

#================================================================================================================================================
def main():
    #uncomment next two lines in order to generate customerID Dictionary
    #It may take a while to run depending on speed
    customerIDRatings = readDataFiles()
    writeDataFiles(customerIDRatings, '../data/customerIDDict.csv')
    #plotTrendTimeline(readFile('370256','../data/customerIDDict.csv'),0)
    #print('Starting read')
    #uncomment next 3 lines in order to generate movieID Dictionary
    #movieIDRatings = readMovieWiseDataFiles()
    #print('Ending reead')
    #print('Starting write')
    #writeDataFiles(movieIDRatings,'../data/movieIDDict.csv')
    #print('Ending write')
    # plotting code | unlock plotting code as needed
    #print('plotting')
    #plotTrendTimeline(readFile('15','../data/movieIDDict.csv'),1)
    #print('plotting done')


if __name__ == "__main__":
    main()
