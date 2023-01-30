import sys      #we will use this to extract command line arguments
from simulation import SIMULATION #Include the SIMULATION class 

directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI) #Create an object (instance) of the SIMULATION class called 'simulation'
simulation.Run()
simulation.Get_Fitness()    #call Get_Fitness
