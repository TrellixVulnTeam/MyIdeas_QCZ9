for a1 in range(1,9):
    for a2 in range(0,9):
        for a3 in range(0,9):
            for a4 in range(0,9):
                for a5 in range(0,9):
                    if (a1-a2==2 or a2-a1==2):
                        if (a2-a3==2 or a3-a2)==2:
                            if (a3-a4==2 or a4-a3)==2:
                                if (a4-a5==2 or a5-a4)==2:
                                    if int(a1+a2+a3+a4+a5)%12==0:
                                        a=[a1,a2,a3,a4,a5]

print(a)

