from turtle import *
import random
import colorgram



miguel_angel = Turtle()
miguel_angel.shape("turtle")
miguel_angel.speed("fastest")
screen = Screen()
screen.colormode(255)

def spirograph (angle):
    for i in range(int(360/ angle)):
        miguel_angel.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        miguel_angel.circle(120, 360)
        miguel_angel.left(angle)

spirograph(2)


screen.exitonclick()
