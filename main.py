from turtle import Turtle, Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

sc = Screen()
sc.setup(600, 600)
sc.bgcolor("black")
sc.tracer(0)  # This turns off the tracer of the screen

game_over = Turtle()
game_over.hideturtle()
game_over.color("orange")

sn = Snake()
sc.onkey(sn.up, 'Up')
sc.onkey(sn.down, 'Down')
sc.onkey(sn.right, 'Right')
sc.onkey(sn.left, 'Left')

f = Food()
score = Scoreboard()
game_is_on = True


# WHILE GAME IS ON, MOVE FORWARDS
while game_is_on:
    sc.update()
    time.sleep(0.1)

    sn.move_snake_forwards()
    sc.listen()

    # DETECT FOOD COLLISION
    if sn.head.distance(f) < 17:
        f.randomize_location()
        score.increase_score()
        sn.increase_snake_length()

    # DETECT WALL COLLISION
    if sn.head.xcor() > 295 or sn.head.xcor() < -295 or sn.head.ycor() > 295 or sn.head.ycor() < -295:
        game_over.write("GAME OVER.", False, "center", font=('Courier', 22, "bold", 'bold'))
        game_is_on = False
        score.reset_score()

    for seg in sn.snake_parts[1:]:
        if sn.head.distance(seg) < 10:
            game_over.write("GAME OVER.", False, "center", font=('Courier', 22, "bold", 'bold'))
            game_is_on = False
            score.reset_score()


sc.exitonclick()
