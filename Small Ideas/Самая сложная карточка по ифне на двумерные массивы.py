'''В массиве первый элемент задается рандомный, а все следующие больше предыдущего на удвоенную
сумму его индексов(строка, столбец)'''
import random as r
line=[]
src=0
for i in range(4):
    if i==0:
        line.append([r.randint(1,10)])
        for j in range(1,4):
            line[i].append(line[i][i-1]+2*(i+(j-1)))
    else:
        line.append([])
        line[i].append(line[i-1][-1]+2*((i-1)+(len(line[i-1])-1)))
        for j in range(1,4):
            line[i].append(line[i][j-1]+2*(i+(j-1)))


for element in line:
    print(element)
