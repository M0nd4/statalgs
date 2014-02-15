import random, pylab, math
import numpy as np

def markov_pi(N, delta): 
    x, y = 1.0, 1.0
    n_hits = 0
    for i in range(N):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
            if x**2 + y**2 < 1.0: 
                n_hits += 1
    return n_hits

n_runs = 500
n_trials = 1000
delta = 0.1
for run in range(n_runs):
    print 4.0 * markov_pi(n_trials, delta) / float(n_trials)

# modified to calculate the acceptance ratio: the number of the moves that are not rejected, divided by n_trials. 
n_runs = 500
n_trials = 1000
delta = 0.5
for run in range(n_runs):
    print markov_pi(n_trials, delta) / float(n_trials)

# Run the new program and compute the acceptance ratio for the following values of δ ("delta" in "markov_pi_multirun.py"): δ=0.1, δ=0.2, δ=0.3,..., δ=5.0 . Plot the computed acceptance ratio as a function of δ and submit the plot as a graphics file (pdf, png or jpeg format). Use linear scaling on both axes.
deltas = [i/10.0 for i in range(1, 51)]
rates = []
for d in deltas:
    #print d
    accepted = 0.0
    for run in range(n_runs):
        accepted += markov_pi(n_trials, d) / float(n_trials)
    #print accepted / n_runs
    rates += [accepted / n_runs]

# plot
pylab.plot(deltas, rates, 'o')
# pylab.gca().set_xscale('log')
# pylab.gca().set_yscale('log')
pylab.xlabel('$\delta$')
pylab.ylabel('Acceptance Ratio')
pylab.title('Markov chain algorithm: Acceptance Ratio as a function of $\delta$')
pylab.savefig('acceptance.png')
pylab.show()

# Find delta interval where acceptance rate = 0.5 (interval of 0.1)
low = rates.index([r for r in rates if r < 0.5][0])

# between rates[8] and rates[9]
deltas[8]
deltas[9]

## Now study the performance of  "markov_pi_multirun.py"  as a function of δ. Again, use n_runs = 500 and  n_trials = 1000. 
## Modify the program so that it computes the rms error for values of δ=0.1,δ=0.2, δ=0.3,.... ,δ=5.0 .
n_runs = 500
n_trials = 1000
deltas = [i / 10.0 for i in range(1,51)]
sigmas = []
for d in deltas:
    sigma = 0.0
    for run in range(n_runs):
        pi_est = 4.0 * markov_pi(n_trials, d) / float(n_trials)
        sigma += (pi_est - math.pi) ** 2
    sigmas += [math.sqrt(sigma/(n_runs))]

# Plot the rms error as a function of δ and submit the plot as a graphics file (pdf, png or jpeg format). Note that the rms error gives the actual precision of your calculation, as you compare with the exact mathematical value of π.
pylab.plot(deltas, sigmas, 'o')
# pylab.gca().set_xscale('log')
# pylab.gca().set_yscale('log')
pylab.xlabel('$\delta$')
pylab.ylabel('$\sigma$')
pylab.title('Markov Chain: Standard deviation $\sigma$ as a function of $\delta$')
pylab.savefig('markov_chain_statistical_error.png')
pylab.show()

# 1.  The acceptance rate of 1/2 gives decent accuracy, around 1 standard deviation.  It looks the most accurate prediction is down around 0.2 delta however.
# 2. As delta approaches 0 it accuracy will decrease since the acceptance rate will approach infinity or 0 depending on the initial starting position. As delta approaches infinity the same problem occurs, the acceptance rate will go to 0 and the accuracy will plateau at a value related to the initial starting position since no moves will be accepted.

