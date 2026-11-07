import turtle
import random

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(0)
t.color("green")
turtle.tracer(0)

x, y = 0, 0
scale = 350

for i in range(30000):
    r = random.random()
    if r < 0.02:
        x, y = .50, .27*y
    elif r < 0.17:
        x, y = -.14*x + .26*y + .57, .25*x + .22*y - .04
    elif r < 0.30:
        x, y = .17*x - .21*y + .41, .22*x + .18*y + .09
    else:
        x, y = .78*x + .03*y + .11, -.03*x + .74*y + .27

    t.goto(x * scale - 150, y * scale - 250)
    t.dot(2)

    if i % 500 == 0:
        turtle.update()

turtle.update()
turtle.done()