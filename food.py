from turtle import Turtle

#food class will have all capabilities of Turtle class + its own
class Food(Turtle):

    def __init__(self):
        #piece of food = turtle object
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize() #allows me to stretch turtle along its length and width
