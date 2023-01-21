#robot.py
import pyrosim.pyrosim as pyrosim #import pyrosim
import pybullet as p
import sensor
class ROBOT:
    def __init__(self):
        self.motors = {}    #create an empty dictionary for motors because we will have multiple motors for each robot
        self.robotID = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotID)
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.sensors = {}   #create an empty dictionary for sensors because we will have multiple sensors for each robot
        for linkName in pyrosim.linkNamesToIndices:
            print(linkName)
            self.sensors[linkName] = sensor.SENSOR(linkName) #try this so we can initiate a sensor instance