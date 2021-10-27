'''
Name        : PlotData.py
Version     : 1.0a
Author      : Alpaca

'''
#import

#================================================================================================================================================
def readDataFiles():
    customerIDRatings = dict()
    # data files. Using the combined data, which are compiled from +17,000 individual files, training data set
    dataFns = ['../data/combined_data_1.txt','../data/combined_data_2.txt',
                '../data/combined_data_3.txt','../data/combined_data_4.txt']
    for fn in dataFns:
        fh = open(fn,'r',encoding='latin1')
        line = fh.readline()
        movieId = ''
        while line:
            if ':' in line:
                # reading the movie title followed by a comma
                movieTitle = line.split(':')[0]
                # print(movieTitle)
            else:
                data = line.split(',')
                if data[0] in customerIDRatings:
                    # data[0] is the CustomerID
                    # data[1] is the Date of Rating
                    # data[2] is the Rating given by the customer
                    customerIDRatings[data[0]] += ','+str(movieTitle+'|'+data[2].strip('\r').strip('\n').strip('\r').strip('\n')+'|'+data[1])
                else:
                    customerIDRatings[data[0]] = str(movieTitle+'|'+data[2].strip('\r').strip('\n').strip('\r').strip('\n')+'|'+data[1])
            line = fh.readline()
        fh.close()
    return customerIDRatings

#================================================================================================================================================
def main():
    customerIDRatings = readDataFiles()



if __name__ == "__main__":
    main()