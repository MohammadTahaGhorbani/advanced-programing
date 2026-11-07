import turtle as t
import random

t.hideturtle()
t.penup()
t.speed(0)
t.color("green")
t.tracer(0)
t.bgcolor('black')

x, y = 0, 0
scale = 150

for i in range(20000):
    r = random.random()
    if r < 0.40:
        x, y = .31*x - .53*y + .89, -.46*x - .29*y + 1.04
    elif r < 0.55:
        x, y = .31*x - .08*y + .22, .15*x - .45*y + 0.34
    else:
        x, y = .55*y + .01, .69*x - .20*y + 0.38

    t.goto(x * scale, y * scale - 150)
    t.dot(3)

    if i % 50000 == 0:
        t.update()

t.update()
t.done()