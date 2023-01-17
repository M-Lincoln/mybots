#robot.py
class ROBOT:
    def __init__(self):
        import pybullet as p
        import pyrosim.pyrosim as pyrosim #import pyrosim
        self.robotID=p.loadURDF("body.urdf") #add a torso to the environment
        pyrosim.Prepare_To_Simulate(self.robotID) #pyrosim needs to set up for simulating sensors. robotID contains an integer, indicating which robot you want prepared for simulation