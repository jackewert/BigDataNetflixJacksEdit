'''

Name        : validateIMDBData.py
Version     : 1.0a
Author      : Alpaca
Requirements: Add title.basics.tsv file in data folder

'''

#================================================================================================================================================
#imports
import collections

#================================================================================================================================================
def read_original_movie_titles():
    path = '../data/movie_titles.csv'
    print('Reading movie tiles...')
    FileHeader = open(path, 'r', encoding='latin1')
    CurrentLine = FileHeader.readline()
    OrderedTitles = collections.OrderedDict()        #An OrderedDict is a dict that remembers the order that keys were first inserted.
    while CurrentLine:
        # Movies Info are: "Movie ID, Year, Title"
        MovieData = CurrentLine.split(',')
        OrderedTitles[MovieData[2].strip('\r').strip('\n').strip('\r').strip('\n')+','+MovieData[0]] = MovieData[1]
        CurrentLine = FileHeader.readline()
    FileHeader.close()
    for key in OrderedTitles:
        print(key)
    print(len(OrderedTitles))
    print('Reading movie titles completed...')
    return OrderedTitles

#================================================================================================================================================
def read_supplemented_movie_titles():
    print('Reading imdb file...')
    path = '../data/title.basics.tsv'
    fileHeader = open(path, 'r', encoding='latin1')
    CurrentLine = fileHeader.readline()
    CurrentLine = fileHeader.readline()
    suppTitles = dict()
    while CurrentLine:
        suppData = CurrentLine.split('\t')
        suppTitles[suppData[2]] = suppData[5]+'\t'+suppData[7]+'\t'+suppData[8]
        CurrentLine = fileHeader.readline()
    fileHeader.close()

    print('Reading imdb file completed.')

    return suppTitles

#================================================================================================================================================
def compares_titles(OriginalTitles, SupplementedTitles, writeFlag):
    hit = 0
    miss = 0
    count = 0

    if writeFlag == 1:
        FileName = '../data/additionalData.csv'
        FileHeader = open(FileName, 'w')

        Genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy',
                 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film Noir',
                 'Game Show', 'History', 'Horror', 'Music','Musical', 'Mystery', 'Romance',
                 'Sci-Fi', 'Short', 'Sport', 'Superhero', 'Thriller', 'War', 'Western']

        # Writing headers
        FileHeader.write('title,runtime,year')

        for currentGenre in Genres:
            FileHeader.write(','+currentGenre)
        FileHeader.write('\n')

    for CurrentOriginalTitle in OriginalTitles.keys():
        count += 1
        movieTitle = CurrentOriginalTitle.split(',')[0]
        if movieTitle in SupplementedTitles.keys():
            hit += 1
            if writeFlag == 1:
                supplementedData = SupplementedTitles[movieTitle].split('\t')
                rTitles = supplementedData[1]
                Year = OriginalTitles[CurrentOriginalTitle]
                if rTitles == '\\N':
                    rTitles = 0
                FileHeader.write(movieTitle+','+str(rTitles)+','+str(Year))
                MovieGenres = supplementedData[2].split(',')
                for currentGenre in Genres:
                    if currentGenre in MovieGenres:
                        FileHeader.write(',1')
                    else:
                        FileHeader.write(',0')
                FileHeader.write('\n')
        else:
            miss += 1
            if writeFlag == 1:
                FileHeader.write(movieTitle+',-1,-1')
                for currentGenre in Genres:
                        FileHeader.write(',-1')
                FileHeader.write('\n')
        #if count % 10 == 0:
        #    print('Count is : %d' % count)
    if writeFlag == 1:
        FileHeader.close()
    print('Hits are : %d and Misses are : %d' % (hit, miss))

#================================================================================================================================================
def main():
    OriginalTitles = read_original_movie_titles()
    print(len(OriginalTitles))
    SupplementedTitlesIMDB = read_supplemented_movie_titles()
    compares_titles(OriginalTitles, SupplementedTitlesIMDB, 1)


if __name__ == "__main__":
    main()
