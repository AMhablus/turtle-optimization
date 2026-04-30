# --------------------------------------------------
# Compute Direction function
# --------------------------------------------------
# Purpose:
# Move toward the average position of neighbors.
#
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
#
# Output:
# Direction vector of shape (dim,)




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