#search.py alternately generates and simulates robots with different sets of synaptic weights
import os
from hillclimber import HILL_CLIMBER

#for index in range(5):
#    os.system("python .\generate.py")
#    os.system("python .\simulate.py")
#    index=index+1

hc = HILL_CLIMBER()
hc.Evolve()     #call Evolve() 
hc.Show_Best()