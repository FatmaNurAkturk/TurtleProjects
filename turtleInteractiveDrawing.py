import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

instance_turtle = turtle.Turtle()

def turtle_forward():
    instance_turtle.forward(100)
def rotate_angle_right():
    instance_turtle.setheading(instance_turtle.heading()+10)
    """instance_turtle.right(10)"""
def rotate_angle_left():
    instance_turtle.setheading(instance_turtle.heading()-10)
    """instance_turtle.left(10)"""
def clear_screen():
    instance_turtle.clear()
def turtle_return_home():
    instance_turtle.penup()
    instance_turtle.home()
    instance_turtle.pendown()
def turtle_pen_up():
    instance_turtle.penup()
def turtle_pen_down():
    instance_turtle.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="space")
drawing_board.onkey(fun=rotate_angle_right,key="Down")
drawing_board.onkey(fun=rotate_angle_left,key="Up")
drawing_board.onkey(fun=clear_screen,key="c")
drawing_board.onkey(fun=turtle_return_home,key="h")
drawing_board.onkey(fun=turtle_pen_up,key="w")
drawing_board.onkey(fun=turtle_pen_down,key="q")


turtle.mainloop()
