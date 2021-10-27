def RatingDate():
    doc = open(r'/Users/Zhang/Desktop/RatingData.txt', 'w')
    linecounter = 1
    f = open("/Users/Zhang/Desktop/Netflix/combined_data_1.txt")
    lines = f.readlines()
    alist = []
    for line in lines:
        if linecounter < len(lines) - 1:
            if ':' not in lines[linecounter + 1]:
                if ':' in line:
                    a = line.strip('\r').strip('\n')
                else:
                    list1 = []
                    rating = line.split(',')[1].strip('\r').strip('\n').strip('\r').strip('\n')
                    date = line.split(',')[2].strip('\r').strip('\n').strip('\r').strip('\n')
                    list1.append(date)
                    list1.append(rating)
                    alist.append(list1)
            else:
                blist = sorted(alist)
                print(a, file = doc)
                for z in blist:
                    print(z[0], z[1], file = doc)
                alist = []
            linecounter += 1
        else:
            break
    blist = sorted(alist)
    print(a, file = doc)
    for z in blist:
        print(z[0], z[1], file = doc)     
    doc.close()
        
RatingDate()
