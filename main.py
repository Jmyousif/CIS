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

# Main method to run all methods in and perform file io
def main():
    # run = 0
    #
    # print(glob.glob('Data\*?-calbody.txt'))
    # calbodyArr = glob.glob('Data\*?-calbody.txt')
    # calreadingsArr = glob.glob('Data\*?-calreadings.txt')
    # empivotArr = glob.glob('Data\*?-empivot.txt')
    # optpivotArr = glob.glob('Data\*?-optpivot.txt')
    #
    # calbodyF = open(calbodyArr[run], "r")
    # calreadingsF = open(calreadingsArr[run], "r")
    # empivotF = open(empivotArr[run], "r")
    # optpivotF = open(optpivotArr[run], "r")
    #
    # calbodyLines = calbodyF.read().splitlines()
    # calreadingsLines = calreadingsF.read().splitlines()
    # empivotLines = empivotF.read().splitlines()
    # optpivotLines = optpivotF.read().splitlines()
    #
    # calbodySplit = [[0 for x in range(3)] for y in range(len(calbodyLines))]
    # calreadingsSplit = [[0 for x in range(3)] for y in range(len(calreadingsLines))]
    # empivotSplit = [[0 for x in range(3)] for y in range(len(empivotLines))]
    # optpivotSplit = [[0 for x in range(3)] for y in range(len(optpivotLines))]
    #
    # for num in range(len(calbodyLines)):
    #     calbodySplit[num] = calbodyLines[num].split(',')
    #     for x in range(len(calbodySplit[num])):
    #         calbodySplit[num][x] = calbodySplit[num][x].strip()
    # for num in range(len(calreadingsLines)):
    #     calreadingsSplit[num] = calreadingsLines[num].split(',')
    #     for x in range(len(calreadingsSplit[num])):
    #         calreadingsSplit[num][x] = calreadingsSplit[num][x].strip()
    # for num in range(len(empivotLines)):
    #     empivotSplit[num] = empivotLines[num].split(',')
    #     for x in range(len(empivotSplit[num])):
    #         empivotSplit[num][x] = empivotSplit[num][x].strip()
    # for num in range(len(optpivotLines)):
    #     optpivotSplit[num] = optpivotLines[num].split(',')
    #     for x in range(len(optpivotSplit[num])):
    #         optpivotSplit[num][x] = optpivotSplit[num][x].strip()
    #
    # print(calbodySplit[0])
    # print(calbodySplit[10])
    # print(calreadingsSplit[0])
    # print(calreadingsSplit[10])
    # print(empivotSplit[0])
    # print(empivotSplit[10])
    # print(optpivotSplit[0])
    # print(optpivotSplit[10])

    # Preliminary code to simplify file operations later
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    run = 0
    output = open("pa1-debug-" + letters[run] + "-testoutput1.txt", "w")

    # Reading in calreadings file to print Nc and Nframes to output file
    calreadingsArr = glob.glob('Data/*calreadings.txt')
    calreadingsF = open(calreadingsArr[run], 'r')
    calreadingsLines = calreadingsF.read().splitlines()
    calreadingsSplit = calreadingsLines[0].split(',')

    # Assigning Nc and Nframes, and writing those along with the output filename to the output file
    Nc = calreadingsSplit[2].strip()
    Nf = calreadingsSplit[3].strip()
    output.write(Nc + ", " + Nf + ", " + output.name + "\n")

    EMpoint = em_tracking.EM_track(run)
    output.write(str(EMpoint[1][0]) + "\n")

    optipoint = opti_tracker.opti_track(run)
    output.write(str(optipoint[1][0]) + "\n")


    output.write(str(distortion_calibration.distortion_calibration(run)))


if __name__ == '__main__':
    main()