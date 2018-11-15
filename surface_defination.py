import time
import numpy as np

from vpython import *
from housekeeping_axis3d import Create_Axis
from shapes_2d import FilledCircle

def get_cirlce(radius, origin, dtheta, frame=100):
	R = radius
	t = np.linspace(0,np.pi*2,dtheta)
	circ = [vector(R*np.cos(angle), R*np.sin(angle), 0) for angle in t]

	for i in range(1,len(circ)+1):
		time.sleep(0.1)
		##print(circ[:i])
		circle = curve(circ[:i], color=color.red, origin=origin)
	return circle

def rise_above(obj, height, dx):
	i = 0
	while i<height:
		rate(100)
		obj.pos.z = obj.pos.z + dx
		i=i+0.1

scene = canvas(width=1600, height=900)
L = 50
scene.center = vec(0.05*L,0.2*L,0)
scene.range = 1.3*L
# scene.camera.pos = vector(5,-5,5)
# scene.camera.axis = vector(-10,0,-3)

# c.lights = []
# lamp=local_light( pos=vector(0.88,-0.22,-0.44), color=color.gray(0.8))
xyz = Create_Axis(color.yellow, opacity=0.8)
xyz.draw_axis_planes(plane = 'xy', plane_size=5, plane_width=0.01, opacity=0.3)

circle = get_cirlce(0.2, vector(1.001,2.001,0), 25)
print(circle)
time.sleep(2)


c = FilledCircle(center=vector(1,2,0), radius=0.2)
c = c.get_circle_obj()
circle.visible = False

time.sleep(2)

ball=sphere(pos=vec(1,2,3), size=vec(0.4,0.4,0.4))
ball.shininess = 0; ball.color = vector(0.513, 0.756, 0.403)

rise_above(c,5.9,0.05)

time.sleep(1)

r = ring(pos=vector(-1,2,5),
        axis=vector(0,0,1),
        radius=2, thickness=1.2)
r.shininess = 0; r.color = color.cyan#vector(1, 0.945, 0.7137)

# while ball.pos.z != 7.6:
# rate(30)
rise_above(ball, 6.3, 0.05)
time.sleep(2)
c.color = vector(0.5450,0.2705, 0.76)
rise_above(c,6.3,0.05)
time.sleep(1)

ball.visible = False


# while ball.pos.z > 	0:
# 	rate(100)
# 	ball.pos.z = ball.pos.z-0.1
# while ball.pos.z 
print("Done")




# todo
# animate the circle - done
# take off the circle and put in extrusion -done
# animate the surface
# project the circle outward and make it a sphere -done
# take the sphere to the surface and remove the other third dimension.
