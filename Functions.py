import pyrosim.pyrosim as pyrosim #import pyrosim
def Create_World(x1,y1,z1,width,length,height):
	pyrosim.Start_SDF("world.sdf") #tells pyrosim the name of the file where info about the world should be stored (in this case, it's a box)
	pyrosim.Send_Cube(name="Box", pos=[x1,y1,z1] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in boxes.sdf
	pyrosim.End() #tells pyrosim to close the sdf file

def Create_Robot(x1,y1,z1,width,length,height):
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name="link0", pos=[x1,y1,z1] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in boxes.sdf
	pyrosim.Send_Joint( name = "link0_link1" , parent= "link0" , child = "link1" , type = "revolute", position = [0,0,1])
	pyrosim.Send_Cube(name="link1", pos=[0,0,.5] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in boxes.sdf
	####start adding link 2 and beyond
	pyrosim.End()