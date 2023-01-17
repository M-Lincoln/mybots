#robot.py
class ROBOT:
    def __init__(self):
        import pybullet as p
        import pyrosim.pyrosim as pyrosim #import pyrosim
        
        self.robotID=p.loadURDF("body.urdf") #add a torso to the environment
        pyrosim.Prepare_To_Simulate(self.robotID) #pyrosim needs to set up for simulating sensors. robotID contains an integer, indicating which robot you want prepared for simulation

    def sensors(self):
        self.sensors = SENSORS() #create a new SIMULATION attribute, and that attribute will hold an instance of the ROBOT class.
        pass
    def motors(self):
        self.motors = MOTORS() #create a new SIMULATION attribute, and that attribute will hold an instance of the ROBOT class.
        pass