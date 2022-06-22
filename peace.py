

from turtle import Screen
import turtle as t
import random


timmy = t.Turtle()
t.colormode(255)
timmy.shape()
colours = ['coral', 'red', 'blue', 'green','cyan']
directions = [0, 90, 190, 270]
timmy.pensize(1)
timmy.speed(0.7)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

#PEACE
timmy.circle(50, -180)
timmy.circle(-50, -180)
timmy.circle(-100)
    

#Turtle SpinoGraph
for _ in range(36):
    timmy.circle(100)
    timmy.color(random_color())
    timmy.left(10)


# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))


# def new_shape(x):
#     angle = 360 / x
#     for num in range(x):
#         timmy.color(random.choice(colours))
#         timmy.forward(100)
#         timmy.right(angle)




# for num in range (3, 11):
#     new_shape(num)




my_screen = Screen()
my_screen.exitonclick()
