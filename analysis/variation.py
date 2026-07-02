import numpy as np

def linear_variation(path):
    increments = np.diff(path)
    return np.sum(increments)

def quadratic_variation(path):
    increments = np.diff(path)
    return np.sum(increments**2)

def n_variation(path):
    increments = np.diff(path)
    return np.sum(increments**3)