import random
import turtle   
t = turtle.Turtle()
# t.width(50)
t.shape("turtle")
t.speed(-1)
screen = turtle.Screen()
t.color("brown")
t.left(20)
while True:
    color=(random.random(),random.random(),random.random())
    t.color(color)
    t.forward(3)
    t.left(3)
    t.forward(3)
    t.left(4)
    t.forward(4)
    t.left(5)
    t.forward(5)
    t.left(6)
    t.forward(6)
    t.left(7)
    t.forward(7)
    t.left(8)
    t.forward(8)
    t.left(9)
    t.forward(9)
    t.left(-200)
    t.forward(-200)




