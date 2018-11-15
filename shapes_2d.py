from vpython import *
"""

"""
class Circle(object):
	
	def __init__(self, radius, position, width=0.01):
		"""
		# Width is needed as Vpython is True 3D and would need to display some width in order to show the circle
		"""
		self.radius = radius
		self.width = width
		if type(position) != "<class 'vpython.cyvector.vector'>" or type(axis) != "<class 'vpython.cyvector.vector'>":
			raise ValueError("Position/Axis is expected to be of type Vector")
		self.position = position
		self.axis = axis


class FilledCircle(object):
	def __init__(self, center=vector(0,0,0), radius=1):
		circle = shapes.circle(radius=radius) # circle is in 2D to display, use extrusion function
		circle_path = [vector(0,0,0),vector(0,0,0.01)] # this take the circle starting at 0,0,0 moving it to 0,0,0.1 filling all the space in between
		self.disk = extrusion(path=circle_path, shape=circle)
		self.disk.color = vector(1.000, 0.522, 0.178)
		self.disk.pos = center
		self.disk.shininess = 0

	def get_circle_obj(self):
		return self.disk