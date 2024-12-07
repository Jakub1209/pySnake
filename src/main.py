import turtle
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

# ---------------------------- CONSTANTS ---------------------------- #

DISTANCE_TO_EAT_FOOD = 18

# ---------------------------- FUNCTIONS ---------------------------- #


def map_value(value, from_range_min, from_range_max, to_range_min, to_range_max):
    return (value - from_range_min) * (to_range_max - to_range_min) / (from_range_max - from_range_min) + to_range_min


def pause_screen():
    snake.pause = not snake.pause
    scoreboard.pause_info(snake.pause)


def check_win_or_lose_conditions():
    loose_condition = snake.snake_head.xcor() > 280 \
                      or snake.snake_head.xcor() < -280 \
                      or snake.snake_head.ycor() > 280 \
                      or snake.snake_head.ycor() < -280 \
                      or snake.has_bitten_itself()

    if loose_condition:
        snake.reset_snake()
        scoreboard.reset_score()


# initialize the objects needed
scoreboard = Scoreboard()
snake = Snake()
food = Food()

# set up the screen
screen = Screen()
screen.title("Snake Game!")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# show a prompt asking user for his name
players_name = screen.textinput("Please enter your name", "Player's name:")
# fetch his highscore from the database
scoreboard.get_highscore_from_database(players_name)

# show a prompt asking user to enter a difficulty level
snake_speed_input = screen.textinput("Please enter your difficulty level", "Choose difficulty(1/10):")
# the input is then mapped from the user-friendly value, to the actual snake speed value
snake_speed = map_value(float(snake_speed_input), 1.0, 10, 0.15, 0.01)

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(pause_screen, "q")

game_is_on = True

while game_is_on:
    snake.move()

    time.sleep(snake_speed)
    screen.update()
    check_win_or_lose_conditions()

    if snake.snake_head.distance(food) < DISTANCE_TO_EAT_FOOD:
        food.spawn_food(snake_segments=snake.snake_segments)
        scoreboard.add_point(int(snake_speed_input))
        snake.add_segment()

turtle.mainloop()
