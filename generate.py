#generate.py
####to run this, go into terminal: 'python .\generate.py' so that it generates the box.sdf file in the specified path
#use pyrosim to generate a link, store it in a special file called world.sdf, and then simulate.py will read and simulate it 
import pyrosim.pyrosim as pyrosim #import pyrosim
pyrosim.Start_SDF("box.sdf") #tells pyrosim the name of the file where info about the world should be stored (in this case, it's a box)
print("here")
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1]) #stores a box with initial position x=0, y=0, z=0.5 and length, width, and height = 1m, in box.sdf
pyrosim.End() #tells pyrosim to close the sdf file
