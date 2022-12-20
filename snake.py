from turtle import Turtle
#turtle = 20X20 px, I can create with for loop, using tuples for positions:
STARTING_POSITIONS= [(0,0), (-20,0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#Creates a three-segment snake when instantiated
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    # snake needs to follow head, so loop from last to first segment 
    # #start at length(segments)-1, end at 0, step=-1:
    def move(self):
        for seg_num in range(len(self.segments)-1 ,0 ,-1): 
            snake_position = self.segments[seg_num-1].position()
            self.segments[seg_num].goto(snake_position)
            #new_x = segments[seg_num - 1].xcor
            #new_y = segments[seg_num - 1].ycor this doesn't work, gives error
        #need to move the first segment:
        self.head.forward(MOVE_DISTANCE)
    #Snake can't go back on it self, needs if check:
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)        


    def down(self):
       if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != DOWN:
            self.head.setheading(LEFT)

  