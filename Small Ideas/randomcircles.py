import math
import turtle
import random
line = turtle.Turtle()

def part(i):
    if i == 1 :
        turtle.width(1)
        turtle.circle(random.randint(20,220))
        i = -1
        turtle.right(random.randint(1, 90))
        part(i)
    elif i == -1:
        turtle.width(1)
        turtle.circle( - random.randint(30,220))
        i = 1
        turtle.right(random.randint(1,90))
        part(i)
part(1)


