import numpy as np
from utils.helpers import euclidean_distance
# --------------------------------------------------
# Neighborhood Selection
# --------------------------------------------------
# Purpose:
# Identify neighboring turtles based on spatial proximity.
def compute_distance_matrix(positions: np.ndarray) -> np.ndarray:
    N = positions.shape[0]
    distance_matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            dist = euclidean_distance(positions[i], positions[j])
            distance_matrix[i, j] = dist
            distance_matrix[j, i] = dist
    return distance_matrix



def get_neighbors(i, positions, alpha, k_min):

    distance_matrix= compute_distance_matrix(positions)
    N=positions.shape[0]
    D_max=np.max(distance_matrix)
    r=D_max*alpha
    neightbors=[j for j in range(N) if j!=i and distance_matrix[i,j] < r]
    if len(neightbors)<k_min:
        sorted_indices=np.argsort(distance_matrix[i])
        neightbors=sorted_indices[1:k_min+1].tolist()
    return neightbors
# Concept:
# Each turtle interacts only with nearby turtles (local awareness).
#
# Distance:
# d(i, j) = ||X_i - X_j||_2
#
# Neighborhood Definition:
# neighbors_i = { j | d(i, j) < r }
#
# Where:
# r = alpha * D_max
# D_max = maximum pairwise distance in population
#
# Constraint:
# Ensure at least k_min neighbors (fallback to closest ones if needed)
#
# Output:
# List of indices of neighboring turtles
