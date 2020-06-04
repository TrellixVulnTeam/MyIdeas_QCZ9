import random
'''Создаю класс кинозала'''

class Zal():
    print('Добро пожаловать на сайт нашего кинотеатра!\nCейчас вам будет представлена модель кинозала для бронирования мест ')
    print('Нумерация рядов идет сверху-вниз (начинается с нуля). А нумерация мест - слева-направо (начинается с нуля)')


    '''Инициализатор'''
    def __init__(self, nothing):
        self.something = nothing
        self.places = self.do_places()


    ''' Предлагает выбрать фильм'''
    def choose_film(self):
        while True:
            print('Введите номер одного из предложенных фильмов для перехода в меню выбора места: ')
            print(' - 1  Вселенная Стивена Хокинга (малый зал: 6 рядов)')
            print(' - 2  Марсианин (НОВИНКА) (большой зал: 10 рядов)')
            print(' - 3  Побег из Шоушенка (средний зал: 8 рядов)')
            self.film = int(input("Ваш выбор: "))
            if (self.film == 1) or (self.film == 2) or (self.film == 3):
                return self.film
            else:
                print('Фильма с таким номером нет в списке. Попробуйте еще раз')


    '''Считает ряды в соответствии с фильмом'''
    def count_rows(self):
        film = self.choose_film()
        if film == 1:
            self.rows = 6
            return self.rows
        elif film == 2:
            self.rows = 10
            return self.rows
        else:
            self.rows = 8
            return self.rows


    '''Создает массив'''
    def do_places(self): # создает массив в качестве модели зала
        rows = self.count_rows()
        places = []
        most_places = rows * 2 + 1
        for i in range(rows):
            places.append([])
            most_places -= 1
            for j in range(most_places):
                places[i].append(random.randint(0,1))
        return places # возвращает сам массив зала


    '''Печатает массив'''
    def show_places(self): # изображает модель зала
        i = 0
        for el in self.places:
            print("Ряд №"+str(i)+' '+(self.places.index(el)* ' '+ str(el)))
            i+=1
        return self.places




    '''Функция запрашивает место. Проверяет, существует ли указанный ряд и место.
    Можно забронировать одно или два места '''
    def get_place(self): # получает координаты места
        show_places = self.show_places()


        while True:
            how_many = int(input('Сколько мест вы бы хотели забронировать? (1/2):  '))
            if how_many == 1:
                while True:
                    row = int(input('Введите номер ряда: '))
                    if row > self.rows:
                        print('Такого ряда нет в зале.')
                    else:
                        while True:
                            place = int(input('Введите номер места: '))
                            if int(place) > len(self.places[row]) - 1:
                                print('Такого места нет в выбранном вами ряду')
                            else:
                                return row, place, self.places, how_many
            elif how_many == 2:
                while True:
                    row = int(input('Введите номер ряда: '))
                    if row > self.rows:
                        print('Такого ряда нет в зале.')
                    else:
                        while True:
                            place_1 = int(input('Введите номер первого места: '))
                            if int(place_1) > len(self.places[row]) - 1:
                                print('Такого места нет в выбранном вами ряду')
                            else:
                                while True:
                                    place_2 = int(input('Введите номер второго места: '))
                                    if place_1 != place_2:
                                        if int(place_2) > len(self.places[row]) - 1:
                                            print('Такого места нет в выбранном вами ряду')
                                        else:
                                            if abs(place_1 - place_2) > 1:
                                                print('Вы можете забронировать только соседние места согласно правилам нашего кинотеатра')
                                            else:
                                                return row,place_1, place_2, self.places, how_many
                                    else:
                                        print('Вы выбрали два одинаковых места')
            else:
                print('Вы можете забронировать за один раз только два места в зале.')


    ''' Проверяет свободно/ы ли выбранное/ые место/а'''
    def check_if_free(self): # проверяет свободно ли место

        check = self.get_place()
        ''' МОЖНО ВЫВОДИТЬ В ФУНКЦИИ НЕСКОЛЬКО ЗНАЧЕНИЙ И ПОТОМ ИСПОЛЬЗОВАТЬ ИХ ЧЕРЕЗ [0], [1] КАК ПОКАЗАНО НИЖЕ'''
        if check[-1] == 1:
            if check[2][check[0]][check[1]] == 0: # ВОТ ТАК
                print('Место свободно')
                return 'kek', check[0], check[1] # 0 - ряд 1 - место
            else:
                print('Место занято. Выберите другое')
                return check[0],check[1],check[2] # 0 - ряд 1- место 2- массив
        else:
            if (check[3][check[0]][check[1]] == 0) and (check[3][check[0]][check[2]] == 0):
                print('Оба выбранных места свободны')
                return 'yes two places first try', check[0], check[1], check[2] , check[3] # 0 - ряд 1 -первое место 2- второе место 3 - массив
            else:
                print('Одно из выбранных мест занято. Вы не сможете забронировать два соседних места, выбранных вами.')
                return 'no two places' , check[0], check[1], check[2], check[3] # 0 - ряд 1 - место 2 -место


    '''Если место занято, запрашивает новое и делает все как в get_place'''
    def get_new_place(self):
        free = self.check_if_free()
        if (free[0] != 'kek') and (free[0] != 'no two places') and (free[0] != 'yes two places first try'):
            while True:
                new_row = int(input('Введите номер нового ряда: '))
                if new_row > self.rows:
                    print('Такого ряда нет в зале.')
                else:
                    max_places = len(free[2])
                    while True:
                        new_place = int(input('Введите номер нового места: '))
                        if new_place > max_places:
                            print('Такого места нет в выбранном вами ряду.')
                        else:
                            if free[2][new_row][new_place] == 0: # 2 - массив
                                print('А это место свободно')
                                return 'yes one place', new_row, new_place # 0 - ряд 1 - место
                            else:
                                print('И это место занято')
                                break

        elif free[0] == 'no two places':
            while True:
                new_row = int(input('Введите номер нового ряда: '))
                if new_row > self.rows:
                    print('Такого ряда нет в зале.')
                else:
                    max_places = len(free[4])
                    while True:
                        new_place_1 = int(input('Введите номер первого нового места: '))
                        if int(new_place_1) > max_places:
                            print('Такого места нет в выбранном ряду')
                        else:
                            while True:
                                new_place_2 = int(input('Введите номер второго нового места: '))
                                if new_place_1 != new_place_2:
                                    if int(new_place_2) > max_places:
                                        print('Такого места нет в выбранном ряду')
                                    else:
                                        if (free[4][new_row][new_place_1] == 0) and (free[4][new_row][new_place_2] == 0 ):
                                            print('Новые места, которые вы выбрали свободны')
                                            return 'yes two places second try', new_row, new_place_1, new_place_2 # 1 - ряд 2 - место 3 - место
                                        else:
                                            print('Одно из выбранных мест занято. Вы не сможете забронировать два соседних места, выбранных вами.')
                                else:
                                    print("Вы выбрали два одинаковых места")
        elif free[0] == 'kek':
            return 'kek' , free[1], free[2]
        elif free[0] == 'yes two places first try':
            return 'yes two places first try', free[1], free[2], free[3]


    ''' Запрашивает подтверждение выбора места
    Если человек отказывается, все начинается сначала'''
    def ask(self):
        while True:
            to_ask = self.get_new_place()
            if to_ask[0] == 'yes one place':
                print('Вы выбрали '+str(to_ask[1])+' ряд и '+str(to_ask[2])+' место в нем.')
                answer = input('Это верно? (да/нет): ')
                if answer == 'да':
                    print('Теперь указанное вами место забронировано.')
                    self.rows = to_ask[1]
                    self.places[to_ask[1]][to_ask[2]] = 1
                    self.show_places()
                    self.number_for_count_money = 1
                    return to_ask[1]
            elif to_ask[0] == 'kek': # первое выбранное место свободно сразу
                print('Вы выбрали ' + str(to_ask[1]) + ' ряд и ' + str(to_ask[2]) + ' место в нем.')
                answer = input('Это верно? (да/нет): ')
                if answer == 'да':
                    print('Теперь указанное вами место забронировано.')
                    self.rows = to_ask[1]
                    self.places[to_ask[1]][to_ask[2]] = 1
                    self.show_places()
                    self.number_for_count_money = 1
                    return to_ask[1]
            elif to_ask[0] == 'yes two places first try':
                print('Вы выбрали ' + str(to_ask[1]) + ' ряд и ' + str(to_ask[2]) + ' и ' + str(to_ask[3]) + ' места в нем')
                answer = input('Это верно? (да/нет): ')
                if answer == 'да':
                    print('Теперь указанные вами места забронированы.')
                    self.rows = to_ask[1]
                    self.number_for_count_money = 2
                    self.places[to_ask[1]][to_ask[2]] = 1
                    self.places[to_ask[1]][to_ask[3]] = 1
                    self.show_places()
                    return 'two', to_ask[1]
            elif to_ask[0] == 'yes two places second try':
                print('Вы выбрали ' + str(to_ask[1]) + ' ряд и ' + str(to_ask[2]) + ' и ' + str(to_ask[3]) + ' места в нем')
                answer = input('Это верно? (да/нет): ')
                if answer == 'да':
                    print('Теперь указанные вами места забронированы.')
                    self.rows = to_ask[1]
                    self.number_for_count_money = 2
                    self.places[to_ask[1]][to_ask[2]] = 1
                    self.places[to_ask[1]][to_ask[3]] = 1
                    self.show_places()
                    return 'two', to_ask[1]



    '''Считает цену билета/ов'''
    def count_money(self):
        price = 100
        if self.number_for_count_money == 1:
            for i in range(self.rows):
                price += 20
            print('Цена билета составит '+str(price)+' рублей.\nПриятного просмотра!')
        else:
            for i in range(self.rows):
                price += 20
            print('Цена билетов составит ' + str(price*2) + ' рублей.\nПриятного просмотра!')


    '''Запрашивает продолжать ли работу'''
    def continue_run(self):
        while True:
            stop = int(input('Введите "1",чтобы выйти из меню или "0", чтобы продолжить бронирование: '))
            if stop == 1:
                break
            elif stop == 0:

                self.count_rows()
                self.ask()
                self.count_money()
                self.doxod_auto()



    '''Запрашивает желание узнать максимальный доход с зала'''
    def doxod_hand(self):
        ask = input('Хотите ли подсчитать максимальную прибыль с сеанса? (да/нет): ')
        if ask == 'да':
            doxod = 0
            price = 80
            for row in self.places:
                price += 20
                for el in row:
                    doxod += price
            print('При условии, что все места заняты, доход составит '+str(doxod)+' рублей.' )
        else:
            pass


    '''Если все места заняты выдает доход с продажи билетов'''
    def doxod_auto(self):
        doxod = 0
        price = 80
        i = 0
        for row in self.places:
            price += 20
            for el in row:
                if el == 1:
                    i += 1
                    doxod += price
                    pass

        if i == len(self.places) + 1:
            print('Все места зала заняты. Общий доход составил '+ str(doxod)+' рублей.')

    ''' Служит для закрытия .exe'''
    def close_exe(self):
        close = input('Чтобы закрыть приложение нажмите любую клавишу.')

''' Вызываю функции из класса'''
zal = Zal (1)
zal.ask()
zal.count_money()
zal.doxod_auto()
zal.continue_run()
zal.doxod_hand()
zal.close_exe()
