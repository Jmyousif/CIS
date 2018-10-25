import numpy as np
from Frame import *
import pivot_calibration
import three_dimension_transform
import glob

# Program to apply optical tracker data to perform pivot calibration of the optical tracking probe.
def opti_track(run):

    # file io for data input
    calbodyArr = glob.glob('Data\*?-calbody.txt')
    calbodyF = open(calbodyArr[run], "r")
    calbodyLines = calbodyF.read().splitlines()
    calbodySplit = [[0 for x in range(3)] for y in range(len(calbodyLines))]
    for num in range(len(calbodyLines)):
        calbodySplit[num] = calbodyLines[num].split(',')
        for x in range(len(calbodySplit[num])):
            calbodySplit[num][x] = calbodySplit[num][x].strip()
    optpivotArr = glob.glob('Data\*?-optpivot.txt')
    optpivotF = open(optpivotArr[run], "r")
    optpivotLines = optpivotF.read().splitlines()
    optpivotSplit = [[0 for x in range(3)] for y in range(len(optpivotLines))]
    for num in range(len(optpivotLines)):
        optpivotSplit[num] = optpivotLines[num].split(',')
        for x in range(len(optpivotSplit[num])):
            optpivotSplit[num][x] = optpivotSplit[num][x].strip()


    Nd = calbodySplit[0][0]
    M = calbodySplit[1:]
    d = M[:Nd,:] #from CALbody

    Nh = optpivotSplit[0][1]
    Nframes = optpivotSplit[0][2]
    M = optpivotSplit[1:]
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
