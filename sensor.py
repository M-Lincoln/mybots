#sensor.py
import numpy
import constants as c
class SENSOR:
    def __init__(self, linkName):
     #  self.motor = MOTOR() #create a new SIMULATION attribute, and that attribute will hold an instance of the WORLD class.
     self.linkName = linkName
     self.values = numpy.zeros(c.iterationNum) #creates the zero vector
     #self.sensor = SENSOR() #don't think we need this???
     
       