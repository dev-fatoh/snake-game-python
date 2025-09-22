from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)
game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with wall
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # Detect collision with the wall
    if (
        snake.head.xcor() > 500
        or snake.head.xcor() < -500
        or snake.head.ycor() > 400
        or snake.head.ycor() < -400
    ):
        game_is_on = False
        scoreboard.game_over()
    # Detect collision with snake tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
