#sensor.py
import numpy
import constants as c
class SENSOR:
    def __init__(self, linkName):
     #  self.motor = MOTOR() #create a new SIMULATION attribute, and that attribute will hold an instance of the WORLD class.
     self.linkName = linkName
     self.values = numpy.zeros(c.iterationNum) #creates the zero 
     #print("Zero vectors for sensor values = ",self.values)
     #self.sensor = SENSOR() #don't think we need this???
     def Get_Value(self):
        self.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg") #add a touch sensor to the back leg
        print("backLegTouch sensor value = %d" %self.backLegSensorValues[i]) #print the sensor value of backLegTouch
     
       