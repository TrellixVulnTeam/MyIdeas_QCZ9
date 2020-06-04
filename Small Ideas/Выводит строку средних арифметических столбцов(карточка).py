line = []
srznl = []
import random

for i in range(5):
    line.append([])
    for j in range(5):
        line[i].append(random.randint(0, 100))

ind = 0
while True:
    col = []

    for x in range(5):
        col.append(line[x][ind])

    ind += 1
    srzn = sum(col) / len(col)
    srznl.append(srzn)

    if len(srznl) == 5:
        print('')
        print(srznl)
        break

print('')
for element in line:
    print(element)