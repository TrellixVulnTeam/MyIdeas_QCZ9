'''На доске написали несколько не обязательно различных двузначных натуральных чисел без нулей в десятичной записи.
Сумма их=363. Потом в каждом поменяли местами первую и последнюю цифру.
-Приведите пример исходных чисел, для которых сумма получившихся чисел ровно в 4 раза больше , чем сумма исходных
-Могла ли сумма получившихся чисел быть ровно в 2 раза больше, чем исходных
-Найдите наибольшее возможное значение суммы получившихся чисел'''
import random
while True:
    line=[]
    for i in range(15):
        a=random.randint(10,100)
        if a%10!=0:
            line.append(a)

        if sum(line)==363:
            print("Оригинал: "+str(line))
            reverse = []

            for number in line:# Меняем местами цифры чисел
                cel=str(number//10)
                ost=str(number%10)
                reverse_odno=[ost,cel]
                string_ot_reverse_odno=''.join(reverse_odno)
                reverse.append(int(string_ot_reverse_odno))
            if sum(reverse)/sum(line)==4:
                print(line)
                break









