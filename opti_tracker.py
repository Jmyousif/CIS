from Frame import *
import pivot_calibration
import three_dimension_transform
import glob

# Jonah Yousif, Justin Joyce
# Program to apply optical tracker data to perform pivot calibration of the optical tracking probe.
def opti_track(run, runtype):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    type = ['debug', 'unknown']

    # file io for data input
    calbodyArr = glob.glob('Data/pa1-' + type[runtype] + '-' + letters[run] + '-calbody.txt')
    calbodyF = open(calbodyArr[0], "r")
    calbodyLines = calbodyF.read().splitlines()
    calbodySplit = [[0 for x in range(3)] for y in range(len(calbodyLines))]
    for num in range(len(calbodyLines)):
        calbodySplit[num] = calbodyLines[num].split(',')
        for x in range(len(calbodySplit[num])):
            calbodySplit[num][x] = calbodySplit[num][x].strip()
    optpivotArr = glob.glob('Data/pa1-' + type[runtype] + '-' + letters[run] + '-optpivot.txt')
    optpivotF = open(optpivotArr[0], "r")
    optpivotLines = optpivotF.read().splitlines()
    optpivotSplit = [[0 for x in range(3)] for y in range(len(optpivotLines))]
    for num in range(len(optpivotLines)):
        optpivotSplit[num] = optpivotLines[num].split(',')
        for x in range(len(optpivotSplit[num])):
            optpivotSplit[num][x] = optpivotSplit[num][x].strip()


    Nd = int(calbodySplit[0][0])
    M1 = np.asarray(calbodySplit[1:]).astype(float)
    d = M1[:Nd][:] #from CALbody
    Nh = int(optpivotSplit[0][1])
    Nframes = int(optpivotSplit[0][2])
    M2 = np.asarray(optpivotSplit[1:]).astype(float)
    D = M2[:Nd][:]
    Fd = three_dimension_transform.rigid_transform(D, d)
    M3 = np.zeros(1)
    for i in range(Nframes):
        to_add = M2[(i+1)*Nd+(i)*Nh:(i+1)*Nd+(i+1)*Nh, :]

        if M3.size == 1:
            M3 = Fd.FPmult(to_add)
        else:
            M3 = np.vstack((M3, Fd.FPmult(to_add)))

    Gframe = M3[:Nh, :]
    Gmid = np.sum(Gframe, axis=0) / np.shape(Gframe)[0]
    gpos = Gframe - Gmid
    G_stack = np.zeros(1)
    p_stack = np.zeros(1)
    # relative frame
    for i in range(Nframes):

        Gg = M3[i * Nh: (i + 1) * Nh, :]
        Mj = three_dimension_transform.rigid_transform(Gg, gpos)

        if G_stack.size == 1:
            G_stack = Mj.rot
        else:
            G_stack = np.vstack((G_stack, Mj.rot))
        if p_stack.size == 1:
            p_stack = Mj.tr.T
        else:
            p_stack = np.vstack((p_stack, Mj.tr.T))
    p_stack = p_stack.reshape(p_stack.size, )
    pivs = pivot_calibration.pivot_calibration(G_stack, p_stack, Nframes)
    return pivs


if __name__ == '__main__':
    pass
