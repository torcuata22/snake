from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
#to get rid of flickering (delay in animation):
screen.tracer(0) #turns tracer off, but you get black screen and nothing else


#Step1: Create snake body (three squares, one next to the other)
#turtle = 20X20 px, I can create with for loop, using tuples for positions:
starting_positions = [(0,0), (-20,0), (-40, 0)]
segments = [] #start as empty list and append segments as they are created below
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

#to get fird of blank screen after tracer off:
#screen.update() #now snake shows as one piece, no delays, but no movement
game_is_on = True
while game_is_on:
    screen.update() #snake moves as entire piece
    time.sleep(1) #delay one second after all three segments have moved
    for seg in segments:
        seg.forward(20)
        
    













screen.exitonclick()