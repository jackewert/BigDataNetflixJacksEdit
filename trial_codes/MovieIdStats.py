'''
function that generates movie stats(max,min,avg,stdev) by using the MovieStats.txt
input: movieId(string)
output: ('max','min','avg','stdev')
'''
def MovieIdStats(movieid):
    file = open('/Users/Zhang/PycharmProjects/BigDataNetflixProject2018/Data/MovieStats.txt', 'r')
    # open the file 'MovieStats.txt' under 'Data' folder
    # 'GenerateMovieStats.py' under 'src_naive_approach' folder shows how I get these stats
    lines = file.readlines()
    linecounter = 0
    for line in lines:
        if (movieid + ':') in line:
            return(lines[linecounter+1].split(' ')[0].strip('\r').strip('\n').strip('\r').strip('\n'), lines[linecounter+1].split(' ')[1].strip('\r').strip('\n').strip('\r').strip('\n'), lines[linecounter+1].split(' ')[2].strip('\r').strip('\n').strip('\r').strip('\n'), lines[linecounter+1].split(' ')[3].strip('\r').strip('\n').strip('\r').strip('\n'))
        linecounter += 1

'''
test
'''
print(MovieIdStats('13'))   #test movieId = 13