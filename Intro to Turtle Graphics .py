# Author='Daniel Lewis'
# Telos='Homework'
# Topic='Turtle Graphics'
# Identifier='Pattern Homework'
# Date=23-09-2024

import turtle
turtle.shape('turtle')
turtle.color('blue')
turtle.speed(10000)

for pattern in range(0,6):
    for star in range(0,9):
        for fivepoint in range(0,5):
            turtle.color('blue')
            turtle.forward(150)
            turtle.right(144)
        turtle.right(6)
    for celestailobject in range(0,5):
        turtle.color('red')
        turtle.forward(200)
        turtle.right(144)
    turtle.right(6)

# Task 7
import random
for random in range(random.randint(1,10),random.randint(10,60)):
    turtle.pencolor(random.choice(['red','blue','green','yellow'])
    turtle.forward(random.randint(10,100))
    turtle.right(random.randint(0,360))
