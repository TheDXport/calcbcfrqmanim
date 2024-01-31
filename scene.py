from manim import *


class Solution(Scene):
    def construct(self):
        # title = Text("AP Calculus BC FRQ 2014 #1").shift(UP)
        # self.play(Write(title))
        # underline = Underline(title, color=WHITE, buff=0.5).shift(UP * 0.35)
        # xin = Text("presented and coded by xinathan :D").scale(0.6)
        # seeattachedforsourcecode = Text("see attached for the source code!").scale(0.34).shift(DOWN * 0.55)
        # self.play(Create(underline), Write(xin, run_time=1.2))
        
        # self.wait(0.7)
        
        # self.play(Write(seeattachedforsourcecode, run_time=0.9))
        
        # self.wait(1.6)
        
        # self.play(FadeOut(title, xin, underline, seeattachedforsourcecode))
        
        # questionbackgroundp1 = Text("Grass clippings are placed in a bin, where they decompose. For 0 ≤ t ≤ 30, the amount of grass ").scale(0.5).shift(UP * 3)
        # questionbackgroundp2 = Text("clippings remaining in the bin is modeled by ").scale(0.5).shift(UP * 2.47 + LEFT * 3.28)
        # equation = MathTex('A(t) = 6.687(0.931)^t').scale(0.67).shift(UP * 2.49 + RIGHT *1.26 )
        # questionbackgroundp3 = Text(", where A(t) is measured in ").scale(0.5).shift(UP * 2.47 + RIGHT * 4.5)
        # questionbackgroundp4 = Text("pounds and t is measured in days.").scale(0.5).shift(UP * 1.94 + LEFT * 4.05)
  
        # self.play(Write(questionbackgroundp1))
        # self.play(Write(questionbackgroundp2))
        # self.play(Write(equation))
        # self.play(Write(questionbackgroundp3))
        # self.play(Write(questionbackgroundp4)) 
        
        # self.wait(1.2)
        
        # partaquestion = Text("a) Find the average rate of change of A(t) over the interval 0 ≤ t ≤ 30. Indicate units of measure. ").scale(0.5).shift(UP * 1.25+ RIGHT * 0.1)
        # self.play(Write(partaquestion))
        
        # self.wait(1.5)
        
        # slope_formula = MathTex(r"\frac{y_2 - y_1}{x_2 - x_1}").shift(DOWN * 0.2)
        # self.play(Write(slope_formula))
        # self.play(slope_formula.animate.shift(LEFT * 1.7), run_time=3.5)
        # equal_sign = MathTex('=').shift(LEFT * 0.4 + DOWN * 0.14)
        # self.wait(0.8)
        # self.play(Write(equal_sign))
        
        # subbed_slope_formula = MathTex(r"\frac{A(30) - A(0)}{30 - 0}").shift(RIGHT * 1.3 + DOWN * 0.12).scale(0.9)
        # self.play(Write(subbed_slope_formula))

        # self.wait(0.9)
        
        # # Substitute
        
        # target_position = slope_formula.get_center()
        # self.play(FadeOut(slope_formula))
        
        
        # self.play(subbed_slope_formula.animate.move_to(target_position + LEFT * 3.3), equal_sign.animate.move_to(target_position + LEFT * 1.6))
        
        # fullySubbed_slope_formula = MathTex(r"\frac{6.687(0.931)^{30} - 6.687(0.931)^0}{30 - 0}").move_to(equal_sign.get_center() + RIGHT * 3.4).scale(0.9)
        # self.play(Write(fullySubbed_slope_formula))
        
        # self.wait(0.8)
        
        # target_position = subbed_slope_formula.get_center()
        # self.play(FadeOut(equal_sign, subbed_slope_formula), fullySubbed_slope_formula.animate.move_to(target_position + RIGHT * 1.7))
        
        # steps = MathTex(r"\frac{6.687(0.931)^{30} - 6.687(1)}{30}").move_to(equal_sign.get_center() + RIGHT * 3.4).scale(0.9).move_to(fullySubbed_slope_formula.get_center() + LEFT * 0.6)
        # self.play(Transform(fullySubbed_slope_formula, steps))
        # steps = MathTex(r"\frac{0.782928 - 6.687}{30}").move_to(equal_sign.get_center() + RIGHT * 3.4).scale(0.9).move_to(fullySubbed_slope_formula.get_center() + LEFT * 0.6)
        # self.play(Transform(fullySubbed_slope_formula, steps))
        # steps = MathTex(r"\frac{-5.9040721306221}{30}").move_to(equal_sign.get_center() + RIGHT * 3.4).scale(0.9).move_to(fullySubbed_slope_formula.get_center())
        # self.play(Transform(fullySubbed_slope_formula, steps))
        # steps = MathTex('-0.196802').move_to(equal_sign.get_center() + RIGHT * 3.4).scale(0.9).move_to(fullySubbed_slope_formula.get_center())
        # self.play(Transform(fullySubbed_slope_formula, steps))
        
        # self.wait(2)
        
        # units = MathTex(r"\frac{pounds}{day}").move_to(fullySubbed_slope_formula.get_center() + RIGHT * 2.03).scale(0.9)
        # self.play(Write(units))
        # answer_combined = VGroup(fullySubbed_slope_formula, units)
        # answer_circle = Ellipse(color=YELLOW).surround(answer_combined)
        # self.play(Create(answer_circle))
        
        # self.wait(1) 
        
        # self.play(FadeOut(questionbackgroundp1, questionbackgroundp2, questionbackgroundp3, questionbackgroundp4, partaquestion, answer_circle, answer_combined, equation))
        
        # self.wait(2)
        # # Visualize the rate of change as compared to the graph
        # partbquestionp1 = Text("b) Find the value of A'(15). Using correct units, interpret the meaning of the value in the context").shift(UP * 3 + LEFT * 0.2).scale(0.5)
        # partbquestionp2 = Text("of the problem.").shift(UP * 2.47 + LEFT * 5.27).scale(0.5)
        
        # self.play(Write(partbquestionp1))
        # self.play(Write(partbquestionp2))

        # axes = Axes(
        #         x_range=[0, 50, 1],
        #         y_range=[0, 9, 1],
        #         axis_config={"color": BLUE},
        #         x_axis_config={
        #         "include_tip": True,  # Show the arrow tip
        #         "numbers_to_include": np.arange(0, 50, 5),  # Numbers to include
        #         "font_size": 30,  # Font size for the numbers
        #     },
        #     y_axis_config={
        #         "include_tip": True,  # Show the arrow tip
        #         "numbers_to_include": np.arange(0, 9, 2),  # Numbers to include
        #         "font_size": 30,  # Font size for the numbers
        #     }, 
        #     tips=True

                 
        #     ).scale(0.7)

        # self.wait(2)
        # graph = axes.plot(lambda t: 6.687 * (0.931)**t, color=GREEN_B)
        
        # graph_label = MathTex('f(t) = 6.687 \cdot (0.931)^t', color=GREEN_B).scale(0.7)

        # # Determine a point on the graph to position the label above
        # label_coord = axes.i2gp(5, graph)  # Get the graph point at x = 5
        # graph_label.next_to(label_coord, RIGHT * 3)
        # self.play(FadeIn (axes))
        # self.play(Create(graph))
        # self.play(Write(graph_label, run_time=0.9))

        # self.wait(2)
        
        

        #  # Calculate the derivative at t = 15
        # t_value = 15
        # slope = 6.687 * np.log(0.931) * (0.931)**t_value
        # f_t = 6.687 * (0.931)**t_value

        # tangent_start = t_value - 1  # Adjust if you want a longer line
        # tangent_end = t_value + 1    # Adjust if you want a longer line


        # start_point = axes.c2p(tangent_start, slope * (tangent_start - t_value) + f_t)
        # end_point = axes.c2p(tangent_end, slope * (tangent_end - t_value) + f_t)

        
        # tangent_line = Line(start_point, end_point, color=RED).scale(10)
        # point_on_graph = axes.c2p(t_value, f_t)
        # dot = Dot(point_on_graph, color=WHITE, radius=0.06)  # Adjust the radius as needed

        # start_point = axes.c2p(t_value, 0)  # Start from the x-axis
        # end_point = point_on_graph          # End at the point of tangency on the graph
        # dotted_line = DashedLine(start_point, end_point, dashed_ratio=0.6, color=WHITE)

        # # Animate the dotted line approaching the point of tangency
        # self.play(Create(dotted_line))
       
        # self.play(FadeIn(dot))
        # self.play(Create(tangent_line))

        # self.wait(2)
        
        # self.play(FadeOut(tangent_line, dot, dotted_line))
        # self.play(FadeOut(axes, graph_label, graph))
        # derivative_function = MathTex('6.687(0.931)^t')
        # deriv = MathTex(r'\frac{d}{dt}').move_to(derivative_function.get_center() + LEFT * 1.8)
        # combined = VGroup(deriv, derivative_function)
        # self.play(Write(combined))
        # step = MathTex(r"6.687(e^{ln(0.931)})^t")
        # self.play(Transform(combined, step))
        # step = MathTex(r"6.687(e^{ln(0.931)t})^1")
        # self.play(Transform(combined, step))
        # step = MathTex(r"6.687(e^{ln(0.931)t}) \cdot ln(0.931)")
        # self.play(Transform(combined, step))

        # self.play(combined.animate.shift(RIGHT * 1.3))
        # function = MathTex(r"A'(t) =").move_to(combined.get_center() + LEFT * 3.9)
        # self.play(Write(function, run_time=0.6))
        # self.play(Transform(function, MathTex(r"A'(15) =").move_to(combined.get_center() + LEFT * 4.06)))
        # step = MathTex(r"6.687(e^{ln(0.931)15}) \cdot ln(0.931)").move_to(function.get_center() + RIGHT * 4.2)
        # self.play(Transform(combined,step))
        # step = MathTex(r"6.687(e^{(-0.0714)15}) \cdot (-0.0714)").move_to(function.get_center() + RIGHT * 4.36)
        # self.play(Transform(combined,step))
        # step = MathTex(r"6.687(0.931^{15}) \cdot (-0.0714)").move_to(function.get_center() + RIGHT * 4.6)
        # self.play(Transform(combined,step), function.animate.shift(RIGHT * 0.7))
        # step = MathTex(r"2.2881 \cdot (-0.0714)").move_to(function.get_center() + RIGHT * 3.5)
        # self.play(Transform(combined,step), function.animate.shift(RIGHT * 0.5))
        # step = MathTex(r"-0.1635").move_to(function.get_center() + RIGHT * 2.6)
        # self.play(Transform(combined,step), function.animate.shift(RIGHT * 0.56))
        # combined = VGroup(function, combined)
        # self.play(combined.animate.shift(LEFT * 1.2))
        # units = MathTex(r"\frac{pounds}{day}").move_to(combined.get_center() + RIGHT * 3)
        # self.play(Write(units))
        # combined = VGroup(combined, units)
        # self.play(combined.animate.scale(0.8))
        # self.play(combined.animate.shift(LEFT * 3.7 + UP))
        # explanation = Text("This means that the total amount of grass clippings in the bin is decreasing at exactly\n-0.1635 pounds per day specifically on day 15 (t = 15).", line_spacing=1.1).scale(0.5).shift(LEFT * 0.11 + DOWN * 0.37)
        # self.play(Write(explanation))
        # combined = VGroup(combined, explanation)
        # answer_circle = Rectangle(color=YELLOW).surround(combined)
        # answer_circle.stretch_to_fit_height(answer_circle.height * 0.5)
        # answer_circle.stretch_to_fit_width(answer_circle.width * 1.02)
        # self.play(ShowCreationThenFadeOut(answer_circle))
        # self.wait(2)
        # self.play(FadeOut(combined, partbquestionp1, partbquestionp2))
        # partcquestion = Text("c) Find the time t for which the amount of grass clippings in the bin is equal to the\n    average amount of grass clippings in the bin over the interval 0 ≤ t ≤ 30.", line_spacing=1.1).shift(UP * 3 + LEFT * 0.2).scale(0.5)
        # self.play(Write(partcquestion), run_time=2.5)
        # recallText = Text("Recall that we are given:").shift(LEFT * 4 + UP * 1.5).scale(0.5)
        # equation = MathTex('A(t) = 6.687(0.931)^t').scale(0.82).next_to(recallText, RIGHT)
        # recallTextp2 = Text("as the total grass clippings").scale(0.5).next_to(equation, RIGHT)
        # self.play(Write(recallText))
        # self.play(Write(equation))
        # self.play(Write(recallTextp2))
        # text = Text("Average amount of grass clippings: ").scale(0.5).shift(LEFT * 3.25 + UP * 0.6)
        
        
        # averageAmount = MathTex(r"\frac{1}{b - a} \int_b^a A(t)\,dt").scale(0.82).next_to(text)
        # self.play(Write(text))
        # self.play(Write(averageAmount))
        # zero = MathTex("0").shift(LEFT)
        # middleOfInterval = MathTex("\leq t \leq")
        # thirty = MathTex("30").shift(RIGHT)
        # interval = VGroup(zero, middleOfInterval, thirty).scale(0.82).shift(DOWN * 0.4)
        # self.play(Write(interval))
        # arrowa = Arrow(start=interval.get_center() + DOWN * 1.2 + LEFT * 0.7, end = interval.get_center() + DOWN * 0.1 + LEFT * 0.7)
        # arrowb = Arrow(start=interval.get_center() + DOWN * 1.2 + RIGHT * 0.6, end = interval.get_center() + DOWN * 0.1 + RIGHT * 0.6)
        # a = Text("a").scale(0.5).shift(arrowa.get_center() + DOWN * 0.5)
        # b = Text("b").scale(0.5).shift(arrowb.get_center() + DOWN * 0.5)
        
        # self.wait(1)
        
        # self.play(Write(arrowa))  
        # self.play(Write(arrowb)) 
        # self.play(Write(a), Write(b))
        
        # self.play(Transform(averageAmount, MathTex(r"\frac{1}{30 - 0}\int_0^{30}A(t)\,dt").scale(0.82).next_to(text, RIGHT)))
        
        # self.wait(2) 
                  
        # self.play(Transform(averageAmount, MathTex(r"\frac{1}{30}\int_0^{30}A(t)\,dt").scale(0.82).next_to(text, RIGHT)))

        # # Script: Now the question is asking: when is the total number of grass clippings equal to average amount? 
        # # So, we simply set them equal to each other! 
        
        # self.wait(9)
        
        # self.play(FadeOut(recallText, recallTextp2, text, arrowa, arrowb, a, b, interval))
        # self.play(Transform(equation, MathTex("6.687(0.931)^t").scale(0.82).move_to(equation.get_center())))
        # self.play(equation.animate.shift(LEFT * 3))
        # equalSign = MathTex("=").scale(0.82).next_to(equation, RIGHT)
        # self.play(Write(equalSign))
        
        # self.play(averageAmount.animate.shift(equalSign.get_center() + RIGHT * 0.85 + DOWN * 0.6 ))
        
        
        # self.wait(3)
        
        # self.play(Transform(averageAmount, MathTex(r"\frac{1}{30}\,\int_0^{30}6.687(0.931)^t\,dt").move_to(equalSign.get_center() + RIGHT * 2.5).scale(0.82)))
        
        # self.wait()
        
        # # Let's evaluate the right side first!
        # self.wait(1)
        
        # self.play(averageAmount.animate.shift(LEFT * 4), FadeOut(equalSign, equation))
        # self.play(Transform(averageAmount, MathTex(r"\frac{1}{30}\,6.687\int_0^{30}(0.931)^t\,dt").scale(0.82).move_to(averageAmount.get_center())))
        # recallText = Text("We know that ").scale(0.5)
        # eln = MathTex("e^{ln(k)}").scale(0.82)
        # recallTextp2 = Text("cancels out to").scale(0.5)
        # k = MathTex("k").scale(0.82)
        # combined = VGroup(recallText, eln, recallTextp2, k).arrange(RIGHT)
        # self.play(Write(combined))
        
        # self.wait(2)
        
        # self.play(Transform(combined, Text("Hence, we can rewrite as follows!").scale(0.5)))
        
        # self.wait()
        
        # self.play(Transform(averageAmount, MathTex(r"\frac{1}{30}\,6.687\int_0^{30}e^{ln(0.931^t)}\,dt").scale(0.82).move_to(averageAmount.get_center())))
        # self.play(FadeOut(combined))
        
        # self.wait()
        
        # self.play(Transform(averageAmount, MathTex(r"\frac{1}{30}\,6.687\int_0^{30}e^{ln(0.931)t}\,dt").scale(0.82).move_to(averageAmount.get_center())))
        
        # self.wait(2)
        
        # equalSign = MathTex("=").next_to(averageAmount, RIGHT)
        # integral_expr = MathTex(r"\frac{1}{30}\,(\frac{6.687e^{ln(0.931)t}}{ln(0.931)})").scale(0.82).next_to(equalSign, RIGHT)
        # bounds = MathTex("\\Bigg|", "_0", "^{30}").scale(0.82)
        # bounds.next_to(integral_expr, RIGHT)
        # self.play(Write(equalSign))
        # self.play(Write(integral_expr))
        # self.play(Write(bounds))
        
        # self.wait(2)
        # # Now let's evaluate this!
        # definite_integral_eval = MathTex (r"\frac{1}{30}\,((\frac{6.687e^{ln(0.931)30}}{ln(0.931)})-(\frac{6.687e^{ln(0.931)0}}{ln(0.931)}))").scale(0.82).move_to(averageAmount.get_center() + DOWN * 2.3 + RIGHT * 1.3)
        # self.play(Write(definite_integral_eval))
        
        # self.wait(2)
        
        # self.play(Transform(definite_integral_eval, MathTex(r"\frac{1}{30}\,((\frac{6.687e^{ln(0.931)30}}{ln(0.931)})-(\frac{6.687e^{0}}{ln(0.931)}))").scale(0.82).move_to(definite_integral_eval.get_center())))
        
        # self.wait(1.5)
        
        # self.play(Transform(definite_integral_eval, MathTex(r"\frac{1}{30}\,((\frac{6.687e^{ln(0.931)30}}{ln(0.931)})-(\frac{6.687(1)}{ln(0.931)}))").scale(0.82).move_to(definite_integral_eval.get_center())))
        
        # self.wait(1.5)
        
        # self.play(Transform(definite_integral_eval, MathTex(r"\frac{1}{30}\,((\frac{6.687e^{ln(0.931)30}}{ln(0.931)})-(\frac{6.687}{ln(0.931)}))").scale(0.82).move_to(definite_integral_eval.get_center())))
      
        # self.play(FadeOut(averageAmount, equalSign, integral_expr, bounds))
        # self.wait()
        # self.play(definite_integral_eval.animate.shift(UP * 1.2 + LEFT * 0.3))
        # equalSign.next_to(definite_integral_eval, RIGHT)
        # self.play(Write(equalSign))
        # recallText = Text("Factor").shift(LEFT + DOWN ).scale(0.5)
        # recallTextp2 = MathTex(r"\frac{6.687}{ln(0.931)}").scale(0.82).next_to(recallText, RIGHT)
        # self.play(Write(recallText), Write(recallTextp2))
        # self.wait(2)
        # self.play(FadeOut(recallText, recallTextp2))
        # combined = VGroup(equalSign, definite_integral_eval)
        # self.play(combined.animate.shift(LEFT * 0.7))
        # step = MathTex(r"\frac{1}{30}\,\frac{6.687}{ln(0.931)}(e^{ln(0.931)30})-1").scale(0.82).next_to(equalSign, RIGHT)
        # self.play(Write(step))
        # self.wait(1.5)
        # self.play(Transform(step, MathTex(r"\frac{6.687}{30\,ln(0.931)}(e^{ln(0.931)30})-1").scale(0.82).next_to(equalSign, RIGHT)))
        # self.wait(1)
        # self.play(FadeOut(definite_integral_eval, equalSign))
        # self.play(step.animate.shift(LEFT * 2))
        # self.play(Transform(step, MathTex(r"\frac{6.687}{30\,ln(0.931)}(e^{30\,ln(0.931)})-1").scale(0.82).move_to(step.get_center())))
        # equalSign.next_to(step, LEFT)
        
        # # We now know that the integral of A(t) is equal to this:
        # definiteIntegralExpr = MathTex("\\int_{0}^{30}", "A(", "t", ")", "dt").scale(0.82).next_to(equalSign, LEFT)
      
        # self.play(Write(definiteIntegralExpr), Write(equalSign))
        
        # self.wait(2)
        
        # # Now we need to solve for t 
        # combined = VGroup(definiteIntegralExpr, equalSign, step)
        # self.play(combined.animate.shift(LEFT * 0.5))
        # self.play(FadeOut(definiteIntegralExpr))
        # equation = MathTex("6.687(0.931)^t").next_to(equalSign, LEFT * 0.1).scale(0.82)
        # self.play(Write(equation))
        # arrow = DoubleArrow(start=equation.get_center() + LEFT * 0.4 + UP * 0.05, end=step.get_center() + LEFT * 1.7 + UP * 0.25, color=GOLD_A, tip_length=0.5, max_tip_length_to_length_ratio=0.1)
        
        # self.wait(2)
        
        # self.play(Write(arrow))
      
        # self.wait(2)
        # self.play(FadeOut(arrow))
        # self.play(Transform(equation, MathTex("(0.931)^t").next_to(equalSign, LEFT * 0.7)))
        # self.play(Transform(step, MathTex(r"\frac{1}{30\,ln(0.931)}(e^{30\,ln(0.931)})-1").next_to(equalSign, RIGHT)))
        # self.wait(2)
        # self.play(Transform(step, MathTex(r"\frac{e^{30\,ln(0.931)}-1}{30\,ln(0.931)}").next_to(equalSign, RIGHT)))
        # self.wait(1)
        # self.play(Transform(equation, MathTex("ln(0.931^t)").next_to(equalSign, LEFT)), Transform(step, MathTex(r"ln(\frac{e^{30ln(0.931)}-1}{30ln(0.931)})").next_to(equalSign,RIGHT)))
        # self.wait(2) 
        # # Again, according to the law of natural logs, we can take the t out.
        # self.play(Transform(equation, MathTex("ln(0.931)t").next_to(equalSign, LEFT * 0.7)))
        # self.wait()                      
        # self.play(Transform(equation, MathTex(r"\frac{ln(0.931)t}{ln(0.931)}").next_to(equalSign, LEFT * 0.7)))
        # self.wait(2)
        # self.play(Transform(step, MathTex(r'\frac{ ln(\frac{e^{30ln(0.931)}-1} {30ln(0.931)} ) } {ln(0.931)}').next_to(equalSign, RIGHT)))
        # self.wait(2)
        # self.play( Transform(equation, MathTex("t").next_to(equalSign, LEFT )))
        # self.wait(2)
        # combined = VGroup(equation, equalSign, step)
        # self.play(combined.animate.shift(LEFT * 2 + DOWN * 0.5))
        # equalSign2 = MathTex("=").next_to(step, RIGHT)
        # self.play(Write(equalSign2))
        # answer = MathTex("12.4148").scale(0.9).next_to(equalSign2, RIGHT)
        # units = Text("days").scale(0.6).next_to(answer, RIGHT * 0.7)
        # self.play(Write(answer))
        # self.play(Write(units))
        # answer_circle = Ellipse(color=YELLOW).surround(VGroup(answer, units))
        # self.play(ShowCreationThenFadeOut(answer_circle))
        
        # self.wait(3)
        
        # self.play(FadeOut(partcquestion, equalSign2, combined, answer_circle, answer, units))
        
        
        partdquestion = Text("d) For t > 30, L(t), the linear approximation to A at t = 30, is a better model for the amount of grass clippings\n      remaining in the bin. Use L(t) to predict the time at which there will be 0.5 pound of grass clippings in the\n      bin. Show the work that leads to your answer.", line_spacing=1.1).shift(UP * 3 + LEFT * 0.07).scale(0.43)
        self.play(Write(partdquestion), run_time=7)
        
        text = Text("Point-slope Form:").shift(UP)
        pointslope  = MathTex("y - y_1 = m(x - x_1)")

        
        self.play(Write(text))
        self.wait(1.8)
        self.play(Write(pointslope))
        self.wait()
        self.play(Transform(pointslope, MathTex("y - A(30) = m(x - x_1)")))
        self.play(Transform(pointslope, MathTex("y - A(30) = m(x - 30)")))
        self.play(Transform(pointslope, MathTex("y - A(30) = A'(30)(x - 30)")))
        self.play(FadeOut(text))
        recallText = Text("Recall that when we plug in 30 into our original equation:").shift(UP).scale(0.66)
        equation = MathTex("A(t) = 6.687(0.931)^t")
        self.play(pointslope.animate.shift(DOWN * 1.5))
        self.play(FadeIn(recallText))
        self.wait(1)
        self.play(FadeIn(equation))
        self.wait(2)
        self.play(Transform(equation, MathTex("A(30) = 6.687(0.931)^{30}")))
        self.wait(0.5)
        self.play(Transform(equation, MathTex("A(30) = 0.782928")))
        self.wait(1)
        
        step = MathTex("y - 0.78293 = A'(30)(x - 30)").shift(pointslope.get_center())
        self.play(
            AnimationGroup(
                FadeOut(equation, recallText),
                TransformMatchingTex(pointslope, step, run_time=0.8),
                lag_ratio=0
            )
        ) 
        self.wait(2)
        text = Text("Now we have to find A'(30)").scale(0.69).shift(UP * 1.3)
        self.play(Write(text))
        equation = MathTex(r"\frac{d}{dx}\,A(t) = 6.687(0.931)^t")
        self.play(FadeIn(equation))
        self.play(Transform(equation, MathTex("A'(t) = -0.478094(0.931)^t")))
        self.wait()
        self.play(Transform(equation, MathTex("A'(30) = -0.478094(0.931)^{30}")))
        self.wait()
        self.play(Transform(equation, MathTex("A'(30) = -0.056")))
        self.wait()
        self.play(FadeOut(equation, text), Transform(step, MathTex("y", "- 0.78293" , " = -0.056(x-30)^t").shift(pointslope.get_center())))
        self.play(step.animate.shift(UP * 1.5))
        pointslope = step
        self.wait()
        self.play(pointslope[1:2].animate.shift(DOWN))
        self.play(pointslope[2:].animate.shift(LEFT * 2.15), Transform(pointslope[1:2], MathTex(r"+\,0.78293").shift(pointslope[1:2].get_center())))
        self.play(pointslope[1:2].animate.next_to(pointslope[2:], RIGHT))
        self.play(Transform(pointslope[0:1], MathTex("L(t)").next_to(pointslope[1:], LEFT)))
        # Now the question is asking us when  L(t) = 0.05 pounds of grass clippings
        # To do this, we  need to solve for t given L(t) = 0.05
        self.wait(3) 
        self.play(Transform(pointslope[0:1], MathTex("0.5").next_to(pointslope[1:], LEFT)))
        oppovalue = MathTex("-0.78293").next_to(pointslope[1:2], DOWN)
        oppovalue2 = MathTex("-0.78293").next_to(pointslope[0:1], DOWN)
        self.play(FadeIn(oppovalue, oppovalue2))
        

        
        
        
        
        
        
          
          


  
          

          
            
            
            
            
            
            
          