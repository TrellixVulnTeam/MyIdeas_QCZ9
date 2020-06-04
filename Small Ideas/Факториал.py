
def fact(a): # Сама функция факториала
    line = list(range(1,a+1))
    r = 1
    for i in range(0,len(line)-1):
        r = r * line[i+1]
    return r

