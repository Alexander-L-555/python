# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract('hirst.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random


turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(241, 238, 231), (237, 245, 239), (207, 159, 115), (247, 239, 242), (13, 26, 15), (149, 80, 45), (58, 42, 19), (227, 206, 116), (232, 238, 243), (31, 114, 147), (131, 178, 148), (61, 113, 79), (230, 77, 49), (119, 172, 191), (158, 26, 10), (202, 134, 146), (21, 46, 61), (172, 149, 54), (221, 76, 90), (139, 67, 80), (71, 165, 102), (238, 167, 156), (80, 69, 32), (36, 163, 189), (28, 88, 63), (165, 211, 163), (132, 33, 43), (237, 161, 169), (10, 89, 105), (63, 41, 49)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()