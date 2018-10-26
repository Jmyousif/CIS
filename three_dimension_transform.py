import numpy as np
import Frame
import math


# Jonah Yousif, Justin Joyce
# Function to calculate the rigid transform of two 3D point sets
def rigid_transform(a, b):

    a_mean = (np.sum(a, axis=0) / np.shape(a)[0])
    b_mean = (np.sum(b, axis=0) / np.shape(b)[0])
    a_err = a - a_mean
    b_err = b - b_mean
    # need to find R that minimizes sum(R*a_err -b_err)^2
    # first calculate H
    rset = np.dot(a_err.T, b_err)
    u, s, v = np.linalg.svd(rset)

    if math.floor(np.linalg.det(v.dot(u))) == -1:
        I = np.identity(3)
        I[-1, -1] = -1
        r = np.dot(v.T, np.dot(I, u.T))
    else:
        r = np.dot(v.T, u.T)

    # find p vector
    p = b_mean - np.dot(r, a_mean)
    f = Frame.Frame(r, p)
    return f
