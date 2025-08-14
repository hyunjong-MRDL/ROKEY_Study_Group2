import turtle

def drawStar(pen, x_coord, y_coord, size, color):
    pen.color(color)

    pen.penup()
    pen.goto(x_coord, y_coord)
    pen.pendown()

    for i in range(5):
        pen.forward(size)
        pen.right(180-180/5)

def drawMoon(pen, x_coord, y_coord, size, color):
    pen.color(color)

    pen.penup()
    pen.goto(x_coord, y_coord)
    pen.pendown()

    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()

bg_color = "#1A2B3C"
speed = 0
pensize = 1
star_size = 30
star_color = "gold"
moon_size = 100
moon_color = "lemonchiffon"

turtle.setup(500, 400)
turtle.bgcolor(bg_color)

pen = turtle.Turtle()
pen.speed(speed)
pen.pensize(pensize)

drawMoon(pen, 140, -5, moon_size, moon_color)
drawStar(pen, -200, 150, star_size, star_color)
drawStar(pen, -100, 30, star_size, star_color)
drawStar(pen, 0, 150, star_size, star_color)

pen.hideturtle()
turtle.exitonclick()