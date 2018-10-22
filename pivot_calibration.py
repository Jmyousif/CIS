import numpy as np

"""
Implementing pivot calibration as detailed in slides
"""


"""
Inputs: r = rotation matrix
        p = translation vector        
        dataframes = # of frames
"""
def PivotCalibration(r, p, dataframes):
    i = -1 * np.identity(3)
    i = np.tile(I, (dataframes, 1))

    # first input for least squares
    rot_i_and_identity = np.hstack((r, i))

    # solve the least squares problem
    x = np.linalg.lstsq(rot_i_and_identity, -p)[0]

    p_t = x[0:3, 0]
    p_pivot = x[3:6, 0]
    return p_t, p_pivot

"""
Output: p_t - tip position
        p_pivot - pivot position
"""
