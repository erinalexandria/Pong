import turtle

#create a window
wn = turtle.Screen()
wn.title("Pong by Erin")
wn.bgcolor("black")
wn.setup(width=800, height=600)
#tracer stops the window from updating
wn.tracer(0)

#main game loop
while True:
    wn.update()