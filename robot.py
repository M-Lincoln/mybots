#robot.py
class ROBOT:
    def __init__(self):
        self.sensors = {}   #create an empty dictionary for sensors because we will have multiple sensors for each robot
        self.motors = {}    #create an empty dictionary for motors because we will have multiple motors for each robot
        #pass