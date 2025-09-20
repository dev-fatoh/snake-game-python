import turtle
import random
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

screen = turtle.Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = turtle.textinput(
    title="Make your bet", prompt="Which tutle will win the race? Enter a color : "
)
colors = ["red", "green", "yellow", "blue", "black", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle_racer in all_turtles:
        if turtle_racer.xcor() > 230:
            is_race_on = False
            winning_color = turtle_racer.pencolor()
            if winning_color == user_bet:
                print(f"You have Won! The {winning_color} turtle is the winner !!!!")
            else:
                print(f"You have Lost! The {winning_color} turtle is the winner !!!!")
        random_distance = random.randint(0, 10)
        turtle_racer.forward(random_distance)
screen.exitonclick()
