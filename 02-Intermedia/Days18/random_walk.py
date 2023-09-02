import random
import turtle

walk = turtle.Turtle()

walk.hideturtle()
walk.pensize(15)
walk.speed(0)

def random_color():
    turtle.colormode(255)
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    walk.color(R, G, B)

def turn():
    return random.choice([0, 90, 180, 270])

while True:
    random_color()
    walk.forward(40)
    walk.setheading(turn())

