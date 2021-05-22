import random

def monte_carlo_definite_integral(f, low, high, n):
    result = 0
    for _ in range(n):
        x = random.uniform(low, high)
        result += f(x)
    return (high-low)*result/n
