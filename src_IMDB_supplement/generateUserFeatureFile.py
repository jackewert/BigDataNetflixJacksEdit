'''

Name        : generateUserFeatureFile.py
Version     : 1.0a
Author      : Alpaca
Description : This file generates user feature file in order to cluster them later
Dependencies: additionalData.csv | customerIDDict.csv

'''

from collections import OrderedDict


# This function is used to read additional data
def read_additional_data():
    filename = '../data/additionalData.csv'
    filehandle = open(filename, 'r')
    additional_data_dict = OrderedDict()
    line = filehandle.readline()
    line = filehandle.readline()
    line = line.strip('\n').strip('\r').strip('\n').strip('\r')
    count = 1
    while line:
        data = line.split(',')[1:]
        for element in data:
            if count not in additional_data_dict:
                additional_data_dict[count] = element
            else:
                additional_data_dict[count] += ','+element
        line = filehandle.readline()
        line = line.strip('\n').strip('\r').strip('\n').strip('\r')
        count += 1
    filehandle.close()
    return additional_data_dict


# This function is responsible for reading customer dict
def read_customer_dict(additional_data_dict):
    filename = '../data/customerIDDict.csv'
    filehandle = open(filename, 'r')
    line = filehandle.readline()
    userfeatures = dict()
    print('Reading customer dict started...')
    while line:
        features = [0] * 150
        data = line.split(':')
        cid = data[0]
        data = data[1]
        datapoints = data.split(',')
        for datapoint in datapoints:
            moviefeatures = additional_data_dict[int(datapoint.split('|')[0])]
            rating = int(datapoint.split('|')[2])
            genres = moviefeatures.split(',')[3:]
            for index in range(0, len(genres)):
                if genres[index] == '1':
                    features[index] += 1
                    features[25+(index*rating)] += 1
        featurestr = ''
        for f in features:
            if featurestr == '':
                featurestr = str(f)
            else:
                featurestr += ','+str(f)
        userfeatures[cid] = featurestr
        line = filehandle.readline()
    filehandle.close()
    print('Reading customer dict completed...')
    print('No of features are  : %d' % len(features))
    print('No of users are : %d' % len(userfeatures))
    return userfeatures


# This function is responsible for writing users features to file
def write_features_to_file(userfeatures_dict):
    filename = '../data/userfeatures.csv'
    filehandle = open(filename, 'w')
    for key in userfeatures_dict.keys():
        filehandle.write(str(key)+',')
        filehandle.write(userfeatures_dict[key])
        filehandle.write('\n')
    filehandle.close()


# Main function
def main():
    additional_data_dict = read_additional_data()
    user_features_dict = read_customer_dict(additional_data_dict)
    write_features_to_file(user_features_dict)
    # Debug print statement
    # for key in additional_data_dict:
    #     print(additional_data_dict[key])



if __name__ == "__main__":
    main()



