from turtle import Screen, Turtle

tim = Turtle()
tim.speed('fastest')


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def move_f():
    tim.fd(10)


def move_b():
    tim.backward(10)


def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()


display = Screen()

display.listen()

display.onkey(clear, "c")
display.onkey(move_b, "s")
display.onkey(move_f, "w")
display.onkey(turn_left, "a")
display.onkey(turn_right, "d")

display.exitonclick()
