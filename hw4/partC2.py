# Modify your program of section B (if necessary) to run 
# in high dimensions: Each iteration should take a constant 
# number of operations, independent of d:
# Dont compute squared sum each time, keep a sum_so_far and add/subtract
# as needed
# Store calculations for d = 1,2,3, ...
import random
import math
from pylab import *
import matplotlib.pyplot as pyplot

def Vol1_s(dimension):
    return (math.pi ** (dimension / 2.0) /
            math.gamma(dimension / 2.0 + 1.0))

n_trials = 40000
dim = 200
ratios = []
vols = []
for d in range(1, dim):
    n_hits = 0
    x = [0]*d
    Q = 0
    sum_so_far = 0
    for i in range(n_trials):
        k = random.randint(0, d - 1)
        x_new_k = x[k] + random.uniform(-1.0, 1.0)
        prev_square = x[k]**2
        new_sum = sum_so_far - prev_square + x_new_k**2
        x_supp = random.uniform(-1.0, 1.0)
        if (new_sum < 1):
            x[k] = x_new_k
            n_hits += 1
            sum_so_far = new_sum
        if (sum_so_far + x_supp**2 < 1):
            Q += 1
    ratios.append(2 * (Q / float(n_trials)))
    
# prepend Vol1_s(1)
ratios = [Vol1_s(1) + ratios]

# graphics output
pyplot.plot(xs, vols, marker='.', linestyle='')
pyplot.axes().set_aspect('equal') # set the aspect ratio of the plot
pyplot.title('Hypersphere volume vs dimension')
pyplot.yscale('log')
pyplot.xlabel('Dimension')
pyplot.ylabel('Volume')

pyplot.savefig('nsphere-vol-vs-dim.png')
pyplot.show()

# values for Vol1_s(5), Vol1_s(20), Vol1_s(200)
Vol1_s(5)
Vol1_s(20)
Vol1_s(200)
