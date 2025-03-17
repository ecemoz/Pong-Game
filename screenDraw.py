from turtle import Turtle

class ScreenDraw(Turtle):
    def __init__(self):
        super().__init__()
        super().color("#fafbfb")
        super().pensize(width=4)
        super().hideturtle()
        super().penup()
        super().goto(-420, 315)
        super().pendown()
        super().forward(840)
        super().right(90)
        super().forward(630)
        super().right(90)
        super().forward(840)
        super().right(90)
        super().forward(630)
        super().penup()
        super().goto(0, -305)
        super().setheading(90)
        for i in range(21):
            super().dot(15, "white")
            super().forward(30)