# import necessary libraries
from compas.geometry import Frame
from compas.geometry import Point
from compas.geometry import Polygon
from compas.geometry import Polyline
from compas.geometry import Vector

# of course, it's fine to import like below
# import compas.geometry as cg



# Point, Vector & Plane
point  = Point(0, 0, 0)         # Point(x, y, z)
vector = Vector(0, 0, 1)        # Vector(0, 0, 1)

# print variables
print(point)
print(vector)



# Frame
xaxis = [1, 0, 0]                   # define x axis of a frame you want
yaxis = [0, 1, 0]                   # define y axis of a frame you want
frame = Frame(point, xaxis, yaxis)  # Frame(origin, xaxis, yaxis)

# print a variable
print(frame)



# Polyline
p1 = [0, 0, 0]
p2 = [1, 0, 0]
p3 = [1, 1, 0]
p4 = [0, 0, 0]
polyline = Polyline([p1, p2, p3, p4])

# print a variable
print(polyline)



# Polygon
polygon = Polygon([p1, p2, p3])

# print a varialbe
print(polygon)
