#search.py alternately generates and simulates robots with different sets of synaptic weights
import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

#for index in range(5):
#    os.system("python .\generate.py")
#    os.system("python .\simulate.py")
#    index=index+1

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()     #call Evolve() 
phc.Show_Best()