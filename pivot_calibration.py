import numpy as np

# Jonah Yousif, Justin Joyce
# This program takes a rotation and translation and performs pivot calibration
# Inputs: r = rotation matrix, p = translation vector, dataframes = # of frames
# Output: The p_pivot vector and the unknown p_t vector in a list.
def pivot_calibration(r, p, dataframes=1):
    i = -1 * np.identity(3)
    i = np.tile(i, (dataframes, 1))

    #print(r)
    # first input for least squares
    rot_i_and_identity = np.hstack((r, i)) # [R_i | -I]

    #print(rot_i_and_identity.shape, rot_i_and_identity)
    # solve the least squares problem
    # lstsq returns more than just the solution, the first entry of the output
    # vector is the solution x
    x = np.linalg.lstsq(rot_i_and_identity, -p, rcond=None)[0]

    p_pivot = x[0:3]
    p_t = x[3:6]
    return p_pivot, p_t
