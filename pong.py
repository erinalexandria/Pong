import turtle

#create a window
wn = turtle.Screen()
wn.title("Pong by Erin")
wn.bgcolor("black")
wn.setup(width=800, height=600)
#tracer stops the window from updating
wn.tracer(0)

# score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #no line drawn
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() #no line drawn
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation
ball.shape("square")
ball.color("white")
ball.penup() #no line drawn
ball.goto(0, 0)
#separate the ball into x and y movement
ball.dx = 2 #everytime the ball moves, it moves by 2 pixels
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() #no line drawn
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 #adds 20 pixels to y coordinate
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20 #adds 20 pixels to y coordinate
    paddle_a.sety(y)

#function
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20 #adds 20 pixels to y coordinate
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20 #adds 20 pixels to y coordinate
    paddle_b.sety(y)

#Keyboard binding
wn.listen() #listening for keyboard input
wn.onkeypress(paddle_a_up, "w") #when the user presses w, call the function paddle_a_up
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up") 
wn.onkeypress(paddle_b_down, "Down")

#main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    #compare the balls y coordinate
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverses direction
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0) #put ball back to the center
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0) #put ball back to the center
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

# Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1