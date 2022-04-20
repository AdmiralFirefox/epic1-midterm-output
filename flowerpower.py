import turtle
import math

turtle.bgcolor("#121212")
turtle.setup(960, 720)
turtle.title("Flower Power")

admiral = turtle.Turtle()
admiral.speed(0)


class FlowerPower:
    # Petal
    @staticmethod
    def petal(radius):
        step = 4
        petal_arc = 0.25

        sides = 2 * math.pi * radius / step
        turn = 360 / sides

        for _i in range(2):
            for x in range(int(sides * petal_arc)):
                admiral.forward(step)
                admiral.right(turn)

            admiral.right(180 - 360 * petal_arc)

    # Draw Petals
    def draw_petals(self, num_petals, radius, color):
        admiral.color(color)
        admiral.width(2)
        for i in range(num_petals):
            admiral.home()
            admiral.setheading(0)
            admiral.right(360 * i / num_petals)
            self.petal(radius)

    # Layer
    @staticmethod
    def layer(turtle_name, size):
        for i in range(10):
            turtle_name.circle(size)
            size = size - 4

    # Draw Layer Pattern
    def draw_layer_pattern(self, turtle_name, size, repeat, color):
        admiral.color(color)
        admiral.width(1)
        for i in range(repeat):
            self.layer(turtle_name, size)
            turtle_name.right(360 / repeat)


pattern = FlowerPower()

# Draw Petal Patterns
pattern.draw_petals(10, 200, "#ECB410")

# Draw Layer Patterns
pattern.draw_layer_pattern(admiral, 90, 12, "#C15604")
pattern.draw_layer_pattern(admiral, 50, 12, "#9D7D16")

admiral.hideturtle()
turtle.exitonclick()
