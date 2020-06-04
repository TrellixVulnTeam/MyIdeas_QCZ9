#упражнение 7-1
car=input('Какую машину вы бы хотели получить в аренду? ')
print('Сейчас проверю, есть ли '+car+" в доступе.")
cars={
    'subaru':'green',
    'toyota':'black',
    'kamaz':'red'

}
if str(car) in cars:
    print('Да, '+car.title()+' есть в доступе прямо сейчас.')
color=input('Какой цвет вас устроит? ')
if (str(color) in cars['subaru']) and (str(car)=='subaru'):
    print('Вам повезло, цвет '+color+" доступен для этой машины")
if (str(color) in cars['toyota']) and (str(car) == 'toyota'):
    print('Вам повезло, цвет ' + color + " доступен для этой машины")
if (str(color) in cars['kamaz']) and (str(car)=='kamaz'):
    print('Вам повезло, цвет '+color+" доступен для этой машины")
else:
    if (str(color) not in cars['subaru']) and (str(car)=='subaru'):
        print('К сожалению, для этой машины доступен только цвет ' + str(cars['subaru']))
    if (str(color) not in cars['toyota']) and (str(car) == 'toyota'):
        print('К сожалению, для этой машины доступен только цвет ' + str(cars['toyota']))
    if (str(color) not in cars['kamaz']) and (str(car) == 'kamaz'):
        print('К сожалению, для этой машины доступен только цвет '+str(cars['kamaz']))