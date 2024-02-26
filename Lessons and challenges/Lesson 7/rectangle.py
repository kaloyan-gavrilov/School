from turtle import *
from shape import Shape


class Rectangle(Shape):
    def __init__(self, a, b, x, y):
        self.__a = a
        self.__b = b
        self.__x = x
        self.__y = y

    def draw(self):
        turtle = Turtle()
        speed(1)
        turtle.color("red")
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(self.__a)
            turtle.right(90)
            turtle.forward(self.__b)
            turtle.right(90)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(self.__x + self.__a/2, self.__y - self.__b/2)
        turtle.pendown()
        turtle.color("black")
        turtle.write(f"Area: {self.__a * self.__b}", align="center", font=("Arial", 12, "normal"))

        turtle.screen.mainloop()


r1 = Rectangle(100, 80, 0, 0)
r1.draw()
