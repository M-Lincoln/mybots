#simulation.py
import pyrosim.pyrosim as pyrosim #import pyrosim
import pybullet as p
import constants as c
import pybullet_data
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)#add gravity
from world import WORLD
from robot import ROBOT

class SIMULATION:               #define a class, SIMULATION
    def __init__(self):         #defines the init constructor (AKA method) for the SIMULATION class
        self.world = WORLD()    #creates a new SIMULATION attribute, and that attribute will hold an instance of the WORLD class
        self.robot = ROBOT()    #creates a new SIMULATION attribute, and that attribute will hold an instance of the ROBOT class
        self.robotID = p.loadURDF("body.urdf") #add a torso to the environment 
        pyrosim.Prepare_To_Simulate(self.robotID) #pyrosim needs to set up for simulating sensors. robotID contains an integer, indicating which robot you want prepared for simulation

    def Run(self):
        for i in range(c.iterationLength): #for loop going from 0-999, end with colon and make sure next line is indented. don't need an "end" statement because it will end once no longer indented
            print("iteration number ", i)
        #p.stepSimulation()
        ##add back leg sensor and track values
        #backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg") #add a touch sensor to the back leg
        #print("backLegTouch sensor value = %d" %backLegSensorValues[i]) #print the sensor value of backLegTouch
        ##add front leg sensor and track values
        #frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontleg") #add a touch sensor to the front leg
        #print("frontLegTouch sensor value = %d" %frontLegSensorValues[i]) #print the sensor value of frontLegTouch
        ##simulate a motor for joint 'torso_backleg'
        #pyrosim.Set_Motor_For_Joint(
        #bodyIndex = robotID, #tells simulator what robot the motor should be attached to (which is called 'robot' in this case)
        #jointName = b'torso_backleg', #tells the simulator what joint the motor should be attached to. in this case, the joint connecting back leg and torso
        #controlMode = p.POSITION_CONTROL, #defines the type of control we are using (either position control or velocity control)
        #targetPosition = targetAngles_backleg[i], # desired position (desired angle) between the 2 links connected by the joint
        #maxForce = c.defineMaxForce) #cap the total torque used by the motor [500 Nm]
        ##simulate a motor for joint 'torso_frontleg'
        #pyrosim.Set_Motor_For_Joint(
        #bodyIndex = robotID, #tells simulator what robot the motor should be attached to (which is called 'robot' in this case)
        #jointName = b'torso_frontleg', #tells the simulator what joint the motor should be attached to. in this case, the joint connecting front leg and torso
        #controlMode = p.POSITION_CONTROL, #defines the type of control we are using (either position control or velocity control)
        #targetPosition = targetAngles_frontleg[i], # desired position (desired angle) between the 2 links connected by the joint
        #maxForce = c.defineMaxForce) #cap the total torque used by the motor [500 Nm]
