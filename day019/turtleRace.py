import turtle
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)

turtles = []


def init_turtle():
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color((randint(0, 255), randint(0, 255), randint(0, 255)))
    return new_turtle


def position_turtles(turtle_array):
    start_y = 100
    distance = 50
    for i in range(0, 5):
        turtles[i].setposition(-250, start_y - distance * i)


def check_winner(run_turtle):
    return run_turtle.xcor() >= 300 - 40 / 2  # it's the turtle width


def start_race(turtle_array):
    winner_turtle = 0
    has_finished = True
    while has_finished:
        for i in range(len(turtle_array)):
            turtle_array[i].forward(randint(1, 10))
            if check_winner(turtle_array[i]) and has_finished:
                has_finished = False
                turtle_array[i].color("gold")
                winner_turtle = i
    return winner_turtle


for _ in range(0, 5):
    turtles.append(init_turtle())

position_turtles(turtles)
bet = int(screen.textinput("Turtle race!", "Choose number of turtle (from top to bottom): "))
winner = start_race(turtles)
screen.exitonclick()

print(f"You bet on number {bet} and {winner} won.")
if bet == winner:
    print("You won!")
else:
    print("You lose...")
