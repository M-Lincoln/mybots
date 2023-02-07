#constants.py contains all of the constants being pulled in simulate.py
from cmath import pi

length=1
width=1
height=1
xworld=5
yworld=5
zworld=height/2

#define number of sensor neurons and motor neurons
numSensorNeurons = 2
numMotorNeurons = 3

#create motor joint angle range for the legs' joints:
motorJointRange = 0.5

#create sin variables for legs
amplitude = pi #pi/4 is good
frequency = 10 #10 is good
offset = 0


#iteration range
iterationLength = 1000

#define max force for the motor in the joints
defineMaxForce = 35 #35 works

#define the sleep time for the simulation
sleepTime=1/60 #1/60 is better for longer simulation but not too long. 0.005 is quick

#define the number of Generations for evolution:
numberOfGenerations = 10

#define size of population:
populationSize = 10