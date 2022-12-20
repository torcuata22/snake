from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

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
        self.write(f"Score = {self.score}", align = ALIGNMENT, font = FONT)  #font needs to be a tuple

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)

    def add_to_score(self):
        self.score += 1
        self.clear() #clears previous text
        self.update_scoreboard()
       

