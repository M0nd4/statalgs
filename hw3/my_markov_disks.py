## Modify the algorithm for periodic boundary conditions. Run this algorithm for four disks. Attention: there are no walls and no more wall collisions. Use the modulo operator discussed in this homework's introductory paragraph to ensure that, after each accepted move, x and y positions of each disk are folded back into the interval 0.0 <= x <
import math, random, pylab, os

def show_conf(L, title, fname):
    pylab.axes()
    for [x, y] in L:
        for delx in range(-1, 2):
            for dely in range(-1, 2):
                cir = pylab.Circle((x + delx, y + dely), radius = sigma,  fc = 'r')
                pylab.gca().add_patch(cir)
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.savefig(fname)
    pylab.show()

def dist(x, y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return d_x**2 + d_y**2

N =  64
eta = 0.72
filename = '/home/noah/class/statalgs/hw3/disk_configuration_' + '%.2f' % eta
if os.path.isfile(filename):
    f = open(filename, 'r')
    L = []
    for line in f:
        a, b = line.split()
        L.append([float(a), float(b)])
    f.close()
    print 'starting from file', filename
else:
    N_sqrt = int(math.sqrt(N) + 0.5)
    delxy = 1./ 2. / N_sqrt
    two_delxy = 2.0 * delxy
    L = [ [delxy + i * two_delxy, delxy + j * two_delxy] \
        for i in range(N_sqrt) for j in range(N_sqrt)]
    print 'starting from scratch'
sigma = math.sqrt(eta / N / math.pi)
sigma_sq = sigma ** 2
delta = 0.3 * sigma
n_steps = 10000
for steps in range(n_steps):
    a = random.choice(L)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    min_dist_sq = min(dist(b, c) for c in L if c != a)
    if  min_dist_sq > 4.0 * sigma ** 2:
        a[:] = [b[0] % 1.0, b[1] % 1.0]
show_conf(L, 'N='+str(N)+' $\eta =$'+str(eta), \
          '/home/noah/class/statalgs/hw3/configuration_'+str(N)+'_'+str(eta)+ '.png')
f = open(filename, 'w')
for a in L:
   f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close
