import Frame
import three_dimension_transform
import pivot_calibration
import numpy as np
import em_tracking
import opti_tracker
import distortion_calibration
import glob


class unit_testing:
    # Testing Constructor
    testMatrix1 = np.zeros((3, 3))
    testVector1 = np.zeros((3, ))
    testFrame1 = Frame.Frame(testMatrix1, testVector1)
    assert np.array_equal(testFrame1.getRot(), np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    assert np.array_equal(testFrame1.getTr(), np.array([0, 0, 0]))

    # Testing setRot
    testFrame1.setRot(np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]))
    assert np.array_equal(testFrame1.getRot(), np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]))

    # Testing setTr
    testFrame1.setTr(np.array([1, 2, 3]))
    assert np.array_equal(testFrame1.getTr(), np.array([1, 2, 3]))

    # Testing Invert
    testFrameInv = testFrame1.invert()
    assert np.array_equal(testFrameInv.getRot(), np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]]))

    # Testing FFmult
    testMatrix2 = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
    testVector2 = np.array([3, 2, 1])
    testFrame2 = Frame.Frame(testMatrix2, testVector2)
    testFFprod = testFrame1.FFmult(testFrame2)
    assert np.array_equal(testFFprod.getRot(), np.array([[0, -1, 0], [0, 0, 1], [-1, 0, 0]]))
    assert np.array_equal(testFFprod.getTr(), np.array([-1, 5, 4]))
    assert np.array_equal(testFFprod.getTr(), (np.array([-1, 5, 4])))

    # Testing FPmult
    testVector3 = np.array([7, 9, 5])
    testFPprod = testFrame1.FPmult(testVector3)
    assert np.array_equal(testFPprod, np.array([-8, 9, 8]))

    # Testing pivot calibration
    # TestMatrix2 = [[0, 0, 1], [0, 1, 0], [-1, 0, 0]], testVector3 = [7, 9, 5]
    p_list = pivot_calibration.pivot_calibration(testMatrix2, testVector3, 1)
    array = np.asarray([3.5, 4.5, 2.5])
    assert np.allclose(p_list[1], np.asarray([3.5, 4.5, 2.5]))
    # The unknown p_t in this problem should be [3.5, 4.5, 2.5].

    # Testing Three-Dimensional Transform, rotation with
    # [[0, -1, 0], [1, 0, 0], [0, 0, 1]] and then translation with
    # [3, 2, 1]
    pointset1 = np.array([[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9],
                          [8, 9, 10], [9, 10, 11]])
    pointset2 = np.array([[2, 2, 3], [1, 3, 4], [0, 4, 5], [-1, 5, 6], [-2, 6, 7], [-3, 7, 8], [-4, 8, 9],
                          [-5, 9, 10], [-6, 10, 11], [-7, 11, 12]])
    threedframe = three_dimension_transform.rigid_transform(pointset1, pointset2)
    # 90 degree rotation matrix, add 3,2,1

    # Testing Distortion Calibration
    outputArr = glob.glob('Data/pa1-debug-a-output1.txt')
    outputF = open(outputArr[0], "r")
    outputLines = outputF.read().splitlines()
    outputSplit = [[0 for x in range(3)] for y in range(len(outputLines))]
    for num in range(len(outputLines)):
        outputSplit[num] = outputLines[num].split(',')
        for x in range(len(outputSplit[num])):
            outputSplit[num][x] = outputSplit[num][x].strip()
    np.testing.assert_almost_equal(distortion_calibration.distortion_calibration(0, 0),
                        np.asarray(outputSplit[3:][:]).astype(float), decimal=2)
    np.testing.assert_almost_equal(np.subtract(distortion_calibration.distortion_calibration(0, 0),
                        np.asarray(outputSplit[3:][:]).astype(float)).round(1), np.asarray(np.zeros((216, 3))))

    # Testing EM_Tracker on pa1-a and comparing with its given output file
    assert (np.allclose(em_tracking.EM_track(0, 0)[0], np.asarray([202.89, 190.20, 201.55])))

    # Testing Optical_Tracker
    assert (np.allclose(opti_tracker.opti_track(0, 0)[0], np.asarray([403.49, 390.87, 199.8])))

    # #To test with read-in files
    # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # for i in range(len(letters)):
    #     output = open("pa1-debug-" + letters[i] + "-testoutput2.txt", "w")
    #
    #     calreadingsArr = glob.glob('Data/pa1-debug-' + letters[i] + '-calreadings.txt')
    #     # Reading in calreadings file to print Nc and Nframes to output file
    #     calreadingsF = open(calreadingsArr[i], 'r')
    #     calreadingsLines = calreadingsF.read().splitlines()
    #     calreadingsSplit = calreadingsLines[0].split(',')
    #
    #     # Assigning Nc and Nframes, and writing those along with the output filename to the output file
    #     Nc = calreadingsSplit[2].strip()
    #     Nf = calreadingsSplit[3].strip()
    #     output.write(Nc + ", " + Nf + ", " + output.name + "\n")
    #
    #     # Running EM tracker calibration, adding point values to output file
    #     EMpoint = em_tracking.EM_track(i)
    #     output.write(str(EMpoint[1][0]) + "\n")
    #
    #     # Running optical tracker calibration, adding point values to output file
    #     optipoint = opti_tracker.opti_track(i)
    #     output.write(str(optipoint[1][0]) + "\n")
    #
    #     Distortion_calibration = distortion_calibration.distortion_calibration(i)
    #     output.write(str(Distortion_calibration))




if __name__ == "__main__":
    unit_testing()