"""There are several ways to construct a `Rotation`.
"""
import math

from compas.geometry import Frame
from compas.geometry import Rotation

R = Rotation.from_axis_and_angle([1, 0, 0], math.radians(30))
R = Rotation.from_axis_and_angle([1, 0, 0], math.radians(30), point=[1, 0, 0])
R = Rotation.from_frame(Frame([1, 1, 1], [0.68, 0.68, 0.27], [-0.67, 0.73, -0.15]))
R = Rotation.from_euler_angles([1.4, 0.5, 2.3], static=True, axes='xyz')

print(R)
