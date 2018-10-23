import math
import numpy as np

class Frame():
    def __init__(self, rot=np.zeros(3), tr=0):
        self.rot = rot
        self.tr = tr

    def setRot(self, rot):
        if rot.shape[0] != 3 or rot.shape[1] != 3:
            print("input rotation matrix is not 3x3!")
            return
        self.rot = rot

    def setTr(self, tr):
        if tr.shape[0] != 1 or tr.shape[1] != 3:
            print("input vector is not a column vector!")
            return
        self.tr = tr

    def FFmult(self, F):
        if not isinstance(F, Frame):
            print("not a frame!")
            return
        return Frame(self.rot * F.rot, self.rot * F.tr + self.tr)

    def FPmult(self, p):
        if p.shape[0] != 1 or p.shape[1] != 3:
            print("input vector is not a column vector!")
            return
        return self.rot * p + self.tr