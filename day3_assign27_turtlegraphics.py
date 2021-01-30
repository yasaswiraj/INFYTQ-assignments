import turtle           # allows us to use the turtles library
wn = turtle.Screen()    # creates a graphics window
wn.setup(500,500)       # set window dimension

alex = turtle.Turtle()  # create a turtle named alex
alex.shape("turtle")    # alex looks like a turtle


alex.color("green")    # alex has a color
alex.right(60)         # alex turns 60 degrees right
alex.left(60)          # alex turns 60 degrees left
alex.circle(50)        # draws a circle of radius 50
#draws circles
for counter in range(1,5):
    alex.circle(20*counter)

alex.color("red")
alex.left(120)
alex.circle(50)
for cntr in range(1,5):
    alex.circle(20*cntr)

alex.color("blue")
alex.right(240)
alex.circle(50)
for c in range(1,5):
    alex.circle(20*c)
