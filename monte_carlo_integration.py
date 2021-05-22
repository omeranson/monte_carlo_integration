import numpy as np
import numpy.random

rng = np.random.default_rng()


def monte_carlo_definite_integral(f, low, high, n):
    xs = rng.uniform(low, high, n)
    f_v = np.vectorize(f)
    ys = f_v(xs)
    mean = np.mean(ys)
    std = np.std(ys, ddof=1)
    range_size = high - low
    return range_size*mean, range_size*std/np.sqrt(n-1)
