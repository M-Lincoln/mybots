#world.py
class WORLD:
    def __init__(self):
        import pybullet as p
        #import pyrosim.pyrosim as pyrosim #import pyrosim
        #import pybullet_data
        #import time
        #import numpy
        #import os #need this to be able to save a variable in another directory/folder
        ##import random #need this package for returning random numbers
        ##import matplotlib.pyplot 
        ##import constants as c
        self.planeID=p.loadURDF("plane.urdf") #add a floor to the environment
        p.loadSDF("world.sdf")