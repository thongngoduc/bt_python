import turtle,random
colors=['red','blue','green']
painter=turtle.Turtle()
painter.pensize(3)
for i in range(12):
    for i in range(0,3):
        color=(colors)[i]
        painter.pencolor(color)
        painter.circle(100)
        painter.right(30)
        painter.left(60)
        painter.setposition(0,0)
