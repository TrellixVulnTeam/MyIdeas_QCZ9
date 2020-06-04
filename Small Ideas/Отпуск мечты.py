trip={}
ppl=[]
locations=[]
info=[]
while True:
    name=input("Hello! What`s your name? ")
    place=input('What`s the country you want to go to? ')
    print("And what places do you want to visit there? ")
    for i in range(0,3):
        location=input()
        locations.append(location)
    company=input("Do you want to go there all alone?(yes/no) ")
    if company=='no':
        print("Who is going to be there with you? ")
        for i in range(0,3):
            man=input()
            ppl.append(man)
    decision=input("Do you want to change your dream trip?(yes/no)")
    if decision=='no':
        break

trip[name]=place
for one,two in trip.items():
    print('Your name is '+one.title()+' and you want to go to '+two.title())
print('In '+two.title()+" you want to visit: ")
for location in locations:
    print(location)
print('And your friends: ')
for man in ppl:
    print(man.title())
print('Are coming with you, of course')
print('Good Luck!')