#generate.py
####to run this, go into terminal: 'python .\generate.py' so that it generates the box.sdf file in the specified path
#use pyrosim to generate a link, store it in a special file called world.sdf, and then simulate.py will read and simulate it 

x1=0
y1=0
length=1
width=1
height=1
z1=height/2 #makes it so that the initial position of the box is at ground-level
from Functions import Create_World #I, Noah J Katz, called a function from "Functions", specifically the function from "Functions" was called Create_World.
Create_World(x1,y1,z1,width,length,height) #you must put 6 variables into this function from "Functions" otherwise it blows up.
