from core.optimizer import optimize
from core.fitness import objective_function
import config

x_best, f_best = optimize(config.N, config.dim, config.bounds, config.T, objective_function, config.parameters)
print("Best solution:", x_best)
print("Best fitness:", f_best)