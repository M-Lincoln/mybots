##trial of simulate.py
from simulation import SIMULATION
#from cmath import pi
#import pyrosim.pyrosim as pyrosim #import pyrosim
#import pybullet as p
#import pybullet_data
#import time
#import numpy
#import os #need this to be able to save a variable in another directory/folder
#import random #need this package for returning random numbers
#import matplotlib.pyplot 
#import constants as c

#physicsClient = p.connect(p.GUI)
#p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.setGravity(c.grav_x,c.grav_y,c.grav_z)#add gravity
#planeID=p.loadURDF("plane.urdf") #add a floor to the environment
#robotID=p.loadURDF("body.urdf") #add a torso to the environment
#p.loadSDF("world.sdf")
#pyrosim.Prepare_To_Simulate(robotID) #pyrosim needs to set up for simulating sensors. robotID contains an integer, indicating which robot you want prepared for simulation
#backLegSensorValues = numpy.zeros(c.iterationNum)
#frontLegSensorValues = numpy.zeros(c.iterationNum)

###closed loop control 
#x = numpy.linspace(c.lowerBound,c.upperBound,c.iterationNum)
#targetAngles_backleg = c.amplitude_backleg*(numpy.sin(c.frequency_backleg*x+c.phaseOffset_backleg)) #create an array with sin(x) values 
#targetAngles_frontleg = c.amplitude_frontleg*(numpy.sin(c.frequency_frontleg*x+c.phaseOffset_frontleg)) #create an array with sin(x) values 
#print("targetAngles_backleg = ",targetAngles_backleg)
#print("targetAngles_frontleg = ",targetAngles_frontleg) 

##numpy.save(os.path.join('data','targetAngles_backleg'),targetAngles_backleg, allow_pickle=False, fix_imports=False) #save an array to a binary file in Numpy, .npy format, in a different folder called "data"
##numpy.save(os.path.join('data','targetAngles_frontleg'),targetAngles_frontleg, allow_pickle=False, fix_imports=False) #save an array to a binary file in Numpy, .npy format, in a different folder called "data"

##matplotlib.pyplot.plot(x, targetAngles)
##matplotlib.pyplot.xlabel('Angle [rad]')
##matplotlib.pyplot.ylabel('sin(x)')
##matplotlib.pyplot.axis('tight')
##matplotlib.pyplot.show()


#for i in range(c.iterationNum): #for loop going from 0-999, end with colon and make sure next line is indented. don't need an "end" statement because it will end once no longer indented
#    p.stepSimulation()
#    ##add back leg sensor and track values
#    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg") #add a touch sensor to the back leg
#    print("backLegTouch sensor value = %d" %backLegSensorValues[i]) #print the sensor value of backLegTouch
#    ##add front leg sensor and track values
#    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontleg") #add a touch sensor to the front leg
#    print("frontLegTouch sensor value = %d" %frontLegSensorValues[i]) #print the sensor value of frontLegTouch
    
    

#    ##simulate a motor for joint 'torso_backleg'
#    pyrosim.Set_Motor_For_Joint(
#        bodyIndex = robotID, #tells simulator what robot the motor should be attached to (which is called 'robot' in this case)
#        jointName = b'torso_backleg', #tells the simulator what joint the motor should be attached to. in this case, the joint connecting back leg and torso
#        controlMode = p.POSITION_CONTROL, #defines the type of control we are using (either position control or velocity control)
#        targetPosition = targetAngles_backleg[i], # desired position (desired angle) between the 2 links connected by the joint
#        maxForce = c.maxForceMotor) #cap the total torque used by the motor [500 Nm]

#    ##simulate a motor for joint 'torso_frontleg'
#    pyrosim.Set_Motor_For_Joint(
#        bodyIndex = robotID, #tells simulator what robot the motor should be attached to (which is called 'robot' in this case)
#        jointName = b'torso_frontleg', #tells the simulator what joint the motor should be attached to. in this case, the joint connecting front leg and torso
#        controlMode = p.POSITION_CONTROL, #defines the type of control we are using (either position control or velocity control)
#        targetPosition = targetAngles_frontleg[i], # desired position (desired angle) between the 2 links connected by the joint
#        maxForce = c.maxForceMotor) #cap the total torque used by the motor [500 Nm]

#    time.sleep(c.assignSleepTime) #time.sleep(0.005) is nice viewing time, not too slow
#    print(i) 
#    #to move the camera, control+click and drag with a mouse, or 2-fingered swipe on trackpad for zooming in/out
#p.disconnect()
#print("backLegSensorValues = ",backLegSensorValues) #printing array of backLegSensorValues
#print("frontLegSensorValues = ",frontLegSensorValues) #printing array of frontLegSensorValues
#numpy.save(os.path.join('data','backLegSensorValues'),backLegSensorValues, allow_pickle=False, fix_imports=False) #save an array to a binary file in Numpy, .npy format, in a different folder called "data"
#numpy.save(os.path.join('data','frontLegSensorValues'),frontLegSensorValues, allow_pickle=False, fix_imports=False) #save an array to a binary file in Numpy, .npy format, in a different folder called "data"