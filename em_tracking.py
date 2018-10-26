from Frame import *
import pivot_calibration
import three_dimension_transform
import glob


# Jonah Yousif, Justin Joyce
# Method to apply EM tracking data to perform a pivot calibration for the EM probe
# input is the "run," determining which data file set to use
# Output is the
def EM_track(run, runtype):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    type = ['debug', 'unknown']

    # File IO
    empivotArr = glob.glob('Data/pa1-' + type[runtype] + '-' + letters[run] + '-empivot.txt')
    empivotF = open(empivotArr[0], "r")
    empivotLines = empivotF.read().splitlines()
    empivotSplit = [[0 for x in range(3)] for y in range(len(empivotLines))]
    for num in range(len(empivotLines)):
        empivotSplit[num] = empivotLines[num].split(',')
        for x in range(len(empivotSplit[num])):
            empivotSplit[num][x] = empivotSplit[num][x].strip()

    # Assigning Variables
    Ng = int(empivotSplit[0][0])
    Nframes = int(empivotSplit[0][1])
    M = np.asarray(empivotSplit[1:]).astype(float)
    # coordinates based on frame 1
    Gframe = M[:Ng, :]
    Gmid = np.sum(Gframe, axis=0)/np.shape(Gframe)[0]
    gpos = Gframe - Gmid
    G_stack = np.zeros(1)
    p_stack = np.zeros(1)
    # relative frame
    for i in range(Nframes):

        Gg = M[i*Ng: (i+1)*Ng, :]
        Mj = three_dimension_transform.rigid_transform(Gg, gpos)

        if G_stack.size == 1:
            G_stack = Mj.rot
        else:
            G_stack = np.vstack((G_stack, Mj.rot))
        if p_stack.size == 1:
            p_stack = Mj.tr.T
        else:
            p_stack = np.vstack((p_stack, Mj.tr.T))
    p_stack = p_stack.reshape(p_stack.size,)
    pivs = pivot_calibration.pivot_calibration(G_stack, p_stack, Nframes)
    return pivs


if __name__ == '__main__':
    pass
