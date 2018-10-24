import numpy as np
import Frame

def rigid_transform(a, b):
    a_mean = np.sum(a, axis=1) / np.size(a, axis=1)
    b_mean = np.sum(b, axis=1) / np.size(b, axis=1)
    a_err = a - a_mean
    b_err = b - b_mean
    # need to find R that minimizes sum(R*a_err -b_err)^2
    # first calculate H
    u, s, v = np.linalg.svd(np.dot(a_err, b_err))
    r = np.dot(v, np.transpose(u))
    # find p vector
    p = b_mean - np.dot(r, a_mean)
    f = Frame(r, p)
    return f
