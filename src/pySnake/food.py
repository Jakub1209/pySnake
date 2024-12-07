from turtle import Turtle
from random import choice

FOOD_X_AXIS = [num for num in range(-260, 261, 20)]
FOOD_Y_AXIS = [num for num in range(-260, 221, 20)]


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.spawn_food(food_pos=(0, 0))

    def spawn_food(self, **kwargs):
        food_pos = kwargs.get("food_pos")
        snake_segments = kwargs.get("snake_segments")
        self.goto(self.choose_new_food_position(food_pos=food_pos, snake_segments=snake_segments))

    def choose_new_food_position(self, **kwargs) -> tuple:
        food_pos = kwargs.get("food_pos")
        snake_segments = kwargs.get("snake_segments")

        if snake_segments is not None:
            # choose a random x and y number from the lists
            x_choice = choice(FOOD_X_AXIS)
            y_choice = choice(FOOD_Y_AXIS)
            food_pos_tuple = (x_choice, y_choice)
            # make a list of all the current snake segments positions
            list_of_snake_positions = [snake_segment.pos() for snake_segment in snake_segments]

            if food_pos_tuple in list_of_snake_positions:
                x_choice = choice(FOOD_X_AXIS)
                y_choice = choice(FOOD_Y_AXIS)
        else:
            food_pos_tuple = food_pos

        new_position = food_pos_tuple
        return new_position
