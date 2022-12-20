from turtle import Turtle

#Scoreboard is a Turtle Object and inherits its properties and methods, use turtle.write method:
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
       
    def update_scoreboard(self):
        self.write(f"Score = {self.score}", align = "center", font = ("Arial", 24, "normal")) #font needs to be a tuple

    def add_to_score(self):
        self.score += 1
        self.clear() #clears previous text
        self.update_scoreboard()
       

