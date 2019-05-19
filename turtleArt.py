from turtle import*
from random import*

def randomplace():
    x = randint(-100,100)
    y = randint(-100,100)
    goto(x,y)

shape("turtle")
color("red")

for i in range (4):
    randomplace()
    stamp()
    penup()
    randomplace()
    stamp()
    pendown()
