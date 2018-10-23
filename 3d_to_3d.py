import numpy as np
import math

def rigid_transform(a, b):
    a_mean = np.sum(a, axis=1) / np.size(a, axis=1)
    b_mean = np.sum(b, axis=1) / np.size(b, axis=1)
    a_err = a - a_mean
    b_err = b - b_mean
    # need to find R that minimizes sum(R*a_err -b_err)^2
    # first calculate H
    np.linalg.svd(np.dot(a_err, b_err))
    R =

    # find p vector
    p = b_mean - np.dot(R, a_mean)

    F = Frame(R,p)