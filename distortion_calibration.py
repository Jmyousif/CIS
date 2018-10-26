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

    calbodyArr = glob.glob('Data/pa1-debug-a-calbody.txt')
    calbodyF = open(calbodyArr[run], "r")
    calbodyLines = calbodyF.read().splitlines()
    calbodySplit = [[0 for x in range(3)] for y in range(len(calbodyLines))]
    for num in range(len(calbodyLines)):
        calbodySplit[num] = calbodyLines[num].split(',')
        for x in range(len(calbodySplit[num])):
            calbodySplit[num][x] = calbodySplit[num][x].strip()

    c_expected = np.zeros(1)
    Nd = int(calbodySplit[0][0])
    Na = int(calbodySplit[0][1])
    Nc = int(calbodySplit[0][2])
    M1 = np.asarray(calbodySplit[1:]).astype(float)
    d = M1[0: Nd, :]
    a = M1[Nd: Nd + Na, :]
    c = M1[Nd + Na:, :]

    calreadingsArr = glob.glob('Data/pa1-debug-a-calreadings.txt')
    calreadingsF = open(calreadingsArr[run], "r")
    calreadingsLines = calreadingsF.read().splitlines()
    calreadingsSplit = [[0 for x in range(3)] for y in range(len(calreadingsLines))]
    for num in range(len(calreadingsLines)):
        calreadingsSplit[num] = calreadingsLines[num].split(',')
        for x in range(len(calreadingsSplit[num])):
            calreadingsSplit[num][x] = calreadingsSplit[num][x].strip()

    ND = int(calreadingsSplit[0][0])
    NA = int(calreadingsSplit[0][1])
    NC = int(calreadingsSplit[0][2])
    M2 = np.asarray(calreadingsSplit[1:]).astype(float)
    Nframes = int(calreadingsSplit[0][3])
    #print(calreadingsSplit[0][4])

    for i in range(Nframes):
        sum = i*(ND + NA + NC)
        D = M2[sum: sum + ND, :]
        A = M2[sum + ND: sum + ND + NA, :]
        Fd = three_dimension_transform.rigid_transform(d, D)
        Fa = three_dimension_transform.rigid_transform(a, A)
        Fd_n1 = Fd.invert()
        F_ac = Fd_n1.FFmult(Fa)
        cexp_new = F_ac.FPmult(c)
        if c_expected.size == 1:
            c_expected = cexp_new
        else:
            c_expected = np.vstack((c_expected,cexp_new))

    return c_expected
