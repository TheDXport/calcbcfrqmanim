from manim import *

class Solution(Scene):
    def construct(self):
        integral = MathTex("\int_a^b A(t)\,dt").shift(UP)
        a = MathTex("0").shift(LEFT)
        b = MathTex("30").shift(RIGHT)
        
        self.play(Transform(integral, MathTex("\int_0^{30} A(t)\, dt")))