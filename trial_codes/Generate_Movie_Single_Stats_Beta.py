'''
Name        : Generate_Movie_Single_Stats_Beta.py
Version     : 1.0b
Author      : Alpaca (Rebecca & Yuchen)


Input: MovieID
Output is Rating Statistics: Mean, Minimum, Maximum, Standard Deviation, (other stuff to added later)

Details:
1. This function will return statistics for a single User ratings for all movies that that user watches
2. It will call Mine_Movie_Rating.py to get all the movie ratings for a particular user.
3. Its output will be pass to Generate_User_Cluster_Stat.py
'''

'''
programs to generate movieids with their max, min and average ratings:
'''

'''
program to generate stats for data in combined data 1:
'''
def stats():
    a = 1
    for line in open("../Data/combined_data_1.txt"):
        if ':' in line:
            if a>1:
                print(max(list), min(list), ave(list))
                print('\n')
            list = []
            print(line)
        else:
            data = line.split(',')[1].strip('\r').strip('\n').strip('\r').strip('\n')
            data = int(data)
            list.append(data)
        a += 1
    print(max(list), min(list), ave(list))

def ave(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)

if 1:
    stats()

'''
program to generate stats for data in combined data 2:
'''
def stats():
    a = 1
    for line in open("/Users/Zhang/Desktop/Netflix/combined_data_2.txt"):
        if ':' in line:
            if a>1:
                print(max(list), min(list), ave(list))
                print('\n')
            list = []
            print(line)
        else:
            data = line.split(',')[1].strip('\r').strip('\n').strip('\r').strip('\n')
            data = int(data)
            list.append(data)
        a += 1
    print(max(list), min(list), ave(list))

def ave(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)

if 1:
    stats()

'''
program to generate stats for data in combined data 3:
'''
def stats():
    a = 1
    for line in open("/Users/Zhang/Desktop/Netflix/combined_data_3.txt"):
        if ':' in line:
            if a>1:
                print(max(list), min(list), ave(list))
                print('\n')
            list = []
            print(line)
        else:
            data = line.split(',')[1].strip('\r').strip('\n').strip('\r').strip('\n')
            data = int(data)
            list.append(data)
        a += 1
    print(max(list), min(list), ave(list))

def ave(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)

if 1:
    stats()

'''
program to generate stats for data in combined data 4:
'''
def stats():
    a = 1
    for line in open("/Users/Zhang/Desktop/Netflix/combined_data_4.txt"):
        if ':' in line:
            if a>1:
                print(max(list), min(list), ave(list))
                print('\n')
            list = []
            print(line)
        else:
            data = line.split(',')[1].strip('\r').strip('\n').strip('\r').strip('\n')
            data = int(data)
            list.append(data)
        a += 1
    print(max(list), min(list), ave(list))

def ave(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)

if 1:
    stats()

'''
combine data and delete blank lines
'''
def delblankline():
    infopen1 = open('/Users/Zhang/Desktop/stats1.txt', 'r', encoding="utf-8")
    infopen2 = open('/Users/Zhang/Desktop/stats2.txt', 'r', encoding="utf-8")
    infopen3 = open('/Users/Zhang/Desktop/stats3.txt', 'r', encoding="utf-8")
    infopen4 = open('/Users/Zhang/Desktop/stats4.txt', 'r', encoding="utf-8")
    outfopen = open('/Users/Zhang/Desktop/MovieStats.txt', 'w', encoding="utf-8")

    lines1 = infopen1.readlines()
    lines2 = infopen2.readlines()
    lines3 = infopen3.readlines()
    lines4 = infopen4.readlines()
    for line in lines1:
        if line.split():
            outfopen.writelines(line)
        else:
            outfopen.writelines("")
    for line in lines2:
        if line.split():
            outfopen.writelines(line)
        else:
            outfopen.writelines("")
    for line in lines3:
        if line.split():
            outfopen.writelines(line)
        else:
            outfopen.writelines("")
    for line in lines4:
        if line.split():
            outfopen.writelines(line)
        else:
            outfopen.writelines("")

    infopen1.close()
    infopen2.close()
    infopen3.close()
    infopen4.close()
    outfopen.close()


delblankline()

'''
see the data in \Data\MovieStats.txt
'''