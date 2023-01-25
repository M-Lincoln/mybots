#generate.py
####to run this, go into terminal: 'python .\generate.py' so that it generates the box.sdf file in the specified path
#use pyrosim to generate a link, store it in a special file called world.sdf, and then simulate.py will read and simulate it 
import pyrosim.pyrosim as pyrosim #import pyrosim
length=1
width=1
height=1
x1=0
y1=0
z1=height/2 #makes it so that the initial position of the box is at ground-level
xworld=5
yworld=5
zworld=height/2
from Functions import Create_World #I, Noah J Katz, called a function from "Functions", specifically the function from "Functions" was called Create_World.
def Generate_Body(x1,y1,z1,width,length,height):
	pyrosim.Start_URDF("body.urdf")

	#create a robot with an abdomen and 2 legs:
	pyrosim.Send_Cube(name="torso", pos=[0,0,1.5] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
	#create backleg
	pyrosim.Send_Joint( name = "torso_backleg" , parent= "torso" , child = "backleg" , type = "revolute", position = [-0.5,0,1]) #Joint
	pyrosim.Send_Cube(name="backleg", pos=[-0.5,0,-0.5] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
	#create frontleg
	pyrosim.Send_Joint( name = "torso_frontleg" , parent= "torso" , child = "frontleg" , type = "revolute", position = [0.5,0,1]) #Joint
	pyrosim.Send_Cube(name="frontleg", pos=[0.5,0,-0.5] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf


Create_World(xworld,yworld,zworld,width,length,height) #you must put 6 variables into this function from "Functions" otherwise it blows up.
Generate_Body(x1,y1,z1,width,length,height)
