# Generalize markov_pi.py to implement a Markov-chain Monte Carlo
# algorithm to sample point inside the d-dimensional unit hypersphere:

import random
import math

d = 2
n_trials = 40000
n_hits = 0
x = [0]*d
for i in range(n_trials):
    k = random.randint(0, d - 1)
    x_new_k = x[k] + random.uniform(-1.0, 1.0)
    if (sum([x[side]**2 for side in range(len(x)) if side != k]) +
            x_new_k**2 < 1):
        x[k] = x_new_k
        n_hits += 1

print n_hits


# print 4.0 * n_hits / float(n_trials)
# Compute the mean value of r^2 = x[0] **2 + x[1] ** 2. 
# In d=2, this value should be equal to 1/2.

means = []
for i in range(100):
    x = [0]*d
    for i in range(n_trials):
        k = random.randint(0, d - 1)
        x_new_k = x[k] + random.uniform(-1.0, 1.0)
        if (sum([x[side]**2 for side in range(len(x)) if side != k]) +
                x_new_k**2 < 1):
            x[k] = x_new_k
            n_hits += 1
    means.append((x[0]**2 + x[1]**2))
print sum(means) / 100.0

# Comes out t0 1/2
