from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():

    def __init__(self):
        self.snakes = []
        self.pos = 0

        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.snake_parts = []
        self.make_snake_body()
        self.head = self.snake_parts[0]

    def make_snake_body(self):
        for pos in self.starting_positions:
            snake = Turtle("square")
            snake.color('white')
            snake.penup()
            snake.goto(pos)

            self.snake_parts.append(snake)

    def move_snake_forwards(self):
        for num_parts in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[num_parts - 1].xcor()
            new_y = self.snake_parts[num_parts - 1].ycor()
            self.snake_parts[num_parts].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake_parts[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def increase_snake_length(self):
        snake = Turtle("square")
        snake.color('white')
        snake.penup()
        snake.goto(self.snake_parts[-1].position())
        self.snake_parts.append(snake)

    def reset_body(self):
        self.snake_parts.clear()
        self.make_snake_body()
