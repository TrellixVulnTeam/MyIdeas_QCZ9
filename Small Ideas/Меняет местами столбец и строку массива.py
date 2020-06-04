import random
line = []
n = int(input('Введите размер массива: '))
for i in range(n):
    line.append([])
    for j in range(n):
        line[i].append(random.randint(1,9))
for el in line:
    print(el)
string = int(input('Введите номер строки: '))
col = int(input('Введите номер столбца: '))
for i in range(n):
    el = line[string][i]
    line[string][i] = line[i][col]
    line[i][col] = el
for el in line:
    print(el)

