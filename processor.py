import numpy as np


# subway storage block in ->


def generate_nxn_matrix(i):
    generated_matrix = np.zeros((i, i))
    return generated_matrix


# set distance in time in minutes between two stations
def set_interval_beetwen_two_stations(matrix, i, j, interval):
    if i == j:
        interval = 0
    matrix[i, j] = interval
    matrix[j, i] = interval


# set distance in time in minutes between neighbour stations for whole line


# get distance between two stations for the route
# generate simple route


subway_distances = generate_nxn_matrix(10)
set_interval_beetwen_two_stations(subway_distances, 0, 1, 3)
print(subway_distances[0, 1])

# A = np.array([[1,1],[0,1]])
# B = np.array([[2,2],[0,2]])
# C = np.dot(A,B)
# print(C)
