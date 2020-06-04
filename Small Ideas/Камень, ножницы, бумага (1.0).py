import random
while True:
    rps=['rock','paper','scissors']
    x=input('CHOOSE:rock, paper, scissors: ')
    if x not in rps:
        print('This item is not on the list')
    ind=random.randint(0,len(rps)-1)
    chose=rps[ind]
    if x=='rock':
        if chose == 'scissors':
            print("You have chosen "+x.title()+' but a computer have chosen '+chose.title())
            print('YOU WIN')
        elif chose=='paper':
            print("You have chosen "+x.title()+' but a computer have chosen '+chose.title())
            print('YOU LOST')
        elif chose=='rock':
            print('You have chosen '+x.title()+' but the computer have chosen the same!')
            print('Try again')
    elif x =='paper':
        if chose=='rock':
            print("You have chosen "+x.title()+' but a computer have chosen '+chose.title())
            print("YOU WON")
        elif chose=='scissors':
            print("You have chosen " + x.title() + ' but a computer have chosen ' + chose.title())
            print("YOU LOST")
        elif chose=='paper':
            print('You have chosen '+x.title()+' but the computer have chosen the same!')
            print('Try again')
    elif x=='scissors':
        if chose=='rock':
            print("You have chosen " + x.title() + ' but a computer have chosen ' + chose.title())
            print("YOU LOST")
        elif chose=='paper':
            print("You have chosen " + x.title() + ' but a computer have chosen ' + chose.title())
            print("YOU WON")
        elif chose=='scissors':
            print('You have chosen '+x.title()+' but the computer have chosen the same!')
            print('Try again')