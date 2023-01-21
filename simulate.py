#trial of simulate.py
from simulation import SIMULATION #Include the SIMULATION class 

#from cmath import pi


#import time
#import numpy

#import random #need this package for returning random numbers
#import matplotlib.pyplot 

simulation = SIMULATION() #Create an object (instance) of the SIMULATION class called 'simulation'
simulation.Run()





###closed loop control 

#print("targetAngles_backleg = ",targetAngles_backleg)
#print("targetAngles_frontleg = ",targetAngles_frontleg) 

##simulate a motor for joint 'torso_backleg'
        #pyrosim.Set_Motor_For_Joint(
        #bodyIndex = robotID, #tells simulator what robot the motor should be attached to (which is called 'robot' in this case)
        #jointName = b'torso_backleg', #tells the simulator what joint the motor should be attached to. in this case, the joint connecting back leg and torso
        #controlMode = p.POSITION_CONTROL, #defines the type of control we are using (either position control or velocity control)
        #targetPosition = targetAngles_backleg[i], # desired position (desired angle) between the 2 links connected by the joint
        #maxForce = c.defineMaxForce) #cap the total torque used by the motor [500 Nm]
        ##simulate a motor for joint 'torso_frontleg'
        #pyrosim.Set_Motor_For_Joint(
        #bodyIndex = robotID, #tells simulator what robot the motor should be attached to (which is called 'robot' in this case)
        #jointName = b'torso_frontleg', #tells the simulator what joint the motor should be attached to. in this case, the joint connecting front leg and torso
        #controlMode = p.POSITION_CONTROL, #defines the type of control we are using (either position control or velocity control)
        #targetPosition = targetAngles_frontleg[i], # desired position (desired angle) between the 2 links connected by the joint
        #maxForce = c.defineMaxForce) #cap the total torque used by the motor [500 Nm]

##numpy.save(os.path.join('data','targetAngles_backleg'),targetAngles_backleg, allow_pickle=False, fix_imports=False) #save an array to a binary file in Numpy, .npy format, in a different folder called "data"
##numpy.save(os.path.join('data','targetAngles_frontleg'),targetAngles_frontleg, allow_pickle=False, fix_imports=False) #save an array to a binary file in Numpy, .npy format, in a different folder called "data"

##matplotlib.pyplot.plot(x, targetAngles)
##matplotlib.pyplot.xlabel('Angle [rad]')
##matplotlib.pyplot.ylabel('sin(x)')
##matplotlib.pyplot.axis('tight')
##matplotlib.pyplot.show()



#time.sleep(c.sleepTime) #time.sleep(0.005) is nice viewing time, not too slow
#    print(i) 
#    #to move the camera, control+click and drag with a mouse, or 2-fingered swipe on trackpad for zooming in/out

#print("backLegSensorValues = ",backLegSensorValues) #printing array of backLegSensorValues
#print("frontLegSensorValues = ",frontLegSensorValues) #printing array of frontLegSensorValues
#numpy.save(os.path.join('data','backLegSensorValues'),backLegSensorValues, allow_pickle=False, fix_imports=False) #save an array to a binary file in Numpy, .npy format, in a different folder called "data"
#numpy.save(os.path.join('data','frontLegSensorValues'),frontLegSensorValues, allow_pickle=False, fix_imports=False) #save an array to a binary file in Numpy, .npy format, in a different folder called "data"