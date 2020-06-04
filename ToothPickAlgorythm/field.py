from settings import FieldSize #размеры экрана
from tkinter import *
from picks import Pick # класс зубочистки

size = FieldSize()
width = size.width
height = size.height

root = Tk()#корневая функция для работы всего модуля

'''Создание поля'''
field = Canvas(root, width = width, height = height)#создание поля

'''Создание кнопки для запуска программы'''
button = Button(root)
button['text'] = 'Поiхалi'
button.pack()

'''Рисует зубочистку по координатам двух точек'''
def draw_pick(a_x, a_y, b_x, b_y, field):
    field.create_line(a_x, a_y, b_x, b_y)

'''Координаты первой зубочистки'''
first_a_x = 50
first_a_y = 50
first_b_x = 50
first_b_y = 70

'''Создание первой зубочистки'''
picks = []
pick = Pick(first_a_x, first_a_y, first_b_x, first_b_y, 1)
picks.append(pick)
print(len(picks))
draw_pick(pick.a_x, pick.a_y, pick.b_x, pick.b_y, field)
pick.change_pick(pick, picks)
print(len(picks))





field.pack()#без этого не будет отображаться то, что на экране нарисовано
field.mainloop()