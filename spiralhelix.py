import turtle

turtle_picture = turtle.Screen()
turtle_picture.bgcolor("black")
turtle_picture.title("Python Turtle")

instance_turtle = turtle.Turtle()
instance_turtle.color("white")
turtle.speed(0)

turtle_color = ["red","purple","green","orange","yellow"]
for i in range(10):
    instance_turtle.color(turtle_color[i % len(turtle_color)])
    instance_turtle.circle(10 * i)
    instance_turtle.circle(-10 * i)
    instance_turtle.right(10)


turtle.done()