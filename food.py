from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.spawn_food((0, 0))

    def spawn_food(self, spawned_food_position):
        self.goto(spawned_food_position)
