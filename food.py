from turtle import Turtle
import random

#food class will have all capabilities of Turtle class + its own
class Food(Turtle):

    def __init__(self):
        #piece of food = turtle object
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #allows me to stretch turtle along its length and width
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)