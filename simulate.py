##trial of simulate.py
from world import WORLD
from robot import ROBOT
from simulation import SIMULATION


simulation = SIMULATION() #create an object (an instance of the SIMULATION class) called simulation
simulation.Run()
world = WORLD() #create an object (an instance of the SIMULATION class) called simulation
robot = ROBOT() #create an object (an instance of the SIMULATION class) called simulation

#from robot import ROBOT
#from world import WORLD
#from cmath import pi

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




#print("backLegSensorValues = ",backLegSensorValues) #printing array of backLegSensorValues
#print("frontLegSensorValues = ",frontLegSensorValues) #printing array of frontLegSensorValues
#numpy.save(os.path.join('data','backLegSensorValues'),backLegSensorValues, allow_pickle=False, fix_imports=False) #save an array to a binary file in Numpy, .npy format, in a different folder called "data"
#numpy.save(os.path.join('data','frontLegSensorValues'),frontLegSensorValues, allow_pickle=False, fix_imports=False) #save an array to a binary file in Numpy, .npy format, in a different folder called "data"