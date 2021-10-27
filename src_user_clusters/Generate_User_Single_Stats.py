'''
Name        : Generate_User_Single_Stats.py
Version     : 1.0b
Author      : Alpaca (Rebecca & Yuchen)


Input: UserID
Output is Rating Statistics: Mean, Minimum, Maximum, Standard Deviation, (other stuff to added later)

Details:
1. This function will return statistics for a single User ratings for all movies that that user watches
2. It will call Mine_Movie_Rating.py to get all the movie ratings for a particular user.
3. Its output will be pass to Generate_User_Cluster_Stat.py
'''


'''
program to generate userids with their max, min and average ratings
'''
import operator

doc = open(r'/Users/Zhang/Desktop/out.txt', 'w')


def stats():
    a = 0
    list = []
    for line in open("/Users/Zhang/Desktop/Netflix/combined_data_1.txt"):
        if ':' not in line:
            list1 = []
            data1 = line.split(',')[0].strip('\r').strip('\n').strip('\r').strip('\n')
            data2 = line.split(',')[1].strip('\r').strip('\n').strip('\r').strip('\n')
            data1 = int(data1)
            data2 = int(data2)
            list1.append(data1)
            list1.append(data2)
            list.append(list1)
    for line in open("/Users/Zhang/Desktop/Netflix/combined_data_2.txt"):
        if ':' not in line:
            list1 = []
            data1 = line.split(',')[0].strip('\r').strip('\n').strip('\r').strip('\n')
            data2 = line.split(',')[1].strip('\r').strip('\n').strip('\r').strip('\n')
            data1 = int(data1)
            data2 = int(data2)
            list1.append(data1)
            list1.append(data2)
            list.append(list1)
    for line in open("/Users/Zhang/Desktop/Netflix/combined_data_3.txt"):
        if ':' not in line:
            list1 = []
            data1 = line.split(',')[0].strip('\r').strip('\n').strip('\r').strip('\n')
            data2 = line.split(',')[1].strip('\r').strip('\n').strip('\r').strip('\n')
            data1 = int(data1)
            data2 = int(data2)
            list1.append(data1)
            list1.append(data2)
            list.append(list1)
    for line in open("/Users/Zhang/Desktop/Netflix/combined_data_4.txt"):
        if ':' not in line:
            list1 = []
            data1 = line.split(',')[0].strip('\r').strip('\n').strip('\r').strip('\n')
            data2 = line.split(',')[1].strip('\r').strip('\n').strip('\r').strip('\n')
            data1 = int(data1)
            data2 = int(data2)
            list1.append(data1)
            list1.append(data2)
            list.append(list1)
    list.sort()
    b = 0
    c = []
    for m in list:
        if b != len(list) - 1:
            if operator.eq(m[0], list[b + 1][0]) == True:
                c.append(m[1])
            else:
                c.append(m[1])
                avg = ave(c)
                print(m[0], max(c), min(c), avg, file=doc)
                c = []
        else:
            c.append(m[1])
            avg = ave(c)
            print(m[0], max(c), min(c), avg, file=doc)
            c = []
        b += 1


def ave(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)


if 1:
    stats()

doc.close()