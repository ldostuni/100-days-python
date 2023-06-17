import colorgram
import turtle
import random

colors = colorgram.extract('yoshi.jpg', 12)

vedal = turtle.Turtle()
turtle.colormode(255)


print(random.choice(colors).rgb.r)

my_screen = turtle.Screen()
my_screen.setworldcoordinates(-1, -1, my_screen.window_width() - 1, my_screen.window_height() - 1)

dot_size = 20
step = 50
# for some reason, these things get evaluated only if after the screen object is evaluated
vedal.speed("fastest")
vedal.penup()
vedal.hideturtle()

while vedal.position()[1] < my_screen.window_height() - 1:
    while vedal.position()[0] < my_screen.window_width() - 1:
        col = random.choice(colors).rgb
        vedal.dot(dot_size, col)
        vedal.forward(step)
    vedal.goto(0, vedal.position()[1] + step)

my_screen.exitonclick()


