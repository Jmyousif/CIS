import numpy as np
from Frame import *
import pivot_calibration
import three_dimension_transform
import glob

def EM_track(run):

    empivotArr = glob.glob('Data/*empivot.txt')
    empivotF = open(empivotArr[run], "r")
    empivotLines = empivotF.read().splitlines()
    empivotSplit = [[0 for x in range(3)] for y in range(len(empivotLines))]
    for num in range(len(empivotLines)):
        print(type(num))
        empivotSplit[num] = empivotLines[num].split(',')
        for x in range(len(empivotSplit[num])):
            empivotSplit[num][x] = empivotSplit[num][x].strip()


    # file io
    Ng = int(empivotSplit[0][0])
    Nframes = int(empivotSplit[0][1])
    M = np.asarray(empivotSplit[1:]).astype(float)
    # coordinates based on frame 1
    Gframe = M[:Ng - 1, :]
    Gmid = np.sum(Gframe, axis=0)/np.shape(Gframe)[0]
    # relative frame
    gpos = np.subtract(Gframe,Gmid)

    for i in range(Nframes):

        Gg = M[i*Ng: (i+1)*Ng, :]
        gg = Gg - Gmid

        Mj = three_dimension_transform.rigid_transform(Gg, gg)
        return gpos, pivot_calibration.pivot_calibration(Mj.getRot(), Mj.getTr(), Nframes)


if __name__ == '__main__':
    pass
