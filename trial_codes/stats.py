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