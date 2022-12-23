from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

#Scoreboard is a Turtle Object and inherits its properties and methods, use turtle.write method:
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        #read high_score from data.txt:
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
       
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)  #font needs to be a tuple

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align = ALIGNMENT, font = FONT)

    #to add the high score feature:
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def add_to_score(self):
        self.score += 1
        self.update_scoreboard()
       

