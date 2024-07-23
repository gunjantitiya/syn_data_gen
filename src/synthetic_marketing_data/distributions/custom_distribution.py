import numpy as np
from scipy import stats

def pareto_spending(size, shape, scale):
    """Generate spending data following a Pareto distribution."""
    return (np.random.pareto(shape, size) + 1) * scale

def poisson_visits(size, lam):
    """Generate website visit data following a Poisson distribution."""
    return np.random.poisson(lam, size)

def normal_age(size, mean=35, std=10):
    """Generate age data following a normal distribution."""
    return np.clip(np.random.normal(mean, std, size), 18, 80).astype(int)

def exponential_time_between_purchases(size, scale=30):
    """Generate time between purchases following an exponential distribution."""
    return np.random.exponential(scale, size)