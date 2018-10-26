import Frame
import three_dimension_transform
import point_transformations
import pivot_calibration
import opti_tracker
import em_tracking
import numpy as np
import glob
import em_tracking
import opti_tracker
import distortion_calibration

class unit_testing():
    #testing Constructor
    testMatrix1 = np.zeros((3, 3))
    testVector1 = np.zeros((3, 1))
    testFrame1 = Frame.Frame(testMatrix1, testVector1)
    assert (testFrame1.getRot() == np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])).all()
    assert (testFrame1.getTr() == np.array([[0], [0], [0]])).all()

    #Testing setRot
    testFrame1.setRot(np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]))
    assert (testFrame1.getRot() == np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])).all()

    #Testing setTr
    testFrame1.setTr(np.array([[1], [2], [3]]))
    assert (testFrame1.getTr() == np.array([[1], [2], [3]])).all()

    #Testing Invert
    testFrameInv = testFrame1.invert()
    assert (testFrameInv.getRot() == np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])).all()

    #Testing FFmult
    testMatrix2 = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
    testVector2 = np.array([[3], [2], [1]])
    testFrame2 = Frame.Frame(testMatrix2, testVector2)
    testFFprod = testFrame1.FFmult(testFrame2)
    assert (testFFprod.getRot() == np.array([[0, -1, 0], [0, 0, 1], [-1, 0, 0]])).all()
    assert (testFFprod.getTr() == np.array([[-1], [5], [4]])).all()
    assert (testFFprod.getTr() == (np.array([[-1], [5], [4]]))).all()

    #Testing FPmult
    testVector3 = np.array([[7], [9], [5]])
    testFPprod = testFrame1.FPmult(testVector3)
    assert (testFPprod == np.array([[-8], [9], [8]])).any()


    #To test with read-in files, asserting that each file is the same as the given output file
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for i in range(len(letters)):
        output = open("pa1-debug-" + letters[i] + "-testoutput2.txt", "w")

        calreadingsArr = glob.glob('Data/pa1-debug-' + letters[i] + '-calreadings.txt')
        # Reading in calreadings file to print Nc and Nframes to output file
        calreadingsF = open(calreadingsArr[i], 'r')
        calreadingsLines = calreadingsF.read().splitlines()
        calreadingsSplit = calreadingsLines[0].split(',')

        # Assigning Nc and Nframes, and writing those along with the output filename to the output file
        Nc = calreadingsSplit[2].strip()
        Nf = calreadingsSplit[3].strip()
        output.write(Nc + ", " + Nf + ", " + output.name + "\n")

        # Running EM tracker calibration, adding point values to output file
        EMpoint = em_tracking.EM_track(i)
        output.write(str(EMpoint[1][0]) + "\n")

        # Running optical tracker calibration, adding point values to output file
        optipoint = opti_tracker.opti_track(i)
        output.write(str(optipoint[1][0]) + "\n")

        Distortion_calibration = distortion_calibration.distortion_calibration(i)
        output.write(str(Distortion_calibration))




if __name__ == "__main__":
    unit_testing()