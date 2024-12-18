from turtle import Turtle


class Snake:
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

    def __init__(self) -> None:
        self.pause = False
        self.snake_step = 20
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self) -> None:
        for _ in self.STARTING_POSITIONS:
            self.add_segment()

    def add_segment(self) -> None:
        snake_segment = Turtle()
        snake_segment.color("white")
        snake_segment.shape("square")
        snake_segment.penup()
        self.snake_segments.append(snake_segment)
        snake_segment.goto(self.snake_segments[-1].pos())

    def up(self) -> None:
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self) -> None:
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def left(self) -> None:
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def right(self) -> None:
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def move(self) -> None:
        if self.pause:
            return

        for i in range(len(self.snake_segments) - 1, 0, -1):
            current_snake = self.snake_segments[i]
            next_snake = self.snake_segments[i - 1]

            new_x = next_snake.xcor()
            new_y = next_snake.ycor()

            current_snake.goto(new_x, new_y)

        self.snake_head.forward(self.snake_step)

    def has_bitten_itself(self) -> bool:
        for snake_segment in self.snake_segments[1:]:
            if snake_segment.distance(self.snake_head) < 8:
                return True
        return False

    def reset_snake(self) -> None:
        for segment in self.snake_segments:
            segment.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.snake_head = self.snake_segments[0]
