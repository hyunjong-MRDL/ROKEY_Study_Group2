import turtle

def drawMoon(x,y,size,color1):
    moon = turtle.Turtle()
    moon.pensize(3)
    moon.color(color1,color1)
    moon.speed(3)
    moon.penup()
    moon.goto(x,y)
    moon.pendown()
    moon.begin_fill()
    moon.circle(size)
    moon.end_fill()
    moon.hideturtle()

if __name__ == '__main__':
    turtle.setup(800,600)
    turtle.bgcolor()
    drawMoon(-50,-50,50,'yellow')
    turtle.exitonclick()