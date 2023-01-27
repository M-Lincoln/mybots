#robot.py
import pyrosim.pyrosim as pyrosim #import pyrosim
import pybullet as p
import sensor
import motor
import numpy
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self):
        self.motors = {}    #create an empty dictionary for motors because we will have multiple motors for each robot
        self.robotID = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotID)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()           
        self.nn = NEURAL_NETWORK("brain.nndf")      #create a neural network (self.nn) and add any neurons and synapses to it from brain.nndf

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
            self.motors[jointName] = motor.MOTOR(jointName)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Act(self,i):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                print(neuronName)
                print(jointName)
        #for motor in self.motors:
        #     self.motors[motor].Set_Value(robot,i)
        