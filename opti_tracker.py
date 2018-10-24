import numpy as np
from Frame import *
import pivot_calibration
import three_dimension_transform


def opti_track(filename):
    # file io
    Nd = 0
    M = np.zeros()
    d = M[:Nd,:] #from CALbody
    Nh = 0
    Nframes = 0
    M = np.zeros[0]
    D = M[:Nd, :]
    Fd = three_dimension_transform.rigid_transform(d, D)
    # coordinates based on frame 1
    Hframe = M[Nd:Nd + Nh, :]
    # Hframe = M[:, 3] = 1
    Hadjust = np.linalg.lstsq(Fd, Hframe)
    Hmid = np.sum(Hadjust, axis=1)/np.shape(Hadjust)[0]

    # relative frame
    for i in range(Nframes):
        D = M[i*(Nd + Nh), i*(Nd+Nh) + Nd]
        H = M[i*(Nd+Nh)+Nd, ]

        Fd = three_dimension_transform.rigid_transform(d, D)
        #H(:, 3) = 1
        H_em = np.linalg.lstsq(Fd, H)
        h_em = np.subtract(H_em - Hmid)
        reg = three_dimension_transform.rigid_transform(h_em, H_em)
        pivs = pivot_calibration.pivot_calibration(reg.rot, reg.tr, Nframes)
        return np.hstack(pivs)


if __name__ == '__main__':
    pass
