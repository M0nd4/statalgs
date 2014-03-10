import random
import math


# Generalize the program direct_pi_multirun.py from d-2 dimensions
# into a python program in d dimensions. This allows you to sample points
# in the d-dimensional unit hypercube and to compute Vol1_s(d)/Vol1_cube(d)
# from the ratio of hits to trials.
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

# Print the table
n_dims = 13
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
