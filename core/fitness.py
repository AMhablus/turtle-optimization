import numpy as np

def objective_function(x: np.ndarray, mode: str = "sphere") -> float:
    """
    Computes fitness based on selected benchmark function.
    x: (dim,) vector
    mode: function name
    Returns scalar fitness (minimization)
    """

    if mode == "sphere":
        # Sphere: f(x) = sum(x_i^2)
        # Convex, unimodal → easy test (min at 0)
        return float(np.sum(x ** 2))

    elif mode == "rosenbrock":
        # Rosenbrock: f(x) = sum[(1 - x_i)^2 + 100(x_{i+1} - x_i^2)^2]
        # Narrow curved valley → tests path-following (min at 1)
        return float(np.sum((1 - x) ** 2 + 100 * (x[1:] - x[:-1]**2) ** 2))

    elif mode == "rastrigin":
        # Rastrigin: f(x) = 10n + sum[x_i^2 - 10cos(2πx_i)]
        # Many local minima → tests exploration (min at 0)
        return float(10 * len(x) + np.sum(x ** 2 - 10 * np.cos(2 * np.pi * x)))

    elif mode == "ackley":
        # Ackley: multimodal with flat regions
        # Tests robustness against local minima (min at 0)
        return float(
            20
            - 20 * np.exp(-0.2 * np.sqrt(np.mean(x ** 2)))
            - np.exp(np.mean(np.cos(2 * np.pi * x)))
        )

    else:
        raise ValueError("Unknown objective function mode")