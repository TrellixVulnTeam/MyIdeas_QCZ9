import random
pars = []
n = int(input('Сколько пришло сообщений: '))
for i in range(0,n):
    pars.append(random.randint(0,16))
l_of_much = {}
for el in pars:
    much = pars.count(el)
    l_of_much[el] = much
#распределение элементов словаря по уменьшению value
value1 = max(l_of_much.values())
for key,value in l_of_much.items():
    if value1 == value:
        print(key,value)
    else:
        value -= 1




