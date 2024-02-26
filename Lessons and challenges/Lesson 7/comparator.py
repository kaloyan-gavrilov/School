from turtle import *
from shape import Shape


class Comparator(Shape):
    def __init__(self, a, b, angle_a, angle_b, x, y):
        self.__a = a
        self.__b = b
        self.__angle_a = angle_a
        self.__angle_b = angle_b
        self.__x = x
        self.__y = y

    def draw(self):
        turtle = Turtle()
        speed(1)
        turtle.color("red")
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(self.__a)
            turtle.right(self.__angle_a)
            turtle.forward(self.__b)
            turtle.right(self.__angle_b)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(self.__x + self.__a / 2 - 20, self.__y - self.__b / 2)
        turtle.pendown()
        turtle.color("black")
        turtle.write(f"Area: {self.__a * self.__b}", align="center", font=("Arial", 12, "normal"))

        turtle.screen.mainloop()


c1 = Comparator(300, 120, 120, 60, 0, 0)
c1.draw()
