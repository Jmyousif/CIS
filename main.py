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
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    output = open("pa1-debug-" + letters[run] + "-testoutput1.txt", "w")

    calreadingsArr = glob.glob('Data/pa1-debug-a-calreadings.txt')
    # Reading in calreadings file to print Nc and Nframes to output file
    calreadingsF = open(calreadingsArr[run], 'r')
    calreadingsLines = calreadingsF.read().splitlines()
    calreadingsSplit = calreadingsLines[0].split(',')

    # Assigning Nc and Nframes, and writing those along with the output filename to the output file
    Nc = calreadingsSplit[2].strip()
    Nf = calreadingsSplit[3].strip()
    output.write(Nc + ", " + Nf + ", " + output.name + "\n")

    # Running EM tracker calibration, adding point values to output file
    EMpoint = em_tracking.EM_track(run)
    output.write(str(EMpoint[1][0]) + "\n")

    # Running optical tracker calibration, adding point values to output file
   # optipoint = opti_tracker.opti_track(run)
    #output.write(str(optipoint[1][0]) + "\n")

    
    #Distortion_calibration = distortion_calibration.distortion_calibration(run)
    #output.write(str(Distortion_calibration))


if __name__ == '__main__':
    main()
