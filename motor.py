#motor.py
import numpy
import constants as c
import pyrosim.pyrosim as pyrosim #import pyrosim

class MOTOR:
    def __init__(self,jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.motorValues = numpy.zeros(c.iterationLength)
        self.amplitude = c.amplitude      #property of each motor
        self.frequency = c.frequency      #property of each motor
        self.offset = c.offset            #property of each motor
        x = numpy.linspace(0,2*pi,1000)
        self.motorValues = self.amplitude*(numpy.sin(self.frequency*x+self.offset)) #create an array with sin(x) values 
        #targetAngles_frontleg = c.amplitude_frontleg*(numpy.sin(c.frequency_frontleg*x+c.phaseOffset_frontleg)) #create an array with sin(x) values 
    
    def Set_Value(self):
        ##simulate a motor for joint 'torso_frontleg'
        #pyrosim.Set_Motor_For_Joint(
        #bodyIndex = robotID, #tells simulator what robot the motor should be attached to (which is called 'robot' in this case)
        #jointName = b'torso_frontleg', #tells the simulator what joint the motor should be attached to. in this case, the joint connecting front leg and torso
        #controlMode = p.POSITION_CONTROL, #defines the type of control we are using (either position control or velocity control)
        #targetPosition = targetAngles_frontleg[i], # desired position (desired angle) between the 2 links connected by the joint
        #maxForce = c.defineMaxForce) #cap the total torque used by the motor [500 Nm]
