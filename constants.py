#constants.py contains all of the constants being pulled in simulate.py
from cmath import pi

length=1
width=1
height=1
xworld=5
yworld=5
zworld=height/2

#define number of sensor neurons and motor neurons
numSensorNeurons = 8
numMotorNeurons = 7

#create sin variables for front and back legs
amplitude = pi/4 #pi/4 is good
frequency = 10 #10 is good
offset = 0


#iteration range
iterationLength = 1000

#define max force for the motor in the joints
defineMaxForce = 35

#define the sleep time for the simulation
sleepTime=0.005 #1/60 is better for longer simulation but not too long

#define the number of Generations for evolution:
numberOfGenerations = 10

#define size of population:
populationSize = 10