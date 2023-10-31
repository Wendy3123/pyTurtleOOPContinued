from turtle import Turtle,Screen
import turtle
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




#make the turtle go random directions 100 times

direction = [0,90,180,270]

#create our random color generator instead of using a list array above where we manually entered the color name
turtle.colormode(255) #set the color from 0 to 255 instead of 0 to 1
def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    random_color = (r,g,b)
    return random_color

wendy.width(10)          #make line width thicker
wendy.speed('fastest')      #draws all the lines faster
colors =['violet','hot pink','medium orchid','blue violet','light sky blue','aquamarine']
for x in range(100):
    wendy.color(random_color())
    wendy.forward(30)
    wendy.setheading(random.choice(direction))
    




screen.exitonclick()


