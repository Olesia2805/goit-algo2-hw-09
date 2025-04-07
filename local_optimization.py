import random
import math
import numpy as np
import matplotlib.pyplot as plt


# Definition of the Sphere function
def sphere_function(x):
    return sum(xi**2 for xi in x)


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    def get_neighbors(current, step_size=0.1):
        x, y = current
        return [
            [x + step_size, y],
            [x - step_size, y],
            [x, y + step_size],
            [x, y - step_size],
        ]

    current_point = [random.uniform(*bounds[0]), random.uniform(*bounds[1])]
    current_value = func(current_point)

    for _ in range(iterations):
        neighbors = get_neighbors(current_point, epsilon)

        next_point = None
        next_value = np.inf

        for neighbor in neighbors:
            value = func(neighbor)
            if value < next_value:
                next_point = neighbor
                next_value = value

        if next_value >= current_value:
            break

        current_point, current_value = next_point, next_value

    return current_point, current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    pass


# Simulated Annealing
def simulated_annealing(
    func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6
):
    pass


if __name__ == "__main__":
    # Bounds for the function
    bounds = [(-5, 5), (-5, 5)]

    # Execute algorithms
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Solution:", hc_solution, "Value:", hc_value)

    # print("\nRandom Local Search:")
    # rls_solution, rls_value = random_local_search(sphere_function, bounds)
    # print("Solution:", rls_solution, "Value:", rls_value)

    # print("\nSimulated Annealing:")
    # sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    # print("Solution:", sa_solution, "Value:", sa_value)
