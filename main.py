from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet",
                            "Which turtle will win the race? Enter a color (blue/red/green/black/violet)").lower()

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()

t1.color('blue')
t2.color('red')
t3.color('green')
t4.color('black')
t5.color('violet')

turtles = [t1, t2, t3, t4, t5]
winner = ""
current_pos = -150


def move(n_turtle, distance):
    n_turtle.forward(distance)


for turtle in turtles:
    turtle.shape('turtle')
    turtle.penup()
    current_pos += 50
    turtle.setpos(-250, current_pos)

race_on = True
while race_on:
    for turtle in turtles:
        step = random.randint(0, 10)
        move(turtle, step)
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            race_on = False

if user_bet == winner:
    print(f"YOU'VE WON! {winner.title()} turtle is the winner" )
else:
    print(f"YOU'VE LOST! {winner.title()} turtle is the winner")

screen.exitonclick()
