'''
Name            : CalcRMSE.py
Version         : 1.0a
Author          : Alpaca
'''
import math
from matplotlib import pyplot as plt

def create_movie_stat_dict():
    file_name = '../data/movieMinAvgMax.csv'
    file_header = open(file_name, 'r')
    line = file_header.readline()
    print('Creating movie dict...')
    movie_dict = dict()
    count = 0
    while line:
        count += 1
        if count % 1000 == 0:
            print('Count is : %d' % count)
        data = line.split(',')
        stat_list = []
        for d in data[1:]:
            stat_list.append(float(d.strip('\r').strip('\n').strip('\r').strip('\n')))
        movie_dict[data[0]] = stat_list
        line = file_header.readline()
    file_header.close()
    print('Finished creating movie dict...')
    return movie_dict


def create_user_stat_dict():
    file_name = '../data/userMinAvgMax.csv'
    file_header = open(file_name, 'r')
    line = file_header.readline()
    print('Creating user dict...')
    user_dict = dict()
    count = 0
    while line:
        count += 1
        if count % 1000 == 0:
            print('Count is : %d' % count)
        data = line.split(',')
        stat_list = []
        for d in data[1:]:
            stat_list.append(float(d.strip('\r').strip('\n').strip('\r').strip('\n')))
        user_dict[data[0]] = stat_list
        line = file_header.readline()
    file_header.close()
    print('Finished creating user dict...')
    return user_dict


def movie_avg_RMSE(movie_dict):
    squaredSum = 0.0
    file_name = '../data/probeRating.csv'
    file_header = open(file_name, 'r')
    line = file_header.readline()
    count = 0
    while line:
        if count % 1000 == 0:
            print('Count is : %d' % count)
        data = line.split(':')
        movieId = data[0]
        rats = data[1].split(',')
        for d in rats:
            info = d.split('|')[1]
            rat = int(info.strip('\r').strip('\n').strip('\r').strip('\n'))
            squaredSum += ((rat - movie_dict[movieId][1])*(rat - movie_dict[movieId][1]))
            count += 1
        line = file_header.readline()
    RMSE = math.sqrt(squaredSum/count)
    print('RMSE with just movie avg is : %f' % RMSE)
    file_header.close()
    return RMSE


def user_avg_RMSE(user_dict):
    squaredSum = 0.0
    file_name = '../data/probeRating.csv'
    file_header = open(file_name, 'r')
    line = file_header.readline()
    count = 0
    while line:
        if count % 1000 == 0:
            print('Count is : %d' % count)
        data = line.split(':')
        rats = data[1].split(',')
        for d in rats:
            uid = d.split('|')[0]
            rat = int(d.split('|')[1])
            squaredSum += ((rat - user_dict[uid][1])*(rat - user_dict[uid][1]))
            count += 1
        line = file_header.readline()
    RMSE = math.sqrt(squaredSum / count)
    print('RMSE with just user avg is : %f' % RMSE)
    file_header.close()
    return RMSE


def user_movie_avg_weighted_RMSE(movie_dict, user_dict, weight_movie=0.5, weight_user=0.5):
    squaredSum = 0.0
    file_name = '../data/probeRating.csv'
    file_header = open(file_name, 'r')
    line = file_header.readline()
    count = 0
    while line:
        if count % 1000 == 0:
            print('Count is : %d' % count)
        data = line.split(':')
        movieID = data[0]
        ratM = movie_dict[movieID][1]
        rats = data[1].split(',')
        for d in rats:
            uid = d.split('|')[0]
            rat = int(d.split('|')[1])
            predicted_rat = weight_movie * ratM + weight_user * user_dict[uid][1]
            squaredSum += ((rat - predicted_rat) * (rat - predicted_rat))
            count += 1
        line = file_header.readline()
    RMSE = math.sqrt(squaredSum / count)
    print('RMSE is : %f' % RMSE)
    file_header.close()
    return RMSE




def plot_naive_approach_results():
    RMSEs = [1.051938, 1.042614, 1.003171, 0.8554]
    X = [1, 2, 3, 4]
    plt.bar(X, RMSEs)
    plt.xticks(X, ['Movie Avg', 'User Avg', 'Weighted', 'Winner'])
    plt.xlabel('Techniques')
    plt.ylabel('RMSE')
    plt.title('Naive Approach Results')
    plt.savefig('../plots/naive_approach_results.png')
    plt.show()

# main function
def main():
    #movie_dict = create_movie_stat_dict()
    #user_dict = create_user_stat_dict()
    #RMSE_movie = movie_avg_RMSE(movie_dict)
    #RMSE_user = user_avg_RMSE(user_dict)
    #flag = 0
    #min_weight = 0.0
    #weight = 0.01
    #while weight < 1.0:
    # movie_dict = create_movie_stat_dict()
    # user_dict = create_user_stat_dict()
    #
    #
    # RMSE_movie = movie_avg_RMSE(movie_dict)
    # RMSE_user = user_avg_RMSE(user_dict)
    #
    #
    # flag = 0
    # min_weight = 0.0
    # weight = 0.01
    # while weight < 1.0:
    #    RMSE_user_movie_weighted = user_movie_avg_weighted_RMSE(movie_dict, user_dict, weight, 1-weight)
    #    if flag == 0:
    #        RMSE_user_minimum = RMSE_user_movie_weighted
    #        min_weight = weight
    #        flag = 1
    #    if RMSE_user_movie_weighted < RMSE_user_minimum:
    #         RMSE_user_minimum = RMSE_user_movie_weighted
    #         min_weight = weight
    #         weight += 0.01
    # print('RMSE (just movie avg) is : %f' % RMSE_movie)
    # print('RMSE (just user avg) is : %f' % RMSE_user)
    # print('Minimum RMSE (movie - user avg weight) is %f and with weight : %f' % (RMSE_user_minimum, min_weight))

    # # Results
    # # RMSE (just movie avg) is : 1.051938
    # # RMSE (just user avg) is : 1.042614
    # # Minimum RMSE (movie - user avg weight) is 1.003171 and with weight : 0.470000
    plot_naive_approach_results()


if __name__ == "__main__":
    main()