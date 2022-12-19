from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")

#Step1: Create snake body (three squares, one next to the other)
#turtle = 20X20 px, I can create with for loop, using tuples for positions:
starting_positions = [(0,0), (-20,0), (-40, 0)]

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)
    













screen.exitonclick()