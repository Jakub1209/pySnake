import time
import turtle
from turtle import Screen

from pySnake.scoreboard import Scoreboard
from pySnake.snake import Snake
from pySnake.food import Food


# ---------------------------- FUNCTIONS ---------------------------- #


def map_value(value, from_range_min, from_range_max, to_range_min, to_range_max):
    return (value - from_range_min) * (to_range_max - to_range_min) / (from_range_max - from_range_min) + to_range_min


class Game:
    DISTANCE_TO_EAT_FOOD = 18

    def __init__(self):
        # initialize the objects needed
        self.scoreboard = Scoreboard()
        self.snake = Snake()
        self.food = Food()

        # set up the screen
        self.screen = Screen()
        self.screen.title("Snake Game!")
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)

    def pause_screen(self):
        self.snake.pause = not self.snake.pause
        self.scoreboard.pause_info(self.snake.pause)

    def check_win_or_lose_conditions(self):
        loose_condition = self.snake.snake_head.xcor() > 280 \
                          or self.snake.snake_head.xcor() < -280 \
                          or self.snake.snake_head.ycor() > 280 \
                          or self.snake.snake_head.ycor() < -280 \
                          or self.snake.has_bitten_itself()

        if loose_condition:
            self.snake.reset_snake()
            self.scoreboard.reset_score()

    def run(self):
        # show a prompt asking user for his name
        players_name = self.screen.textinput("Please enter your name", "Player's name:")
        # fetch his highscore from the database
        self.scoreboard.get_highscore_from_database(players_name)

        # show a prompt asking user to enter a difficulty level
        snake_speed_input = self.screen.textinput("Please enter your difficulty level", "Choose difficulty(1/10):")
        # the input is then mapped from the user-friendly value, to the actual snake speed value
        snake_speed = map_value(float(snake_speed_input), 1.0, 10, 0.15, 0.01)

        self.screen.listen()
        self.screen.onkeypress(self.snake.up, "Up")
        self.screen.onkeypress(self.snake.down, "Down")
        self.screen.onkeypress(self.snake.left, "Left")
        self.screen.onkeypress(self.snake.right, "Right")
        self.screen.onkeypress(self.pause_screen, "q")

        game_is_on = True

        while game_is_on:
            self.snake.move()

            time.sleep(snake_speed)
            self.screen.update()
            self.check_win_or_lose_conditions()

            if self.snake.snake_head.distance(self.food) < self.DISTANCE_TO_EAT_FOOD:
                self.food.spawn_food(snake_segments=self.snake.snake_segments)
                self.scoreboard.add_point(int(snake_speed_input))
                self.snake.add_segment()

        turtle.mainloop()
