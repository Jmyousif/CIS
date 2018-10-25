import math
import numpy as np
import point_transformations as PT


class Frame:

    def __init__(self, rotation=np.zeros((3, 3)), translation=np.zeros((3, 1))):
        try:
            if not rotation.shape[0] == 3 or not rotation.shape[1] == 3:
                print("bad rot", rotation.shape)
                raise ValueError
            translation_0 = translation.shape[0]
            translation_1 = translation.shape[1]
            if not translation_0 * translation_1 == 3:
                print("bad tr", translation.shape)
                raise ValueError
        except ValueError:
            print("Not valid parameters")
            return
        self.rot = rotation
        self.tr = translation

    def setRot(self, rot):
        try:
            if not rot.shape[0] == 3 or not rot.shape[1] == 3:
                raise ValueError
            self.rot = rot
        except ValueError:
            print("input rotation matrix is not 3x3!")
        self.rot = rot

    def setTr(self, tr):
        try:
            if not tr.shape[0] * tr.shape[1] == 3:
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

    def invert(self):
        try:
            if not isinstance(self, Frame):
                raise ValueError
        except ValueError:
            print("Not a frame!")
        return Frame(np.linalg.inv(self.rot), np.dot(-self.rot, self.tr))

    def FFmult(self, f):
        try:
            if not isinstance(f, Frame):
                raise ValueError
            return Frame(self.rot * f.rot, np.dot(self.rot, f.tr) + self.tr)
        except ValueError:
            print("not a frame!")

    def FPmult(self, p):
        p_0 = p.shape[0]
        p_1 = p.shape[1]
        if p_0 == 3 or p_1 == 3:
            flag = True
        try:
            if not flag:
                print("ERR")
                raise ValueError
        except ValueError:
            print("VALERR", flag, "0 ", p_0, "1 " , p_1)
        return np.add(np.dot(self.rot, p.T), self.tr).T

    def getRot(self):
        return self.rot

    def getTr(self):
        return self.tr
