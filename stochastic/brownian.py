"""
This file generates Brownian motion paths

"""

import numpy as np

def generate_brownian(T=1.0, n=1000, seed=None):
    if seed is not None:
        np.random.seed(seed)

    dt = T / n
    increments = np.random.normal(
        loc=0,
        scale=np.sqrt(dt),
        size=n,
    )
    B = np.concatenate(([0], np.cumsum(increments)))
    t = np.linspace(0, T, n + 1)

    return t, B
