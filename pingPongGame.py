import turtle
from random import choice, randint

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

# рисуем пунктир
for i in range(25):
    if i%2==0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()

# рисуем ракетки
rocket_p1 =turtle.Turtle()
rocket_p1.color("white")
rocket_p1.shape("square")
rocket_p1.shapesize(stretch_len=1, stretch_wid=5)
rocket_p1.penup()
rocket_p1.goto(-450,0)

rocket_p2 =turtle.Turtle()
rocket_p2.color("white")
rocket_p2.shape("square")
rocket_p2.shapesize(stretch_len=1, stretch_wid=5)
rocket_p2.penup()
rocket_p2.goto(450,0)

# движение ракетки
def move_up_p1():
    y = rocket_p1.ycor() + 15
    if y > 250:
        y = 250
    rocket_p1.sety(y)

def move_down_p1():
    y = rocket_p1.ycor() - 15
    if y < -250:
        y = -250
    rocket_p1.sety(y)

def move_up_p2():
    y = rocket_p2.ycor() + 15
    if y > 250:
        y = 250
    rocket_p2.sety(y)

def move_down_p2():
    y = rocket_p2.ycor() - 15
    if y < -250:
        y = -250
    rocket_p2.sety(y)

# рисуем мяч
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.speed(0)

# задаем скорость движения
ball.dx = 3
ball.dy = -3
ball.penup()

# Назначение клавиш ракеток
window.listen()
window.onkeypress(move_up_p1, "w")
window.onkeypress(move_down_p1, "s")
window.onkeypress(move_up_p2, "Up")
window.onkeypress(move_down_p2, "Down")

# задаем параметра движения мяча
while True:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    if ball.ycor() <= -290:
        ball.dy = -ball.dy

    if ball.xcor() >= 490:
        ball.goto(0,randint(-150,150))
        ball.dx = choice([-4,-3,-2,2,3,4])
        ball.dy = choice([-4,-3,-2,2,3,4])

    if ball.xcor() <= -490:
        ball.goto(0,randint(-150,150))
        ball.dx = choice([-4,-3,-2,2,3,4])
        ball.dy = choice([-4,-3,-2,2,3,4])


window.mainloop()
