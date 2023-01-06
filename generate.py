#generate.py
####to run this, go into terminal: 'python .\generate.py' so that it generates the box.sdf file in the specified path
#use pyrosim to generate a link, store it in a special file called world.sdf, and then simulate.py will read and simulate it 
import pyrosim.pyrosim as pyrosim #import pyrosim
pyrosim.Start_SDF("boxes.sdf") #tells pyrosim the name of the file where info about the world should be stored (in this case, it's a box)
print("here")
length=1
width=1
height=1
x1=0
y1=0
z1=height/2 #makes it so that the initial position of the box is at ground-level
x2=length #makes it so that the box is staggered
y2=0  
z2=z1+height #initially on top of the first box
for j in range(10):
    s=str(j) #assign box # per iterations
    pyrosim.Send_Cube(name="Box"+s, pos=[x1,y1,z1] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in boxes.sdf
    ### NEED TO EDIT### z1=(2*z1)+z1 #update the starting height position of the box, st they stack on top of each other
#pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in boxes.sdf
pyrosim.End() #tells pyrosim to close the sdf file
