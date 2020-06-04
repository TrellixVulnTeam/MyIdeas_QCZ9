figures=['Квадрат','Треугольник','Шестиугольник']
print('На данный момент программа может рисовать следующие фигуры: ')
for i in figures:
    print('- '+i)
figure=input('Какую фигуру вы хотели бы нарисовать? ')
if figure=='Квадрат':
    x=input("Введите длину стороны квадрата: ")
    for i in range(int(x)):
        print('* '*int(x))
if figure=='Треугольник':
    x=input('Введите длину стороны треугольника: ')
    start=1
    while start<=int(x):
        print('* '*start)

        start+=1
    while start>=0:
        print('* '*(start-1))
        start-=1


