import turtle

# размер и заголовок диалогового окна
window = turtle.Screen()
window.title("Ping-Pong")
window.setup(width=1.0, height=1.0)
window.bgcolor("black")


# размеры  и отрисовка поля
border = turtle.Turtle()
border.speed(0)
border.color('green')
border.begin_fill()
border.goto(500,300)
border.goto(-500,300)
border.goto(-500,-300)
border.goto(500,-300)
border.goto(500,300)
border.end_fill()

border.goto(0,300)
border.color('white')
border.setheading(270)
for i in range(25):
    if i%2==0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()
