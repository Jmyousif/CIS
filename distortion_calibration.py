import numpy as np
from Frame import *
import three_dimension_transform
import glob

# Need to compute Ci_expected for each Ci
# for each calib frame compute transform between optical and EM
# ie: find FD s.t. D = FD dot d
# compute FA between calibration obj and optical tracker
# ie: Aj = FA dot a
# given FD and FA compute Cexp = FD-1 dot FA dot c
# output Cexpected

# input is data frame
def distortion_calibration(run):

    # first read in Calbody (Nd, Na, Nc)
    # then readings  (ND, NA, NC, nframes)

    print(glob.glob('Data\*?-calbody.txt'))
    calbodyArr = glob.glob('Data\*?-calbody.txt')
    calbodyF = open(calbodyArr[run], "r")
    calbodyLines = calbodyF.read().splitlines()
    calbodySplit = [[0 for x in range(3)] for y in range(len(calbodyLines))]
    for num in range(len(calbodyLines)):
        calbodySplit[num] = calbodyLines[num].split(',')
        for x in range(len(calbodySplit[num])):
            calbodySplit[num][x] = calbodySplit[num][x].strip()
    print(calbodySplit[0])
    print(calbodySplit[10])

    c_expected = None
    Nd = calbodySplit[0][0]
    Na = calbodySplit[0][1]
    Nc = calbodySplit[0][2]
    M1 = calbodySplit[1:]
    d = M1[0: Nd - 1, :]
    a = M1[Nd: Nd + Na - 1, :]
    c = M1[Nd + Na:, :]

    print(glob.glob('Data\*?-calreadings.txt'))
    calreadingsArr = glob.glob('Data\*?-calreadings.txt')
    calreadingsF = open(calreadingsArr[run], "r")
    calreadingsLines = calreadingsF.read().splitlines()
    calreadingsSplit = [[0 for x in range(3)] for y in range(len(calreadingsLines))]
    for num in range(len(calreadingsLines)):
        calreadingsSplit[num] = calreadingsLines[num].split(',')
        for x in range(len(calreadingsSplit[num])):
            calreadingsSplit[num][x] = calreadingsSplit[num][x].strip()
    print(calreadingsSplit[0])
    print(calreadingsSplit[10])

    ND = calreadingsSplit[0][0]
    NA = calreadingsSplit[0][1]
    NC = calreadingsSplit[0][2]
    M2 = calreadingsSplit[1:]
    Nframes = calreadingsSplit[0][3]

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
