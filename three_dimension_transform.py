import numpy as np
import Frame


# Function to calculate the rigid transform of two 3D point sets
def rigid_transform(b, a):

    print(type(a))
    print(type(b))
    a_mean = (np.sum(a, axis=0) / np.shape(a)[0])
    b_mean = (np.sum(b, axis=0) / np.shape(b)[0])
    a_err = a - a_mean
    b_err = b - b_mean
    # need to find R that minimizes sum(R*a_err -b_err)^2
    # first calculate H
    rset = np.dot(a_err.T, b_err)
    u, s, v = np.linalg.svd(rset)
    r = np.dot(v.T, u.T)
    # find p vector
    p = (b_mean - np.dot(r, a_mean)).reshape(3, 1)
    f = Frame.Frame(r, p)
    return f
