#sensor.py
import numpy
import constants as c
import pyrosim.pyrosim as pyrosim #import pyrosim
class SENSOR:
    def __init__(self, linkName):
     #  self.motor = MOTOR() #create a new SIMULATION attribute, and that attribute will hold an instance of the WORLD class.
     self.linkName = linkName
     self.values = numpy.zeros(c.iterationNum) #creates the zero 
     #print("Zero vectors for sensor values = ",self.values)
     #self.sensor = SENSOR() #don't think we need this???

    def Get_Value(self):
        self.values = pyrosim.Get_Touch_Sensor_Value_For_Link("self.linkName") #store the values in self.values, using self.linkName to know which link to extract touch sensor values from
        print("link %s sensor value = %d", self.linkName, self.values) #print the sensor value of backLegTouch
     
       