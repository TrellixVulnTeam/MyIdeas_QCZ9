import random
tabl=input("Введите число.Создастя массив с таким количеством столбцов и строк: ")
x=input("Введите строки, которую вы хотите поменять местами с некоторой другой: ")
y=input("Введите номер строки, которую вы хотите поменять местами с той, которую обозначили ранее: ")
line=[]
ud=[]
for i in range(int(tabl)):
    line.append([])
    for j in range(int(tabl)):
        line[i].append(random.randint(10,50))
print('\nИсходный массив: ')
for element in line:
    print(element)
print('\nНовый массив: ')
for element in line:
    element.insert(int(x),element[int(y)])
    element[int(y)+1]=element[int(x)+1]
    del element[int(x)+1]
    print(element)