import math

from big_ol_pile_of_manim_imports import *
"""Compiled with manim (py2.7 commit may 9th)"""

class Surface_Definition(Scene):
    def construct(self):
        q1 = TextMobject(r"""A subset $S \in \mathbb{R}^3$ is a""", r"\textbf{regular surface} \\",
            r"if for any point in this set, there exist an open set" ,r"$V \subset \mathbb{R}^3$ \\",
            r"\textit{such that}, $p \in V$ and $\exists$ ",
            r"$\bar{X}: U \rightarrow V \cap S$\\",
            r"Where U is an",
            r"\textbf{open set}",
            r"of $\mathbb{R}^2$, and $\bar{X}$ is a ",
            r"\textbf{surjective mapping}")
        q1.set_color_by_tex("regular", BLUE)
        q1.set_color_by_tex(r"$V \subset", MAROON_E)
        q1.set_color_by_tex(r"$\bar{X}:", ORANGE)
        q1.set_color_by_tex(r"\textbf{open set}", PINK)
        q1.set_color_by_tex(r"\textbf{surjective mapping}", GOLD_C)
        # q2 = TextMobject(r"""""")

        bp1 = TexMobject(r"""  i) \text{$\bar{X}$ is $C^{\infty}$}"""); bp1.set_color_by_tex("", YELLOW)
        bp2 = TexMobject(r""" ii) \text{$\bar{X}$ is homeomorphism}"""); bp2.set_color_by_tex("", RED)
        bp3 = TexMobject(r"""iii) \text{$\forall$ q $\in I$, $d_2\bar{X}_q: \mathbb{R}^2 \rightarrow \mathbb{R}^3$ is injective}"""); bp3.set_color_by_tex("", TEAL_D)
        

        # q3 = TextMobject(def_part_2)
        self.play(ShowCreation(q1))
        self.wait(2)
        self.play(ApplyMethod(q1.shift,2.5*UP))
        self.wait(2)
        # q2.shift(1.5*UP)
        # self.play(ShowCreation(q2))
        self.play(ShowCreation(bp1))
        
        self.play(ApplyMethod(bp1.shift, 5*LEFT))
        
        self.play(ShowCreation(bp2))
        self.play(ApplyMethod(bp2.shift, 1*DOWN+3.5*LEFT))
        
        bp3.shift(1.2*RIGHT)
        self.play(ShowCreation(bp3))
        self.play(ApplyMethod(bp3.shift, 2*DOWN+3*LEFT))
        self.wait(2)

        # self.play(FadeIn(q2))
        # self.play(FadeIn(q3))

class Part1(Scene):
    def construct(self):
        q1 = TextMobject(r"""A subset $S \in \mathbb{R}^3$ is a""", r"\textbf{regular surface} \\",
            r"if for any point in this set, there exist an open set" ,r"$V \subset \mathbb{R}^3$ \\",
            r"\textit{such that}, $p \in V$ and $\exists$ ",
            r"$\bar{X}: U \rightarrow V \cap S$\\",
            r"Where U is an",
            r"\textbf{open set}",
            r"of $\mathbb{R}^2$, and $\bar{X}$ is a ",
            r"\textbf{surjective mapping}")
        q1.set_color_by_tex("regular", BLUE)
        q1.set_color_by_tex(r"$V \subset", MAROON_E)
        q1.set_color_by_tex(r"$\bar{X}:", ORANGE)
        q1.set_color_by_tex(r"\textbf{open set}", PINK)
        q1.set_color_by_tex(r"\textbf{surjective mapping}", GOLD_C)
        q1.shift(2.5*UP)
        cover_up_sq = Square(side_length=5, fill_color=BLACK, fill_opacity=1, color=BLACK)
        circle = Circle(fill_color=ORANGE, fill_opacity=1, color=ORANGE)
        circle_exp = TextMobject(r"$U$ is an open set in $\mathbb{R}^2$")

        self.add(q1)
        self.wait(1)
        self.play(Transform(q1, circle_exp))
        self.wait(2)
        self.add(cover_up_sq)
        self.play(ApplyMethod(circle_exp.move_to,2.5*UP))
        #self.play(ApplyMethod(circle_exp.move_to, 2*UP))
        # circle.shift(2*DOWN)
        self.play(ShowCreation(circle))
        self.wait(2)

class VintersectionS(Scene):
    def construct(self):
        # q1 = TextMobject(r"$U$ is an open set in $\mathbb{R}^2$")
        # q1.shift(2.5*UP)
        cover_up_sq = Square(side_length=5, fill_color=BLACK, fill_opacity=1, color=BLACK)
        circle = Circle(fill_color=PURPLE_B, fill_opacity=1, color=PURPLE_B)
        circle_exp = TextMobject(r"$V \cap S$")
        self.play(ShowCreation(circle_exp))
        self.play(ApplyMethod(circle_exp.move_to, 2.5*UP))
        # circle_exp.move_to(2*UP)
        # self.add(q1)
        # self.play(Transform(q1, circle_exp))
        self.wait(2)
        # self.add(cover_up_sq)
        #self.play(ApplyMethod(circle_exp.move_to, 2*UP))
        # circle.shift(2*DOWN)
        self.play(GrowFromCenter(circle))
        self.wait(3)



class Part2(ThreeDScene):
    CONFIG = {"plane_kwargs" : { "color" : RED_B }}
    def construct(self):
        # Create axis
        # Rotate

        r3_exp = TextMobject(r"$V$ is a subset of $\mathbb{R}^3$")
        r3_exp.shift(3*UP)
        self.play(ShowCreation(r3_exp))
        
        self.set_camera_position(0, -np.pi/2)
        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        cube_origin = Sphere(2, 0.2, opacity=.35)
        self.play(ShowCreation(cube_origin))

        self.move_camera(0.8*np.pi/2, -0.45*np.pi)
        self.begin_ambient_camera_rotation()
        self.wait(6)

class xbar_homeomorphism(Scene):
    """Show homeomorphism between R2 and v intersection u"""
    def construct(self):
        u_r2 = Circle(fill_color=ORANGE, fill_opacity=1, color=ORANGE)
        vintu = Circle(fill_color=PURPLE_B, fill_opacity=1, color=PURPLE_B)
        morph_square = Square(fill_color=ORANGE, fill_opacity=1, color=ORANGE)
        morph_ring=Annulus(inner_radius=.5, outer_radius=1, color=RED)

        morph_ring.move_to(3*LEFT)
        # Texts
        x_map_homo = TextMobject(r"$\bar{X}$ is a homeomorphism")
        r2 = TextMobject(r"An open set in $\mathbb{R}^2$")
        viu = TextMobject(r"A open set $V \cap S$")
        xinv = TextMobject(r"$\bar{X}^{-1}$ Exists")
        struct = TextMobject(r"The Geometric Structure is preserved")

        x_map_not_homo = TextMobject(r"$\bar{X}$ is", "not" ,"a homeomorphism")
        x_map_not_homo.set_color_by_tex("not", RED)
        x_map_not_homo.move_to(3.5*UP)
        no_xinv = TextMobject(r"$\bar{X}^{-1}$", "does not", "Exists")
        no_xinv.set_color_by_tex("does not", RED)
        no_xinv.move_to(1.5*UP)
        no_struct = TextMobject(r"The Geometric Structure is","not","preserved")
        no_struct.set_color_by_tex("not", RED)
        no_struct.move_to(2.5*UP)
        # Arrow
        # arrow = Arrow(RIGHT,UP)
        pointer = CurvedArrow(1*LEFT+0.5*DOWN,1*RIGHT+0.5*DOWN,color=BLUE_E)
        pointer2 = CurvedArrow(1*RIGHT+0.5*UP,1*LEFT+0.5*UP,color=BLUE_E)

        self.play(ShowCreation(x_map_homo))
        self.play(ApplyMethod(x_map_homo.move_to, 3.5*UP))
        
        r2.move_to(2*UP)
        self.play(ShowCreation(r2))
        self.play(ShowCreation(u_r2))
        self.wait(1)
        self.play(ApplyMethod(u_r2.move_to, 3*LEFT))
        self.play(ApplyMethod(r2.move_to,3*LEFT+1.5*DOWN))
        viu.move_to(2*UP)
        self.play(ShowCreation(viu))
        self.play(ShowCreation(vintu))
        self.play(ApplyMethod(vintu.move_to, 3*RIGHT))
        self.play(ApplyMethod(viu.move_to,3*RIGHT+1.5*DOWN))
        self.wait(1)
        self.play(ShowCreation(pointer))
        self.wait(2)
        self.play(ShowCreation(pointer2))
        xinv.move_to(1.5*UP)
        self.play(ShowCreation(xinv))
        self.wait(2)
        struct.move_to(2.5*UP)
        self.play(ShowCreation(struct))
        self.wait(2)
        morph_square.move_to(3*LEFT)
        self.play(FadeIn(morph_square))
        self.wait(2)
        u_r2.move_to(50*LEFT)
        # self.play(FadeOut(morph_square))
        self.play(Transform(morph_square, morph_ring))
        self.play(Transform(x_map_homo, x_map_not_homo))
        self.play(Transform(xinv, no_xinv))
        self.play(Transform(struct, no_struct))
        self.wait(2)        

# from numba import vectorize
class Donught(ThreeDScene):
    CONFIG = {"plane_kwargs" : { "color" : RED_B }}
    # @vectorize(['float32(float32, float32)'], target='cuda')
    def construct(self):
        # plane
        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        
        #tex object
        surface = TextMobject(r"S is a surface in $\mathbb{R}^3$")
        surface.move_to(3*UP)

        donught = Torus(5,2,0.08)

        # animaton
        self.play(ShowCreation(surface))
        self.play(ShowCreation(plane))

        self.play(ShowCreation(donught))
        self.move_camera(0.8*np.pi/2, -0.45*np.pi)
        self.begin_ambient_camera_rotation()
        self.wait(10)




# class 3DSphere(Scene):
#     def construct(self):
#         circle = Circle()        
#         circle.shift(3.5*LEFT)
#         self.play(ShowCreation(circle))
#         self.play(ShowCreation(TextMobject(circle_exp)))

#         closed_set = Circle(fill_color=GREEN_B)