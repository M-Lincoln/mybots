import sys      #we will use this to extract command line arguments
from simulation import SIMULATION #Include the SIMULATION class 

directOrGUI = sys.argv[1]       #are we viewing the simulation in GUI or is it hiding?
solutionID = sys.argv[2]        #which solution ID is it? parent? child? which one
simulation = SIMULATION(directOrGUI,solutionID) #Create an object (instance) of the SIMULATION class called 'simulation'
simulation.Run()
simulation.Get_Fitness(solutionID)    #call Get_Fitness
