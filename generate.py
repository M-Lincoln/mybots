#generate.py
####to run this, go into terminal: 'python .\generate.py' so that it generates the box.sdf file in the specified path
#use pyrosim to generate a link, store it in a special file called world.sdf, and then simulate.py will read and simulate it 
from operator import length_hint
import pyrosim.pyrosim as pyrosim #import pyrosim
pyrosim.Start_SDF("boxes.sdf") #tells pyrosim the name of the file where info about the world should be stored (in this case, it's a box)
print("here")
x1=0
y1=0
length=1
width=1
height=1
z1=height/2 #makes it so that the initial position of the box is at ground-level
pyrosim.Send_Cube(name="Box", pos=[x1,y1,z1] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in boxes.sdf

pyrosim.End() #tells pyrosim to close the sdf file
