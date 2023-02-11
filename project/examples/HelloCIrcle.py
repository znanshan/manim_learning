from manim import *

class HelloCircle(Scene):
    def construct(self):

        circle = Circle()
        blue_circle = circle.set_color(BLUE).set_opacity(0.5)

        label = Text("A wild circle appears!")
        label.next_to(blue_circle,DOWN,buff = 0.5)

        self.play(Create(blue_circle),Write(label))
        self.wait()