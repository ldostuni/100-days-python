import turtle

t = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    t.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()