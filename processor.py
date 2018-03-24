import numpy as np


# subway storage block in ->


def generate_nxn_matrix(i):
    generated_matrix = np.zeros((i, i))
    return generated_matrix


# set distance in time in minutes between two stations
def set_interval_between_two_stations(matrix, i, j, interval):
    if i == j:
        interval = 0
    matrix[i, j] = interval
    matrix[j, i] = interval


# set distance in time in minutes between neighbour stations for whole line
# the first interval should be zero
def set_interval_between_neighbour_stations_for_line(subway_intervals, stations, intervals):
    i = 0
    for next_station in stations:
        interval = intervals[i]
        if i == 0:
            i = i + 1
            continue
        current_station = stations[i - 1]
        set_interval_between_two_stations(subway_intervals, current_station, next_station, interval)
        i = i + 1

# get distance between two stations for the route
# generate simple route


subway_distances = generate_nxn_matrix(10)

# example line1
line_one_stations = [0, 1, 2, 3, 4]
line_one_intervals = [0., 2., 3., 2., 5.]

set_interval_between_neighbour_stations_for_line(subway_distances, line_one_stations, line_one_intervals)

# example line2
line_two_stations = [5, 6, 7, 8, 9]
line_two_intervals = [0., 3., 2., 1., 3.]
set_interval_between_neighbour_stations_for_line(subway_distances, line_two_stations, line_two_intervals)

station_changes = [[2, 7]]
station_changes_intervals = [3.]

# set_interval_between_two_stations(subway_distances, 0, 1, 3)
# print(subway_distances[0, 1])

# A = np.array([[1,1],[0,1]])
# B = np.array([[2,2],[0,2]])
# C = np.dot(A,B)
# print(C)
