import turtle

turtle.bgcolor("#121212")
turtle.setup(960, 720)
turtle.title("Star Explosion")

admiral = turtle.Turtle()
admiral.speed(0)

colors = ["#ff0000", "#ff4d00", "#ff6700", "#ff8100", "#ffa700"]


class StarExplosion:
    @staticmethod
    def set_pos(pos_x, pos_y):
        admiral.penup()
        admiral.setpos(pos_x, pos_y)
        admiral.pendown()

    @staticmethod
    def layer(turtle_name, size):
        for i in range(1):
            turtle_name.circle(size)
            size = size - 4

    def draw_layer_pattern(self, turtle_name, size, repeat):
        for i in range(repeat):
            admiral.color(colors[i % 4])
            self.layer(turtle_name, size)
            turtle_name.right(360 / repeat)

    @staticmethod
    def explosion(size, color):
        admiral.width(1)
        admiral.color(color)
        for i in range(size):
            admiral.circle(size - i, 90)
            admiral.left(90)
            admiral.circle(size - i, 90)
            admiral.left(18)


pattern = StarExplosion()

# Draw Red Giant Layer Pattern
pattern.draw_layer_pattern(admiral, 110, 75)

# Draw Explosions
pattern.set_pos(0, 0)
pattern.explosion(220, "#ffa700")

admiral.hideturtle()
turtle.exitonclick()
