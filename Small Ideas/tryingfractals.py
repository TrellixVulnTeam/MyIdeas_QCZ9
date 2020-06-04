import turtle
import math
import random

angle = 20
line = turtle.Turtle()
line.left(90)
line.backward(100)
line.forward(100)

def part(stroke):
    global angle
    if stroke > 10:
        line.right(angle)
        line.forward(stroke)
        stroke -= 10
        part(stroke)
    else:
        stroke += 10
        line.left(angle * 2)
        line.backward (stroke)
        line.right(angle )
        part(stroke )


part(80)

