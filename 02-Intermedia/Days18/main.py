import random
import turtle as t

tim = t.Turtle()

colors = ["blue", "red", "yellow", "green", "purple"]


def draw_shape(num_sides):
    angle = 360 / num_sides

    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)