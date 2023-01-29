#simulation.py
import pyrosim.pyrosim as pyrosim #import pyrosim
import pybullet as p
import constants as c
import pybullet_data
import time
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)#add gravity
from world import WORLD
from robot import ROBOT
import sensor
import motor
#import robot    #added this to see if refactoring works


class SIMULATION:               #define a class, SIMULATION
    def __init__(self):         #defines the init constructor (AKA method) for the SIMULATION class
        self.world = WORLD()    #creates a new SIMULATION attribute, and that attribute will hold an instance of the WORLD class
        self.robot = ROBOT()    #creates a new SIMULATION attribute, and that attribute will hold an instance of the ROBOT class
        #self.robotID = p.loadURDF("body.urdf") #add a torso to the environment 
        #pyrosim.Prepare_To_Simulate(self.robotID) #pyrosim needs to set up for simulating sensors. robotID contains an integer, indicating which robot you want prepared for simulation

    def Run(self):
        for i in range(c.iterationLength): #for loop going from 0-999, end with colon and make sure next line is indented. don't need an "end" statement because it will end once no longer indented
            #print("iteration number %d" %i)
            p.stepSimulation()
            self.robot.Sense(i)       #call "Sense()" method, so robot can sense some of the changes that have occurred for each time step
            self.robot.Think()         #robot thinks each time step
            self.robot.Act(i)           #Then, act on the changes for each time step
            time.sleep(c.sleepTime)
            
    def Get_Fitness(self):
        self.robot.Get_Fitness()
        
    def __del__(self):      #so far, not calling this, so we are not saving any of our values
        p.disconnect()
