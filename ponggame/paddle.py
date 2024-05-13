from turtle import Turtle

class  Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)#paddle of width 0 and length 100 initially it will be(20,20)
        self.goto(position)
    

    def goup(self):
        new_y=self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def godown(self):
        new_y=self.ycor() - 20
        self.goto(self.xcor(),new_y)





