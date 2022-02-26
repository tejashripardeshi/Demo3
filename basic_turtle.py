#Tejashri Pardeshi
#import turtle
#win = turtle.Turtle()
#print(win.shap())
#help(turtle.shape)


#To display different shape
#win.shape("turtle")
#win.shape("arrow")
#win.shape("circle")
#win.shape("square")
#win.shape("triangle")

#to increase size of shape
#win.shapesize(4)

#to set colors
#win.screen.bgcolor("red")
#win.color("white")

#to hide shape icon
#win.hideturtle

#png or gif
#win.screen.bgpic("C:\\Users\\TEJASHRI\\Pictures\\Screenshots\\Screenshot (3).png")


#to change the heading pointer
#win.setheading(90)
#win.setheading(180)

#win.pensize(5)
#win.forward(300)
#win.fd(200)
#win.setheading(90)
#win.fd(300)
#win.setheading(90)
#win.fd(200)
#win.setheading(180)
#win.fd(300)
#win.setheading(270)
#win.hideturtle()





import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()
s.title("Star Program")
s.screensize(600,600,bg="black")
s.colormode(255)

t.pencolor("white")

#t.forward(100)

def star():
    for i in range(5):
        t.right(144)
        t.forward(50)

for i in range(30):
    x = random.randint(-300,300)
    y = random.randint(-300,300)

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    t.pencolor(r,b,g)

    t.penup()
    t.goto(x,y)
    t.pendown()
    star()
    
