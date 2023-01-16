#constants.py contains all constants going into the script simulate.py
from cmath import pi

#assign how fast the simulation will run (define the sleep time)
assignSleepTime=0.005

#gravity constants
grav_x = 0
grav_y = 0
grav_z = -9.8

#range of numbers being input to sin() function
lowerBound = 0
upperBound = 2*pi

#create sin variables for front and back legs of motor control
amplitude_backleg = pi/4
frequency_backleg = 10
phaseOffset_backleg = 0
amplitude_frontleg = pi/4
frequency_frontleg = 10
phaseOffset_frontleg = 0

#set strength of motor for motor control
maxForceMotor = 35

#number of iterations in the for loop:
iterationNum=1000