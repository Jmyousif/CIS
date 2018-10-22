import numpy as np
import math

class PointTransformations():
    def __init__(self):
        print("init")

    def makeRotationMatrix(self, theta, letter):
        rot = np.zeros(3)
        if letter == 'x':
            rot[0,0] = 1
            rot[1,1] = np.cos(theta)
            rot[2,1] = -np.sin(theta)
            rot[1,2] = np.sin(theta)
            rot[2,2] = np.cos(theta)
        if letter == 'y':
            rot[0,0] = np.cos(theta)
            rot[2,0] = np.sin(theta)
            rot[1,1] = 1
            rot[0,2] = -np.sin(theta)
            rot[2,2] = np.cos(theta)
        if letter == 'z':
            rot[0,0] = np.cos(theta)
            rot[1,0] = -np.sin(theta)
            rot[0,1] = np.sin(theta)
            rot[1,1] = np.cos(theta)
            rot[2,2] = 1

        return rot

    def rotatePoint(self, rot, point):
        if point.shape[0] != 1 or point.shape[1] != 3:
            print("input vector is not a column vector!")
            return
        if rot.shape[0] != 3 or rot.shape[1] != 3:
            print("input rotation matrix is not 3x3!")
            return
        return rot * point

    def transformFrame(self, rotation, translation, point):
        if point.shape[0] != 1 or point.shape[1] != 3:
            print("input vector is not a column vector!")
            return
        if rotation.shape[0] != 3 or rotation.shape[1] != 3:
            print("input frame rotation matrix is not 3x3!")
            return
        if translation.shape[0] != 1 or translation.shape[1] != 3:
            print("input frame translation is not a column vector!")
        return rotation * point + translation

#git add
#git status
#git commit
#git pull
#git push

