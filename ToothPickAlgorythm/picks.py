'''Здесь будет находиться инфрмация о всех зубочистках. Обработка этой
информации будет производиться в файле field'''


'''Содержит координаты двух точек, через которые будет проходить прямая и ее ориентацию
а также список всех зубочисток'''
class Pick():
    def __init__(self, a_x, a_y, b_x, b_y, orient):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.length = 100
        self.orient = orient

    '''Изменяет ориентацию зубочистки, добавляет ее в список и выводит список для рисования'''
    def change_pick(self, pick, picks):
        if len(picks) <= 10:
            if pick.orient == -1:# если горизонтально то рисует вертикальную справа
                length = pick.length
                pick.a_x = pick.a_x + length
                pick.a_y = pick.a_y - length / 2
                pick.b_x = pick.b_x
                pick.b_y = pick.b_y + length / 2
                pick.orient = 1
                picks.append(pick)
                print(len(picks))
                pick.change_pick(pick, picks)
            elif pick.orient == 1:# если вертикально, то рисует горизонтальную снизу
                length = pick.length
                pick.a_x = pick.a_x - length / 2
                pick.a_y = pick.a_y + length
                pick.b_x = pick.b_x + length / 2
                pick.b_y = pick.b_y
                pick.orient = -1
                picks.append(pick)
                print(len(picks))
                pick.change_pick(pick, picks)
        else:
            print(1)
            return picks
