import turtle

turtle.up()
turtle.color("red")
turtle.begin_fill()
turtle.backward(300)
turtle.setheading(60)
turtle.down()
turtle.circle(60,steps=(3))
turtle.end_fill()

turtle.up()
turtle.setheading(0)
turtle.forward(150)
turtle.down()

turtle.color("blue")
turtle.begin_fill()
turtle.setheading(45)
turtle.circle(60,steps=(4))
turtle.end_fill()

turtle.up()
turtle.setheading(0)
turtle.forward(150)
turtle.down()

turtle.color("black")
turtle.begin_fill()
turtle.setheading(36)
turtle.circle(60,steps=5)
turtle.end_fill()

turtle.up()
turtle.setheading(0)
turtle.forward(150)
turtle.down()

turtle.color("green")
turtle.begin_fill()
turtle.setheading(30)
turtle.circle(60,steps=(6))
turtle.end_fill()

turtle.up()
turtle.setheading(0)
turtle.forward(150)
turtle.down()

turtle.color("yellow")
turtle.begin_fill()
turtle.setheading(22.5)
turtle.circle(60,steps=(8))
turtle.end_fill()