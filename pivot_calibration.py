import numpy as np

# This program takes a rotation and translation and performs pivot calibraiton
# Inputs: r = rotation matrix, p = translation vector, dataframes = # of frames


def pivot_calibration(r, p, dataframes):
    i = -1 * np.identity(3)
    # i = np.tile(i, (dataframes, 1))

    # first input for least squares
    rot_i_and_identity = np.hstack((r, i)) # [R_i | -I]

    # solve the least squares problem
    # lstsq returns more than just the solution, the first entry of the output
    # vector is the solution x
    x = np.linalg.lstsq(rot_i_and_identity, -p)[0]

    p_t = x[0:3]
    p_pivot = x[3:6]
    return p_t, p_pivot
