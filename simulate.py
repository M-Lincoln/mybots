#trial of simulate.py
import pyrosim.pyrosim as pyrosim #import pyrosim
import pybullet as p
import pybullet_data
import time
import numpy
import os #need this to be able to save a variable in another directory/folder
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)#add gravity
planeID=p.loadURDF("plane.urdf") #add a floor to the environment
robotID=p.loadURDF("body.urdf") #add a torso to the environment
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotID) #pyrosim needs to set up for simulating sensors. robotID contains an integer, indicating which robot you want prepared for simulation
backLegSensorValues = numpy.zeros(1000)
for i in range(1000): #for loop going from 0-999, end with colon and make sure next line is indented. don't need an "end" statement because it will end once no longer indented
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg") #add a touch sensor to the back leg
    print("backLegTouch sensor value = %d" %backLegSensorValues[i]) #print the sensor value of backLegTouch
    time.sleep(.005) #time.sleep(0.005) is nice viewing time, not too slow
    print(i) 
    #to move the camera, control+click and drag with a mouse, or 2-fingered swipe on trackpad for zooming in/out
p.disconnect()
print("backLegSensorValues = ",backLegSensorValues) #printing array of backLegSensorValues
numpy.save(os.path.join('data','backLegSensorValues'),backLegSensorValues, allow_pickle=True, fix_imports=False) #save an array to a binary file in Numpy, .npy format, in a different folder called "data"