import numpy as np

"""
References:
https://numpy.org/doc/2.2/reference/routines.linalg.html
Looked up documentation on numpy linear algebra functions to find a way to solve the system of equations.
Found the np.linalg.solve function as well as the dot product function.
"""

def get_barycentric_coordinates(triangle_coordinates: np.ndarray, point_coordinates: np.ndarray) -> np.ndarray:
    """
    This function takes two arrays, one for the three points of a triangle and the other for the coordinates of a point,
    and returns the barycentric coordinates of the point in an array.

    Parameters
    ----------
    triangle_coordinates : ndarray
        This is a 3x2 numpy array that contains the three points of a triangle
    point_coordinates : ndarray
        This is a 1x2 numpy array that contains the cartesian coordinates of a point

    Returns
    ----------
    ndarray
        The barycentric coordinates of the point in a 1x3 numpy array
    """

    # This creates a system of equations using the triangle coordinates and barycentric properties.
    system_array = np.array(
        [
            [triangle_coordinates[0, 0], triangle_coordinates[1, 0], triangle_coordinates[2, 0]],
            [triangle_coordinates[0, 1], triangle_coordinates[1, 1], triangle_coordinates[2, 1]],
            [1, 1, 1]
        ]
    )

    # This creates the right side of the system of equations using the point coordinates
    point_array = np.array([point_coordinates[0], point_coordinates[1], 1])

    # This uses computational linear algebra to array and return the lambdas that solve the system of equations.
    lambdas_array = np.linalg.solve(system_array, point_array)
    return lambdas_array



def get_cartesian_coordinates(triangle_coordinates: np.ndarray, barycentric_coordinates: np.ndarray) -> np.ndarray:
    """
    This function takes two arrays, one that contains the three points of a triangle and the other for the barycentric
    coordinates of a point, and returns the cartesian coordinates of the point in an array.

    Parameters
    ----------
    triangle_coordinates : ndarray
        This is a 3x2 numpy array that contains the three points of a triangle
    barycentric_coordinates : ndarray
        This is a 1x3 numpy array that contains the barycentric coordinates of a point

    Returns
    ----------
    ndarray
        The cartesian coordinates of the point in a 1x2 numpy array
    """

    # This uses the vector dot product to solve for x and y of the cartesian point.
    triangle_coordinates_new = triangle_coordinates.transpose()
    cartesian_array = np.dot(triangle_coordinates_new, barycentric_coordinates)
    return cartesian_array



def is_inside_triangle(triangle_coordinates: np.ndarray, point_coordinates: np.ndarray) -> bool:
    """
    This function checks if a point is inside a triangle using the properties of barycentric coordinates. It takes two
    numpy arrays, one that contains the three points of a triangle and the other for the cartesian coordinates of a
    point, and returns either True or False.

    Parameters
    ----------
    triangle_coordinates : ndarray
        This is a 3x2 numpy array that contains the three points of a triangle
    point_coordinates : ndarray
        This is a 1x2 numpy array that contains the cartesian coordinates of a point

    Returns
    ----------
    bool
        Whether the point is inside the triangle
    """

    # This utilizes the previously defined function to get the barycentric coordinates using the triangle and point
    lams = get_barycentric_coordinates(triangle_coordinates, point_coordinates)

    # This is a logical expression that returns True if all lambdas are non-negative
    if  lams[0] >= 0 and lams[1] >= 0 and lams[2] >= 0:
        return True
    else:
        return False