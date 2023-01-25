#sensor.py
import pyrosim.pyrosim as pyrosim #import pyrosim
import numpy
import constants as c
import os
import robot #try to save sensor values

class SENSOR:
    def __init__(self,linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.iterationLength)    #create an empty zero vector for all sensor values to populate
        
    def Get_Value(self,i):
        ##add back leg sensor and track values
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName) #add a touch sensor to the specific linkName
        if i == c.iterationLength-1:
            print(self.values) #print the sensor values of all sensors at the last time step
            self.Save_Values() #once the sensor vector is filled, save each vector to its own file
    
    def Save_Values(self):
        ###NEED TO WORK ON THIS MORE###
        #save sensor values
        for linkName in pyrosim.linkNamesToIndices:
            numpy.save(os.path.join('data','SensorValues_%s' %linkName),self.values, allow_pickle=False, fix_imports=False) #save an array to a binary file in Numpy, .npy format, in a different folder called "data"
        