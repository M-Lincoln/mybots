#trial of simulate.py
import pybullet as p
import time
physicsClient = p.connect(p.GUI)
p.loadSDF("box.sdf") #tells pybullet to read in the world described in box.sdf
for i in range(1000): #for loop going from 0-999, end with colon and make sure next line is indented. don't need an "end" statement because it will end once no longer indented
    p.stepSimulation()
    time.sleep(0.05) #time.sleep(0.005) is nice viewing time, not too slow
    print(i)
    #to move the camera, control+click and drag with a mouse, or 2-fingered swipe on trackpad for zooming in/out
p.disconnect()
