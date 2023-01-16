#analyze.py
import numpy
backLegSensorValues = numpy.load('data/backLegSensorValues.npy',mmap_mode ='r', allow_pickle= False, fix_imports = False) #load data/backLegSensorValues.npy (for reading only = 'mmap_mode = r' into the vector backLegSensorValues.
print("backLegSensorValues = ",backLegSensorValues) #printing array of backLegSensorValues