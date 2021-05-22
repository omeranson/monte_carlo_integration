import math
import random

def monte_carlo_definite_integral(f, low, high, n):
    sum_ = 0
    sum_sqrd = 0
    range_size = high - low
    for _ in range(n):
        x = random.uniform(low, high)
        y = f(x)
        sum_ += y
        sum_sqrd += y*y
    mean = sum_/n
    return range_size*mean, math.sqrt(range_size*range_size*(sum_sqrd - n*mean*mean)/(n*(n-1)))
