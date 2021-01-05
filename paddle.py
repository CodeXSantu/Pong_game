from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.coordinate = position
        self.color("orange")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.setpos(self.coordinate)

    def paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)

