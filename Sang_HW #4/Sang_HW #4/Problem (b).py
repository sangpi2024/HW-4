from scipy.optimize import fsolve
import numpy as np

def root_equation1(x):
    """
    Calculate the left-hand side of the first equation: x - 3cos(x).

    Parameters:
    x : float or ndarray
        The value(s) at which to evaluate the function.

    Returns:
    float or ndarray
        The result of the function x - 3cos(x) for the given x.
    """
    return x - 3 * np.cos(x)

def root_equation2(x):
    """
    Calculate the left-hand side of the second equation: cos(2x) * x^3.

    Parameters:
    x : float or ndarray
        The value(s) at which to evaluate the function.

    Returns:
    float or ndarray
        The result of the function cos(2x) * x^3 for the given x.
    """
    return np.cos(2 * x) * x**3

# Initial guess for the root of the first equation
initial_guess_1 = 1
# Solve the first equation using fsolve
root1 = fsolve(root_equation1, initial_guess_1)

# Initial guesses for the root of the second equation (excluding x=0)
# We choose these initial guesses based on the periodicity of the cosine function.
initial_guesses_2 = [np.pi / 4, 3 * np.pi / 4]
# Solve the second equation for each initial guess
roots2 = [fsolve(root_equation2, guess) for guess in initial_guesses_2]

# Check if the functions intersect by comparing the roots
# Note: We are rounding the results to 4 decimal places for comparison.
intersection = set(np.round(root1, 4)) & set(np.round(np.concatenate(roots2), 4))

# Output the results
print(f"Root of the first equation: {root1}")
print(f"Roots of the second equation (excluding x=0): {roots2}")
print(f"Do the functions intersect? {'Yes' if intersection else 'No'}")
if intersection:
    print(f"Point of intersection: {intersection}")
