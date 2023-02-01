#robot.py
import pyrosim.pyrosim as pyrosim #import pyrosim
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import numpy
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    def __init__(self,solutionID):
        self.motors = {}    #create an empty dictionary for motors because we will have multiple motors for each robot
        self.robotID = p.loadURDF("body.urdf")      #"body.urdf" is the unique ID of a body in the simulation
        pyrosim.Prepare_To_Simulate(self.robotID)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()           
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")      #create a neural network (self.nn) and add any neurons and synapses to it from brain(solutionID).nndf
        os.system("del brain" + str(solutionID) + ".nndf")	               #delete the nndf file after it has been read, so we don't clutter our directory

    def Prepare_To_Sense(self):
        self.sensors = {}   #create an empty dictionary for sensors because we will have multiple sensors for each robot
        for linkName in pyrosim.linkNamesToIndices:
            #print(linkName)
            self.sensors[linkName] = SENSOR(linkName) #try this so we can initiate a sensor instance

    def Sense(self,i):    #enable sensing in the robot
         for sensor in self.sensors:
             self.sensors[sensor].Get_Value(i)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            #print(jointName)
            self.motors[jointName] = MOTOR(jointName)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Act(self,desiredAngle):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_of(neuronName)
                jointNameByte = bytes(jointName, "utf-8")
                self.motors[jointNameByte].Set_Value(desiredAngle,self.robotID)
                #print(neuronName)
                #print(jointName)
                #print(desiredAngle)           
        
    def Get_Fitness(self,solutionID):
        stateOfLinkZero = p.getLinkState(self.robotID,0)        #first argument = body ID of a body in the simulation, second argument = particular link we are interested in. First link = "0"
        positionOfLinkZero = stateOfLinkZero[0]                 #extract 1st tuple = position of the link
        xCoordinateOfLinkZero = positionOfLinkZero[0]           #extract the x coordinate of the link's position
        f = open("temp" + solutionID + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        #os.system("rename temp"+ str(solutionID) +".txt fitness" + str(solutionID) +".txt")
        os.rename("temp" +str(solutionID)+ ".txt" ,"fitness"+str(solutionID)+".txt")
        
        #print("stateOfLinkZero = ", stateOfLinkZero)            
        #print("positionOfLinkZero = ", positionOfLinkZero) 
        #print("X coord OfLinkZero = ", xCoordinateOfLinkZero)
        