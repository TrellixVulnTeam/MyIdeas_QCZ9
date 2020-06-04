'''Вычеркните в числе 141565041 три цифры так, чтобы получившееся число делилось на 30.
 В ответе укажите ровно одно получившееся число'''

import random

while True:
    number = 141565041
    l=[str(x) for x in str(number)]
    del l[random.randint(0, 8)]
    del l[random.randint(0, len(l)-1)]
    del l[random.randint(0, len(l)-1)]
    zislo=''.join(l)
    if int(zislo)%30==0:
        print(zislo)
        break








