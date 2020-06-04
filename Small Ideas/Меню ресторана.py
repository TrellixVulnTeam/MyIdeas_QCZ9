active=True
while active:
    def meal():
        menu=['pizza','coffee','vodka','burger','fish','tea']
        print('Here is our menu: ')
        for i in menu:
            print(i)
        while True:
            print('What would you like to have today?(choose 2 dishes only)')
            wish1=input()
            wish2=input()
            if (wish1 not in menu) or (wish2 not in menu):
                print('Sorry, we don`t have that dish on the menu')
            else:
                return wish1,wish2
                break
    meal=meal()
    print('You have ordered: ')
    for dish in meal:
        print('- '+dish)
    correct=input('Is that correct?(yes/no) ')
    if correct=='yes':
        print("Have a great meal!")
        active=False