'''
Name            : ProbeUserIDs.py
Version         : 1.0a
Author          : Alpaca
'''


def create_probe_dict(movie_dict):
    file_name_probe = '../data/probe.txt'
    file_name = '../data/probeRating.csv'
    file_header = open(file_name, 'w')
    file_header_probe = open(file_name_probe, 'r')
    line = file_header_probe.readline()
    print('Started reading probe file...')
    count = 0
    flagnewline = 0
    while line:
        count += 1
        if count % 1000 == 0:
            print('Count is : %d' % count)
        if ':' in line:
            if flagnewline == 1:
                file_header.write('\n')
            movidId = line.split(':')[0]
            data = movie_dict[movidId].split(',')
            userID = dict()
            for d in data:
                info = d.split('|')
                uid = info[0]
                rat = info[2].strip('\r').strip('\n').strip('\r').strip('\n')
                userID[uid] = rat
            file_header.write(str(movidId) + ':')
            flag = 0
            flagnewline = 1
        else:
            uid = line.strip('\r').strip('\n').strip('\r').strip('\n')
            if flag == 0:
                file_header.write(str(uid)+'|'+str(userID[uid]))
                flag = 1
            else:
                file_header.write(','+str(uid) + '|' + str(userID[uid]))
        line = file_header_probe.readline()
    file_header_probe.close()
    file_header.close()
    print('Finished reading probe file...')


def get_movie_dict():
    movie_dict = dict()
    file_name = '../data/movieIDDict.csv'
    file_handle = open(file_name, 'r')
    print('Reading movie dict started...')
    line = file_handle.readline()
    count = 0
    while line:
        count += 1
        data = line.split(':')
        movie_dict[data[0]] = data[1]
        line = file_handle.readline()
        if count % 1000 == 0:
            print('Count is : %d' % count)
    file_handle.close()
    print('Reading movie dict ended...')
    return movie_dict


def main():
    movie_dict = get_movie_dict()
    create_probe_dict(movie_dict)


if __name__ == "__main__":
    main()