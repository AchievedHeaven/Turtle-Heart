import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
text = input("Enter text:  ")

def draw_heart():
    pen.begin_fill()
    pen.fillcolor("red")
    pen.left(50)
    pen.forward(100)
    pen.circle(40, 180)
    pen.right(100)
    pen.circle(40, 180)
    pen.forward(100)
    pen.end_fill()

draw_heart()

pen.penup()
pen.goto(0, -120)
pen.pendown()

pen.write(f"{text}", align="center", font=("Arial", 30, "normal"))

turtle.done()