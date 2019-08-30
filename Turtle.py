import turtle

wn=turtle.Screen()

alex=turtle.Turtle()

mary=turtle.Turtle()
mary.shape('turtle')
mary.up()
mary.goto(100,100)
mary.down()
mary.forward(50)

alex.speed(0)

#drawing square:


#alex.begin_fill()

alex.up()
alex.goto(0, -300)
alex.down()

n=int(input("Please enter the number of sides of a polygon: "))

side=float(input("Give the length of the side in pixels: "))

for i in range(n):
    if i % 3 ==0 :
        alex.color("green")
    elif i % 3 ==1 :
        alex.color("blue")
    else:
        alex.color("red")
    alex.forward(side)
    alex.left(360/n)

alex.end_fill()
    
print("bye")

#drawing triangle:

##alex.forward(300)
##alex.left(120)
##alex.forward(300)
##alex.left(120)
##alex.forward(300)


