from turtle import *

width(2)
penup()
left(180)
forward(100)
pendown()
left(180)
def circle_left(step):
    left(90)
    for i in range(60):
        forward(step)
        left(6)
    right(90)
color('blue')
circle_left(10)
color('black')
circle_left(20)
penup()
forward(20)
pendown()
def circle_right(step):
    left(90)
    for i in range(60):
        forward(step)
        right(6)
    right(90)
color('blue')
circle_right(10)
color('black')
circle_right(20)
right(90)
penup()
forward(200)
right(60)
width(8)
for i in range(60):
    forward(6)
    right(1)
pendown()
color('red')
left(180)
for i in range(50):
    forward(14)
    left(1)
left(180)
penup()
for i in range(25):
    forward(14)
    right(1)
right(90)
forward(250)
left(90)
forward(5)
left(90)
pendown()
color('black')
width(2)
right(70)
for i in range(40):
    forward(4)
    left(1)
for i in range(50):
    forward(2)
    left(3)
forward(50)
for i in range (40):
    forward(0.5)
    right(3)
for i in range(40):
    forward(0.5)
    left(3)
forward(5)
left(90)
