from tkinter import *
import random
all = 0
count = 0
root = Tk()
field = Canvas(root, width = 600, height = 600)
field.pack()
center_x = 300
center_y = 300
box = field.create_rectangle(5, 5, 600, 600, width = 2)
round = field.create_oval(100, 100, 500, 500, width = 2)
r = 200

while True:

    x = random.randint(1, 601)
    y = random.randint(1, 601)
    dot = field.create_rectangle(x , y, x , y , width = 2)
    all += 1
    if (((center_x + x) ** 2 + (center_y + y) ** 2) <= r**2) or (((x + center_x) ** 2 + (center_y + y)**2) <= r**2):
        count +=1
    elif (((center_x - x)**2 + (y - center_y) **2) <= r**2) or (((x - center_x)**2 + (y - center_y)**2) <= r **2):
        count += 1


    root.update()  # mainloop не подходит использую update(
    pi = 4 * (count / all)
    print(pi)
