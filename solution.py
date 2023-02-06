#solution.py
import pyrosim.pyrosim as pyrosim #import pyrosim
import numpy
import constants as c
import os
import time



class SOLUTION:
	def __init__(self,nextAvailableID):
		self.myID = nextAvailableID
		self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons)     #create a matrix filled with random numbers b/w 0 and 1. If you want the weight of the synapse that connects the third sensor neuron to the second motor neuron, for example, you would "walk down" to the third row, and then "walk right" to the second column.
		self.weights = 2*self.weights-1          #shift range of random numbers to [-1,1]
		
	def Start_Simulation(self,directOrGUI):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		os.system("start /B python .\simulate.py " + directOrGUI + " " + str(self.myID))	#causes simulate.py to run in the background while search.py continues to run w/out waiting for simulate.py to finish

	def Wait_For_Simulation_To_End(self):
		fitnessFileName = "fitness" + str(self.myID) + ".txt"
		while not os.path.exists(fitnessFileName):	#checks if the fitnessx.txt file exists. if not, it sleeps search.py for 1/100 of a second if that file can't be found. waiting for other portion of code to catch up
			time.sleep(0.01)
		fitnessFile = open("fitness" + str(self.myID) +".txt","r")
		self.fitness = float(fitnessFile.read())	#convert the incoming string to a float
		#print("For Solution " + str(self.myID) + ":")
		#print("fitness value = ", self.fitness)
		fitnessFile.close()
		#print("del fitness" + str(self.myID) + ".txt")
		os.system("del fitness" + str(self.myID) + ".txt")	               #delete the fitnessx.txt file after it has been read, so we don't clutter our directory

	def Mutate(self):
		randomRow = numpy.random.randint(0,c.numMotorNeurons)
		randomColumn = numpy.random.randint(0,1)
		self.weights[randomRow,randomColumn] = numpy.random.random()*2-1		#specifies a random element in self.weights (the weight of the synapse that connects the randomRow'th sensor neuron to the randomColumn'th motor neuron.)

	def Set_ID(self,ID):
		self.myID = ID

	def Create_World(self):
		pyrosim.Start_SDF("world.sdf") #tells pyrosim the name of the file where info about the world should be stored (in this case, it's a box)
		pyrosim.Send_Cube(name="Box", pos=[c.xworld,c.yworld,c.zworld] , size=[c.width,c.length,c.height]) #stores a box with initial position x, y, z and length, width, and height, in boxes.sdf
		pyrosim.End() #tells pyrosim to close the sdf file

	def Create_Body(self):
		pyrosim.Start_URDF("body.urdf")
		#create a robot with an abdomen:
		pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[c.width,c.length,c.height]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
		
		#create backleg
		pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0") #Joint
		pyrosim.Send_Cube(name="Backleg", pos=[0,-0.5,0] , size=[0.2,1,0.2]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
		#create BackLowerLeg
		pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "Backleg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0") #Joint
		pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
		
		#create frontleg
		pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0") #Joint
		pyrosim.Send_Cube(name="Frontleg", pos=[0,0.5,0] , size=[0.2,1,0.2]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
		#create FrontLowerLeg
		pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "Frontleg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0") #Joint
		pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1]) 
		
		#create leftleg
		pyrosim.Send_Joint( name = "Torso_Leftleg" , parent= "Torso" , child = "Leftleg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0") #Joint
		pyrosim.Send_Cube(name="Leftleg", pos=[-0.5,0,0] , size=[1,0.2,0.2]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
		#create LowerLeftLeg
		pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "Leftleg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0") #Joint
		pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

		#create rightleg
		pyrosim.Send_Joint( name = "Torso_Rightleg" , parent= "Torso" , child = "Rightleg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0") #Joint
		pyrosim.Send_Cube(name="Rightleg", pos=[0.5,0,0] , size=[1,0.2,0.2]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
		#create LowerRightLeg
		pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "Rightleg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0") #Joint
		pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
		pyrosim.End()

	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")		#creating a unique brain for each child and parent
		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso") #sensor neurons receive values from sensors. This neuron will receive a value from sensor stored in torso.
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")	#sensor neuron attached to touch sensor in back leg
		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")	#sensor neuron attached to touch sensor in front leg
		pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "Leftleg")	#sensor neuron attached to touch sensor in left leg
		pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "BackLowerLeg")
		pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg")
		pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "LeftLowerLeg")
		pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "RightLowerLeg")

		pyrosim.Send_Motor_Neuron(name = 8 , jointName = "Torso_Backleg")	#motor neuron will send values to the motor controlling joint torso_backleg
		pyrosim.Send_Motor_Neuron(name = 9 , jointName = "Torso_Frontleg")
		pyrosim.Send_Motor_Neuron(name = 10 , jointName = "Torso_Leftleg")
		pyrosim.Send_Motor_Neuron(name = 11 , jointName = "BackLeg_BackLowerLeg")
		pyrosim.Send_Motor_Neuron(name = 12 , jointName = "FrontLeg_FrontLowerLeg")
		pyrosim.Send_Motor_Neuron(name = 13 , jointName = "LeftLeg_LeftLowerLeg")
		pyrosim.Send_Motor_Neuron(name = 14 , jointName = "RightLeg_RightLowerLeg")

		for currentRow in range(c.numSensorNeurons):
			for currentColumn in range(c.numMotorNeurons):
				pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName= currentColumn + c.numSensorNeurons , weight=2*numpy.random.random()-1)	#generate a synapse b/w the ith sensor neuron and the jth motor neuron between range -1,1)

		pyrosim.End()
		