'''
Name        : getMovieInfo.py
Version     : 1.0a
Author      : Alpaca

'''
import sys
from threading import Thread
import requests
import json
#================================================================================================================================================
debug = 1

def ifDebug():
    global debug
    return debug

#================================================================================================================================================
def read_movie_titles():
    path = '../data/movie_titles.csv'
    fh = open(path,'r',encoding='latin1')
    line = fh.readline()
    line = fh.readline()
    titles = []
    while line:
        titles.append(line.split(',')[-1].strip('\r').strip('\n').strip('\r').strip('\n'))
        line = fh.readline()
    fh.close()
    return titles

#================================================================================================================================================
def fetch_thread(start,end):
    titles = read_movie_titles()
    basic_url = 'http://www.omdbapi.com/?apikey=9ec662d5&'
    fn = '../data/additionalData_'+str(start)+'_'+str(end)+'.csv'
    if ifDebug():
        print('Titles')
        for t in titles:
            print(t)
        print('Titles end')
    keys = ['Title', 'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writer', 'Actors', 'Plot',
            'Language', 'Country']
    fh = open(fn,'w')
    flag = 0
    for key in keys:
        if flag == 0:
            fh.write(str(key))
            flag = 1
        else:
            fh.write('\t'+str(key))
    fh.write('\n')
    for index in range(start, end):
        print('Title is : %s' % titles[index])
        url = basic_url + 't=%s' % titles[index]
        response = requests.get(url)
        json_data = json.loads(response.text)
        flag = 0
        for key in keys:
            if key in json_data:
                if flag == 0:
                    fh.write(str(json_data[key]))
                    flag = 1
                else:
                    fh.write('\t'+str(json_data[key]))
            else:
                if flag != 0:
                    fh.write('\t')
        fh.write('\n')

#================================================================================================================================================
def main():
    # fetch from imdb
    # tr = []
    # for index in range(0, 18):
    #     start = index*1000+1
    #     end = (index+1)*1000
    #     t = Thread(target=fetch_thread, args=(start, end))
    #     t.start()
    #     tr.append(t)
    # for index in range(0, 18):
    #     tr[index].join()

    # validate - 4.5 % not good.

    # hit = 0
    # miss = 0
    # for index in range(0, 18):
    #     start = index * 1000 + 1
    #     end = (index + 1) * 1000
    #     fn = '../data/additionalData_'+str(start)+'_'+str(end)+'.csv'
    #     fh = open(fn, 'r')
    #     line = fh.readline()
    #     line = fh.readline()
    #     while line:
    #         d = line.split('\t')
    #         if len(d[0]) > 1:
    #             hit += 1
    #         else:
    #             miss += 1
    #         line = fh.readline()
    #     fh.close()
    #     print('hit : %d and miss : %d' % (hit, miss))

    fn = '../data/title.basics.tsv'
    fh = open(fn,'r')
    line = fh.readline()
    print(line)
    line = fh.readline()
    print(line)
    fh.close()


if __name__ == "__main__":
    main()
