#motor.py
import numpy
import constants as c
import pyrosim.pyrosim as pyrosim #import pyrosim
import pybullet as p

class MOTOR:
    def __init__(self,jointName):
        self.jointName = jointName
       

    def Set_Value(self,desiredAngle, RobotID):
        ##simulate a motor for joint
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = RobotID, #tells simulator what robot the motor should be attached to (which is called 'robot' in this case)
        jointName = self.jointName, #tells the simulator what joint the motor should be attached to. in this case, the joint connecting front leg and torso
        controlMode = p.POSITION_CONTROL, #defines the type of control we are using (either position control or velocity control)
        targetPosition = desiredAngle, # desired position (desired angle) between the 2 links connected by the joint
        maxForce = c.defineMaxForce) #cap the total torque used by the motor [500 Nm]
        