#simulation.py
import pybullet as p
import pyrosim.pyrosim as pyrosim #import pyrosim
import pybullet_data
import time
import numpy
import os #need this to be able to save a variable in another directory/folder
#import random #need this package for returning random numbers
#import matplotlib.pyplot 
import constants as c
from world import WORLD
from robot import ROBOT

class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.grav_x,c.grav_y,c.grav_z)#add gravity
        self.world = WORLD() #create a new SIMULATION attribute, and that attribute will hold an instance of the WORLD class.
        self.robot = ROBOT() #create a new SIMULATION attribute, and that attribute will hold an instance of the ROBOT class.
        

    def Run(self):        
        for i in range(c.iterationNum): #for loop going from 0-999, end with colon and make sure next line is indented. don't need an "end" statement because it will end once no longer indented
            print("loop index variable = ",i)
            p.stepSimulation()
            self.robot.sense() #call the "sense" method in the ROBOT constructor
            
            ###simulate a motor for joint 'torso_backleg'
            #pyrosim.Set_Motor_For_Joint(
            #    bodyIndex = self.robotID, #tells simulator what robot the motor should be attached to (which is called 'robot' in this case)
            #    jointName = b'torso_backleg', #tells the simulator what joint the motor should be attached to. in this case, the joint connecting back leg and torso
            #    controlMode = p.POSITION_CONTROL, #defines the type of control we are using (either position control or velocity control)
            #    targetPosition = self.targetAngles_backleg[i], # desired position (desired angle) between the 2 links connected by the joint
            #    maxForce = c.maxForceMotor) #cap the total torque used by the motor [500 Nm]
            ###simulate a motor for joint 'torso_frontleg'
            #pyrosim.Set_Motor_For_Joint(
            #    bodyIndex = robotID, #tells simulator what robot the motor should be attached to (which is called 'robot' in this case)
            #    jointName = b'torso_frontleg', #tells the simulator what joint the motor should be attached to. in this case, the joint connecting front leg and torso
            #    controlMode = p.POSITION_CONTROL, #defines the type of control we are using (either position control or velocity control)
            #    targetPosition = self.targetAngles_frontleg[i], # desired position (desired angle) between the 2 links connected by the joint
            #    maxForce = c.maxForceMotor) #cap the total torque used by the motor [500 Nm]
            time.sleep(c.assignSleepTime) #time.sleep(0.005) is nice viewing time, not too slow
            #print(i) 
            ##to move the camera, control+click and drag with a mouse, or 2-fingered swipe on trackpad for zooming in/out

    def __del__(self):
        p.disconnect()
    
