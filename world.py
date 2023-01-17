#world.py
class WORLD:
    def __init__(self):
        import pybullet as p
        self.planeID=p.loadURDF("plane.urdf") #add a floor to the environment
        p.loadSDF("world.sdf")