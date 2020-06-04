#Создание поля
field=[]
import random
field.append(['╩' for i in range(8)])
for hor in range(1,6):
    field.append([])
    for vert in range(0,7):
        if vert==0:
            field[hor].append('╣')
        elif (vert==6):
            field[hor].append('╠ ')
        else:
            field[hor].append(' ')

field[random.randint(1,5)][random.randint(1,5)]='B'
field.append(['╦' for i in range(8)])

#Назначение индекса буквы "В"
for line in field:
    if "B" in line:
        ind_1_B = field.index(line)
        ind_2_B = line.index("B")

#Создание звездочки
while True:
    ind_1_zv=random.randint(1,5)
    ind_2_zv=random.randint(1,5)
    if (ind_1_zv != ind_1_B) and ( ind_2_zv != ind_2_B):
        field[ind_1_zv][ind_2_zv]="*"
        break

#Функция печати поля
def print_func():
    for line in field:
        string=''.join(line)
        print(string)
print_func()
#функция печати при победе
def win():
    print("----->ПОБЕДА, ТОВАРИЩ!<-----")
#функция печати при невозможности движения
def imp():
    print('Движение невозможно. Вы достигли границ поля')

#Само тело игры
while True:
    move=input('Куда бы вам хотелось передвинуть "*"(вверх, вниз, вправо, влево)?: ')#Ввод команды
    moves=['вверх','вниз','вправо','влево']
    if move in moves:

        if move=='вправо':
            field[ind_1_zv][ind_2_zv]=" "
            ind_2_zv+=1
            if ind_2_zv>=6:
                ind_2_zv-=1
                imp()
                continue
            field[ind_1_zv][ind_2_zv]="*"
            print_func()
            if (ind_1_zv==ind_1_B) and (ind_2_zv==ind_2_B):
                win()
                break



        elif move=='влево':
            field[ind_1_zv][ind_2_zv] = " "
            ind_2_zv -= 1
            if ind_2_zv == 0:
                ind_2_zv+=1
                imp()
                continue
            field[ind_1_zv][ind_2_zv] = "*"
            print_func()
            if (ind_1_zv==ind_1_B) and (ind_2_zv==ind_2_B):
                win()
                break


        elif move=='вверх':
            field[ind_1_zv][ind_2_zv] = " "
            ind_1_zv -= 1
            if ind_1_zv == 0:
                ind_1_zv+=1
                imp()
                continue
            field[ind_1_zv][ind_2_zv] = "*"
            print_func()
            if (ind_1_zv==ind_1_B) and (ind_2_zv==ind_2_B):
                win()
                break

        elif move=='вниз':
            field[ind_1_zv][ind_2_zv] = " "
            ind_1_zv += 1
            if ind_1_zv == 6:
                ind_1_zv-=1
                imp()
                continue
            field[ind_1_zv][ind_2_zv] = "*"
            print_func()
            if (ind_1_zv==ind_1_B) and (ind_2_zv==ind_2_B):
                win()
                break
    else:
        print('Такого направления нет. ПОвторите ввод: ')



