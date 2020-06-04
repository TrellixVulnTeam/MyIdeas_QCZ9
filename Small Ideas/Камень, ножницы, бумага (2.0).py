while True:
    import random

    list = ['rock', 'paper', 'scissors']
    x = input('CHOOSE: rock, paper, scissors: ')
    if x not in list:
        print('This value is not on the list. Try again')
    else:
        ind_1 = list.index(x)
        ind_2 = random.randint(0, len(list) - 1)
        if ind_1 == ind_2:
            print('IT`S A TIE!')
        else:
            if ((ind_1 == 0) and ind_2 == 2) or ((ind_1 == 1) and (ind_2 == 0)) or ((ind_1 == 2) and (ind_2 == 1)):
                print('You have chosen ' + list[ind_1].title() + ' and the computer have chosen ' + list[ind_2].title())
                print('YOU WIN!')
            if ((ind_1 == 0) and (ind_2 == 1)) or ((ind_1 == 1) and (ind_2 == 2)) or ((ind_1 == 2) and (ind_2 == 0)):
                print('You have chosen ' + list[ind_1].title() + ' and the computer have chosen ' + list[ind_2].title())
                print('YOU LOST!')
