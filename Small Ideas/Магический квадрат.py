''' Провеярет является ли массив магическим квадратом. То есть равны ли у него суммы всех строк,
суммы двух диагоналей, суммы всех столбцов.'''


import random
line = []
for i in range(10):
    line.append([])
    for j in range(10):
        line[i].append(random.randint(-10,10))
for el in line:
    print(el)

# проверяет равны ли суммы всех строк
for i in range(1,10):
    if sum(line[i]) == sum(line[i-1]):
        check_str = True
    else:
        check_str = False



# проверяет равны ли суммы всех столбцов

line_stolbs = []
k = 0
for i in range(10):
    sum_stolb = 0
    for j in range(10):
        sum_stolb += line[j][i]
    if k == sum_stolb:
        check_stolb = True
    else:
        k = sum_stolb
        check_stolb = False




# проверяет равны ли суммы диагоналей
sum_diag_1 = 0
sum_diag_2 = 0
for i in range(10):
        sum_diag_1 += line[i][i]
for i in range(10):
        sum_diag_2 += line[i][-i]

if sum_diag_1 == sum_diag_2:
    check_diag = True
else:
    check_diag = False



# выводит окончательное решение

if (check_stolb == True) and (check_diag == True) and (check_str == True):
    print('\nЯвляется магическим квадратом')
else:
    print('\nНе является магическим квадратом')