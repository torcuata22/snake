from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")

#Step1: Create snake body (three squares, one next to the other)
#turtle = 20X20 px
segment1 = Turtle("square")
segment1.color("white")

segment2 = Turtle("square")
segment2.color("white")
segment2.goto(x=-20, y=0)

segment3 = Turtle("square")
segment3.color("white")
segment3.goto(x=-40, y=0)











screen.exitonclick()