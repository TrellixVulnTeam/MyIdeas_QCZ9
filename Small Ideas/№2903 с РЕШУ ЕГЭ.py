''' В списке находит количество элементов каждый из которых больше предыдущего и потом выводит максимальную из этих длинн
апрмиер в 01230120 должно вывести 4 т.к. 0123 - 4 элемента. Багов нет'''


import random
line = [0,1,2,3,0,1,2]
l = 0
m = 0
for i in range(10):
    line.append(random.randint(0,100))
for i in range(10):
    if line[i] > line[i - 1]:
        l += 1

    elif l > m:
        m = l
    else:
        l = 1

print(line)
print(m)
