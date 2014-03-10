# Extend the python program of section B2:
# Complement the random sample x_0...x_{d-1} in the d-dimensional
# hypersphere to a random sample in the (d+1)-dimensional unit
# HYPERCYLINDER, by simply drawing one additional random number
# x_supp = random.uniform(-1.0, 1.0).

# Now, define an observable Q
# Q = 1 if  x_0^2 + .... + x_{d - 1} ^2 + x_supp ^2 < 1
# Q = 0 otherwise.
import random
import math

d = 2
n_trials = 40000
n_hits = 0
x = [0]*d
Q = 0
for i in range(n_trials):
    k = random.randint(0, d - 1)
    x_new_k = x[k] + random.uniform(-1.0, 1.0)
    x_supp = random.uniform(-1.0, 1.0)
    if (sum([x[side]**2 for side in range(len(x)) if side != k]) +
            x_new_k**2 < 1):
        x[k] = x_new_k
        n_hits += 1
    if (sum([x[side]**2 for side in range(len(x))]) +
            x_supp**2 < 1):
        Q += 1

def Vol1_s(dimension):
    return (math.pi ** (dimension / 2.0) /
            math.gamma(dimension / 2.0 + 1.0))

# Show 2 * <Q> = Vol1_s(d + 1) / Vol1_s(d)
print 2 * (Q / float(n_trials))
print Vol1_s(d+1) / Vol1_s(d)
