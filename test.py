import turtle
from random import randint


tur = turtle.Turtle()
tur.fillcolor('cyan')
scr = turtle.Screen()
tur.penup()
tur.setpos(-300,0)
tur.pendown()
def koch(n,l):
    if n ==0:
        tur.forward(l)
    else:
        koch(n-1,l/3)
        tur.left(60)
        koch(n-1,l/3)
        tur.right(120)
        koch(n-1,l/3)
        tur.left(60)
        koch(n-1,l/3)
koch(2,400)
tur.exitonclick() # pour  garder ouverte la fenêtre