'''
Name        : plotTrends.py
Version     : 1.0a
Author      : Alpaca

'''

from matplotlib import pyplot as plt
import time
import datetime

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


def get_user_dict():
    user_dict = dict()
    file_name = '../data/customerIDDict.csv'
    file_handle = open(file_name, 'r')
    print('Reading user dict started...')
    line = file_handle.readline()
    count = 0
    while line:
        count += 1
        data = line.split(':')
        user_dict[data[0]] = data[1]
        line = file_handle.readline()
        if count % 1000 == 0:
            print('Count is : %d' % count)
    file_handle.close()
    print('Reading user dict ended...')
    return user_dict


def plot_movie_rating_distribution(movie_dict):
    print('Plotting movie rating started...')
    stars = [0, 0, 0, 0, 0]
    for id in range(1, 17770):
        if id % 100 == 0:
            print('Id is : %d' % id)
        info = movie_dict[str(id)]
        data = info.split(',')
        for d in data:
            datapoint = d.split('|')
            star = int(datapoint[2])
            stars[star-1] += 1
    X = [1, 2, 3, 4, 5]
    plt.bar(X, stars)
    plt.xlabel('Ratings')
    plt.ylabel('Distribution')
    plt.title('Rating distribution')
    plt.savefig('../plots/ratingsDistribution.png')
    plt.show()
    print('Plotting movie rating ended...')


def plot_movie_wise_distribution(movie_dict, write=0):
    print('Plotting movie wise rating started...')
    stars = [0, 0, 0, 0, 0]
    maxR = []
    minR = []
    avgR = []
    X = []
    file_name = '../data/movieMinAvgMax.csv'
    if write == 1:
        file_header = open(file_name, 'w')
    for id in range(1, 17771):
        X.append(id)
        rat = []
        if id % 100 == 0:
            print('Id is : %d' % id)
        info = movie_dict[str(id)]
        data = info.split(',')
        for d in data:
            datapoint = d.split('|')
            rat.append(int(datapoint[2]))
        maximum = max(rat)
        minimum = min(rat)
        average = sum(rat) / len(rat)
        if write == 1:
            file_header.write(str(id) + ',' + str(minimum) + ',' + str(average) + ',' + str(maximum) + '\n')
        maxR.append(maximum)
        minR.append(minimum)
        avgR.append(average)
    if write == 1:
        file_header.close()
    plt.plot(X, maxR)
    plt.plot(X, minR)
    plt.plot(X, avgR)
    plt.xlabel('movies')
    plt.ylabel('Ratings')
    plt.title('Movie Wise Rating Distribution')
    plt.savefig('../plots/movieWiseDistribution.png')
    plt.show()
    print('Plotting movie rating ended...')


def plot_user_wise_distribution(user_dict, write=0):
    print('Plotting user wise rating started...')
    maxR = []
    minR = []
    avgR = []
    X = []
    count = 0
    file_name = '../data/userMinAvgMax.csv'
    if write == 1:
        file_header = open(file_name, 'w')
    for id in user_dict.keys():
        count += 1
        X.append(count)
        rat = []
        if count % 1000 == 0:
            print('Id is : %d' % count)
        info = user_dict[str(id)]
        data = info.split(',')
        for d in data:
            datapoint = d.split('|')
            rat.append(int(datapoint[2]))
        maximum = max(rat)
        minimum = min(rat)
        average = sum(rat) / len(rat)
        if write == 1:
            file_header.write(str(id)+','+str(minimum)+','+str(average)+','+str(maximum)+'\n')
        maxR.append(maximum)
        minR.append(minimum)
        avgR.append(average)
    if write == 1:
        file_header.close()
    plt.plot(X, maxR)
    plt.plot(X, minR)
    plt.plot(X, avgR)
    plt.xlabel('Users')
    plt.ylabel('Ratings')
    plt.title('User Wise Rating Distribution')
    plt.savefig('../plots/userWiseDistribution.png')
    plt.show()
    print('Plotting movie rating ended...')


def plot_weekday_wise_ratings(movie_dict, weekends=0):
    print('Plotting weekday wise movie rating started...')
    days = []
    if weekends == 0:
        for index in range(0, 7):
            temp = [0, 0, 0, 0, 0]
            days.append(temp)
    else:
        for index in range(0, 2):
            temp = [0, 0, 0, 0, 0]
            days.append(temp)
    for id in range(1, 17771):
        if id % 100 == 0:
            print('Id is : %d' % id)
        info = movie_dict[str(id)]
        data = info.split(',')
        for d in data:
            datapoint = d.split('|')
            dateinfo = datapoint[1]
            dateparts = dateinfo.split('-')
            yr = int(dateparts[0])
            mnth = int(dateparts[1])
            day = int(dateparts[2])
            dt = datetime.datetime(yr, mnth, day)
            wkday = dt.weekday()
            star = int(datapoint[2])
            if weekends == 0:
                days[wkday][star - 1] += 1
            else:
                if wkday < 5:
                    days[0][star - 1] += 1
                else:
                    days[1][star - 1] += 1
    if weekends == 0:
        for index in range(0, 7):
            plt.clf()
            X = [1, 2, 3, 4, 5]
            plt.bar(X, days[index])
            plt.xlabel('Ratings')
            plt.ylabel('Distribution')
            plt.title('Rating Distribution by Day%d' % index)
            plt.savefig('../plots/ratingsDistributionByDay%d.png' % index)
            plt.show()
    else:
        for index in range(0, 2):
            plt.clf()
            X = [1, 2, 3, 4, 5]
            plt.bar(X, days[index])
            plt.xlabel('Ratings')
            plt.ylabel('Distribution')
            if index == 0:
                plt.title('Rating Distribution by WeekDays')
            else:
                plt.title('Rating Distribution by Weekends')
            if index == 0:
                plt.savefig('../plots/ratingsDistributionByWeekdays.png')
            else:
                plt.savefig('../plots/ratingsDistributionByWeekends.png')
            plt.show()
    print('Plotting weekday wise movie rating ended...')


# Main function
def main():
    start_time = time.time()
    movie_dict = get_movie_dict()
    end_time = time.time()
    print('Movie dict parsed in : %f secs' %(end_time - start_time))
    start_time = time.time()
    user_dict = get_user_dict()
    end_time = time.time()
    print('User dict parsed in : %f secs' % (end_time - start_time))
    start_time = time.time()
    #plot_movie_rating_distribution(movie_dict)
    plot_movie_wise_distribution(movie_dict, write=1)
    plot_user_wise_distribution(user_dict, write=1)
    #plot_weekday_wise_ratings(movie_dict, weekends=1)
    end_time = time.time()
    print('Movie rating / plotted in : %f secs' % (end_time - start_time))



if __name__ == "__main__":
    main()