import turtle
X = eval(input("Enter lenght of star sides: "))

turtle.up()

turtle.pensize(9)
turtle.forward(100)
turtle.down()

turtle.begin_fill()

turtle.color("blue")
turtle.right(144)
turtle.forward(X)

turtle.color("green")
turtle.right(144)
turtle.forward(X)

turtle.color("red")
turtle.right(144)
turtle.forward(X)

turtle.color("yellow")
turtle.right(144)
turtle.forward(X)

turtle.color("purple")
turtle.right(144)
turtle.forward(X)

turtle.color("white")
turtle.end_fill()

turtle.done()