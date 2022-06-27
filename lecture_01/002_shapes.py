from compas.geometry import Box
from compas.geometry import Circle
from compas.geometry import Cylinder
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Sphere

# Box
b1 = Box(Frame.worldXY(), 5, 1, 3)          # xsize, ysize, zsize
b2 = Box.from_width_height_depth(5, 3, 1)   # width=xsize, height=zsize, depth=ysize
print(b1==b2)
print(b1)
print(b2)

# Sphere
s1 = Sphere([0, 0, 0], 5)  # Sphere(center, radius)
print(s1)

# Cylinder
plane = Plane([0, 0, 0], [0, 0, 1]) # Plane(origin, normal)
circle = Circle(plane, 5)           # Circle(center, radius)
c1 = Cylinder(circle, height=4)     # Cylinder(base, height)
print(c1)
