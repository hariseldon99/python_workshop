# estimate pi using the monte carlo method concurrently
import numpy as np
from math import pi
from multiprocessing import Pool
 
# monte carlo simulation of points in a quadrant within unit square
def task(n):
    # generate random points
    points = np.random.rand(n,2)
    # count the number of points in the circle
    return sum([1 for x,y in points if (x**2 + y**2) < 1])
 
# entry point
if __name__ == '__main__':
    # define the number of processes
    nprocs = 12
    # define number of points per process
    n = int(5E6)
    # create the process pool
    with Pool(nprocs) as p:
        # submit tasks
        total_in_quadrant = sum(p.map(task, [n]*nprocs))
    # estimate pi
    pi_estimate = total_in_quadrant / (nprocs * n) * 4
    print(f'pi (estimate):\t{pi_estimate}')
    print(f'pi (actual):\t{pi}')
