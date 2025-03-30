import numpy as np
from scipy.optimize import fsolve

def find_max_value(x):
    """
    Finds the maximum value of a function f(x) = x^2 - 4x + 3.
    
    Parameters:
        x (float): The variable for which to find the maximum value.

    Returns:
        float: The maximum value of the function.
    """
    f_x = x**2 - 4*x + 3
    return fsolve(f_x, 2.5)

max_value = find_max_value(0)
print("The maximum value is:", max_value)
