import math
from pylab import *
import matplotlib.pyplot as pyplot

def Vol1_s(dimension):
    return (math.pi ** (dimension / 2.0) /
            math.gamma(dimension / 2.0 + 1.0))

# Plot Vol_S(d) for d in 1:100, linear in x, log in y
vols = []
for dimension in range(1, 200):
    vols.append(Vol1_s(dimension))

xs = range(1, 200)

# graphics output
pyplot.plot(xs, vols, marker='.', linestyle='')
pyplot.axes().set_aspect('equal') # set the aspect ratio of the plot
pyplot.title('Hypersphere volume vs dimension')
pyplot.yscale('log')
pyplot.xlabel('Dimension')
pyplot.ylabel('Volume')

pyplot.savefig('nsphere-vol-vs-dim.png')
pyplot.show()
