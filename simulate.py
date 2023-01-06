#trial of simulate.py
import pybullet as p
import time
physicsClient = p.connect(p.GUI)
for i in range(1000): #for loop going from 0-999, end with colon and make sure next line is indented. don't need an "end" statement because it will end once no longer indented
    p.stepSimulation()
    time.sleep(0.005)
    print(i)
p.disconnect()
