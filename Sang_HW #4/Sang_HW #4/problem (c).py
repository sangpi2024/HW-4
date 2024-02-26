import numpy as np
from scipy.linalg import solve

def solve_linear_system(coefficients, constants):
    """
    Solves a linear system of equations.

    This function takes a 2D array 'coefficients' where each row represents the coefficients of the variables
    in one equation of the system, and a 1D array 'constants' which represents the constant terms of the equations.

    Args:
        coefficients (np.ndarray): A 2D array of shape (n, n) representing the coefficients matrix.
        constants (np.ndarray): A 1D array of shape (n,) representing the constants vector.

    Returns:
        np.ndarray: A 1D array containing the solutions to the system of linear equations.
    """
    # Use SciPy's `solve` function to find the solution to the system of linear equations
    solution = solve(coefficients, constants)
    return solution

# Define the coefficients for the first set of linear equations
coefficients_1 = np.array([
    [3, 1, -1],
    [1, 4, 1],
    [2, 1, 2]
])

# Define the constants for the first set of linear equations
constants_1 = np.array([2, 12, 10])

# Call the function to solve the first system of equations
solution_1 = solve_linear_system(coefficients_1, constants_1)

# Output the solution for the first system
print("Solution for the first system of equations:")
print(solution_1)

# Define the coefficients for the second set of linear equations
coefficients_2 = np.array([
    [1, -10, 2, 4],
    [3, 1, 4, 12],
    [9, 2, 3, 4],
    [-1, 2, 7, 3]
])

# Define the constants for the second set of linear equations
constants_2 = np.array([2, 12, 21, 37])

# Call the function to solve the second system of equations
solution_2 = solve_linear_system(coefficients_2, constants_2)

# Output the solution for the second system
print("\nSolution for the second system of equations:")
print(solution_2)
