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

    # Preliminary code to simplify file operations later
    run = 0
    runtype = 0
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    type = ['debug', 'unknown']
    output = open("pa1-" + type[runtype] + "-" + letters[run] + "-testoutput.txt", "w")
    np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

    calreadingsArr = glob.glob('Data/pa1-' + type[runtype] + '-' + letters[run] + '-calreadings.txt')
    # Reading in calreadings file to print Nc and Nframes to output file
    calreadingsF = open(calreadingsArr[0], 'r')
    calreadingsLines = calreadingsF.read().splitlines()
    calreadingsSplit = calreadingsLines[0].split(',')

    # Assigning Nc and Nframes, and writing those along with the output filename to the output file
    Nc = calreadingsSplit[2].strip()
    Nf = calreadingsSplit[3].strip()
    output.write(Nc + ", " + Nf + ", " + output.name + "\n")

    # Running EM tracker calibration, adding point values to output file
    EMpoint = np.around(em_tracking.EM_track(run, runtype), 2)
    output.write("  " + str(EMpoint[0][0]) + ",   " + str(EMpoint[0][1]) + ",   " + str(EMpoint[0][2]) + "\n")

    # Running optical tracker calibration, adding point values to output file
    optipoint = np.around(opti_tracker.opti_track(run, runtype), 2)
    output.write("  " + str(optipoint[0][0]) + ",   " + str(optipoint[0][1]) + ",   " + str(optipoint[0][2]) + "\n")

    Distortion_calibration = np.around(distortion_calibration.distortion_calibration(run, runtype), 2)
    for i in range(len(Distortion_calibration)):
        for j in range(len(Distortion_calibration[i])):
            output.write("  " + str(Distortion_calibration[i][j]))
            if (j < len(Distortion_calibration[i]) - 1):
                output.write(", ")
        output.write("\n")


if __name__ == '__main__':
    main()
