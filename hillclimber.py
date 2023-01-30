#hillclimber.py
from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()        #create an instance of SOLUTION

    def Evolve(self):
        self.parent.Evaluate()
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)     #self.child will receive a copy of self.parent's weights, as well as its fitness.

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        #print("parent's fitness = ", self.parent.fitness)
        #print("child's fitness = ", self.child.fitness)
        if self.child.fitness>self.parent.fitness:      #replace the parent with its child if the parent does worse
            self.parent = self.child
