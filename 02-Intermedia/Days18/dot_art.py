import random
import turtle as T
import colorgram

# =============== 获取图片中的颜色 ==============
rgb_color = []
colors = colorgram.extract("image.jpg", 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)


print(rgb_color)


# ================ 使用这些颜色去绘图 ============
import turtle as turtle_module
import random

turtle_module.colormode(255)  # 色彩模式
tim = turtle_module.Turtle()  # 使用 Turtle()创建一个对象
tim.speed("fastest")  # 速度为最快
tim.penup()  # 开始
tim.hideturtle()  # 隐藏海龟，这样就不会有海归模型出现在跑
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71),
              (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)  # 朝向
tim.forward(300)  # 距离
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    # 每10个一行
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()