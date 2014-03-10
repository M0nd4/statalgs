# Compute the Monte Carlo estimate for Vol1_s(20) twenty times, and determine the mean value <Vol1_s(20)>, the mean square <Vol1_s(20)^2>  and the Error = \sqrt{ <Vol1_s(20)^2> - <Vol1_s(20)>^2> } / sqrt{20}. This is your final result, and it only depends on n_trials.

import random
import math

def Vol1_s(dimension):
    return (math.pi ** (dimension / 2.0) /
            math.gamma(dimension / 2.0 + 1.0))

num_trials = [1, 10, 100, 1000, 10000, 100000]
d = 20
vols = []
for n_trials in num_trials:
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
