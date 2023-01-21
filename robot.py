#robot.py
import pyrosim.pyrosim as pyrosim #import pyrosim
import pybullet as p
import sensor
import numpy
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

    def Sense(self,i):    #enable sensing in the robot
         for sensor in self.sensors:
             self.sensors[sensor].Get_Value(i)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            print(jointName)

    def Act(self,i):
        for motor in self.motors:
             self.motors[motor].Set_Value(i)
        