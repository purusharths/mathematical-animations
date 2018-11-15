from vpython import *

class Create_Axis:
    """
    Create x,y,z axis
    PS: Z axis projecting out of the screen
    """
    def __init__(self, color, opacity, distance = 5, radius=0.05,label=False, sw=0.05, hw=0.2, hl=0.3):
        self.color = color
        if label == True:
            pass
        else:
            arrow(pos=vector(-distance,0,0), axis=(vector(2*distance,0,0)), # x-axis
            radius=radius,color=self.color,opacity=opacity, shaftwidth=0.05, headwidth=0.2, headlength=0.3)

            arrow(pos=vector(0,-distance,0), axis=(vector(0,2*distance,0)), # y-axis
            radius=radius,color=self.color,opacity=opacity, shaftwidth=0.05, headwidth=0.2, headlength=0.3)

            arrow(pos=vector(0,0,-distance),axis=(vector(0,0,2*distance)), # z-axis
            radius=radius,color=self.color, opacity=opacity, shaftwidth=0.05, headwidth=0.2, headlength=0.3)

    def draw_axis_planes(self,plane_size, plane_width, opacity, plane):
        plane_size = plane_size*2
        if plane == 'xy':
            axis = vector(1,0,0)
            size = vector(plane_size, plane_size, plane_width)
        if plane == "yz":
            pass
        if plane == "zx":
            pass
        mybox = box(pos=vector(0,0,0), axis=axis, size=size,  opacity=opacity)



# testing 
if __name__ == '__main__':
    xyz = Create_Axis(color.yellow, opacity=0.9)
    xyz.draw_axis_planes(plane = 'xy', plane_size=5, plane_width=0.01, opacity=0.3)
    # pointer = arrow(pos=vec(0,2,1),axis_and_length=vec(5,0,0) )
# pointer = points(pos=vec(5, 0, 0), radius=3)  # z-axis comes out of the screen
 