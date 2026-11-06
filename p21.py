import turtle
import random

G = (-200, 150)
R = (0, -200)
B = (200, 150)

t = turtle.Turtle()
t.speed(0)
t.penup()

x, y = R

n = 10000

for i in range(n):
    p = random.choice([G, R, B])

    x = (x + p[0]) / 2
    y = (y + p[1]) / 2

    t.goto(x, y)
    t.dot(2)

turtle.done()