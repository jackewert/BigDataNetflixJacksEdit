'''
Name        : compareDB.py
Version     : 1.0a
Author      : Alpaca

'''

import sys

debug = 1

def ifDebug():
    global debug
    return debug

def read_movie_titles():
    path = '../data/movie_titles.csv'
    fh = open(path,'r',encoding='latin1')
    line = fh.readline()
    line = fh.readline()
    titles = []
    while line:
        data = line.split(',')[-1].strip('\r').strip('\n').strip('\r').strip('\n')
        data = data.lower()
        titles.append(data)
        line = fh.readline()
    fh.close()
    return titles

def read_imdb_titles():
    path = './imdb.csv'
    fh = open(path,'r',encoding='latin1')
    line = fh.readline()
    line = fh.readline()
    titles = dict()
    while line:
        line = line.split(',')
        if line[3] not in titles:
            titles[line[3].lower()] = 1
        line = fh.readline()
    fh.close()
    return titles

def main():
    hit = 0
    miss = 0
    imdb_dict = read_imdb_titles()
    titles = read_movie_titles()
    for t in titles:
        if t in imdb_dict:
            print(t)
            hit += 1
        else:
            miss += 1
    print('Hits are : %d and misses are : %d' % (hit,miss))


if __name__ == "__main__":
    main()
