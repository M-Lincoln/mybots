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
