from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.scoreboard_update()


    def scoreboard_update(self):
        self.hideturtle()
        self.penup()
        self.goto(-300,-300)
        self.write(f"score:{self.score}/50" ,font=('Arial',20, 'normal'))

    def marks_up(self):
        self.clear()
        self.goto(-300,-300)
        self.score+=1
        self.write(f"score:{self.score}/50" , font=('Arial', 20, 'normal'))
        if self.score==50:
            self.clear()
            self.goto(-300,-300)
            self.write("You Guessed all states Write!! ",font=('Arial', 20, 'normal'))