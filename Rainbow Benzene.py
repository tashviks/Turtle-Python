import turtle
turtle.speed(1000)
wn=turtle.Screen()
wn.bgcolor("black")
clrs = ["red" , "purple" , "green" , "orange" , "blue" , "yellow"]
p = turtle.Pen()
for i in range (360) :
    p.pencolor(clrs[i%6])
    p.width(i//100 + 1)
    p.forward(i)
    p.left(61)
    
    
    
