'''
Файл сделан для проверки правильности вычислений при численном интегрировании (лекция от 13.05.20)
Реализованы:
1) Метод прямоугольников
2) Метод трапеций
3) Метод Симпсона
'''

import math

# задаем функцию (для каждого задания она индивидуальна)
def f(x):
    return 1 / math.sqrt(x**2 + 3.2)

# функция метода прямоугольников
def rectangle(low, high, steps):
    print("\nМетод прямоугольников")
    h = (high - low) / steps
    sum = 0
    while low < high:
        middle = low + (h / 2)
        result = f(middle) * h
        sum += result
        print(f'При x в пределах [{low} , {low+h}] значение функции равно {result}')
        low += h
    print(f'Итоговое значение интеграла равно {sum}')


# функция метода трапеций
def trapeze(low, high, steps):
    print("\nМетод трапеций")
    h = (high - low) / steps
    sum = 0
    while low < high:
        result = ((f(low) + f(low+h)) * h) / 2
        sum += result
        print(f'При x в пределах [{low} , {low + h}] значение функции равно {result}')
        low += h
    print(f'Итоговое значение интеграла равно {sum}')


# функция метода Симпсона (которая дает приблизительное значени)
def simpson(low, high, steps):
    print("\nМетод Симпсона")
    h = (high - low) / steps
    sum = 0
    while low < high:
        result = (h * (f(low) + 4 * f(low+(h/2)) + f(low+h))) / 6
        sum += result
        print(f'При x в пределах [{low} , {low+h}] значение функции равно {result}')
        low += h
    print(f'Итоговое значение интеграла равно {sum}')




low = float(input("Введите нижнюю границу интегрирования: \n"))
high = float(input("Введите верхнюю границу интегрирования: \n"))
steps = int(input("Введите количество участков: \n"))
while True:
    print("\nВыберите способ решения:\n1)Метод прямоугольников\n2)Метод трапеций\n3)Метод Симпсона")
    print("4 - Выйти")
    choice = int(input())
    if choice == 1:
        rectangle(low, high, steps)
    elif choice == 2:
        trapeze(low, high, steps)
    elif choice == 3:
        simpson(low, high, steps)
    elif choice == 4:
        print("Пока!")
        exit()






