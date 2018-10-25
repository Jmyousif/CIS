import numpy as np
import math
import Frame
import point_transformations as PT
import glob
import re
import pivot_calibration
import opti_tracker
import distortion_calibration
import em_tracking


def main():

    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    run = 0
    output = open("pa1-debug-" + letters[run] + "-testoutput1.txt", "w")

    calreadingsArr = glob.glob('Data/pa1-debug-a-calreadings.txt')
    calreadingsF = open(calreadingsArr[run], 'r')
    calreadingsLines = calreadingsF.read().splitlines()
    calreadingsSplit = [[0 for x in range(3)] for y in range(len(calreadingsLines))]
    for num in range(len(calreadingsLines)):
        calreadingsSplit[num] = calreadingsLines[num].split(',')
        for x in range(len(calreadingsSplit[num])):
            calreadingsSplit[num][x] = calreadingsSplit[num][x].strip()

    Nc = calreadingsSplit[0][2]
    Nf = calreadingsSplit[0][3]

    output.write(Nc + ", " + Nf + ", " + output.name)

   # EMpoint = em_tracking.EM_track(run)

    #print(EMpoint[1][0][0] + ", " + EMpoint[1][0][1] + ", " + EMpoint[1][0][2])
    #output.write(EMpoint[1][0][0] + ", " + EMpoint[1][0][1] + ", " + EMpoint[1][0][2])
    output.write(str(distortion_calibration.distortion_calibration(run)))


if __name__ == '__main__':
    main()