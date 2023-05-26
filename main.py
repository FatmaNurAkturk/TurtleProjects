import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Python Turtle")
turtle_instance = turtle.Turtle()

turtle_instance.forward(100)

#square
drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Square")

drawing_instance1 = turtle.Turtle()
drawing_instance1.forward(100)

drawing_instance1.left(90)
drawing_instance1.forward(100)

drawing_instance1.left(90)
drawing_instance1.forward(100)

drawing_instance1.left(90)
drawing_instance1.forward(100)

for i in range(4):
    drawing_instance1.left(90)
    drawing_instance1.forward(100)

# star
drawing_instance3 = turtle.Turtle()
for i in range(6):
    drawing_instance3.left(50)
    drawing_instance3.forward(100)


turtle.done()

drawing_instance3 = turtle.Turtle()
num_sides = 5
angle = 360.0 / num_sides
side_length = 100

for i in range(num_sides):
    drawing_instance3.right(angle)
    drawing_instance3.forward(side_length)

turtle.done()

#shrinking square
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("turtle python")

turtle_instance = turtle.Turtle()
turtle_instance.color("dark green")

def square(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size -= 5
square(150)
square(130)
square(110)
square(90)
square(50)
square(30)
square(10)

turtle.done()