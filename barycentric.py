import numpy as np

def get_barycentric_coordinates(triangle_coordinates: ndarray, point_coordinates: np.ndarray) -> ndarray:
    system_array = np.array(
        [
            [triangle_coordinates[0, 0], triangle_coordinates[0, 1], triangle_coordinates[0, 2]],
            [triangle_coordinates[1, 0], triangle_coordinates[1, 1], triangle_coordinates[1, 2]],
            [1, 1, 1]
        ]
    )

    point_array = np.array([point_coordinates[0], point_coordinates[1], point_coordinates[0]])

    lambdas_array = np.linalg.solve(system_array, point_array)

    return lambdas_array

def get_cartesian_coordinates(triangle_coordinates: ndarray, barycentric_coordinates: ndarray) -> ndarray:
    x = np.dot(triangle_coordinates[0:], barycentric_coordinates)
    y = np.dot(triangle_coordinates[1:], barycentric_coordinates)
    return np.array([x, y])

def is_inside_triangle(triangle_coordinates: ndarray, point_coordinates: np.ndarray) -> bool:
    lams = get_barycentric_coordinates(triangle_coordinates, point_coordinates)

    if  lams[0] > 0 and lams[1] > 0 and lams[2] > 0:
        return True
    else:
        return False
