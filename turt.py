import turtle

turtle.shape("turtle")
turtle.speed(7)
turtle.color("green")
turtle.bgcolor("black")
counter = 0
while counter < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    counter += 1
    turtle.left(10)

turtle.exitonclick()