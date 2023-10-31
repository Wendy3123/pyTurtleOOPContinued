from turtle import Turtle,Screen
import random

wendy = Turtle()
wendy.shape('turtle')
wendy.color('hotpink')

screen = Screen()
screen.bgcolor("pink")

#creates dashed lines

# for x in range(7):         
#     wendy.forward(20)
#     wendy.penup()       #picks pen up so it stops drawing 
#     wendy.forward(20)
#     wendy.pendown()         #puts pen back down to draw again



#for a full circle its 360 deg so how we get each shape is by doiong 360/sides the shape has

# colors =['violet','hot pink','medium orchid','blue violet','light sky blue','aquamarine']
# def shapes(sides):
#     for x in range(sides):
#         wendy.forward(90)
#         wendy.right(360/sides)
    

# for x in range(3,9):
#     wendy.color(random.choice(colors))  #changed the color every shape
#     shapes(x)

#shorter way to call all these is to use a for loop it will give us same results as the codes below line 28-32
# shapes(3)       #makes a triangle
# shapes(4)       #makes a square
# shapes(5)       #makes a pentagon
# shapes(6)       #makes a hexagon
# shapes(7)       #makes a 7 sided shape

direction = ['right','left','forward']
randomChoice= random.choice(direction)
for x in range(10):
    wendy.randomChoice(100)



screen.exitonclick()


