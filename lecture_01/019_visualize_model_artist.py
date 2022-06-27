from compas.artists import Artist
from compas.robots import RobotModel
import os

here = os.path.dirname(os.path.abspath(__file__))
path_urdf = os.path.join(here, "models/01_myfirst.urdf")
print(path_urdf)

model = RobotModel.from_urdf_file(path_urdf)

artist = Artist(model, layer="Robot")
artist.clear_layer()
artist.draw_visual()
artist.redraw()
