from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import numpy as np

import barycentric

import numpy as np
def get_barycentric_coordinates(triangle_coordinates, point_coordinates):
    left_side = np.array([[point_coordinates[0]], [point_coordinates[1]], [1]])
    right_side = np.array(
        [
            [triangle_coordinates[0][0], triangle_coordinates[0][1], triangle_coordinates[0][2]],
            [triangle_coordinates[1][0], triangle_coordinates[1][1], triangle_coordinates[1][2]],
            [1, 1, 1]
        ]
    )
    return np.linalg.solve(right_side, left_side).tolist() 


def get_cartesian_coordinates(triangle_coordinates, barycentric_coordinates):
    the_x = (triangle_coordinates[0][0] * (barycentric_coordinates[0][0]) +
         triangle_coordinates[0][1] * float(barycentric_coordinates[1][0]) +
         triangle_coordinates[0][2] * float(barycentric_coordinates[2][0]))
    
    the_y = (triangle_coordinates[1][0] * barycentric_coordinates[0][0] +
         triangle_coordinates[1][1] * barycentric_coordinates[1][0] +
         triangle_coordinates[1][2] * barycentric_coordinates[2][0])
    
    return [the_x, the_y]

def is_inside_triangle(triangle_coordinates, point_coordinates):
    the_coords = get_barycentric_coordinates(triangle_coordinates, point_coordinates)
    return the_coords[0][0] >= 0 and the_coords[1][0] >= 0 and the_coords[2][0] >= 0

