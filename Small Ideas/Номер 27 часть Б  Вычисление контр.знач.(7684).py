import random

n = int(input('Введите длину списка: '))
line = []
for i in range(n):
    line.append(int(input('Введите элемент: ')))
go = True

ind1 = random.randint(0, n - 1)
el1 = line[ind1]
ind2 = random.randint(0, n - 1)
el2 = line[ind2]
if ind1 == ind2:
    go = False
r = el1 + el2
if r % 2 == 0:
    go = False
if go:
    print('Вычисленное контрольное значение: ' + str(r))
    print('Контроль пройден')
else:
    print('Контроль не пройден')

