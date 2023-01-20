#simulation.py
import pyrosim.pyrosim as pyrosim #import pyrosim
import pybullet as p
import pybullet_data
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)#add gravity
from world import WORLD
from robot import ROBOT

class SIMULATION:               #define a class, SIMULATION
    def __init__(self):         #defines the init constructor (AKA method) for the SIMULATION class
        self.world = WORLD()    #creates a new SIMULATION attribute, and that attribute will hold an instance of the WORLD class
        self.robot = ROBOT()    #creates a new SIMULATION attribute, and that attribute will hold an instance of the ROBOT class
        self.robotID = p.loadURDF("body.urdf") #add a torso to the environment 
        pyrosim.Prepare_To_Simulate(self.robotID) #pyrosim needs to set up for simulating sensors. robotID contains an integer, indicating which robot you want prepared for simulation