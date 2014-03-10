# Compute the Monte Carlo estimate for Vol1_s(20) twenty times, and determine the mean value <Vol1_s(20)>, the mean square <Vol1_s(20)^2>  and the Error = \sqrt{ <Vol1_s(20)^2> - <Vol1_s(20)>^2> } / sqrt{20}. This is your final result, and it only depends on n_trials.

import random
import math

def Vol1_s(dimension):
    return (math.pi ** (dimension / 2.0) /
            math.gamma(dimension / 2.0 + 1.0))

def direct_vol1_s(N, d):
    n_hits = 0
    for i in range(N):
        dims = []
        sum_so_far = 0
        for j in range(d):
            next_dim = random.uniform(-1.0, 1.0)
            sum_so_far += next_dim**2
            if (sum_so_far) >= 1:
                break
            dims.append(random.uniform(-1.0, 1.0))
            if (j == d-1):
                n_hits += 1
    return n_hits

num_trials = [1, 10, 100, 1000, 10000, 100000]
d = 20
vols = []

# Print the table
n_dims = 20
n_trials = 1000000
filename = "vol_sphere_table.txt"
f = open(filename, 'w')
f.write("--------------------------------------------------------\n\
%d trials used for all\n\
d | estimation of Vol1_s(d) | Vol1_s(d) (exact) | n_hits\n\
--------------------------------------------------------\n" % n_trials)
for dim in range(n_dims):
    n_hits = direct_vol1_s(n_trials, dim)
    vol_estimate = (n_hits / float(n_trials)) * 2 ** dim
    vol_exact = Vol1_s(dim)
    f.write("%d\t| %0.3f\t| %0.3f\t| %d\n" %
            (dim, vol_estimate, vol_exact, n_hits))
f.close()
