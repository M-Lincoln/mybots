#analyze.py
import matplotlib.pyplot
import numpy
backLegSensorValues = numpy.load('data/backLegSensorValues.npy',mmap_mode ='r', allow_pickle= False, fix_imports = False) #load data/backLegSensorValues.npy (for reading only = 'mmap_mode = r' into the vector backLegSensorValues.
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy',mmap_mode ='r', allow_pickle= False, fix_imports = False) #load data/frontLegSensorValues.npy (for reading only = 'mmap_mode = r' into the vector frontLegSensorValues.
print("backLegSensorValues = ",backLegSensorValues) #printing array of backLegSensorValues
print("frontLegSensorValues = ",frontLegSensorValues) #printing array of frontLegSensorValues

matplotlib.pyplot.plot(backLegSensorValues) #plot the values of backLegSensorValues array
matplotlib.pyplot.plot(frontLegSensorValues) #plot the values of frontLegSensorValues array

matplotlib.pyplot.show() #show the above plot