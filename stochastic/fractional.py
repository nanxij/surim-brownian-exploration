"""
fractional.py

Simulation of fractional Brownian motion using the covariance matrix method.
"""

import numpy as np


def covariance_matrix(t, H):
    n = len(t)
    Sigma = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            # defined by the adjusted min expression
            Sigma[i, j] = 0.5 * (
                t[i] ** (2 * H)
                + t[j] ** (2 * H)
                - abs(t[i] - t[j]) ** (2 * H)
            )

    return Sigma


def generate_fractional(H, T=1.0, n=500, seed=None):

    if not (0 < H < 1):
        raise ValueError("H must satisfy 0 < H < 1.")

    if seed is not None:
        np.random.seed(seed)

    t = np.linspace(0, T, n + 1)

    Sigma = covariance_matrix(t, H)

    # Numerical stabilization
    Sigma += 1e-12 * np.eye(n + 1)

    B = np.random.multivariate_normal(
        mean=np.zeros(n + 1),
        cov=Sigma
    )

    return t, B