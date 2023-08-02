from turtle import Turtle, Screen
import random
race_on = False
splinter = Turtle()
splinter.hideturtle()
splinter.pensize(15)
splinter.penup()
mikey = Turtle(shape="turtle")
mikey.name = mikey
leo = Turtle(shape="turtle")
leo.color("blue")
leo.penup()
leo.name = "leo"
donny = Turtle(shape="turtle")
donny.color("purple")
donny.penup()
donny.name = "donny"
ralph = Turtle(shape="turtle")
ralph.color("red")
ralph.penup()
ralph.name = "ralph"
mikey.color("orange")
my_screen = Screen()
my_screen.setup(width=1000, height=800)
mikey.name = "mikey"
mikey.penup()
leo.goto(x=-450, y=350)
donny.goto(x=-450, y=150)
ralph.goto(x=-450, y=-50)
mikey.goto(x=-450, y=-250)
splinter.goto(x=400, y=800)
splinter.right(90)
for i in range(10):
    splinter.pendown()
    splinter.forward(120)
    splinter.penup()
    splinter.forward(40)
    splinter.pendown()
turtles = [leo, donny, mikey, ralph]
user_bet = my_screen.textinput(title="Place your bet.", prompt="What TMNT do you think is winning? ")
if user_bet:
    race_on = True
while race_on:

    for turtle in turtles:
        if user_bet == f"{turtle.name}.":
            turtle.forward(20)
        if turtle.xcor() > 400:
            race_on = False
            if user_bet == turtle.name or user_bet == f"{turtle.name}.":
                print(f"{turtle.name} won!! congrats")
            else:
                print(f"{turtle.name} won, that sucks bro, you owe me $1000")
        random_number = random.randint(0, 50)
        turtle.forward(random_number)

my_screen.exitonclick()
