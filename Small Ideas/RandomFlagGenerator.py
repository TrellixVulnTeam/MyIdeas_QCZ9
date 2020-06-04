import turtle
import random

line = turtle.Turtle()

line.penup()
line.goto(-480, 385)
line.pendown()


def toody_soody():
    line.width(random.randint(40, 80))
    line.color(random.choice(['green', 'blue', 'yellow' , 'red', 'purple', 'orange', 'pink']))
    for i in range(95):
        line.forward(10)
    line.right(90)
    line.forward(40)
    line.right(90)
    for i in range(95):
        line.forward(10)
    line.left(90)
    line.forward(40)
    line.left(90)
    line.width(random.randint(30, 80))
    toody_soody()

toody_soody()


