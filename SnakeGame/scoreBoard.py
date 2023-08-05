from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align="center",font=("Arial",25,"normal"))
        self.hideturtle()
        self.updateScore()
        
        
    def updateScore(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center",font=("Arial",25,"normal"))
        
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.updateScore()
        
        
    def increaseScore(self):
        self.score += 1
        self.updateScore()
        
        
    # def gameOver(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!",align="center",font=("Arial",45,"normal"))
        
        
        