from big_ol_pile_of_manim_imports import *

from copy import copy
import numpy as np

mult = [0, np.pi/2, np.pi, 3*np.pi/2]
mult_caption = [r"Multiplication by $1$", r"Multiplication by $i$", r"Multiplication by $i^2$", r"Multiplication by $-i$"]

def create_arrow(arrow_caption, arrow_position, arrow_text_position, color=YELLOW, scale=0.65):
    arrow = Arrow(LEFT, RIGHT, color=color)
    arrow.move_to(arrow_position)
    arrow_text = TextMobject(arrow_caption)
    arrow_text.scale(scale)
    arrow_text.move_to(arrow_text_position)
    return [arrow, arrow_text]

def rotate_arrow(self, arrow_obj, angle):
    if angle == np.pi:
        self.play(ApplyMethod(arrow_obj.rotate, np.pi/2))
        self.play(ApplyMethod(arrow_obj.rotate, np.pi/2))
    elif angle == 3*np.pi/2:
        self.play(ApplyMethod(arrow_obj.rotate, np.pi/2))
        self.play(ApplyMethod(arrow_obj.rotate, np.pi/2))
        self.play(ApplyMethod(arrow_obj.rotate, np.pi/2))
    else:
        self.play(ApplyMethod(arrow_obj.rotate, angle))

def scaling_texmobject(text, pos, scale_value=1.5):
    ret_obj = TextMobject(text)
    ret_obj.scale(scale_value)
    ret_obj.move_to(pos)
    return ret_obj

class Titles(Scene):
    def construct(self):
        caption = TextMobject("Properties of Group")
        self.play(ShowCreation(caption))
        self.play(ApplyMethod(caption.move_to, 3*UP))
        closure = TextMobject(r"""\begin{enumerate}
            \item Closure
            \item Identity
            \item Inverse
            \item Associativity
            \item Commutativity
            \end{enumerate}""")
        closure.move_to(3*LEFT)
        self.play(ShowCreation(closure))
        self.wait(2)

class Create_Group_Elements(Scene):
    def construct(self):
        caption = TextMobject("Group of Complex Numbers under Multiplication"); caption.move_to(3*UP)
        extras = [scaling_texmobject(r"[", 6.5*LEFT, scale_value=3.5),
                  scaling_texmobject(r"]", 6.5*RIGHT, scale_value=3.5),
                  scaling_texmobject(r",", 3.3*LEFT+1*DOWN, scale_value=1),
                  scaling_texmobject(r",", 1*DOWN, scale_value=1),
                  scaling_texmobject(r",", 3.35*RIGHT+1*DOWN, scale_value=1)]

        arrows = [create_arrow(mult_caption[0],5*LEFT,5*LEFT+1*DOWN, scale=0.5),
                 create_arrow(mult_caption[1],1.8*LEFT,1.8*LEFT+1*DOWN,color=RED, scale=0.5), 
                 create_arrow(mult_caption[2],1.8*RIGHT,1.8*RIGHT+1*DOWN,color=BLUE, scale=0.5),    
                 create_arrow(mult_caption[3],5*RIGHT,5*RIGHT+1*DOWN,color=GREEN, scale=0.5)]

        for index,element in enumerate(arrows):
            self.play(ShowCreation(element[0]))
            self.play(ShowCreation(element[1]))
            rotate_arrow(self, element[0], mult[index])

        [self.play(ShowCreation(extra)) for extra in extras]
        self.wait(2)
        self.play(ShowCreation(caption))
        self.wait(2)

class Closure(Scene):
    def construct(self):
        mult = [np.pi/2, np.pi, 3*np.pi/2]
        arrow = [create_arrow(mult_caption[1],5.5*LEFT,5.5*LEFT+1*DOWN),
        create_arrow(mult_caption[2],1.5*LEFT,1.5*LEFT+1*DOWN,color=RED), 
        create_arrow(mult_caption[3],4*RIGHT,4*RIGHT+1*DOWN,color=BLUE)]

        plus = scaling_texmobject("$*$",3.5*LEFT)
        equals = scaling_texmobject("$=$",1.5*RIGHT)
        caption = TextMobject("Closure"); caption.move_to(3*UP)
        belongs_to_G = TextMobject(r"$\in G$"); belongs_to_G.move_to(6.5*RIGHT)

        i = 0
        for complex_number in arrow:
            self.play(ShowCreation(complex_number[0]))
            self.play(ShowCreation(complex_number[1]))
            rotate_arrow(self, complex_number[0], mult[i])
            i = i + 1

        self.play(ShowCreation(plus))
        self.play(ShowCreation(equals))
        self.wait(1)
        self.play(ShowCreation(belongs_to_G))
        self.wait(1)
        self.play(ShowCreation(caption))
        self.wait(2)

class Associativity(Scene):

    def construct(self):
        caption = TextMobject("Associativity")
        mult = [ np.pi,3*np.pi/2,np.pi/2 ]
        plus   =  scaling_texmobject("$*$", 3.5*LEFT+3*UP, scale_value=1)
        plus2  =  scaling_texmobject("$*$", 3*UP+0.5*RIGHT, scale_value=1)
        equals =  scaling_texmobject("$=$", 3.5*RIGHT+3*UP, scale_value=1)
        plus11  =  scaling_texmobject("$*$", 3.5*LEFT+2*DOWN, scale_value=1)
        plus22  =  scaling_texmobject("$*$", 2*DOWN+0.5*RIGHT, scale_value=1)
        equals1 =  scaling_texmobject("$=$", 3.5*RIGHT+2*DOWN, scale_value=1)
        plus_list = [plus, plus2, equals, plus11, plus22, equals1]

        bracket  = [scaling_texmobject("$[$", 6.5*LEFT+3*UP, scale_value=2),
                    scaling_texmobject("$]$", 3*UP, scale_value=2),
                    scaling_texmobject("$[$", 3*LEFT+2*DOWN, scale_value=2),
                    scaling_texmobject("$]$", 3*RIGHT+2*DOWN, scale_value=2)]
        caption = TextMobject("Associativity")

        arrow_1 = [create_arrow(mult_caption[2], 5.5*LEFT+3*UP, 5.5*LEFT+2*UP, color=RED),
                   create_arrow(mult_caption[3], 1.5*LEFT+3*UP, 1.5*LEFT+2*UP, color=BLUE),
                   create_arrow(mult_caption[1], 2*RIGHT+3*UP, 2*RIGHT+2*UP,color=PURPLE)]
        
        arrow_2 = [create_arrow(mult_caption[2], 5.5*LEFT+2*DOWN, 5.5*LEFT+1*DOWN, color=RED),
                   create_arrow(mult_caption[3], 1.5*LEFT+2*DOWN,  1.5*LEFT+1*DOWN, color=BLUE),
                   create_arrow(mult_caption[1], 2*RIGHT+2*DOWN, 2*RIGHT+1*DOWN,color=PURPLE)]
        
        answer  = [create_arrow(mult_caption[2], 5.5*RIGHT+3*UP, 5.5*RIGHT+2*UP, color=YELLOW),
                   create_arrow(mult_caption[2], 5.5*RIGHT+2*DOWN, 5.5*RIGHT+1*DOWN, color=YELLOW)]
        i = 0
        for arrow in arrow_1:
            self.play(ShowCreation(arrow[0]))
            self.play(ShowCreation(arrow[1]))
            rotate_arrow(self, arrow[0], mult[i])
            i = i+1

        [self.play(GrowFromCenter(object)) for object in plus_list[:3]]
        [self.play(GrowFromCenter(object)) for object in bracket[:2]]
        self.play(ShowCreation(answer[0][0]))
        rotate_arrow(self,answer[0][0], np.pi); self.wait(1); rotate_arrow(self,answer[0][0], 3*np.pi/2); self.wait(1); rotate_arrow(self, answer[0][0], np.pi/2)
        self.play(ShowCreation(answer[0][1]))
        i = 0
        [self.play(GrowFromCenter(object)) for object in plus_list[3:]]
        
        for arrow in arrow_2:
            self.play(ShowCreation(arrow[0]))
            self.play(ShowCreation(arrow[1]))
            rotate_arrow(self, arrow[0], mult[i])
            i = i+1
        [self.play(GrowFromCenter(object)) for object in bracket[2:]]
        self.play(ShowCreation(answer[1][0]))
        rotate_arrow(self,answer[1][0], 3*np.pi/2); self.wait(1); rotate_arrow(self,answer[1][0], np.pi/2); self.wait(1); rotate_arrow(self, answer[1][0], np.pi)
        self.play(ShowCreation(answer[1][1]))
        self.wait(2)
        caption.move_to(0.5*UP)
        self.play(ShowCreation(caption))
        self.wait(2)

class Identity(Scene):
    def construct(self):
        caption = TextMobject("Multiplication by 1 is the identity of the group"); caption.move_to(3*UP)
        mult = [ 0, np.pi/2,np.pi,3*np.pi/2 ]
        identity_element = create_arrow(mult_caption[0], 1.5*LEFT, 1.5*LEFT+1*DOWN, color=BLUE)
        
        arrow_1 = [create_arrow(mult_caption[0], 5.5*LEFT, 5.5*LEFT+1*DOWN, color=RED),
                   create_arrow(mult_caption[1], 5.5*LEFT, 5.5*LEFT+1*DOWN, color=RED),
                   create_arrow(mult_caption[2], 5.5*LEFT, 5.5*LEFT+1*DOWN, color=RED),
                   create_arrow(mult_caption[3], 5.5*LEFT, 5.5*LEFT+1*DOWN, color=RED)]
        self.play(ShowCreation(identity_element[0]))
        self.play(ShowCreation(caption))
        self.play(ShowCreation(identity_element[1]))

        extras = [scaling_texmobject("$*$",3.5*LEFT, scale_value=0.8), scaling_texmobject("$=$",1.5*RIGHT,scale_value=0.8)]
        [self.play(GrowFromCenter(extra)) for extra in extras]

        for index, arrow in enumerate(arrow_1):
            self.play(ShowCreation(arrow[0]))
            self.play(ShowCreation(arrow[1]))
            rotate_arrow(self, arrow[0], mult[index])
            mult_result = create_arrow(mult_caption[index], 4*RIGHT, 4*RIGHT+1*DOWN, color=PINK)
            self.play(ShowCreation(mult_result[0]))
            self.play(ShowCreation(mult_result[1]))
            rotate_arrow(self, mult_result[0], mult[index])
            self.wait(2)
            arrow[0].move_to(50*DOWN); arrow[1].move_to(50*DOWN)
            mult_result[0].move_to(50*DOWN); mult_result[1].move_to(50*DOWN)

class Inverse(Scene):
    def construct(self):
        caption = TextMobject("Inverse Elemets of the Group"); caption.move_to(3*UP)
        identity_element = create_arrow(mult_caption[0], 5.5*RIGHT, 5.5*RIGHT+1*DOWN, color=YELLOW)
        self.play(ShowCreation(identity_element[0]))
        self.play(ShowCreation(caption))
        self.play(ShowCreation(identity_element[1]))

        arrow_1 = [create_arrow(mult_caption[0], 5.5*LEFT, 5.5*LEFT+1*DOWN, color=RED),
                   create_arrow(mult_caption[1], 5.5*LEFT, 5.5*LEFT+1*DOWN, color=BLUE),
                   create_arrow(mult_caption[2], 5.5*LEFT, 5.5*LEFT+1*DOWN, color=GREEN),
                   create_arrow(mult_caption[3], 5.5*LEFT, 5.5*LEFT+1*DOWN, color=ORANGE)]
        mult = [ 0, np.pi/2,np.pi,3*np.pi/2 ]

        arrow_2 = [create_arrow(mult_caption[0], 1.5*LEFT, 1.5*LEFT+1*DOWN, color=RED),
                   create_arrow(mult_caption[3], 1.5*LEFT, 1.5*LEFT+1*DOWN, color=ORANGE),
                   create_arrow(mult_caption[2], 1.5*LEFT, 1.5*LEFT+1*DOWN, color=GREEN),
                   create_arrow(mult_caption[1], 1.5*LEFT, 1.5*LEFT+1*DOWN, color=BLUE)]
        mult_inverse = [0, 3*np.pi/2, np.pi, np.pi/2]
        extras = [scaling_texmobject("$*$",3.6*LEFT, scale_value=0.8), scaling_texmobject("$=$",1.5*RIGHT,scale_value=0.8)]
        [self.play(GrowFromCenter(extra)) for extra in extras]
        index = 0
        for first, second in zip(arrow_1, arrow_2):
            self.play(ShowCreation(first[0]))
            self.play(ShowCreation(first[1]))
            rotate_arrow(self, first[0], mult[index])
            self.play(ShowCreation(second[0]))
            self.play(ShowCreation(second[1]))
            rotate_arrow(self, second[0], mult_inverse[index])
            self.wait(3)
            first[0].move_to(50*DOWN); first[1].move_to(50*DOWN)
            second[0].move_to(50*DOWN); second[1].move_to(50*DOWN)
            index = index + 1

class Commutativity(Scene):
    def construct(self):
        caption = TextMobject("Commutativity")
        mult = [ np.pi/2, np.pi, 3*np.pi/2]
        plus_list   =  [scaling_texmobject("$*$", 1.5*LEFT+3*UP, scale_value=1),
                        scaling_texmobject("$=$", 2.7*RIGHT+3*UP, scale_value=1),
                        scaling_texmobject("$*$", 1.5*LEFT+3*DOWN, scale_value=1),
                        scaling_texmobject("$=$", 2.7*RIGHT+3*DOWN, scale_value=1)]

        arrow_1 = [create_arrow(mult_caption[1], 3.5*LEFT+3*UP,  3.5*LEFT+2*UP, color=RED),
                   create_arrow(mult_caption[2], 0.5*RIGHT+3*UP, 0.5*RIGHT+2*UP, color=BLUE),
                   create_arrow(mult_caption[3], 5*RIGHT+3*UP, 5*RIGHT+2*UP, color=YELLOW)]


        arrow_2 = [create_arrow(mult_caption[2], 3.5*LEFT+3*DOWN,  3.5*LEFT+2*DOWN, color=BLUE),
                   create_arrow(mult_caption[1], 0.5*RIGHT+3*DOWN, 0.5*RIGHT+2*DOWN, color=RED),
                   create_arrow(mult_caption[3], 5*RIGHT+3*DOWN, 5*RIGHT+2*DOWN, color=YELLOW)]
        for index,arrows in enumerate(arrow_1):
            self.play(ShowCreation(arrows[0]))
            rotate_arrow(self, arrows[0], mult[index])
            self.play(ShowCreation(arrows[1]))
        [self.play(ShowCreation(operator)) for operator in plus_list[:2]]

        self.wait(2)
        mult_commutative_index = [np.pi, np.pi/2, 3*np.pi/2]
        for index,arrows in enumerate(arrow_2):
            self.play(ShowCreation(arrows[0]))
            rotate_arrow(self, arrows[0], mult_commutative_index[index])
            self.play(ShowCreation(arrows[1]))

        [self.play(ShowCreation(operator)) for operator in plus_list[2:]]
        self.play(ShowCreation(caption))
        self.wait(2)

