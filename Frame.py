import math
import numpy as np
import point_transformations as PT


# A Frame Class to imitate a frame transformation as an object
class Frame:
    # Initialization of a frame, input is a rotation matrix and a translation vector
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

    # Method to modify the rotation matrix of a frame
    # Input parameters of the new rotation matrix
    # No output
    def setRot(self, rot):
        try:
            if not rot.shape[0] == 3 or not rot.shape[1] == 3:
                raise ValueError
            self.rot = rot
        except ValueError:
            print("input rotation matrix is not 3x3!")
        self.rot = rot

    # Method to modify the translation vector of a frame
    # Input parameters of the new translation vector
    # No output
    def setTr(self, tr):
        try:
            if not tr.shape[0] * tr.shape[1] == 3:
                raise ValueError
            self.tr = tr
        except ValueError:
            print("input vector is not a column vector!")

        self.tr = tr

    # Method to return the inverse of a frame
    # No input parameters, the method is operated on a frame
    # Output of the inverted frame
    def invert(self):
        try:
            if not isinstance(self, Frame):
                raise ValueError
        except ValueError:
            print("Not a frame!")
        return Frame(np.linalg.inv(self.rot), np.dot(-self.rot, self.tr))

    # Method to multiply two Frame objects together using the proper composition equation
    # Input parameters of the second frame to be multiplied, the method is operated on the first
    # Output of the product of the two frames, as a frame object
    def FFmult(self, f):
        try:
            if not isinstance(f, Frame):
                raise ValueError
        except ValueError:
            print("not a frame!")
        return Frame(np.dot(self.rot, f.rot), np.dot(self.rot, f.tr) + self.tr)


    # Method to multiply a frame by a translation vector
    # Input parameters of the translation vector, the method is operated on the Frame
    # Output of the result of the multiplication, as a vector
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
        return np.dot(self.rot, p) + self.tr

    # Method to get the rotation matrix of a frame
    # No input parameters
    # Output the rotation matrix of the frame the method is operated on
    def getRot(self):
        return self.rot

    # Method to get the translation vector of a frame
    # No input parameters
    # Output the translation vector of the frame the method is operated on
    def getTr(self):
        return self.tr
