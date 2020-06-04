from tkinter import *

run = Tk()

field = Canvas(run, width = 800, height = 800)
field.pack()


def part(x1, y1, x2, y2):
    r = (x2 - x1) / 2
    field.create_oval(x1, y1, x2, y2)
    if r > 2: # экран не может нарисовать круг с радиусом меньше двух пикселей
        part(x1 + 1.5 * r, y1 + 0.5 * r, x2 + 0.5 * r, y2 - 0.5 * r)
        part(x1 - 0.5 * r, y1 + 0.5 * r, x2 - 1.5 * r, y2 - 0.5 * r)



part(200, 200, 600, 600)

field.mainloop()
