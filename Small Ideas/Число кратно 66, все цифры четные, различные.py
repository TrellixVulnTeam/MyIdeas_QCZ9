import random
all=[]
while True:
    number=[]
    number.append(str(random.randint(1,9)))
    for i in range(1,4):
        number.append(str(random.randint(0,9)))
    string=''.join(number)
    a=number[0]
    b=number[1]
    c=number[2]
    d=number[3]
    if (number.count(a)==1) and (int(a)%2==0):
        if (number.count(b) == 1) and (int(b)%2==0):
            if (number.count(c) == 1) and (int(c)%2==0):
                if (number.count(d)) == 1 and (int(d)%2==0):
                    if int(string)%66==0:
                        if all.count(string)==0:
                            all.append(string)
                            print(all)
                            break