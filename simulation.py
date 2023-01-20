#simulation.py
from world import WORLD
from robot import ROBOT

class SIMULATION:               #define a class, SIMULATION
    def __init__(self):         #defines the init constructor (AKA method) for the SIMULATION class
        self.world = WORLD()    #creates a new SIMULATION attribute, and that attribute will hold an instance of the WORLD class
        self.robot = ROBOT()    #creates a new SIMULATION attribute, and that attribute will hold an instance of the ROBOT class