import random, math, pylab

def direct_pi(N):
    n_hits = 0
    for i in range(N):
        x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
        if x ** 2 + y ** 2 < 1.0:
            n_hits += 1
    return n_hits

n_runs = 500
n_trials_list = []
sigmas = []
for poweroftwo in range(4, 13):
    n_trials = 2 ** poweroftwo
    sigma = 0.0
    for run in range(n_runs):
        pi_est = 4.0 * direct_pi(n_trials) / float(n_trials)
        sigma += (pi_est - math.pi) ** 2
    sigmas.append(math.sqrt(sigma/(n_runs)))
    n_trials_list.append(n_trials)

pylab.plot(n_trials_list, sigmas, 'o')
pylab.gca().set_xscale('log')
pylab.gca().set_yscale('log')
pylab.xlabel('n_trials')
pylab.ylabel('$\sigma$')
pylab.title('Direct sampling: Standard deviation $\sigma$ as a function of n_trials')
pylab.savefig('direct_sampling_statistical_error.png')
pylab.show()

# Estimate the proportionality constant relating the number of trials to the rms errors
slope = (math.log(sigmas[0]) - math.log(sigmas[len(sigmas) - 1])) / (math.log(n_trials_list[0]) - math.log(n_trials_list[len(n_trials_list) - 1]))

# alpha ~ 0.5, such that rms error = n_trials ** -alpha
