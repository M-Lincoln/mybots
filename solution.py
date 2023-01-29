#solution.py
import numpy

class SOLUTION:
    def __init__(self):
        self.weights = numpy.random.rand(3,2)     #create a 3x2 matrix filled with random numbers b/w 0 and 1. If you want the weight of the synapse that connects the third sensor neuron to the second motor neuron, for example, you would "walk down" to the third row, and then "walk right" to the second column.
        self.weights = 2*self.weights -1          #shift range of random numbers to [-1,1]
 