# import turtle
#
# vedal = turtle.Turtle()
#
# vedal.shape("turtle")
# vedal.color("aquamarine")
# vedal.forward(100)
# vedal.right(90)
# vedal.forward(100)

# my_screen = turtle.Screen()
# my_screen.exitonclick()

import prettytable

table = prettytable.PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtle", "Bulbasaur"])
table.add_column("Type", ["Electric", "Fire", "Water", "Grass"])
table.align = "c"
print(table)

