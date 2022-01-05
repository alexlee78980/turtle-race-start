from turtle import Turtle, Screen
import random


def turtle_race_start():
    screen = Screen()
    no_finish = True
    winner = None
    width = 500
    height = 400
    screen.setup(width, height)
    user_input = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
    red = Turtle()
    red.color("red")
    green = Turtle()
    green.color("green")
    purple = Turtle()
    purple.color("purple")
    yellow = Turtle()
    yellow.color("yellow")
    blue = Turtle()
    blue.color("blue")
    black = Turtle()
    black.color("black")
    turtle_list = [red, green, purple, blue, yellow, black]
    random.shuffle(turtle_list)
    start_x = -width / 2 + 10
    start_y = -150
    for turtle in turtle_list:
        turtle.shape("turtle")
        turtle.penup()
        turtle.setposition(start_x, start_y)
        start_y += 50
    while no_finish:
        for turtle in turtle_list:
            turtle.forward(random.randint(1, 10))
            if turtle.xcor() >= width / 2 - 10:
                winner = turtle
                no_finish = False
                break

    if winner.color()[0] == user_input:
        print("Congratulations! You bet on the correct turtle")
    else:
        print("You bet on the wrong turtle")
    print(f"The winner is the {winner.color()[0]} turtle!")
    screen.exitonclick()
