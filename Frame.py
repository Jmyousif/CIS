import math
import numpy as np
import point_transformations as PT


class Frame:

    def __init__(self, rotation=np.zeros((3, 3)), translation=np.zeros((3, 1))):
        try:
            if rotation.shape[0] != 3 or rotation.shape[1] != 3:
                print("bad rot")
                raise ValueError
            if translation.shape[0] != 3 or translation.shape[1] != 1:
                print("bad tr")
                raise ValueError
        except ValueError:
            print("Not valid parameters")
            return
        self.rot = rotation
        self.tr = translation

    def setRot(self, rot):
        try:
            if rot.shape[0] != 3 or rot.shape[1] != 3:
                raise ValueError
            self.rot = rot
        except ValueError:
            print("input rotation matrix is not 3x3!")
        self.rot = rot

    def setTr(self, tr):
        try:
            if tr.shape[0] != 3 or tr.shape[1] != 31:
                raise ValueError
            self.tr = tr
        except ValueError:
            print("input vector is not a column vector!")

        self.tr = tr

    def FFmult(self, F):
        if not isinstance(F, Frame):
            print("not a frame!")
            return
        return Frame(self.rot * F.rot, self.rot * F.tr + self.tr)

    def invert(self, f):
        try:
            if not isinstance(f, Frame):
                raise ValueError
            f.setRot(np.invert(f.rot))
            f.setTr(np.dot(-f.rot, f.tr))
        except ValueError:
            print("Not a frame!")

    def FFmult(self, f):
        try:
            if not isinstance(f, Frame):
                raise ValueError
            return Frame(self.rot * f.rot, np.dot(self.rot, f.tr) + self.tr)
        except ValueError:
            print("not a frame!")

    def FPmult(self, p):
        try:
            if p.shape[0] != 3 or p.shape[1] != 1:
                raise ValueError
            return self.rot * p + self.tr
        except ValueError:
            print("input vector is not a column vector!")

    def getRot(self):
        return self.rot

    def getTr(self):
        return self.tr
