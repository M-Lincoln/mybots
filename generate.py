#generate.py
####to run this, go into terminal: 'python .\generate.py' so that it generates the box.sdf file in the specified path
#use pyrosim to generate a link, store it in a special file called world.sdf, and then simulate.py will read and simulate it 
from tkinter import END
import pyrosim.pyrosim as pyrosim #import pyrosim
length=1
width=1
height=1
xworld=5
yworld=5
zworld=height/2

from Functions import Create_World 
Create_World(xworld,yworld,zworld,width,length,height) #you must put 6 variables into this function from "Functions" otherwise it blows up.

def Generate_Body(width,length,height):
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

def Generate_Brain():
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


	pyrosim.End()

Generate_Body(width,length,height)
Generate_Brain()