# Introductory message: A House with a garden and front yard on a sunny day located in housesstreet, GA (not a real city)
# File: HomeScape.py
# CSC 1301 - Homework 4
# Author: Hemant Kosaraju 
# Email: hkosaraju2@student.gsu.edu
# Section: Section 014 and CRN 84157
# Date: November 1 2022
""" Description: This program creates an image or vector image of a house and landscape similar to one you see in Google images. This program is implemented with Turtle module inside
of the Python interpreter using import turtle. The remaining code works with this imported module to use objects within the turtle module by using dot — notation, for example: .color(),
.speed(), .forward(), .right(), .left(), .circle(), and more.  """

import turtle

turtle.speed(10)
turtle.pensize(5)

turtle.bgcolor("#71BCE1")

turtle.penup()
turtle.goto(-400, -100)
turtle.pendown()
turtle.color("#486F38")
turtle.begin_fill()

for _ in range(2):
    turtle.forward(1920)
    turtle.right(90)
    turtle.forward(329)
    turtle.right(90)
turtle.end_fill()

turtle.color("#486F38")
turtle.begin_fill()
for _ in range(2):
    turtle.right(90)
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(500)
turtle.end_fill()

turtle.setpos(-120, -100)

walls = turtle.color("#8a3732")
turtle.begin_fill()

for item in range(1,5):
    turtle.forward(300)
    turtle.left(90)
turtle.end_fill()

turtle.penup()
turtle.left(90)
turtle.forward(300)
turtle.pendown()

roof = turtle.color("#b39c79")
turtle.begin_fill()
turtle.left(90)
turtle.forward(30)
turtle.right(180)
turtle.forward(360)
turtle.left(150)
turtle.forward(210)
turtle.left(60)
turtle.forward(210)
turtle.end_fill()

turtle.penup()
turtle.left(150)
turtle.forward(150)
turtle.right(90)
turtle.forward(110)

turtle.pensize(2)

inside_window = turtle.color("#FFFFFF")
turtle.begin_fill()
turtle.pendown()
for item in range(1,5):
    turtle.right(90)
    turtle.forward(100)
turtle.end_fill()

window = turtle.color("#000000")
turtle.back(50)
turtle.right(90)
turtle.forward(100)
turtle.back(50)
turtle.right(90)
turtle.back(50)
turtle.forward(100)

door = turtle.color("#b39c79") # Using this hex decimal temporarily

turtle.penup()
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(150)
turtle.pendown()
turtle.begin_fill()
turtle.forward(140)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(70)
turtle.end_fill()

turtle.penup()
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(60)

turtle.pendown()
turtle.color("#000000")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.left(90)
turtle.forward(220)

inside_window = turtle.color("#FFFFFF")
turtle.begin_fill()
turtle.pendown()
for item in range(1,5):
    turtle.right(90)
    turtle.forward(100)
turtle.end_fill()

window = turtle.color("#000000")
turtle.back(50)
turtle.right(90)
turtle.forward(100)
turtle.back(50)
turtle.right(90)
turtle.back(50)
turtle.forward(100)


turtle.penup()
turtle.forward(190)
turtle.left(90)
turtle.forward(105)
turtle.left(135)


turtle.pendown()
count = 0
turtle.color("#4e8c3c")
turtle.begin_fill()  
for item in range(274):
    turtle.speed(10)
    turtle.forward(1)
    turtle.right(1)
    count += 1
turtle.end_fill()

turtle.penup()
turtle.left(140)
turtle.forward(50)
turtle.left(135)

turtle.pendown()
turtle.begin_fill()
for item in range(274):
    turtle.speed(10)
    turtle.forward(1)
    turtle.right(1)
    count += 1
turtle.end_fill()

turtle.penup()
turtle.right(42)
turtle.forward(570)
turtle.right(135)

turtle.pendown()
turtle.begin_fill()
for item in range(274):
    turtle.speed(10)
    turtle.forward(1)
    turtle.left(1)
    count += 1
turtle.end_fill()

turtle.penup()
turtle.right(140)
turtle.forward(50)
turtle.right(135)

turtle.pendown()
turtle.begin_fill()
for item in range(274):
    turtle.speed(10000000000)
    turtle.forward(1)
    turtle.left(1)
    count += 1
turtle.end_fill()

turtle.penup()
turtle.left(180)
turtle.right(30)
turtle.forward(440)
turtle.pendown()

Sun = turtle.color("#FFA500")
turtle.begin_fill()
count = 0
for _ in range(360):
    turtle.speed(10)
    turtle.forward(1)
    turtle.left(1)
    count += 1
turtle.end_fill()

turtle.penup()
turtle.goto(330, 260)
turtle.pendown()


turtle.color("#FFFFFF")
turtle.begin_fill()
turtle.goto(360, 260)
turtle.circle(25)
turtle.end_fill()

turtle.begin_fill()
turtle.goto(380, 300)
turtle.circle(25)
turtle.end_fill()

turtle.begin_fill()
turtle.goto(390, 275)
turtle.circle(25)
turtle.end_fill()

turtle.begin_fill()
turtle.goto(340, 285)
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(-200, 260)
turtle.pendown()

turtle.color("#FFFFFF")
turtle.begin_fill()
turtle.goto(-220, 260)
turtle.circle(25)
turtle.end_fill()

turtle.begin_fill()
turtle.goto(-240, 300)
turtle.circle(25)
turtle.end_fill()

turtle.begin_fill()
turtle.goto(-250, 275)
turtle.circle(25)
turtle.end_fill()

turtle.begin_fill()
turtle.goto(-200, 285)
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(-600, -200)
turtle.pendown()


turtle.pensize(5) 
turtle.speed(10) 
turtle.fillcolor("yellow") 
turtle.begin_fill() 

for i in range(4):
    turtle.circle(40, 50)
    turtle.circle(10, 180)
    turtle.left(180)
    turtle.circle(10, 180)
    turtle.circle(40, 50)
    turtle.left(180)
turtle.end_fill() 

turtle.penup()
turtle.goto(-600, -200)
turtle.pendown()
turtle.circle(1)


turtle.penup()
turtle.goto(-600, -200)
turtle.pendown()
turtle.right(180)
turtle.circle(-100, 80)

turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()


turtle.pensize(5) 
turtle.speed(10) 
turtle.fillcolor("purple") 
turtle.begin_fill() 

for i in range(4):
    turtle.circle(40, 50)
    turtle.circle(10, 180)
    turtle.left(180)
    turtle.circle(10, 180)
    turtle.circle(40, 50)
    turtle.left(180)
turtle.end_fill() 

turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.circle(1)


turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.right(0)
turtle.circle(-100, 80)

turtle.penup()
turtle.goto(200, -200)
turtle.pendown()


turtle.pensize(5) 
turtle.speed(10) 
turtle.fillcolor("blue") 
turtle.begin_fill() 

for i in range(4):
    turtle.circle(40, 50)
    turtle.circle(10, 180)
    turtle.left(180)
    turtle.circle(10, 180)
    turtle.circle(40, 50)
    turtle.left(180)
turtle.end_fill() 

turtle.penup()
turtle.goto(200, -200)
turtle.pendown()
turtle.circle(1)


turtle.penup()
turtle.goto(200, -200)
turtle.pendown()
turtle.right(270)
turtle.circle(-100, 80)


turtle.penup()
turtle.goto(600, -200)
turtle.pendown()


turtle.pensize(5) 
turtle.speed(10) 
turtle.fillcolor("red") 
turtle.begin_fill() 

for i in range(4):
    turtle.circle(40, 50)
    turtle.circle(10, 180)
    turtle.left(180)
    turtle.circle(10, 180)
    turtle.circle(40, 50)
    turtle.left(180)
turtle.end_fill() 

turtle.penup()
turtle.goto(600, -200)
turtle.pendown()
turtle.circle(1)


turtle.penup()
turtle.goto(600, -200)
turtle.pendown()
turtle.right(0)
turtle.circle(-100, 80)


turtle.done()