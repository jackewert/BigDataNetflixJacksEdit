import statistics

'''
program to generate stats for data in combined data 1:
'''
def stats1():
    a = 1
    for line in open("/Users/Zhang/Desktop/Netflix/combined_data_1.txt"):
        if ':' in line:
            if a>1:
                print(max(list), min(list), ave(list), statistics.stdev(list), file = doc)
                print('\n', file = doc)
            list = []
            print(line, file = doc)
        else:
            data = line.split(',')[1].strip('\r').strip('\n').strip('\r').strip('\n')
            data = int(data)
            list.append(data)
        a += 1
    print(max(list), min(list), ave(list), statistics.stdev(list), file = doc)

'''
program to generate stats for data in combined data 2:
'''
def stats2():
    a = 1
    for line in open("/Users/Zhang/Desktop/Netflix/combined_data_2.txt"):
        if ':' in line:
            if a>1:
                print(max(list), min(list), ave(list), statistics.stdev(list), file = doc)
                print('\n', file = doc)
            list = []
            print(line, file = doc)
        else:
            data = line.split(',')[1].strip('\r').strip('\n').strip('\r').strip('\n')
            data = int(data)
            list.append(data)
        a += 1
    print(max(list), min(list), ave(list), statistics.stdev(list), file = doc)

'''
program to generate stats for data in combined data 3:
'''
def stats3():
    a = 1
    for line in open("/Users/Zhang/Desktop/Netflix/combined_data_3.txt"):
        if ':' in line:
            if a>1:
                print(max(list), min(list), ave(list), statistics.stdev(list), file = doc)
                print('\n', file = doc)
            list = []
            print(line, file = doc)
        else:
            data = line.split(',')[1].strip('\r').strip('\n').strip('\r').strip('\n')
            data = int(data)
            list.append(data)
        a += 1
    print(max(list), min(list), ave(list), statistics.stdev(list), file = doc)

'''
program to generate stats for data in combined data 4:
'''
def stats4():
    a = 1
    for line in open("/Users/Zhang/Desktop/Netflix/combined_data_4.txt"):
        if ':' in line:
            if a>1:
                print(max(list), min(list), ave(list), statistics.stdev(list), file = doc)
                print('\n', file = doc)
            list = []
            print(line, file = doc)
        else:
            data = line.split(',')[1].strip('\r').strip('\n').strip('\r').strip('\n')
            data = int(data)
            list.append(data)
        a += 1
    print(max(list), min(list), ave(list), statistics.stdev(list), file = doc)

def ave(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)

'''
put all stats into one file
'''
doc = open(r'/Users/Zhang/Desktop/GenerateMovieStats.txt', 'w')
stats1()
stats2()
stats3()
stats4()
doc.close()

'''
delete blank lines
'''
def delblankline():
    infopen1 = open('/Users/Zhang/Desktop/GenerateMovieStats.txt', 'r', encoding="utf-8")
    outfopen = open('/Users/Zhang/Desktop/MovieStats.txt', 'w', encoding="utf-8")

    lines1 = infopen1.readlines()
    for line in lines1:
        if line.split():
            outfopen.writelines(line)
        else:
            outfopen.writelines("")

    infopen1.close()

delblankline()