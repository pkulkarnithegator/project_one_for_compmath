import numpy as np
def left_endpoint(x_vals: np.ndarray, func: np.ufunc) -> float:
    """
    author: Logan Mitchell
    :param x_vals: np.ndarray
    :param func: np.ufunc
    :return: left_riemann_sum
    Multiplies function values at left endpoint with width and then sums that value
    """
    width = np.diff(x_vals)
    left = func(x_vals[:-1])
    product = left * width
    left_riemann_sum = np.sum(product)
    return left_riemann_sum

def trapezoidal(x_vals: np.ndarray, func: np.ufunc) -> float:
    """
    author: Logan Mitchell
    :param x_vals: np.ndarray
    :param func: np.ufunc
    :return: trapezoidal_sum
`   Multiplies function value and left/right endpoint, multiplies by width, returns sum
    """
    width = np.diff(x_vals)
    left_side = func(x_vals[:-1])
    right_side = func(x_vals[1:])
    left_right_average = (left_side + right_side) / 2
    product = left_right_average * width
    trapezoidal_sum = np.sum(product)
    return trapezoidal_sum

def simpson(x_vals: np.ndarray, func: np.ufunc) -> float:
    """
    author: Logan Mitchell
    :param x_vals: np.ndarray
    :param func: np.ufunc
    :return: simpson_sum
    Weights function at evenly spaced interval and returns sum
    """
    width = np.diff(x_vals)
    first_point = func(x_vals[0])
    last_point = func(x_vals[-1])
    odds = func(x_vals[1:-1:2])
    evens = func(x_vals[2:-2:2])
    odd_sum = np.sum(odds)
    even_sum = np.sum(evens)
    partial_sum = first_point + last_point + (4*odd_sum) + (2*even_sum)
    simpson_sum = (width[0]/3) * partial_sum
    return simpson_sum

