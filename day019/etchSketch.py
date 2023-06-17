from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(10)


def move_backwards():
    t.forward(-10)


def rotate_right():
    t.right(10)


def rotate_left():
    t.right(-10)


def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()