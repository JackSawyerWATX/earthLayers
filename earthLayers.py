import turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.bgcolor("black")

for r, c in [(150, "green"), (140, "orange"), (50, "red")]:
  t.penup(); t.goto(0, -r); t.pendown()
  t.color(c); t.begin_fill(); t.circle(r); t.end_fill()

t.penup(); t.color("white")

t.goto(0, 220)
t.write("Earth's Layers", align="center", font=("Arial", 18, "bold"))

t.goto(0, 160); t.write("Crust", align="center")
t.goto(0, 90); t.write("Mantle", align="center")
t.goto(0, 10); t.write("Core", align="center")

turtle.done()