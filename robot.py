#robot.py
class ROBOT:
    def __init__(self):
        import pybullet as p
        import pyrosim.pyrosim as pyrosim #import pyrosim
        
        self.robotID=p.loadURDF("body.urdf") #add a torso to the environment
        pyrosim.Prepare_To_Simulate(self.robotID) #pyrosim needs to set up for simulating sensors. robotID contains an integer, indicating which robot you want prepared for simulation

    def Prepare_To_Sense(self):
        from sensor import SENSOR
        import pyrosim.pyrosim as pyrosim #import pyrosim
        self.sensors = {} #create an empty dictionary 
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName) #this results in the SENSOR's constructor being called 3 times. EAch time, it returns an instance of SENSOR. That instance is stored as an entry in the self.sensors dictionary. The key for each dictionary entry is the name of the link that stores that sensor


    
    #self.motors = {} #create an empty dictionary
        
    