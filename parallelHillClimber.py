#parallelHillClimber.py
from solution import SOLUTION
import constants as c
import copy
import simulation

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}        #create an empty dictionary to store multiple random parents for our parallel hillclimber
        for parent in range(c.populationSize):
            self.parents[parent]=SOLUTION()


    def Evolve(self):
        for parent in self.parents:
            self.parents[parent].Evaluate("GUI")        #Evaluate each of the parents, one after the other

        #for currentGeneration in range(c.numberOfGenerations): 
        ##for currentGeneration in range(3):  #view behavior of the FIRST randomly generated solution
        #    self.Evolve_For_One_Generation()
        pass

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)     #self.child will receive a copy of self.parent's weights, as well as its fitness.

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.child.fitness<self.parent.fitness:      #replace the parent with its child if the parent does worse
            self.parent = self.child

    def Print(self):
        print("parent's fitness = ", self.parent.fitness, "; child's fitness = ", self.child.fitness)       #print the fitness of parent and child
        
    def Show_Best(self):
        #self.parent.Evaluate("GUI")     #try to evaluate the parent with graphics turned on
        pass