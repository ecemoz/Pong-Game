from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,coordinate):
        super().__init__()
        super().shape("square")
        super().color("purple")
        super().shapesize(stretch_wid=5, stretch_len= 1)
        super().penup()
        super().goto(coordinate)

    def go_up(self):
        new_y = super().ycor() + 20
        super().goto(super().xcor(), new_y)

    def go_down(self):
        new_y = super().ycor() - 20
        super().goto(super().xcor(), new_y)
