# data_N20.py
import numpy as np
import math

# ==========================
# DATASET METADATA
# ==========================
N = 20
cities = np.random.rand(N, 2) * 100 #city coordinats

# ==========================
# DISTANCE FUNCTIONS
# ==========================
def dist(i, j):
    return math.dist(cities[i], cities[j])

dist_matrix = [
    [dist(i, j) for j in range(N)]
    for i in range(N)
]

# ==========================
# TOUR COST
# ==========================
def tour_cost(tour):
    return sum(
        dist(tour[i], tour[(i + 1) % len(tour)])
        for i in range(len(tour))
    )

