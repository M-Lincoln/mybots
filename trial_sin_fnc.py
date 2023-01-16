#trial of simulate.py
from cmath import pi
import pyrosim.pyrosim as pyrosim #import pyrosim
import pybullet as p
import pybullet_data
import time
import numpy
import os #need this to be able to save a variable in another directory/folder
import random #need this package for returning random numbers
import matplotlib.pyplot 
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)#add gravity
planeID=p.loadURDF("plane.urdf") #add a floor to the environment
robotID=p.loadURDF("body.urdf") #add a torso to the environment
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotID) #pyrosim needs to set up for simulating sensors. robotID contains an integer, indicating which robot you want prepared for simulation
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

##closed loop control 
x = numpy.linspace(0,2*pi,1000)
targetAngles = numpy.sin(x) #create an array with sin(x) values 
matplotlib.pyplot.plot(x, targetAngles)
matplotlib.pyplot.xlabel('Angle [rad]')
matplotlib.pyplot.ylabel('sin(x)')
matplotlib.pyplot.axis('tight')
matplotlib.pyplot.show()
print("targetAngles = ",targetAngles) 
