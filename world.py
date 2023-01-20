#world.py
import pybullet as p
class WORLD:
    def __init__(self):
        self.planeID=p.loadURDF("plane.urdf") #add a floor to the environment
        p.loadSDF("world.sdf")