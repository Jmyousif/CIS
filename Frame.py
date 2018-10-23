import math
import numpy as np

class Frame():
    def __init__(self, rot = np.zeros(3), tr = 0):
        try:
            if rot.shape[0] != 3 or rot.shape[1] != 3:
                raise ValueError
            self.rot = rot
            if tr.shape[0] != 1 or tr.shape[1] != 3:
                raise ValueError
            self.tr = tr
        except ValueError:
            print("Not valid parameters")

    def setRot(self, rot):
        try:
            if rot.shape[0] != 3 or rot.shape[1] != 3:
                raise ValueError
            self.rot = rot
        except ValueError:
            print("input rotation matrix is not 3x3!")

    def setTr(self, tr):
        try:
            if tr.shape[0] != 1 or tr.shape[1] != 3:
                raise ValueError
            self.tr = tr
        except ValueError:
            print("input vector is not a column vector!")

    def FFmult(self, F):
        try:
            if not isinstance(F, Frame):
                raise ValueError
            return Frame(self.rot * F.rot, self.rot * F.tr + self.tr)
        except ValueError:
            print("not a frame!")

    def FPmult(self, p):
        try:
            if p.shape[0] != 1 or p.shape[1] != 3:
                raise ValueError
            return self.rot * p + self.tr
        except ValueError:
            print("input vector is not a column vector!")