# This is the initial code used to extract a list of tupples
# from an image file in order to complete the Hirst Painting Project


# import colorgram
# 
#
# def value_extract(color_obj):
#     rgb = color_obj.rgb
#     red = rgb[0]
#     green = rgb[1]
#     blue = rgb[2]
#     color_tup = (red, green, blue)
#     return color_tup
#
#
# colors = colorgram.extract('hirst_dot.jpg', 30)
# rgb_list = []
# for color_extracted in colors:
#     rgb_list.append(value_extract(color_extracted))



import turtle
from turtle import Turtle, Screen
import random


def hirst_art(my_turtle):
    my_turtle.penup()
    my_turtle.forward(50)
    my_turtle.pendown()
    my_turtle.dot(20, random.choice(color_list))


turtle.colormode(255)
color_list = [(167, 77, 38), (24, 115, 157), (216, 150, 90), (19, 35, 28), (188, 177, 28), (29, 133, 87),
              (214, 73, 116), (160, 57, 94), (118, 186, 155), (101, 175, 201), (208, 129, 162), (59, 166, 111),
              (228, 79, 41), (224, 206, 89), (22, 166, 196), (132, 33, 58), (12, 98, 64), (227, 219, 200),
              (27, 57, 120), (217, 227, 221), (131, 37, 28), (229, 206, 11), (83, 77, 26), (17, 84, 99),
              (212, 224, 229), (158, 209, 190), (225, 167, 193)]

h_turtle = Turtle()
my_screen = Screen()
h_turtle_x = 0
h_turtle_y = 0

for rows in range(9):
    h_turtle.setposition(h_turtle_x, h_turtle_y)
    for dots in range(9):
        h_turtle.speed("fastest")
        hirst_art(h_turtle)
        h_turtle.penup()
    h_turtle_y += 50

my_screen.exitonclick()