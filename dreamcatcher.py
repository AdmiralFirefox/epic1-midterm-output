import turtle
import math

turtle.bgcolor("#121212")
turtle.title("Dream Catcher")

admiral = turtle.Turtle()
admiral.speed(0)

colors = ["#1946e7", "#006de7", "#0797dd", "#00a9c1", "#00c5c0"]


class DreamCatcher:
    @staticmethod
    def set_pos(pos_x, pos_y):
        admiral.penup()
        admiral.setpos(pos_x, pos_y)
        admiral.pendown()

    @staticmethod
    def draw_circle(size, color):
        admiral.color(color)
        admiral.width(3)
        admiral.circle(size)

    @staticmethod
    def draw_centered_circle(size, inner_color, outer_color):
        admiral.begin_fill()
        admiral.color(inner_color, outer_color)
        admiral.width(2)
        admiral.circle(size)
        admiral.end_fill()

    @staticmethod
    def web_pattern(radius):
        step = 4
        petal_arc = 0.25

        sides = 2 * math.pi * radius / step
        turn = 360 / sides

        for _i in range(2):
            for x in range(int(sides * petal_arc)):
                admiral.forward(step)
                admiral.right(turn)

            admiral.right(180 - 360 * petal_arc)

    def draw_web_patterns(self, num_petals, radius):
        admiral.width(2)
        for i in range(num_petals):
            admiral.color(colors[i % 5])
            admiral.home()
            admiral.setheading(0)
            admiral.right(360 * i / num_petals)
            self.web_pattern(radius)


pattern = DreamCatcher()

# Web Patterns
pattern.set_pos(0, 0)
pattern.draw_web_patterns(14, 150)

# Outer Circles
pattern.set_pos(-100, 185)
pattern.draw_circle(-210, "#00a9c1")

pattern.set_pos(-105, 194)
pattern.draw_circle(-220, "#00a9c1")

# Central Circle
pattern.set_pos(-13, 23)
pattern.draw_centered_circle(-25, "#00c5c0", "#121212")

admiral.hideturtle()
turtle.exitonclick()
