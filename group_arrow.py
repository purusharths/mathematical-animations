from big_ol_pile_of_manim_imports import *


class ComplexRotationTriangle(Scene):
    """docstring for ComplexRotationTriangle"""
    # DEFAULT_PLANE_CONFIG = { "stroke_width" : 2}

    def create_triangle(self, pos, label_pos, color_index=0):
        color = [RED, GREEN, BLUE, ORANGE]
        triangle=Polygon(np.array(pos[0]),np.array(pos[1]),np.array(pos[2]), color=color[color_index])
        # self.add(triangle)
        triangle_label = TextMobject("A"); triangle_label.move_to(label_pos)
        return triangle, triangle_label

    def construct(self):
        
        plane_config =  { "stroke_width" : 2}
        
        
        # radius = norm**(1./n)
        # zoom_value = (FRAME_Y_RADIUS-0.5)/radius
        # plane_config["unit_to_spatial_width"] = zoom_value
        # plane = ComplexPlane(**plane_config) 
        # self.play(ShowCreation(plane))
        caption = TextMobject("Rotational Group of Isosceles Triange")
        rotation_labels = ["Rotation by 0", r"Rotation by $\frac{\pi}{2}$", r"Rotation by $\pi$", r"Rotation by $3\frac{\pi}{2}$"]
        # multiplication by 1
        triangle = []
        for i in range(0,4):
            t, tl = self.create_triangle([[0,-1,0], [1,0,0], [0,1,0]], 1.5*RIGHT, i)
            triangle.append([t,tl]) # triangle, triangle_label
        # triangle[0][0], triangle[0][1] = self.create_triangle([[-1,0,0], [1,0,0], [0,1,0]], 1.5*UP)
        self.play(ShowCreation(triangle[0][0])); self.add(triangle[0][1])
        self.play(ApplyMethod(triangle[0][0].move_to, 5*LEFT+0.5*UP))
        self.play(ApplyMethod(triangle[0][1].move_to, 4*LEFT+0.5*UP))
        rotate1 = TextMobject(rotation_labels[0]); rotate1.scale(0.65); rotate1.move_to(5*LEFT+1*DOWN); self.play(ShowCreation(rotate1))
        # multiplication by i
        self.play(ShowCreation(triangle[1][0])); 
        self.play(ApplyMethod(triangle[1][0].rotate, np.pi/2))
        self.play(ApplyMethod(triangle[1][0].move_to, 1.5*LEFT+0.5*UP)); self.play(ApplyMethod(triangle[1][1].move_to,1.5*UP+1.5*LEFT)) #self.add(triangle[1][1])
        rotate2 = TextMobject(rotation_labels[1]); rotate2.scale(0.65); rotate2.move_to(1.5*LEFT+1*DOWN); self.play(ShowCreation(rotate2))
        # multiplication by i^2
        self.play(ShowCreation(triangle[2][0])); triangle[2][1].move_to(1.5*UP+2*RIGHT)
        self.play(ApplyMethod(triangle[2][0].rotate, np.pi/2)); self.play(ApplyMethod(triangle[2][0].rotate, np.pi/2)) # 180 rotation
        self.play(ApplyMethod(triangle[2][0].move_to, 2*RIGHT+0.5*UP)); self.play(ApplyMethod(triangle[2][1].move_to,0.5*UP+1*RIGHT))
        rotate3 = TextMobject(rotation_labels[2]); rotate3.scale(0.65); rotate3.move_to(2*RIGHT+1*DOWN); self.play(ShowCreation(rotate3))
        # multiplication by -i
        self.play(ShowCreation(triangle[3][0])); #triangle[3][1].move_to(0.5*DOWN+5*RIGHT)
        self.play(ApplyMethod(triangle[3][0].rotate, np.pi/2)); self.play(ApplyMethod(triangle[3][0].rotate, np.pi/2)); self.play(ApplyMethod(triangle[3][0].rotate, np.pi/2)) # 270 rotation
        self.play(ApplyMethod(triangle[3][0].move_to, 5*RIGHT+0.5*UP)); self.play(ApplyMethod(triangle[3][1].move_to,0.5*DOWN+5*RIGHT))
        rotate4 = TextMobject(rotation_labels[3]); rotate4.scale(0.65); rotate4.move_to(5*RIGHT+1*DOWN); self.play(ShowCreation(rotate4))        
        caption.move_to(3*UP)
        self.play(ShowCreation(caption))
        self.wait(6)

class HomomorphismIntution(Scene):
    def construct(self):
        title = TextMobject("Group Homomorphism")
        title2 = TextMobject("Group", "Isomorphism"); title2.move_to(3.5*UP); title2.set_color_by_tex("Isomorphism", BLUE)
        self.play(ShowCreation(title))
        self.play(ApplyMethod(title.move_to, 3.5*UP))

        defn = TextMobject(r"A group homomorphism is a map $f:G\rightarrow H$\\ between two groups such that the group operation is preserved.")
        self.play(ShowCreation(defn))
        self.play(ApplyMethod(defn.move_to, 2.5*UP))
        self.wait()

        group_example = TextMobject(r"G: Group of Complex Number Under Multiplication \\ H: Rotational Group of Isosceles Triange."); group_example.scale(0.7)
        group_example.move_to(2.5*UP)
        # self.play(ShowCreation(group_example))
        self.play(Transform(defn, group_example))
        self.wait()
        circle1 = Circle(radius=1, color=BLUE); circle1.move_to(2*LEFT+1*DOWN)
        circle2 = Circle(radius=1, color=PINK); circle2.move_to(2*RIGHT+1*DOWN)
        g = TextMobject("$G$"); g.move_to(2*LEFT+1*DOWN); h = TextMobject("$H$"); h.move_to(2*RIGHT+1*DOWN); 
        self.play(ShowCreation(circle1))
        self.play(ShowCreation(circle2))
        self.play(GrowFromCenter(g));self.play(GrowFromCenter(h))
        pointer = CurvedArrow(1*RIGHT+0.5*DOWN, 1*LEFT+0.5*DOWN,color=MAROON_C)
        f = TextMobject(r"$f:G\rightarrow H$"); f.scale(0.65); f.move_to(0.5*UP)
        preserve = TextMobject("Group Operation is preserved"); preserve.scale(0.65); preserve.move_to(1.5*UP)
        preserve.set_color_by_tex("Group", RED)
        self.play(GrowFromCenter(pointer))
        self.play(GrowFromCenter(f))
        self.play(ShowCreation(preserve))
        self.wait(3)
        self.play(Transform(title, title2))
        pointer2 = CurvedArrow(1*LEFT+1.5*DOWN, 1*RIGHT+1.5*DOWN,color=GREEN)
        self.play(GrowFromCenter(pointer2))
        self.wait(2)

class HomomorphismDefinition(Scene):
    # not very efficient, fix later
    def create_triangle(self, pos, label_pos, color_index=0):
        color = [GREEN, RED, BLUE, YELLOW]
        triangle=Polygon(np.array(pos[0]),np.array(pos[1]),np.array(pos[2]), color=color[color_index])
        # self.add(triangle)
        triangle_label = TextMobject("A"); triangle_label.move_to(label_pos)
        return triangle, triangle_label


    def construct(self):
        # plane_config =  { "stroke_width" : 2}
        # plane = ComplexPlane(**plane_config) 
        # self.play(ShowCreation(plane))

        housekeeping = TextMobject(r"$*$ : Group operation of $G$\\ $+$ : Group operation of $H$")
        housekeeping.scale(0.7); housekeeping.move_to(3*UP)
        text = TextMobject("$f(x*y) = f(x)+f(y)$")
        x = TextMobject("$x$,"); x.move_to(0.7*LEFT)
        y = TextMobject("$y$"); y.move_to(0.3*LEFT)
        g = TextMobject(r"$\in G$");g.move_to(0.5*RIGHT+0.025*UP)
        h = TextMobject(r"$\in H$");h.move_to(0.5*RIGHT)
        equal = TextMobject(r"$=$");equal.move_to(0.5 *RIGHT)
        func_left = TextMobject(r"$f$(");func_left.scale(2); func_left.move_to(6.4*LEFT)
        func_right = TextMobject(r")"); func_right.scale(2); func_right.move_to(0.25*LEFT)
        self.play(ShowCreation(housekeeping))
        self.play(ShowCreation(text))
        self.play(ApplyMethod(text.move_to, 2*UP))
        self.play(GrowFromCenter(x)); self.play(GrowFromCenter(y)); self.play(GrowFromCenter(g))
        self.wait(2)

        comma = TextMobject(","); comma.move_to(3.25*LEFT)
        group_operation = TextMobject("*"); group_operation.move_to(3.25*LEFT)
        cplx_mult_i   = Arrow(DOWN, UP, color=RED); cplx_mult_i.rotate(3*np.pi/2)
        mult_i_text   = TextMobject(r"Multiplication by $i$"); mult_i_text.scale(0.5); mult_i_text.move_to(5*LEFT+1*DOWN)
        cplx_mult_i2  = Arrow(DOWN, UP, color=BLUE); cplx_mult_i2.rotate(3*np.pi/2)
        mult_i2_text  = TextMobject(r"Multiplication by $i^2$"); mult_i2_text.scale(0.5); mult_i2_text.move_to(1.5*LEFT+1*DOWN)
        cplx_mult_i.move_to(5*LEFT); cplx_mult_i.rotate(np.pi/2)
        cplx_mult_i2.move_to(1.5*LEFT);cplx_mult_i2.rotate(np.pi)
        self.play(Transform(x,cplx_mult_i))
        # self.play(ApplyMethod(cplx_mult_i.rotate,np.pi/2))
        self.play(Transform(y, cplx_mult_i2))
        self.add(comma)
        self.play(ShowCreation(mult_i_text)); self.play(ShowCreation(mult_i2_text))
        self.play(Transform(comma, group_operation))
        self.play(GrowFromCenter(func_left))
        self.play(GrowFromCenter(func_right))
        self.play(Transform(g,h))
        ######################## remove comment
        square = Square(side_length=3, fill_color=BLACK, color=BLACK, fill_opacity=1); square.move_to(1.5*RIGHT); self.add(square)
        self.play(Transform(h,equal))
        # self.play(ApplyMethod(cplx_mult_i2.rotate,np.pi/2)); self.play(ApplyMethod(cplx_mult_i2.rotate,np.pi/2))
        self.wait(2)

        # after = part

        cplx_mult_if   = Arrow(DOWN, UP, color=RED); cplx_mult_if.rotate(3*np.pi/2)
        mult_i_textf   = TextMobject(r"Multiplication by $i$"); mult_i_textf.scale(0.5); mult_i_textf.move_to(2.5*RIGHT+1*DOWN)
        cplx_mult_i2f  = Arrow(DOWN, UP, color=BLUE); cplx_mult_i2f.rotate(3*np.pi/2)
        mult_i2_textf  = TextMobject(r"Multiplication by $i^2$"); mult_i2_textf.scale(0.5); mult_i2_textf.move_to(6*RIGHT+1*DOWN)
        cplx_mult_if.move_to(2.5*RIGHT); cplx_mult_if.rotate(np.pi/2)
        cplx_mult_i2f.move_to(6*RIGHT); cplx_mult_i2f.rotate(np.pi)
        self.play(GrowFromCenter(cplx_mult_if)); self.play(ShowCreation(mult_i_textf))
        self.play(GrowFromCenter(cplx_mult_i2f)); self.play(ShowCreation(mult_i2_textf))
        self.wait(2)
        fbrac_i_left = TextMobject("$f$("); fbrac_i_left.scale(2); fbrac_i_right = TextMobject(")"); fbrac_i_right.scale(2)
        fbrac_i2_left = TextMobject("$f($"); fbrac_i2_left.scale(2); fbrac_i2_right = TextMobject(")"); fbrac_i2_right.scale(2)

        fbrac_i_left.move_to(1.7*RIGHT); fbrac_i_right.move_to(3*RIGHT)
        fbrac_i2_left.move_to(4.9*RIGHT); fbrac_i2_right.move_to(6.8*RIGHT)

        self.add(fbrac_i_left); self.add(fbrac_i_right)
        self.add(fbrac_i2_left); self.add(fbrac_i2_right)
        self.wait(1)

        plus = TextMobject("+");plus.move_to(4*RIGHT);self.play(ShowCreation(plus))

        # traingle symmetry
        self.wait(1)
        equal2 = TextMobject("$=$"); equal2.move_to(0.5*RIGHT+2.5*DOWN)
        self.add(equal2)
        self.wait(1)

        triangle = []
        for i in range(0,4):
            t, tl = self.create_triangle([[0,-1,0], [1,0,0], [0,1,0]], 1.5*RIGHT, i)
            triangle.append([t,tl]) # triangle, triangle_label

        rotation_labels = ["Rotation by 0", r"Rotation by $\frac{\pi}{2}$", r"Rotation by $\pi$", r"Rotation by $3\frac{\pi}{2}$"]

        triangle[1][0].move_to(2.5*RIGHT+2.5*DOWN)
        triangle[1][1].move_to(2.5*RIGHT+1.75*DOWN)
        self.play(ShowCreation(triangle[1][0])); 
        self.play(ApplyMethod(triangle[1][0].rotate, np.pi/2))
        self.play(GrowFromCenter(triangle[1][1]))
        rotate2 = TextMobject(rotation_labels[1]); rotate2.scale(0.65); rotate2.move_to(2.5*RIGHT+3.75*DOWN); self.play(ShowCreation(rotate2))

        self.wait(1)
        triangle[2][0].move_to(6*RIGHT+2.5*DOWN)
        triangle[2][1].move_to(5.2*RIGHT+2.5*DOWN)
        self.play(ShowCreation(triangle[2][0]))
        self.play(ApplyMethod(triangle[2][0].rotate, np.pi/2)); self.play(ApplyMethod(triangle[2][0].rotate, np.pi/2)) # 180 rotation
        self.play(GrowFromCenter(triangle[2][1]))
        rotate3 = TextMobject(rotation_labels[2]); rotate3.scale(0.65); rotate3.move_to(6*RIGHT+3.75*DOWN); self.play(ShowCreation(rotate3))

        plus2 = TextMobject("+");plus2.move_to(4*RIGHT+2.5*DOWN);self.play(ShowCreation(plus2))
        self.wait(1)
        # equal2 = TextMobject("$=$");equal2.move_to(1.5*RIGHT+2.5*DOWN)

        fbrac_homo = TextMobject("$f$("); fbrac_homo.scale(2); fbrac_homoR = TextMobject(")"); fbrac_homoR.scale(2)
        fbrac_homo.move_to(4.5*LEFT+2.5*DOWN);self.add(fbrac_homo)
        fbrac_homoR.move_to(2.4*LEFT+2.5*DOWN);self.add(fbrac_homoR)
        # f(i * i^2)
        textList = [TextMobject("Multiplicaltion by $i$"), TextMobject("Multiplicaltion by $i^2$")]
        textList[0].move_to(3.75*DOWN+3.25*LEFT); textList[0].scale(0.65)
        textList[1].move_to(3.75*DOWN+3.25*LEFT); textList[1].scale(0.65)
        arrow_homo = Arrow(LEFT, RIGHT, color=YELLOW); #cplx_mult_1.rotate(3*np.pi/2)
        arrow_homo.move_to(3.25*LEFT+2.5*DOWN)
        self.play(ShowCreation(arrow_homo));self.wait()
        self.play(ShowCreation(textList[0]))
        self.play(ApplyMethod(arrow_homo.rotate, np.pi/2))
        self.wait(1)
        self.wait(2)
        self.play(Transform(textList[0],textList[1]))
        self.play(ApplyMethod(arrow_homo.rotate, np.pi/2));self.play(ApplyMethod(arrow_homo.rotate, np.pi/2))
        self.wait(1)
        self.wait(2)

        # Final Trianlge of roatation
        triangle[3][0].rotate(3*np.pi/2)
        triangle[3][0].move_to(3.25*LEFT+2.5*DOWN)
        triangle[3][1].move_to(3.25*DOWN+3.25*LEFT)
        # self.play(ShowCreation(triangle[3][0])); #triangle[3][1].move_to(0.5*DOWN+5*RIGHT)
        self.play(Transform(arrow_homo, triangle[3][0]))
        self.play(Transform(fbrac_homo,triangle[3][1]))
        fbrac_homoR.move_to(50*LEFT)
        rotation_angle = TextMobject(r"Rotation by $\frac{3\pi}{2}$");
        rotation_angle.move_to(3.75*DOWN+3.25*LEFT); rotation_angle.scale(0.65); rotation_angle.set_color_by_tex("Rotation", ORANGE)
        sq = Square(fill_color=BLACK, fill_opacity=1, side_length=3, color=BLACK);sq.move_to(3.2*LEFT+5*DOWN);self.add(sq)
        self.play(Transform(textList[1], rotation_angle))
        self.wait(2)
        # self.play(ApplyMethod())
        # rotate4 = TextMobject(rotation_labels[3]); rotate4.scale(0.65); rotate4.move_to(5*RIGHT+1*DOWN); self.play(ShowCreation(rotate4))        
        
        # finally rotate the other triangles
        triangle[2][0].move_to(50*RIGHT)
        triangle[2][1].move_to(50*RIGHT)
        self.play(ApplyMethod(plus2.move_to, 3.75*DOWN+4.25*RIGHT))
        self.wait(2)
        self.play(ApplyMethod(triangle[1][0].move_to,4*RIGHT+2.5*DOWN))
        self.play(ApplyMethod(triangle[1][1].move_to,4*RIGHT+1.75*DOWN))
        new_text1 = TextMobject(r"Rotation by $\frac{\pi}{2}$"); new_text1.scale(0.45)
        new_text2 = TextMobject(r"Rotation by $\frac{\pi}{2}$ + \\Rotation by $\pi$"); new_text2.scale(0.45)
        new_text1.move_to(6*RIGHT+2*DOWN)
        new_text2.move_to(6*RIGHT+2*DOWN)
        self.play(ShowCreation(new_text1))
        self.wait(2) #Arrow
        self.play(Transform(new_text1, new_text2))
        self.play(ApplyMethod(triangle[1][0].rotate,np.pi/2)); self.play(ApplyMethod(triangle[1][0].rotate,np.pi/2))
        self.play(ApplyMethod(triangle[1][1].move_to,4*RIGHT+3.25*DOWN))
        rotate2.move_to(7*DOWN)
        rotate3.move_to(7*DOWN)
        transform_triangle = TextMobject(r"Rotation by $\frac{3\pi}{2}$");
        transform_triangle.move_to(3.75*DOWN+4*RIGHT); transform_triangle.scale(0.65); transform_triangle.set_color_by_tex("Rotation", ORANGE)
        self.play(Transform(plus2, transform_triangle))
        self.wait(2)
