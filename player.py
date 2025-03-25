from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.penup()
        self.starting()
        self.left(90)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def starting(self):
        self.goto(STARTING_POSITION)

    
