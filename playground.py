from manim import *

class Solution(Scene):
    def construct(self):
        partcquestion = Text("c) Find the time t for which the amount of grass clippings in the bin is equal to the\n    average amount of grass clippings in the bin over the interval 0 ≤ t ≤ 30.", line_spacing=1.1).shift(UP * 3 + LEFT * 0.2).scale(0.5)
          self.play(Write(partcquestion), run_time=2.5)
          recallText = Text("Recall that we are given:").shift(LEFT * 4 + UP * 1.5).scale(0.5)
          equation = MathTex('A(t) = 6.687(0.931)^t').scale(0.7).move_to(recallText.get_center() + RIGHT * 3.42)
          recallTextp2 = Text("as the total grass clippings").scale(0.5).move_to(equation.get_center() + RIGHT * 3.6)
          self.play(Write(recallText))
          self.play(Write(equation))
          self.play(Write(recallTextp2))
          text = Text("Average amount of grass clippings: ").scale(0.5).shift(LEFT * 3.25 + UP * 0.6)
          
          
          averageAmount = MathTex(r"\frac{1}{b - a} \int_b^a A(t)\,dt").scale(0.7).move_to(text.get_center() + RIGHT * 4)
          self.play(Write(text))
          self.play(Write(averageAmount))
          zero = MathTex("0").shift(LEFT)
          middleOfInterval = MathTex("\leq t \leq")
          thirty = MathTex("30").shift(RIGHT)
          interval = VGroup(zero, middleOfInterval, thirty).scale(0.7).shift(DOWN * 0.4)
          self.play(Write(interval))
          arrowa = Arrow(start=interval.get_center() + DOWN * 1.2 + LEFT * 0.7, end = interval.get_center() + DOWN * 0.1 + LEFT * 0.7)
          arrowb = Arrow(start=interval.get_center() + DOWN * 1.2 + RIGHT * 0.6, end = interval.get_center() + DOWN * 0.1 + RIGHT * 0.6)
          a = Text("a").scale(0.5).shift(arrowa.get_center() + DOWN * 0.5)
          b = Text("b").scale(0.5).shift(arrowb.get_center() + DOWN * 0.5)
          
          self.wait(1)
          
          self.play(Write(arrowa))  
          self.play(Write(arrowb)) 
          self.play(Write(a), Write(b))
          
          self.play(Transform(averageAmount, MathTex(r"\frac{1}{30 - 0}\int_0^{30}A(t)\,dt").scale(0.7).move_to(text.get_center() + RIGHT * 4.18)))
          
          self.wait(2) 
                    
          self.play(Transform(averageAmount, MathTex(r"\frac{1}{30}\int_0^{30}A(t)\,dt").scale(0.7).move_to(text.get_center() + RIGHT * 4)))

          # Script: Now the question is asking: when is the total number of grass clippings equal to average amount? 
          # So, we simply set them equal to each other! 
          
          self.wait(9)
          
          self.play(FadeOut(recallText, recallTextp2, text, arrowa, arrowb, a, b, interval))
          self.play(Transform(equation, MathTex("6.687(0.931)^t").scale(0.7).move_to(equation.get_center())))
          self.play(equation.animate.shift(LEFT * 3), averageAmount.animate.shift(UP * 0.9 + LEFT * 1.6))
          equalSign = MathTex("=").scale(0.7).move_to(equation.get_center() + RIGHT * 1.3)
          self.play(Write(equalSign))
          
          self.wait(3)
          
          self.play(Transform(averageAmount, MathTex(r"\frac{1}{30}\,\int_0^{30}6.687(0.931)^t\,dt").move_to(averageAmount.get_center() + RIGHT * 0.67).scale(0.7)))
          
          self.wait()
          
          # Let's evaluate the right side first!
          self.wait(1)
          
          self.play(averageAmount.animate.shift(LEFT * 4), FadeOut(equalSign, equation))
          self.play(Transform(averageAmount, MathTex(r"\frac{1}{30}\,6.687\int_0^{30}(0.931)^t\,dt").scale(0.7).move_to(averageAmount.get_center())))
          recallText = Text("We know that ").scale(0.5)
          eln = MathTex("e^{ln(k)}").scale(0.7)
          recallTextp2 = Text("cancels out to").scale(0.5)
          k = MathTex("k").scale(0.7)
          combined = VGroup(recallText, eln, recallTextp2, k).arrange(RIGHT)
          self.play(Write(combined))
          
          self.wait(2)
          
          self.play(Transform(combined, Text("Hence, we can rewrite as follows!").scale(0.5)))
          
          self.wait()
          
          self.play(Transform(averageAmount, MathTex(r"\frac{1}{30}\,6.687\int_0^{30}e^{ln(0.931^t)}\,dt").scale(0.7).move_to(averageAmount.get_center() + RIGHT * 0.32)))
          self.play(FadeOut(combined))
          
          self.wait()
          
          self.play(Transform(averageAmount, MathTex(r"\frac{1}{30}\,6.687\int_0^{30}e^{ln(0.931)t}\,dt").scale(0.7).move_to(averageAmount.get_center())))
          
          self.wait(2)
          
          equalSign = MathTex("=").scale(0.7).move_to(averageAmount.get_center() + RIGHT * 2.2)
          integral_expr = MathTex(r"\frac{1}{30}\,(\frac{6.687e^{ln(0.931)t}}{ln(0.931)})").scale(0.7).move_to(equalSign.get_center() + RIGHT * 1.8)
          bounds = MathTex("\\Bigg|", "_0", "^{30}").scale(0.7)
          bounds.next_to(integral_expr, RIGHT)
          self.play(Write(equalSign))
          self.play(Write(integral_expr))
          self.play(Write(bounds))
          definite_integral_eval = MathTex (r"\frac{1}{30}\,((\frac{6.687e^{ln(0.931)30}}{ln(0.931)})-(\frac{6.687e^{ln(0.931)0}}{ln(0.931)}))").scale(0.7).move_to(averageAmount.get_center() + DOWN * 1.5 + RIGHT * 1.3)
          self.play(Write(definite_integral_eval))
          
          self.wait(2)
          
          self.play(Transform(definite_integral_eval, MathTex(r"\frac{1}{30}\,((\frac{6.687e^{(ln(0.931))30}}{ln(0.931)})-(\frac{6.687e^{0}}{ln(0.931)}))").scale(0.7).move_to(definite_integral_eval.get_center())))
          
          self.wait(1.5)
          
          self.play(Transform(definite_integral_eval, MathTex(r"\frac{1}{30}\,((\frac{6.687e^{(ln(0.931))30}}{ln(0.931)})-(\frac{6.687(1)}{ln(0.931)}))").scale(0.7).move_to(definite_integral_eval.get_center())))
          
          self.wait(1.5)
          
          self.play(Transform(definite_integral_eval, MathTex(r"\frac{1}{30}\,((\frac{6.687e^{(ln(0.931))30}}{ln(0.931)})-(\frac{6.687}{ln(0.931)}))").scale(0.7).move_to(definite_integral_eval.get_center())))
        
          self.play(FadeOut(averageAmount, equalSign, integral_expr, bounds))
          self.wait()
          self.play(definite_integral_eval.animate.shift(UP * 1.2 + LEFT * 0.3))
          equalSign.next_to(definite_integral_eval, RIGHT)
          self.play(Write(equalSign))
          recallText = Text("Factor").shift(LEFT + DOWN ).scale(0.5)
          recallTextp2 = MathTex(r"\frac{6.687}{ln(0.931)}").scale(0.7).next_to(recallText, RIGHT)
          self.play(Write(recallText), Write(recallTextp2))
          self.wait(2)
          self.play(FadeOut(recallText, recallTextp2))
          step = MathTex(r"\frac{1}{30}\,\frac{6.687}{ln(0.931)}(e^{(ln(0.931))30})-1").scale(0.7).next_to(equalSign, RIGHT)
          self.play(Write(step))
          self.wait(1.5)
          self.play(Transform(step, MathTex(r"\frac{6.687}{30\,ln(0.931)}(e^{(ln(0.931))30})-1").scale(0.7).next_to(equalSign, RIGHT)))
          self.wait(1)
          self.play(FadeOut(definite_integral_eval, equalSign))
          self.play(step.animate.shift(LEFT * 2))
          self.play(Transform(step, MathTex(r"\frac{6.687}{30\,ln(0.931)}(e^{30\,ln(0.931)})-1").scale(0.7).move_to(step.get_center())))
          equalSign.next_to(step, LEFT)
          
          # We now know that the integral of A(t) is equal to this:
          definiteIntegralExpr = MathTex("\\int_{0}^{30}", "A(", "t", ")", "dt").scale(0.7).next_to(equalSign, LEFT)
        
          self.play(Write(definiteIntegralExpr), Write(equalSign))
          
          self.wait(2)
          
          # Now we need to solve for t 
          self.play(FadeOut(definiteIntegralExpr))
          equation = MathTex("6.687(0.931)^t").next_to(equalSign, LEFT * 0.1).scale(0.7).shift(RIGHT * 0.3)
          self.play(Write(equation))
          arrow = DoubleArrow(start=equation.get_center() + LEFT * 0.4 + UP * 0.05, end=step.get_center() + LEFT * 1.5 + UP * 0.25, color=GOLD_A, tip_length=0.5, max_tip_length_to_length_ratio=0.1)
          self.play(Write(arrow))
        
          self.wait(2)
          self.play(FadeOut(arrow))
          self.play(Transform(equation, MathTex("(0.931)^t").next_to(equalSign, LEFT * 0.7).scale(0.7).shift(RIGHT * 0.3)))
          self.play(Transform(step, MathTex(r"\frac{1}{30\,ln(0.931)}(e^{30\,ln(0.931)})-1").scale(0.7).next_to(equalSign, RIGHT)))
          self.wait(2)
          self.play(Transform(step, MathTex(r"\frac{e^{30\,ln(0.931)}-1}{30\,ln(0.931)}").scale(0.7).next_to(equalSign, RIGHT)))
          self.wait(1)
          self.play(Transform(equation, MathTex("ln(0.931^t)").scale(0.7).next_to(equalSign, LEFT)), Transform(step, MathTex(r"ln(\frac{e^{30ln(0.931)}-1}{30ln(0.931)})").scale(0.7).next_to(equalSign,RIGHT)))
          self.wait(2) 
          # Again, according to the law of natural logs, we can take the t out.
          self.play(Transform(equation, MathTex("ln(0.931)t").next_to(equalSign, LEFT * 0.7).scale(0.7).shift(RIGHT * 0.3)))
          self.wait()                      
          self.play(Transform(equation, MathTex(r"\frac{ln(0.931)t}{ln(0.931)}").next_to(equalSign, LEFT * 0.7)))
          self.wait(2)
          self.play(Transform(step, MathTex(r'\frac{ ln(\frac{e^{30ln(0.931)}-1} {30ln(0.931)} ) } {ln(0.931)}').next_to(equalSign, RIGHT)))
          self.wait(2)
          self.play( Transform(equation, MathTex("t").next_to(equalSign, LEFT )))
          self.wait(2)
          combined = VGroup(equation, equalSign, step)
          self.play(combined.animate.shift(LEFT * 2 + DOWN * 0.5))
          equalSign2 = MathTex("=").next_to(step, RIGHT)
          self.play(Write(equalSign2))
          answer = MathTex("12.4148").next_to(equalSign2, RIGHT)
          self.play(Write(answer))