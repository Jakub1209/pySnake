import turtle
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time
from random import choice

# ---------------------------- CONSTANTS ---------------------------- #

DISTANCE_TO_EAT_FOOD = 18

FOOD_X_AXIS = [num for num in range(-260, 261, 20)]
FOOD_Y_AXIS = [num for num in range(-260, 221, 20)]


# ---------------------------- FUNCTIONS ---------------------------- #


def choose_new_food_position():
    # choose a random x and y number from the lists
    x_choice = choice(FOOD_X_AXIS)
    y_choice = choice(FOOD_Y_AXIS)
    food_pos_tuple = (x_choice, y_choice)

    # make a list of all the current snake segments positions
    list_of_snake_positions = [snake_segment.pos() for snake_segment in snake.snake_segments]
    print(list_of_snake_positions)
    print((x_choice, y_choice))

    # if the chosen position is not in list of snake positions, then spawn food there
    if food_pos_tuple in list_of_snake_positions:
        x_choice = choice(FOOD_X_AXIS)
        y_choice = choice(FOOD_Y_AXIS)
        print("I chose a new position!")

    new_position = (x_choice, y_choice)
    return new_position


def map_value(value, from_range_min, from_range_max, to_range_min, to_range_max):
    return (value - from_range_min) * (to_range_max - to_range_min) / (from_range_max - from_range_min) + to_range_min


def pause_screen():
    snake.pause = not snake.pause
    scoreboard.pause_info(snake.pause)


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

    if (snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or
            snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280 or
            snake.has_bitten_itself()):
        snake.reset_snake()
        scoreboard.reset_score()

    if snake.snake_head.distance(food) < DISTANCE_TO_EAT_FOOD:
        food.spawn_food(choose_new_food_position())
        scoreboard.add_point(int(snake_speed_input))
        snake.add_segment()

turtle.mainloop()
