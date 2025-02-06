import turtle

t = turtle.Turtle()

def draw_A():
    t.left(75)
    t.forward(100)
    t.right(150)
    t.forward(100)
    t.backward(50)
    t.right(105)
    t.forward(30)
    t.backward(30)
    t.right(75)
    t.backward(50)
    t.right(90)

def draw_R():
    t.right(-75)
    t.forward(100)
    t.right(90)
    t.circle(-25,180)
    t.left(150)
    t.forward(70)
    t.right(320)

def draw_Y():
    t.right(-90)
    t.forward(50)
    t.right(-30)
    t.forward(30)
    t.backward(30)
    t.left(-60)
    t.forward(30)
    t.backward(30)
    t.left(30)
    t.backward(50)
    t.right(90)

def draw_N():
    t.right(-90)
    t.forward(100)
    t.right(135)
    t.forward(100)
    t.left(135)
    t.forward(100)
    t.backward(100)


def move():
    t.penup()
    t.forward(50)
    t.pendown()

draw_A()
move()
draw_R()
move()
draw_Y()
move()
draw_A()
move()
draw_N()

turtle.done()