#ЦИФРЫ ЧЕТЫРЕХЗНАЧНОГО ЧИСЛА , КРАТНОГО ПЯТИ, ЗАПИСАЛИ В ОБРАТНОМ ПОРЯДКЕ, ПОЛУЧИЛИ ВТОРОЕ ЧИСЛО,
#ЗАТЕМ ИЗ ПЕРВОГО ЧИСЛА ВЫЧЛИ ВТОРОЕ И ПОЛУЧИЛИ 2457. НАЙДИТЕ ТАКОЕ ЧИСЛО.

import random
string1=0
string2=0
while int(string1)-int(string2)!=2457:
    l=[0,0,0,0]
    while l[3]!='5':
        l[0]=str(random.randint(1,9))
        for i in range(0,4):
            l[i]=str(random.randint(0,9))
    string1=''.join(l)

    l.reverse()
    string2=''.join(l)

if int(string1)-int(string2)==2457:
    print('Исходное число равно ' + string1)
    print('Новое число равно '+string2)
    print("Ответ: "+string1)



