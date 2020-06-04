y=0
while y<=10:
    a = [[0] * 4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            if i < j:
                a[i][j] = 0
            elif i == j:
                a[i][j] = 1
            if i > j:
                a[i][j] = 2


    for element in a:
        print(' '.join([str(point) for point in element]))
    print('    ')
    for i in range(4):
        for j in range(4):
            if i < j:
                a[i][j] = 2
            elif i == j:
                a[i][j] = 1
            if i > j:
                a[i][j] = 0
    for element in a:
        print(' '.join([str(point) for point in element]))
    print('    ')
    y+=1
