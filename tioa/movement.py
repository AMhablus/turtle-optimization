import numpy as np

# --------------------------------------------------
# Compute Direction function
# --------------------------------------------------
# Purpose:
# Move toward the average position of neighbors.


# Equation:
# D_i = mean(X_neighbors) - X_i
#
# Where:
# X_neighbors = positions of neighboring turtles
# X_i = current turtle position
#
# Intuition:
# - If neighbors are better → move toward them
# - Encourages local convergence
#
# Edge Case:
# If no neighbors → return zero vector

# Output:
# Direction vector of shape (dim,)
def compute_direction(i, neighbors, positions):

    if len(neighbors) == 0:
        return np.zeros_like(positions[i])

    X_i = positions[i]                  # shape (dim,)
    X_neighbors = positions[neighbors]  # shape (k, dim)

    mean_neighbors = np.mean(X_neighbors, axis=0)

    D_i = mean_neighbors - X_i

    return D_i




# --------------------------------------------------
# Compute Migration function
# --------------------------------------------------
# Purpose:
# Pull turtle toward best-known solutions.
#
# Equation:
# M_i = μ (X_best - X_i) + ν (X_pbest - X_i)
#
# Where:
# X_best  = global best position
# X_pbest = personal best position of turtle i
# μ       = global influence coefficient
# ν       = personal influence coefficient
#
# Intuition:
# - Global term → convergence toward best solution
# - Personal term → memory of good past positions
#
# Output:
# Migration vector of shape (dim,)

def compute_migration(x_i, X_best, pbest_positions, i, mu, nu):
     X_pbest = pbest_positions[i]
     M_i = (mu*(X_best - x_i)) + (nu* (X_pbest - x_i))
     return M_i


# --------------------------------------------------
# Compute Update function
# --------------------------------------------------
# Purpose:
# Combine all movement components into final displacement.
#
# Equation:
# ΔX_i = S_i * D_i + E_i * R_i + M_i
#
# Final Position:
# X_i_new = X_i + ΔX_i
#
# Where:
# S_i = step size (PAS)
# D_i = direction vector
# E_i = exploration factor (TDE)
# R_i = random vector
# M_i = migration vector
#
# Intuition:
# - S_i * D_i → local exploitation
# - E_i * R_i → exploration
# - M_i       → global guidance
#
# Output:
# ΔX_i (vector of shape (dim,))

def compute_update(x_i, S_i, D_i, E_i, R_i, M_i):
    delta_X = (S_i * D_i) + (E_i * R_i) + M_i
    return delta_X
