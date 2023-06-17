import turtle
from turtle import Turtle, Screen
from tkcolors import COLORS
import random

t = Turtle()
turtle.colormode(255)
t.shape("turtle")
t.color("red")
t.width(2)
t.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# for _ in range(1, 51):
#     t.pd()
#     t.forward(5)
#     t.pu()
#     t.forward(5)


def shape_color(timmy):
    sides = 3
    while sides < 9:
        timmy.color(random.choice(COLORS))
        angle = 360 / sides
        for _ in range(sides):
            timmy.forward(100)
            timmy.right(angle)
        sides += 1


def random_walk(timmy):
    steps = 100
    angle_list = [0, 90, 180, -90]
    while steps > 0:
        timmy.color(random_color())
        timmy.right(random.choice(angle_list))
        timmy.forward(30)
        steps -= 1


def spirograph(timmy):
    full_rotation = 360
    tilt = 5
    circle_numbers = full_rotation / tilt
    while circle_numbers >= 0:
        timmy.color(random_color())
        timmy.circle(100)
        timmy.right(tilt)
        circle_numbers -= 1


# spirograph(t)
random_walk(t)
screen = Screen()
screen.exitonclick()
