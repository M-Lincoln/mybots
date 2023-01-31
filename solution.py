#solution.py
import pyrosim.pyrosim as pyrosim #import pyrosim
import numpy
import constants as c
import os



class SOLUTION:
	def __init__(self):
		self.weights = numpy.random.rand(3,2)     #create a 3x2 matrix filled with random numbers b/w 0 and 1. If you want the weight of the synapse that connects the third sensor neuron to the second motor neuron, for example, you would "walk down" to the third row, and then "walk right" to the second column.
		self.weights = 2*self.weights-1          #shift range of random numbers to [-1,1]

	def Evaluate(self,directOrGUI):
		self.Create_World(c.xworld,c.yworld,c.zworld,c.width,c.length,c.height)
		self.Create_Body(c.width,c.length,c.height)
		self.Create_Brain()
		os.system("python .\simulate.py "+ directOrGUI)
		fitnessFile = open("fitness.txt","r")
		self.fitness = float(fitnessFile.read())	#convert the incoming string to a float
		fitnessFile.close()

	def Mutate(self):
		randomRow = numpy.random.randint(0,2)
		randomColumn = numpy.random.randint(0,1)
		self.weights[randomRow,randomColumn] = numpy.random.random()*2-1		#specifies a random element in self.weights (the weight of the synapse that connects the randomRow'th sensor neuron to the randomColumn'th motor neuron.)

	def Create_World(self,x1,y1,z1,width,length,height):
		pyrosim.Start_SDF("world.sdf") #tells pyrosim the name of the file where info about the world should be stored (in this case, it's a box)
		pyrosim.Send_Cube(name="Box", pos=[x1,y1,z1] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in boxes.sdf
		pyrosim.End() #tells pyrosim to close the sdf file
	def Create_Body(self,width,length,height):
		pyrosim.Start_URDF("body.urdf")
		#create a robot with an abdomen and 2 legs:
		pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
		#create backleg
		pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [-0.5,0,1]) #Joint
		pyrosim.Send_Cube(name="Backleg", pos=[-0.5,0,-0.5] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
		#create frontleg
		pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [0.5,0,1]) #Joint
		pyrosim.Send_Cube(name="Frontleg", pos=[0.5,0,-0.5] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
		pyrosim.End()

	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain.nndf")
		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso") #sensor neurons receive values from sensors. This neuron will receive a value from sensor stored in torso.
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")	#sensor neuron attached to touch sensor in back leg
		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")	#sensor neuron attached to touch sensor in front leg

		pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Torso_Backleg")	#motor neuron will send values to the motor controlling joint torso_backleg
		pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_Frontleg")

		pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName=3 , weight=1.0)	#generate a synapse b/w the torso sensor and the torso_backleg motor
		pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName=3 , weight=2.0)	#generate a synapse b/w the backleg sensor and the torso_backleg motor
		pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName=4 , weight=1.0)	#generate a synapse b/w the torso sensor and the torso_frontleg motor
		pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName=4 , weight=0.25)	#generate a synapse b/w the frontleg sensor and the torso_frontleg motor
		pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName=4 , weight=0.25)	#generate a synapse b/w the backleg sensor and the torso_frontleg motor
		pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName=3 , weight=0.25)	#generate a synapse b/w the frontleg sensor and the torso_backleg motor

		for i in range(3):
			for j in range(3,5):
				pyrosim.Send_Synapse( sourceNeuronName = i , targetNeuronName= j , weight=2*numpy.random.random()-1)	#generate a synapse b/w the ith sensor neuron and the jth motor neuron between range -1,1)

		pyrosim.End()