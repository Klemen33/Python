import turtle as t
import colorsys

t.bgcolor('black')
t.speed('fastest')

t.pensize(2)

hue=0.0

t.hideturtle()


for i in range(310):
    color = colorsys.hsv_to_rgb(hue, 1,1)
    t.pencolor(color)
    hue += 0.005

    for j in range(2):
        t.forward(i)
        t.right(120)
        t.forward(10)
        t.right(60)
        t.circle(70)
    t.right(90*2+1)
    t.tracer(10)
t.exitonclick()
