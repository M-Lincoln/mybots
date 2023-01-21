#sensor.py
import numpy
import constants as c
class SENSOR:
    def __init__(self,linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.iterationLength)    #create an empty zero vector for all sensor values to populate
        print("sensor values = ",self.values)