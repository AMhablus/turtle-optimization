# --------------------------------------------------
# Neighborhood Selection
# --------------------------------------------------
# Purpose:
# Identify neighboring turtles based on spatial proximity.
#
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