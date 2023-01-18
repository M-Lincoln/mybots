import pyrosim.pyrosim as pyrosim #import pyrosim
def Create_World(x1,y1,z1,width,length,height):
	pyrosim.Start_SDF("world.sdf") #tells pyrosim the name of the file where info about the world should be stored (in this case, it's a box)
	pyrosim.Send_Cube(name="Box", pos=[x1,y1,z1] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in boxes.sdf
	pyrosim.End() #tells pyrosim to close the sdf file

def Create_Robot(x1,y1,z1,width,length,height):
	pyrosim.Start_URDF("body.urdf")

	#create a robot with an abdomen and 2 legs:
	pyrosim.Send_Cube(name="torso", pos=[1.5,0,1.5] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
	#create backleg
	pyrosim.Send_Joint( name = "torso_backleg" , parent= "torso" , child = "backleg" , type = "revolute", position = [1,0,1]) #Joint
	pyrosim.Send_Cube(name="backleg", pos=[-0.5,0,-0.5] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
	#create frontleg
	pyrosim.Send_Joint( name = "torso_frontleg" , parent= "torso" , child = "frontleg" , type = "revolute", position = [2,0,1]) #Joint
	pyrosim.Send_Cube(name="frontleg", pos=[0.5,0,-0.5] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf


	#archway of cubes joined by revolute joints
	#pyrosim.Send_Cube(name="link0", pos=[x1,y1,z1] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
	#pyrosim.Send_Joint( name = "link0_link1" , parent= "link0" , child = "link1" , type = "revolute", position = [0,0,1])
	#pyrosim.Send_Cube(name="link1", pos=[0,0,.5] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
	## add link 2 
	#pyrosim.Send_Joint( name = "link1_link2" , parent= "link1" , child = "link2" , type = "revolute", position = [0,0,1])
	#pyrosim.Send_Cube(name="link2", pos=[0,0,.5] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
	## add link 3
	#pyrosim.Send_Joint( name = "link2_link3" , parent= "link2" , child = "link3" , type = "revolute", position = [0.5,0,0.5])
	#pyrosim.Send_Cube(name="link3", pos=[0.5,0,0] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
	## add link 4
	#pyrosim.Send_Joint( name = "link3_link4" , parent= "link3" , child = "link4" , type = "revolute", position = [1,0,0])
	#pyrosim.Send_Cube(name="link4", pos=[0.5,0,0] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
	## add link 5
	#pyrosim.Send_Joint( name = "link4_link5" , parent= "link4" , child = "link5" , type = "revolute", position = [0.5,0,-0.5])
	#pyrosim.Send_Cube(name="link5", pos=[0,0,-0.5] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
	## add link 6
	#pyrosim.Send_Joint( name = "link5_link6" , parent= "link5" , child = "link6" , type = "revolute", position = [0,0,-1])
	#pyrosim.Send_Cube(name="link6", pos=[0,0,-0.5] , size=[width,length,height]) #stores a box with initial position x, y, z and length, width, and height, in body.urdf
	pyrosim.End()