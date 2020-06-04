from tkinter import *
import time
import sys
import random
'''Создание поля'''
tk = Tk()
canvas = Canvas(tk, width = 500, height = 500)
tk.title('Drawing')
canvas.pack()
ball=canvas.create_oval(40, 40, 100, 100, fill='green')
colors = ['green', 'blue', 'yellow' , 'red', 'purple', 'orange', 'pink']
xspeed = random.randint(1,3)
yspeed = random.randint(1,3)
while True:

    canvas.move(ball, xspeed, yspeed) # двигает что и две скорости
    pos = canvas.coords(ball)
    # право и лево
    if (pos[3]>=500) or (pos[1]<=0):
        canvas.delete(ball)
        ball=canvas.create_oval(pos,fill = random.choice(colors))
        yspeed= -yspeed
    # верх и низ
    if (pos[2]>=500) or (pos[0]<=0):
        canvas.delete(ball)
        ball = canvas.create_oval(pos, fill = random.choice(colors))
        xspeed= -xspeed
    tk.update()
    time.sleep(0.01)


canvas.mainloop()
'''-------'''


