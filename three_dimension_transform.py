import numpy as np
import Frame

def rigid_transform(a, b):
    a_mean = (np.sum(a, axis=0) / np.shape(a)[0]).reshape(3, 1)
    b_mean = (np.sum(b, axis=0) / np.shape(b)[0]).reshape(3, 1)
    a_err = a.T - a_mean
    b_err = np.subtract(b.T, b_mean)
    # need to find R that minimizes sum(R*a_err -b_err)^2
    # first calculate H
    dot = np.dot(a_err, b_err)
    u, s, v = np.linalg.svd(dot)

    r = np.dot(v, np.transpose(u))
    # find p vector
    p = b_mean - np.dot(r, a_mean)
    f = Frame.Frame(r, p)
    return f
