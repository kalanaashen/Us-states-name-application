from turtle import Turtle

class Cursor(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def travel(self,x_cor,y_cor,name):
        self.shape("circle")
        self.goto(x_cor,y_cor)
        self.write(f"{name}")


