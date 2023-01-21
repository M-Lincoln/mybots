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
#x = numpy.linspace(0,2*pi,1000)
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



#time.sleep(c.sleepTime) #time.sleep(0.005) is nice viewing time, not too slow
#    print(i) 
#    #to move the camera, control+click and drag with a mouse, or 2-fingered swipe on trackpad for zooming in/out

#print("backLegSensorValues = ",backLegSensorValues) #printing array of backLegSensorValues
#print("frontLegSensorValues = ",frontLegSensorValues) #printing array of frontLegSensorValues
#numpy.save(os.path.join('data','backLegSensorValues'),backLegSensorValues, allow_pickle=False, fix_imports=False) #save an array to a binary file in Numpy, .npy format, in a different folder called "data"
#numpy.save(os.path.join('data','frontLegSensorValues'),frontLegSensorValues, allow_pickle=False, fix_imports=False) #save an array to a binary file in Numpy, .npy format, in a different folder called "data"