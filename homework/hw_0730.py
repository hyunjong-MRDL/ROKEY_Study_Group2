import turtle

def drawStar(x,y,size,color):
    star = turtle.Turtle()
    star.pensize(3)
    star.speed(3)
    star.pencolor(color)
    star.penup()
    star.goto(x,y)
    star.pendown()
    for _ in range(5):

        star.fd(size)
        star.left(144)
    star.hideturtle()

if __name__ == '__main__':
    turtle.setup(800,600)
    turtle.bgcolor()
    drawStar(50,50,50,'red')
    turtle.exitonclick()