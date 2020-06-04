import math

summa_s = []

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())


def ploshad(x,y,z):
    if (x > (y + z)) or  (y > (x + z)) or  (z > (x + y)):
        k = False
        return k
    else:
        per = int(x) + int(y) + int(z)
        pol = per /2
        s = math.sqrt(pol * (pol - x) * (pol - y) * (pol - z))
        summa_s.append(s)


while True:
    ploshad(a,b,f)
    ploshad(f,g,c)
    ploshad(g,d,e)
    if ploshad(a,b,f) == False:
        print('Треугольника со сторонами ' + str(a) + str(b) + str(f) + ' не существует')
        break
    elif ploshad(f,g,c) == False:
        print('Треугольника со сторонами ' + str(f) + str(g) + str(c) + ' не существует')
        break
    elif ploshad(g,d,e) == False:
        print('Треугольника со сторонами ' + str(g) + str(d) + str(e) + ' не существует')
        break
    else:
        print(sum(summa_s))
        break

