import numpy as np
from Frame import *
import pivot_calibration
import three_dimension_transform
def EM_track(filename):
    # file io
    Ng = 0
    Nframes = 0
    M = np.zeros[0]
    # coordinates based on frame 1
    Gframe = M[:Ng - 1, :]
    Gmid = np.sum(Gframe, axis=1)/np.shape(Gframe[0])
    # relative frame
    gpos = np.subtract(Gframe-Gmid)

    for i in range(Nframes):

        Gg = M[i*Ng: (i+1)*Ng, :]
        gg = Gg - Gmid

        Mj = three_dimension_transform.rigid_transform(Gg, gg)
        return np.hstack((gpos, pivot_calibration.pivot_calibration(Mj.rot, Mj.tr, Nframes)))


if __name__ == '__main__':
    pass
