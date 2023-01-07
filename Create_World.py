def Create_World():
	from operator import length_hint
	import pyrosim.pyrosim as pyrosim #import pyrosim
	pyrosim.Start_SDF("world.sdf") #tells pyrosim the name of the file where info about the world should be stored (in this case, it's a box)
	pyrosim.Send_Cube(name="Box", pos=[x1,y1,z1] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in boxes.sdf
	pyrosim.End() #tells pyrosim to close the sdf file