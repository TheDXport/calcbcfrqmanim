from manim import *


class Solution(Scene):
    def construct(self):
        title = Text("AP Calculus AB FRQ 2014 #1").shift(UP)
        self.play(Write(title))
        underline = Underline(title, color=WHITE, buff=0.5).shift(UP * 0.35)
        xin = Text("presented and coded by xinathan :D").scale(0.6)
        seeattachedforsourcecode = Text("see attached for the source code!").scale(0.34).shift(DOWN * 0.55)
        self.play(Create(underline), Write(xin, run_time=1.2))
        
        self.wait(0.7)
        
        self.play(Write(seeattachedforsourcecode, run_time=0.9))
        
        self.wait(1.6)
        
        self.play(FadeOut(title, xin, underline, seeattachedforsourcecode))
        
        questionbackgroundp1 = Text("Grass clippings are placed in a bin, where they decompose. For 0 ≤ t ≤ 30, the amount of grass ").scale(0.5).shift(UP * 3)
        questionbackgroundp2 = Text("clippings remaining in the bin is modeled by ").scale(0.5).shift(UP * 2.47 + LEFT * 3.28)
        equation = MathTex('A(t) = 6.687(0.931)^t').scale(0.67).shift(UP * 2.49 + RIGHT *1.26 )
        questionbackgroundp3 = Text(", where A(t) is measured in ").scale(0.5).shift(UP * 2.47 + RIGHT * 4.5)
        questionbackgroundp4 = Text("pounds and t is measured in days.").scale(0.5).shift(UP * 1.94 + LEFT * 4.05)
  
        self.play(Write(questionbackgroundp1))
        self.play(Write(questionbackgroundp2))
        self.play(Write(equation))
        self.play(Write(questionbackgroundp3))
        self.play(Write(questionbackgroundp4)) 
        
        self.wait(1.2)
        
        partaquestion = Text("a) Find the average rate of change of A(t) over the interval 0 ≤ t ≤ 30. Indicate units of measure. ").scale(0.5).shift(UP * 1.25+ RIGHT * 0.1)
        self.play(Write(partaquestion))
        
        self.wait(1.5)
        
        slope_formula = MathTex(r"\frac{y_2 - y_1}{x_2 - x_1}").shift(DOWN * 0.2)
        self.play(Write(slope_formula))
        self.play(slope_formula.animate.shift(LEFT * 1.7), run_time=3.5)
        equal_sign = MathTex('=').shift(LEFT * 0.4 + DOWN * 0.2)
        self.wait(0.8)
        self.play(Write(equal_sign))
        
        subbed_slope_formula = MathTex(r"\frac{A(30) - A(0)}{30 - 0}").shift(RIGHT * 1.3 + DOWN * 0.2).scale(0.9)
        self.play(Write(subbed_slope_formula))

        self.wait(0.9)
        
        # Substitute
        
        target_position = slope_formula.get_center()
        self.play(FadeOut(slope_formula))
        
        
        self.play(subbed_slope_formula.animate.move_to(target_position + LEFT * 0.5))
        