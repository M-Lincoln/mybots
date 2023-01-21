#motor.py
import numpy
import constants as c

class MOTOR:
    def __init__(self,jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.motorValues = numpy.zeros(c.iterationLength)
        self.amplitude = c.amplitude      #property of each motor
        self.frequency = c.frequency      #property of each motor
        self.offset = c.offset            #property of each motor
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
    