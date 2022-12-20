from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")

#Step1: Create snake body (three squares, one next to the other)
#turtle = 20X20 px, I can create with for loop, using tuples for positions:
starting_positions = [(0,0), (-20,0), (-40, 0)]
segments = [] #start as empty list and append segments as they are created below
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)
    













screen.exitonclick()