import numpy as np
import Frame
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

    c_expected = None

    # for loop?
    fd = object[0][0]

    for frame in tracker:
        f_d = object[0][0].register(frame[0])
        f_a = object[0][1].register(frame[1])

        c_exp.append(object_frame[0][2].transform(f_d.inv.compose(f_a)))

    return c_exp


    # bernstein polynomials