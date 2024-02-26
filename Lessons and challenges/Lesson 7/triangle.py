from turtle import *
from shape import Shape
import math


class Triangle(Shape):
    def __init__(self, angle_a, angle_b, angle_c, side_a, side_b, side_c, x, y):
        self.__angle_a = angle_a
        self.__angle_b = angle_b
        self.__angle_c = angle_c
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c
        self.__x = x
        self.__y = y

    def draw(self):
        turtle = Turtle()

        s = (self.__side_a + self.__side_b + self.__side_b) / 2
        area = (s * (s - self.__side_a) * (s - self.__side_b) * (s - self.__side_c)) ** 0.5
        perimeter = self.__side_a + self.__side_b + self.__side_b

        if area > perimeter:
            turtle.color("blue")
        elif area < perimeter:
            turtle.color("green")
        else:
            turtle.color("red")

        turtle.penup()
        turtle.goto(self.__x, self.__y)
        turtle.pendown()

        x1 = turtle.xcor()
        y1 = turtle.ycor()
        turtle.begin_fill()
        turtle.forward(self.__side_a)
        x2 = turtle.xcor()
        y2 = turtle.ycor()
        turtle.left(180 - self.__angle_b)
        turtle.forward(self.__side_b)
        x3 = turtle.xcor()
        y3 = turtle.ycor()
        turtle.left(180 - self.__angle_c)
        turtle.forward(self.__side_c)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(self.__x + (x1+x2+x3)/3, self.__y + (y1 + y2 + y3)/3)
        turtle.pendown()
        turtle.color("black")

        if area > perimeter:
            turtle.write(f"Area: {area}", align="center", font=("Arial", 12, "normal"))
        elif perimeter > area:
            turtle.write(f"Perimeter: {perimeter}", align="center", font=("Arial", 12, "normal"))
        else:
            turtle.write(f"They are equal", align="center", font=("Arial", 12, "normal"))


t = Turtle()
t1 = Triangle(30, 60, 90, 240, 120, 200, 0, 0)
t1.draw()
t.screen.mainloop()
