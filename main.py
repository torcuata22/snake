from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
#to get rid of flickering (delay in animation):
screen.tracer(0) #turns tracer off, but you get black screen and nothing else

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
    #Detect collision with food(eating) by using turtle distance method where x can be another instance:
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_to_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail:if head collides with any segment in tail, game over sequence
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()


    






screen.exitonclick()