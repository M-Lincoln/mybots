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
from Functions import Create_World, Create_Robot #I, Noah J Katz, called a function from "Functions", specifically the function from "Functions" was called Create_World.
Create_World(xworld,yworld,zworld,width,length,height) #you must put 6 variables into this function from "Functions" otherwise it blows up.
Create_Robot(x1,y1,z1,width,length,height)
