import random
coords = []
n = int(input('Введите количество точек в множестве: '))
for i in range(n):
    coords.append([])
    for j in range(2):
        coords[i].append(int(input('Введите координаты точки: ')))
run = True
ind1 = random.randint(0,n - 1)
ind2 = random.randint(0,n - 1)
if ind1 == ind2:
    run = False
point1 = coords[ind1]
point2 = coords[ind2]
point3 = [0,0]
stor1 = abs(point1[0] - point2[0])
stor2 = abs(point1[1] - point2[1])
if (stor1 == 0) or (stor2 == 0):
    run = False
else:
    s = stor1 * stor2 / 2
    print(stor1, stor2)
    print(s)

