%%manim -qm -v WARNING RandomWalk

from manim import *
import numpy as np

class RandomWalk(Scene):
    def construct(self):
        # Number of steps for the random walks
        n_steps = 100
        
        # Generate Gaussian random steps (from a normal distribution)
        gaussian_steps_1 = np.random.randn(n_steps)
        gaussian_walk_1 = np.cumsum(gaussian_steps_1)
        gaussian_steps_2 = np.random.randn(n_steps)
        gaussian_walk_2 = np.cumsum(gaussian_steps_2)
        gaussian_steps_3 = np.random.randn(n_steps)
        gaussian_walk_3 = np.cumsum(gaussian_steps_3)
        gaussian_steps_4 = np.random.randn(n_steps)
        gaussian_walk_4 = np.cumsum(gaussian_steps_4)
        gaussian_steps_5 = np.random.randn(n_steps)
        gaussian_walk_5 = np.cumsum(gaussian_steps_5)
        
        # Generate Cauchy random steps (from a Cauchy distribution)
        cauchy_steps_1 = np.random.standard_cauchy(n_steps)
        cauchy_walk_1 = np.cumsum(cauchy_steps_1)
        cauchy_steps_2 = np.random.standard_cauchy(n_steps)
        cauchy_walk_2 = np.cumsum(cauchy_steps_2)
        cauchy_steps_3 = np.random.standard_cauchy(n_steps)
        cauchy_walk_3 = np.cumsum(cauchy_steps_3)
        cauchy_steps_4 = np.random.standard_cauchy(n_steps)
        cauchy_walk_4 = np.cumsum(cauchy_steps_4)
        cauchy_steps_5 = np.random.standard_cauchy(n_steps)
        cauchy_walk_5 = np.cumsum(cauchy_steps_5)
        
        # Create axes for the plot (smaller)
        axes = Axes(
            x_range=[0, n_steps, 10],    # X-axis represents steps
            y_range=[-200, 200, 10],       # Y-axis represents position
            axis_config={"color": WHITE}, # Axis color
            x_length=8,                 # X-axis length (smaller)
            y_length=6,                   # Y-axis length (smaller)
            tips = False
        ).to_edge(LEFT)
        
        # Add axis labels
        x_label = axes.get_x_axis_label("t")
        y_label = axes.get_y_axis_label("X(t)")
        
        # Create and position the title at the top
        title = Title("Gaussian Random Walks vs Cauchy Random Walks", font_size = 40, include_underline = False, 
                     match_underline_width_to_text=True)

        # # Create legend inside a box
        # legend_box = Rectangle(width=3, height=2, color=WHITE).to_edge(RIGHT)
        # gaussian_legend_line = Line(legend_box.get_corner(UL), legend_box.get_corner(UL) + RIGHT*0.5, color=YELLOW)
        # gaussian_legend_text = Text("Gaussian", font_size=15, color=WHITE).next_to(gaussian_legend_line, RIGHT)
        # cauchy_legend_line = Line(legend_box.get_corner(UL) + DOWN*0.5, legend_box.get_corner(UL) + RIGHT*0.5 + DOWN*0.5, color=RED)
        # cauchy_legend_text = Text("Cauchy", font_size=15, color=WHITE).next_to(cauchy_legend_line, RIGHT)

        legend_box = Rectangle(width=3, height=2, color=WHITE).to_edge(RIGHT)
        # Calculate positions for the lines and text, centered inside the box
        gaussian_legend_line = Line(ORIGIN, RIGHT * 0.5, color=YELLOW).move_to(legend_box.get_top() - DOWN * 0.5)
        gaussian_legend_text = Text("Gaussian", font_size=30, color=WHITE).next_to(gaussian_legend_line, RIGHT, buff=0.2)
        gaussian_legend_group = VGroup(gaussian_legend_line, gaussian_legend_text).move_to(legend_box.get_center() + UP * 0.5)
        
        cauchy_legend_line = Line(ORIGIN, RIGHT * 0.5, color=RED).move_to(legend_box.get_center() + DOWN * 0.5)
        cauchy_legend_text = Text("Cauchy", font_size=30, color=WHITE).next_to(cauchy_legend_line, RIGHT, buff=0.2)
        cauchy_legend_group = VGroup(cauchy_legend_line, cauchy_legend_text).move_to(legend_box.get_center() + DOWN * 0.5)


        # Plot initial point (Step 0)
        self.play(Create(axes), Write(title), Write(x_label), Write(y_label), 
                  Create(legend_box), Create(gaussian_legend_group), Create(cauchy_legend_group))
        
        # Initial points for both random walks
        previous_gaussian_point_1 = axes.c2p(0, 0)  # Gaussian starts at (0, 0)
        previous_cauchy_point_1 = axes.c2p(0, 0)    # Cauchy starts at (0, 0)
        previous_gaussian_point_2 = axes.c2p(0, 0)  # Gaussian starts at (0, 0)
        previous_cauchy_point_2 = axes.c2p(0, 0)    # Cauchy starts at (0, 0)
        previous_gaussian_point_3 = axes.c2p(0, 0)  # Gaussian starts at (0, 0)
        previous_cauchy_point_3 = axes.c2p(0, 0)    # Cauchy starts at (0, 0)
        previous_gaussian_point_4 = axes.c2p(0, 0)  # Gaussian starts at (0, 0)
        previous_cauchy_point_4 = axes.c2p(0, 0)    # Cauchy starts at (0, 0)
        previous_gaussian_point_5 = axes.c2p(0, 0)  # Gaussian starts at (0, 0)
        previous_cauchy_point_5 = axes.c2p(0, 0)    # Cauchy starts at (0, 0)
        
        # Animate the random walks step by step without dots
        for step in range(1, n_steps):
            # Get the next positions in the random walks
            new_gaussian_point_1 = axes.c2p(step, gaussian_walk_1[step])
            new_cauchy_point_1 = axes.c2p(step, cauchy_walk_1[step])
            new_gaussian_point_2 = axes.c2p(step, gaussian_walk_2[step])
            new_cauchy_point_2 = axes.c2p(step, cauchy_walk_2[step])
            new_gaussian_point_3 = axes.c2p(step, gaussian_walk_3[step])
            new_cauchy_point_3 = axes.c2p(step, cauchy_walk_3[step])
            new_gaussian_point_4 = axes.c2p(step, gaussian_walk_4[step])
            new_cauchy_point_4 = axes.c2p(step, cauchy_walk_4[step])
            new_gaussian_point_5 = axes.c2p(step, gaussian_walk_5[step])
            new_cauchy_point_5 = axes.c2p(step, cauchy_walk_5[step])
            
            # Create lines connecting the previous points to the new points
            gaussian_line_1 = Line(previous_gaussian_point_1, new_gaussian_point_1, color=YELLOW)
            cauchy_line_1 = Line(previous_cauchy_point_1, new_cauchy_point_1, color=RED)
            gaussian_line_2 = Line(previous_gaussian_point_2, new_gaussian_point_2, color=YELLOW)
            cauchy_line_2 = Line(previous_cauchy_point_2, new_cauchy_point_2, color=RED)
            gaussian_line_3 = Line(previous_gaussian_point_3, new_gaussian_point_3, color=YELLOW)
            cauchy_line_3 = Line(previous_cauchy_point_3, new_cauchy_point_3, color=RED)
            gaussian_line_4 = Line(previous_gaussian_point_4, new_gaussian_point_4, color=YELLOW)
            cauchy_line_4 = Line(previous_cauchy_point_4, new_cauchy_point_4, color=RED)
            gaussian_line_5 = Line(previous_gaussian_point_5, new_gaussian_point_5, color=YELLOW)
            cauchy_line_5 = Line(previous_cauchy_point_5, new_cauchy_point_5, color=RED)
            
            # Animate the lines for both walks
            self.play(
                Create(gaussian_line_1),
                Create(cauchy_line_1),
                Create(gaussian_line_2),
                Create(cauchy_line_2),
                Create(gaussian_line_3),
                Create(cauchy_line_3),
                Create(gaussian_line_4),
                Create(cauchy_line_4),
                Create(gaussian_line_5),
                Create(cauchy_line_5),
                run_time=0.05
            )
            
            # Update the previous points
            previous_gaussian_point_1 = new_gaussian_point_1
            previous_cauchy_point_1 = new_cauchy_point_1
            previous_gaussian_point_2 = new_gaussian_point_2
            previous_cauchy_point_2 = new_cauchy_point_2
            previous_gaussian_point_3 = new_gaussian_point_3
            previous_cauchy_point_3 = new_cauchy_point_3
            previous_gaussian_point_4 = new_gaussian_point_4
            previous_cauchy_point_4 = new_cauchy_point_4
            previous_gaussian_point_5 = new_gaussian_point_5
            previous_cauchy_point_5 = new_cauchy_point_5
        
        # Pause at the end of the animation
        self.wait(2)
