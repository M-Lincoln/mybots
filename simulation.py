#simulation.py
class SIMULATION:
    def __init__(self):
        
        import pybullet as p
        import pybullet_data
        #import time
        #import numpy
        import os #need this to be able to save a variable in another directory/folder
        #import random #need this package for returning random numbers
        #import matplotlib.pyplot 
        import constants as c

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.grav_x,c.grav_y,c.grav_z)#add gravity
        
        
      # self.world = WORLD() #create a new SIMULATION attribute, and that attribute will hold an instance of the WORLD class.
       #self.robot = ROBOT() #create a new SIMULATION attribute, and that attribute will hold an instance of the ROBOT class.