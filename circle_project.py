import turtle

my_turtle = turtle.Turtle()
my_turtle.color = ('green')

def square(length, angle):
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)

square(100,90)



for i in range(100):
    my_turtle.right(100)
    square(100,90)
