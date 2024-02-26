from turtle import *
from shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius, x, y):
        self.__radius = radius
        self.__x = x
        self.__y = y

    def draw(self):
        turtle = Turtle()
        turtle.penup()
        turtle.goto(self.__x, self.__y)
        turtle.pendown()
        turtle.color("red")
        # turtle.begin_fill()
        turtle.circle(self.__radius)
        # turtle.end_fill()

        turtle.penup()
        turtle.goto(self.__x, self.__y + self.__radius)
        turtle.pendown()
        turtle.color("black")  # Change color as needed
        turtle.write("Circumference: {:.2f}".format(2 * math.pi * self.__radius), align="center",
                     font=("Arial", 12, "normal"))
        # turtle.screen.mainloop()


t = Turtle()

c1 = Circle(100, -200, 0)
c1.draw()

circle2 = Circle(80, 0, -50)
circle2.draw()

t.screen.mainloop()
