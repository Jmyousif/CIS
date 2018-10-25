import Frame
import three_dimension_transform
import point_transformations
import pivot_calibration
import opti_tracker
import em_tracking
import numpy as np

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






if __name__ == "__main__":
    unit_testing()