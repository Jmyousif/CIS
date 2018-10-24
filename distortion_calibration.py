import numpy as np
from Frame import *
import three_dimension_transform

# Need to compute Ci_expected for each Ci
# for each calib frame compute transform between optical and EM
# ie: find FD s.t. D = FD dot d
# compute FA between calibration obj and optical tracker
# ie: Aj = FA dot a
# given FD and FA compute Cexp = FD-1 dot FA dot c
# output Cexpected

# input is data frame
def distortion_calibration(tracker, object):

    # first read in Calbody (Nd, Na, Nc)
    # then readings  (ND, NA, NC, nframes

    c_expected = np.zeros(np.shape(tracker)[0])
    Nd = 0
    Na = 0
    Nc = 0
    M1 = np.zeros(2)
    d = M1[0: Nd - 1, :]
    a = M1[Nd: Nd + Na - 1, :]
    c = M1[Nd + Na:, :]

    ND = 0
    NA = 0
    NC = 0
    M2 = np.zeros(2)
    Nframes = 0

    for i in range(Nframes):
        sum = i*(ND + NA + NC)
        D = M2[sum: sum + ND, :]
        A = M2[sum + ND: sum + ND + NA, :]
        Fa = three_dimension_transform.rigid_transform(A, a)
        Fd = three_dimension_transform.rigid_transform(D, d)
        Fa_n1 = Frame.invert(Fa)
        F_ac = Fa_n1.FFmult(Fd)
        c_expected = np.hstack((c_expected, F_ac.FPmult(c)))
    return c_expected
