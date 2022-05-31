import turtle

window = turtle.Screen()
window.bgcolor("black")
window.setup(width=800, height=600)
window.title("Pong")
window.tracer(0)


# Creating a Paddle A to the left
paddle_a = turtle.Turtle()
paddle_a.color("yellow")
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.goto(-350, 0)
paddle_a.penup()

# Creating a paddle B to the right

paddle_b = turtle.Turtle()
paddle_b.color("green")
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.goto(350, 0)
paddle_b.penup()

# Creating a Ball in the center

ball = turtle.Turtle()
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.shape("square")
ball.speed(0)
ball.dx = 0.3
ball.dy = -0.3

# Creating a scorecard

score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.goto(0, 250)
score.hideturtle()
score.write("Player 1 : 0  Player 2 : 0", align="center",
            font=("Courier", 24, "normal"))


# variables to count scores of the players
scoreA = 0
scoreB = 0

# functions


def padlle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def padlle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def padlle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def padlle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


window.listen()
window.onkeypress(padlle_a_up, "w")
window.onkeypress(padlle_a_down, 's')
window.onkeypress(padlle_b_down, "l")
window.onkeypress(padlle_b_up, 'o')


while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if(ball.ycor() > 290):
        ball.sety(290)
        ball.dy *= -1

    if(ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *= -1

    if(ball.xcor() > 390):

        scoreA += 1
        score.clear()
        score.write("Player 1 : {}  Player 2 : {}".format(scoreA, scoreB), align="center",
                    font=("Courier", 24, "normal"))
        ball.setx(390)
        ball.dx *= -1

    if(ball.xcor() < -390):

        scoreB += 1
        score.clear()
        score.write("Player 1 : {}  Player 2 : {}".format(scoreA, scoreB), align="center",
                    font=("Courier", 24, "normal"))
        ball.setx(-390)
        ball.dx *= -1

    # collision

    if((ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50)):
        ball.dx *= -1

    if((ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50)):
        ball.dx *= -1
