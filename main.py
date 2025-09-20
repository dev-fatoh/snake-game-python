import turtle
import random

turtle.colormode(255)
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)
tim = turtle.Turtle()


color_list = [
    (228, 235, 231),
    (199, 162, 100),
    (62, 91, 128),
    (140, 170, 192),
    (139, 90, 48),
    (219, 206, 119),
    (135, 27, 52),
    (32, 41, 67),
    (78, 16, 36),
    (149, 59, 85),
    (167, 154, 49),
    (187, 143, 162),
    (134, 183, 147),
    (46, 55, 100),
    (181, 95, 107),
    (56, 39, 27),
    (96, 118, 167),
    (80, 150, 159),
    (89, 152, 92),
    (71, 118, 93),
    (220, 175, 187),
    (169, 207, 163),
    (161, 202, 215),
    (192, 95, 74),
    (178, 187, 213),
    (46, 73, 75),
    (76, 69, 44),
]
tim.speed("fastest")


def move_forward():
    tim.forward(10)


screen = turtle.Screen()
screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()
