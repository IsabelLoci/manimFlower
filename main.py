from manim import *
import numpy as np

class demo(Scene):
    def construct(self):
    
        text = Text("Hello CTP BAI class!",
                    font_size = 30)
        text.to_edge(UP)

        a = 3  # size of petals
        k = 9  # number of petals

        colorOne = RED  # color of first flower petals
        colorTwo = BLUE # color of second overlapping petals

        # middle of the flower
        circle = Circle(radius = 0.5,
                        color = YELLOW,
                        fill_color = YELLOW,
                        fill_opacity = 1)

        stem = Line(start=circle.get_bottom(),
                    color = GREEN,
                    end=DOWN * 5,
                    stroke_width = 5)

        # a* cos(k * theta) rose curve
        def rose_curve(theta):
            r = a * np.cos(k * theta) # calculate radius
            # convert from polar to cartesian coords
            x = r * np.cos(theta) # x=r*cos(theta)
            y = r * np.sin(theta) # y=r*sin(theta)
            return np.array([x, y, 0])
        
        # a* sin(k * theta) rose curve
        def rose_curve_v2(theta):
            r = a * np.sin(k * theta) # calculate radius
            # convert from polar to cartesian coords
            x = r * np.cos(theta) # x=r*cos(theta)
            y = r * np.sin(theta) # y=r*sin(theta)
            return np.array([x, y, 0])

        # animate the curve using ParametricFunction
        flower = ParametricFunction(
            rose_curve,
            t_range=np.array([0, TAU]),
            color=colorOne,
            stroke_width=5
        )

        flowerTwo = ParametricFunction(
            rose_curve_v2,
            t_range=np.array([0, TAU]),
            color=colorTwo,
            stroke_width=5
        )

        # flowers are animated at the same time through self.play taking multiple parameters
        self.play(Write(text, run_time = 3),
                  Create(flower, run_time=4), 
                  Create(flowerTwo, run_time=4), 
                  Create(circle, run_time = 2),
                  Create(stem))
        
        self.play(Rotate(flower, run_time=3), Rotate(flowerTwo, run_time=1.5))

        self.wait()

        # stem cells, keratinocytes, melanocytes, tacticle cells, dendritic cels
