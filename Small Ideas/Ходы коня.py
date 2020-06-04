import random
#Задаются рандомные координаты коня и выводт все клетки куда он может встать
x=4
y=7
print("Исходная Х = "+str(x))
print("Исходная Y = "+str(y))
print("Возможные ходы коня: ")
for i in range(1,9):
    for j in range(1,9):
        if ((abs(i-x)==1) and (abs(j-y)==2)) or ((abs(i-x)==2) and (abs(j-y)==1)):
            print(i,j)