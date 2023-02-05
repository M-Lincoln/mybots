#parallelHillClimber.py
from solution import SOLUTION
import constants as c
import copy
import os
import simulation

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")    #delete all remaining fitness and brain files in case of any previous crashes
        os.system("del fitness*.txt")
        self.nextAvailableID = 0
        self.parents = {}        #create an empty dictionary to store multiple random parents for our parallel hillclimber
        for parent in range(c.populationSize):
            self.parents[parent]=SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID+1       #increment nextAvailableID by 1 after using it for one SOLUTION


    def Evolve(self):
        for parent in self.parents:
            self.parents[parent].Start_Simulation("GUI")        #Evaluate each of the parents, one after the other
        for parent in self.parents:        #activating parallelism in Evolve()
            self.parents[parent].Wait_For_Simulation_To_End()
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations): 
        #for currentGeneration in range(3):  #view behavior of the FIRST randomly generated solution
            self.Evolve_For_One_Generation()
        

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        

    def Spawn(self):
        self.children = {}      #create an empty dictionary for children
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(parent)     #self.children will receive a copy of its parent's weights, as well as its fitness.
            print("Self.children[parent]= ", self.children[parent])
            self.children[parent]=SOLUTION(self.nextAvailableID)
            self.nextAvailableID=self.nextAvailableID+1 #increment up for the next available ID

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Select(self):
        for parent in self.parents:
            if self.children[parent].fitness<self.parents[parent].fitness:      #replace the parent with its child if the parent does worse
                self.parents[parent] = self.children[parent]

    def Print(self):
        print(" ")
        for parent in self.parents:
            print("parent's fitness = ", self.parents[parent].fitness, "; child's fitness = ", self.children[parent].fitness)       #print the fitness of parent and child
            print(" ")
    def Show_Best(self):
        #self.parent.Evaluate("GUI")     #try to evaluate the parent with graphics turned on
        pass

    def Evaluate(self,solutions):
        for parent in solutions:
            solutions[parent].Start_Simulation("DIRECT")        #Evaluate each of the parents, one after the other
        for parent in solutions:        #activating parallelism in Evolve()
            solutions[parent].Wait_For_Simulation_To_End() 