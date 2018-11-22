from big_ol_pile_of_manim_imports import *

class Create_group_elements(Scene):
    def construct(self):
        arrow0   = Arrow(DOWN, UP, color=RED); a0   = TextMobject("Rotation by $0$"); a0.scale(0.65); a0.move_to(5.5*LEFT+1*DOWN)
        arrow90  = Arrow(DOWN, UP, color=BLUE); a90  = TextMobject(r"Rotation by $\frac{\pi}{2}$"); a90.scale(0.65); a90.move_to(2*LEFT+1*DOWN)
        arrow180 = Arrow(DOWN, UP, color=ORANGE); a180 = TextMobject(r"Rotation by $\pi$"); a180.scale(0.65); a180.move_to(2*RIGHT+1*DOWN)
        arrow270 = Arrow(DOWN, UP, color=GREEN_B); a270 = TextMobject(r"Rotation by $\frac{3\pi}{2}$"); a270.scale(0.65); a270.move_to(5.5*RIGHT+1*DOWN)
        caption = TextMobject("Group of rotation of vectors"); caption.move_to(3*UP)
        # comma = TextMobject(",")
        # bracket_left = TextMobject(r"$\bigg \{$")
        # 0 deg
        # self.add(bracket_left)
        self.play(ShowCreation(arrow0))
        self.play(ApplyMethod(arrow0.move_to, 5.5*LEFT))
        self.play(ShowCreation(a0))
        self.wait()
        #90 deg
        self.play(ShowCreation(arrow90))
        self.play(ApplyMethod(arrow90.rotate,np.pi/2))
        self.play(ApplyMethod(arrow90.move_to, 2*LEFT))
        self.play(ShowCreation(a90))
        # 180 deg
        self.play(ShowCreation(arrow180))
        self.play(ApplyMethod(arrow180.rotate,np.pi))
        self.play(ApplyMethod(arrow180.move_to, 2*RIGHT))
        self.play(ShowCreation(a180))
        # 270 deg
        self.play(ShowCreation(arrow270))
        self.play(ApplyMethod(arrow270.rotate,3*np.pi/2))
        self.play(ApplyMethod(arrow270.move_to, 5.5*RIGHT))
        self.play(ShowCreation(a270))
        self.wait(2)
        self.play(ShowCreation(caption))

        # self.play()
        self.wait()

class Closure(Scene):
    def construct(self):
        # closure
        arrow180 = Arrow(DOWN, UP, color=ORANGE); a180 = TextMobject(r"Rotation by $\pi$"); a180.scale(0.65); a180.move_to(5.5*LEFT+1*DOWN)
        arrow270 = Arrow(DOWN, UP, color=GREEN_B); a270 = TextMobject(r"Rotation by $\frac{3\pi}{2}$"); a270.scale(0.65); a270.move_to(1.5*LEFT+1*DOWN)
        arrow90  = Arrow(DOWN, UP, color=BLUE); a90  = TextMobject(r"Rotation by $\frac{\pi}{2}$"); a90.scale(0.65); a90.move_to(4*RIGHT+1*DOWN)
        plus = TextMobject("$+$"); plus.scale(1.5); plus.move_to(3.5*LEFT)
        equals = TextMobject("$=$"); equals.scale(1.5); equals.move_to(1.5*RIGHT)
        caption = TextMobject("Closure"); caption.move_to(3*UP)
        # 180
        self.play(ShowCreation(arrow180))
        self.play(ApplyMethod(arrow180.rotate,np.pi))
        self.play(ApplyMethod(arrow180.move_to, 5.5*LEFT))
        self.play(ShowCreation(a180))
        # +
        self.play(ShowCreation(plus))
        # 270
        self.play(ShowCreation(arrow270))
        self.play(ApplyMethod(arrow270.rotate,np.pi))
        self.play(ApplyMethod(arrow270.rotate,np.pi/2))
        self.play(ApplyMethod(arrow270.move_to, 1.5*LEFT))
        self.play(ShowCreation(a270))
        # =
        self.play(ShowCreation(equals))
        # 90
        self.play(ShowCreation(a90))
        self.play(ApplyMethod(arrow90.rotate,np.pi/2))
        self.play(ApplyMethod(arrow90.move_to, 4*RIGHT))
        self.play(ShowCreation(caption))
        self.wait()

class Identity(Scene):
    def construct(self):
        caption = TextMobject("Rotation by 0 radians is the identity of the group"); caption.move_to(3*UP)
        arrow180 = Arrow(DOWN, UP, color=ORANGE); a180 = TextMobject(r"Rotation by $\pi$"); a180.scale(0.65); a180.move_to(5.5*LEFT+1*DOWN)
        arrow0   = Arrow(DOWN, UP, color=RED); a0 = TextMobject("Rotation by $0$"); a0.scale(0.65); a0.move_to(1.5*LEFT+1*DOWN)
        arrow180_0  = Arrow(DOWN, UP, color=BLUE); a180_0  = TextMobject(r"Rotation by $\frac{\pi}{2}$"); a180_0.scale(0.65); a180_0.move_to(4*RIGHT+1*DOWN)
        plus = TextMobject("$+$"); plus.scale(1.5); plus.move_to(3.5*LEFT)
        equals = TextMobject("$=$"); equals.scale(1.5); equals.move_to(1.5*RIGHT)
        
        self.play(ShowCreation(arrow180))
        self.play(ApplyMethod(arrow180.rotate,np.pi))
        self.play(ApplyMethod(arrow180.move_to, 5.5*LEFT))
        self.play(ShowCreation(a180))

        self.play(ShowCreation(plus))

        self.play(ShowCreation(arrow0))
        # self.play(ApplyMethod(arrow270.rotate,3*np.pi/2))
        self.play(ApplyMethod(arrow0.move_to, 1.5*LEFT))
        self.play(ShowCreation(a0))
        self.play(ShowCreation(equals))

        self.play(ShowCreation(a180_0))
        self.play(ApplyMethod(arrow180_0.rotate,np.pi))
        self.play(ApplyMethod(arrow180_0.move_to, 4*RIGHT))
        self.play(ShowCreation(caption))
        self.wait(3)

class Inverse(Scene):
    def construct(self):
        pass
        # inverse

class Associativity(Scene):

    def get_arrows(self, move):
        arrow180 = Arrow(DOWN, UP, color=ORANGE); a180 = TextMobject(r"Rotation by $\pi$"); a180.scale(0.65); a180.move_to(move[0])
        arrow270 = Arrow(DOWN, UP, color=GREEN_B); a270 = TextMobject(r"Rotation by $\frac{3\pi}{2}$"); a270.scale(0.65); a270.move_to(move[1])
        arrow90  = Arrow(DOWN, UP, color=BLUE); a90  = TextMobject(r"Rotation by $\frac{\pi}{2}$"); a90.scale(0.65); a90.move_to(move[2])
        return arrow180, arrow270, arrow90, a180, a270, a90

    def rotate_arrow(self, arrow, cap, angle, endpos, move=True):
        # rotate = [0, np.pi/2, np.pi, 3*np.pi/2]
        self.add(arrow)
        if angle == np.pi:
            self.play(ApplyMethod(arrow.rotate,np.pi/2))
            self.play(ApplyMethod(arrow.rotate,np.pi/2))
        elif angle == 3*np.pi/2:
            self.play(ApplyMethod(arrow.rotate,np.pi/2))
            self.play(ApplyMethod(arrow.rotate,np.pi/2))
            self.play(ApplyMethod(arrow.rotate,np.pi/2))
        else:
            self.play(ApplyMethod(arrow.rotate,angle))
        if move:                        
            self.play(ApplyMethod(arrow.move_to, endpos))
            self.play(ShowCreation(cap))


    def construct(self):
        arrow_ans1 = Arrow(DOWN, UP, color=ORANGE); ans1 = TextMobject(r"Rotation by $\pi$"); ans1.scale(0.65); ans1.move_to(5.5*RIGHT+2*UP)
        arrow_ans2 = Arrow(DOWN, UP, color=ORANGE); ans2 = TextMobject(r"Rotation by $\pi$"); ans2.scale(0.65); ans2.move_to(5.5*RIGHT+3*DOWN)
        
        plus = TextMobject("$+$"); plus.scale(1); plus.move_to(4*LEFT+3*UP)
        plus2 = TextMobject("$+$"); plus2.scale(1); plus2.move_to(3*UP)
        equals = TextMobject("$=$"); equals.scale(1); equals.move_to(3.5*RIGHT+3*UP)

        plus11 = TextMobject("$+$"); plus11.scale(1); plus11.move_to(4*LEFT+2*DOWN)
        plus22 = TextMobject("$+$"); plus22.scale(1); plus22.move_to(2*DOWN)
        equals1 = TextMobject("$=$"); equals1.scale(1); equals1.move_to(3.5*RIGHT+2*DOWN)
        caption = TextMobject("Associativity ")
        # part 1
        arrow180, arrow270, arrow90, a180, a270, a90= self.get_arrows([6*LEFT+2*UP, 2*LEFT+2*UP, 2*RIGHT+2*UP])
        self.rotate_arrow(arrow180, a180, np.pi ,6*LEFT+3*UP) # 180
        self.play(ShowCreation(plus)) # +
        self.rotate_arrow(arrow270, a270, 3*np.pi/2, 2*LEFT+3*UP ) # 270
        self.play(ShowCreation(plus2))# +
        self.rotate_arrow(arrow90, a90, np.pi/2, 2*RIGHT+3*UP ) # 90    
        self.play(ShowCreation(equals))
        self.rotate_arrow(arrow_ans1, ans1, np.pi, 5.5*RIGHT+3*UP, move=False); self.wait()
        self.rotate_arrow(arrow_ans1, ans1, 3*np.pi/2, 5.5*RIGHT+3*UP, move=False); self.wait()
        self.rotate_arrow(arrow_ans1, ans1, np.pi/2, 5.5*RIGHT+3*UP, move=True)
        # part 2
        ar2180, ar2270, ar290, ar180, ar270, ar90= self.get_arrows([6*LEFT+3*DOWN, 2*LEFT+3*DOWN, 2*RIGHT+3*DOWN])
        self.rotate_arrow(ar2270, ar270, 3*np.pi/2, 6*LEFT+2*DOWN, move=True) # 270 
        self.play(ShowCreation(plus11)) # +
        self.rotate_arrow(ar290, ar90, np.pi/2, 2*LEFT+2*DOWN ) # 90        
        self.play(ShowCreation(plus22))# +
        self.rotate_arrow(ar2180, ar180, np.pi , 2*RIGHT+2*DOWN) # 180
        self.play(ShowCreation(equals1))
        self.rotate_arrow(arrow_ans2, ans2, 3*np.pi/2, 5.5*RIGHT+3*UP, move=False); self.wait()
        self.rotate_arrow(arrow_ans2, ans2, np.pi/2, 5.5*RIGHT+3*UP, move=False);self.wait()
        self.rotate_arrow(arrow_ans2, ans2, np.pi, 5.5*RIGHT+2*DOWN, move=True)     
        self.wait()   
        self.play(ShowCreation(caption))
        # commutativity

class Commutativity(Scene):
    def get_arrows(self, move):
        arrow180 = Arrow(DOWN, UP, color=ORANGE)
        a180 = TextMobject(r"Rotation by $\pi$"); a180.scale(0.65); a180.move_to(move[0])
        arrow270 = Arrow(DOWN, UP, color=GREEN_B)
        a270 = TextMobject(r"Rotation by $\frac{3\pi}{2}$"); a270.scale(0.65); a270.move_to(move[1])
        return arrow180, arrow270, a180, a270,

    def rotate_arrow(self, arrow, cap, angle, endpos, move=True):
        # rotate = [0, np.pi/2, np.pi, 3*np.pi/2]
        # print(endpos)
        # print(angle)
        self.add(arrow)
        if angle == np.pi:
            self.play(ApplyMethod(arrow.rotate,np.pi/2))
            self.play(ApplyMethod(arrow.rotate,np.pi/2))
        elif angle == 3*np.pi/2:
            self.play(ApplyMethod(arrow.rotate,np.pi/2))
            self.play(ApplyMethod(arrow.rotate,np.pi/2))
            self.play(ApplyMethod(arrow.rotate,np.pi/2))
        else:
            self.play(ApplyMethod(arrow.rotate,angle))
        if move:                        
            self.play(ApplyMethod(arrow.move_to, endpos))
            self.play(ShowCreation(cap))


    def construct(self):
        arrow_ans1 = Arrow(DOWN, UP, color=ORANGE); ans1 = TextMobject(r"Rotation by $\frac{\pi}{2}$"); ans1.scale(0.65); ans1.move_to(5.5*RIGHT+2*UP)
        arrow_ans2 = Arrow(DOWN, UP, color=ORANGE); ans2 = TextMobject(r"Rotation by $\frac{\pi}{2}$"); ans2.scale(0.65); ans2.move_to(5.5*RIGHT+3*DOWN)

        plus  = TextMobject("$+$"); plus.scale(1); plus.move_to(3*UP)
        plus2 = TextMobject("$+$"); plus2.scale(1); plus2.move_to(3*UP)
        equals = TextMobject("$=$"); equals.scale(1); equals.move_to(3.5*RIGHT+3*UP)

        plus11 = TextMobject("$+$"); plus11.scale(1); plus11.move_to(2*DOWN)
        plus22 = TextMobject("$+$"); plus22.scale(1); plus22.move_to(2*DOWN)
        equals1 = TextMobject("$=$"); equals1.scale(1); equals1.move_to(3.5*RIGHT+2*DOWN)
        caption = TextMobject("Commutativity")
        # part 1
        arrow180, arrow270, a180, a270 = self.get_arrows([1.5*LEFT+2*UP,1.5*RIGHT+2*UP])
        ar2180, ar2270,ar180, ar270 = self.get_arrows([1.5*RIGHT+3*DOWN,1.5*LEFT+3*DOWN])
        # ar2270, ar2180, ar180, ar270= self.get_arrows([6*LEFT+3*DOWN, 2*LEFT+3*DOWN])


        self.rotate_arrow(arrow180, a180, np.pi ,1.5*LEFT+3*UP) # 180
        self.play(ShowCreation(plus)) # +
        self.rotate_arrow(arrow270, a270, 3*np.pi/2, 1.5*RIGHT+3*UP ) # 270
        self.play(ShowCreation(equals))
        self.rotate_arrow(arrow_ans1, ans1, np.pi, 5.5*RIGHT+3*UP, move=False); self.wait()
        self.rotate_arrow(arrow_ans1, ans1, 3*np.pi/2, 5.5*RIGHT+3*UP, move=True); self.wait()
        
        # part 2
        
        self.rotate_arrow(ar2270, ar270, 3*np.pi/2, 1.5*LEFT+2*DOWN, move=True) # 270 

        self.play(ShowCreation(plus11)) # +
        self.rotate_arrow(ar2180, ar180, np.pi , 1.5*RIGHT+2*DOWN) # 180
        
        self.play(ShowCreation(plus22))# +
        self.play(ShowCreation(equals1))
        
        self.rotate_arrow(arrow_ans2, ans2, 3*np.pi/2, 5.5*RIGHT+3*UP, move=False); self.wait()
        self.rotate_arrow(arrow_ans2, ans2, np.pi, 5.5*RIGHT+2*DOWN, move=True);self.wait()
        # self.rotate_arrow(arrow_ans2, ans2, np.pi, 5.5*RIGHT+2*DOWN, move=True)       
        self.wait()
        caption.move_to(3*LEFT)
        self.play(ShowCreation(caption))
        self.wait()

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

class HomomorphismDefinition(Scene):
    def construct(self):
        pass

class GroupHomomorphism(object):
    """docstring for GroupHomomorphism"""
    def construct(self, arg):
        super(GroupHomomorphism, self).__init__()
        self.arg = arg
        