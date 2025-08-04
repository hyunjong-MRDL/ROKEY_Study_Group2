import turtle
import hw_0730
import hw_0730_1
turtle.setup(400,400)
turtle.bgcolor('black')

for i in range(-30,90,30):
    hw_0730.drawStar(i,0,20,'white')
hw_0730_1.drawMoon(70,50,50,'yellow')



turtle.exitonclick()