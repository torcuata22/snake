from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
#to get rid of flickering (delay in animation):
screen.tracer(0) #turns tracer off, but you get black screen and nothing else


#Step1: Create snake body (three squares, one next to the other)
#Step2: get the three little turtles to act like one
#Step 3: link turtles so they move like a snake. Move n segment to n-1 position until we get to the head


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
    screen.update() 
    time.sleep(0.1) 
    # this made snake move forward as one, but we need body to follow head, so instead:
    #loop from last to first segment, start at length(segments)-1, end at 0, step=-1:
    for seg_num in range(len(segments)-1 ,0 ,-1): 
        snake_position = segments[seg_num-1].position()
        segments[seg_num].goto(snake_position)
        #new_x = segments[seg_num - 1].xcor
        #new_y = segments[seg_num - 1].ycor this doesn't work, gives error
    #need to move the first segment:
    segments[0].forward(20)






screen.exitonclick()