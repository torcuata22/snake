from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
#to get rid of flickering (delay in animation):
screen.tracer(0) #turns tracer off, but you get black screen and nothing else

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    #screen updates every 0.1 seconds
    screen.update() 
    time.sleep(0.1) 
    snake.move()
    






screen.exitonclick()