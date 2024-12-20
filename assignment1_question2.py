'''
# Assignment1_Q2
#    Write python functionS to compute, from Matrix A and B
#       and Vector p, AB, Ap, A^Tp, p1 * p2, p1^T * p2, and
#       A1A2A3A4A5A6A7
#
#  Fuctions:
#    Matrix&Vector Multiplication, Transpose Matrix/Vector,
#    Inverse Matrix/Vector, Multiple Matrix Multiplication,
#    Matrix Multiplication Checker
#
#  Requirements:
#    functions work for all reasonable size matrixes and vectors.
#       ie: up to 10x10 functions check dimension matching.
#       ie: checks if matrixes can multiply
#       (EX: 3x1 matrix can't multiply with a 2x1 but a 3x1 can
#       with a 1x2)
#    functions are properly commented
'''
import numpy as np


class InvalidMatrix(Exception):
    '''execption passed if user inputs invalid matrixes'''

# Fuction 1: Valid Matrix Multiplication Checker

# Checks if the dimensions of two matrixes match, validations
# for multiplication. If the number of columns of the 1st matrix
# does not equal the number of rows in the 2nd matrix you cannot
# multiply the two matrixes


def is_mat_mult_valid(matrix1: np.matrix, matrix2: np.matrix):
    '''checks if you can do matrix multiplication given two matrixes, ie: dimension matching'''

    result = True

    # checks if the number of columns of the 1st matrix equals
    # the number of rows in the 2nd matrix and that the two
    # matrixes are not empty
    if (matrix1.shape[1] != matrix2.shape[0]) | (matrix1.size == 0) | (matrix2.size == 0):
        result = False

    return result


# fuction 2: Matrix||Vector Multiplication

# checks if two matrixes can multiply and then multiplys the two matrixes
# the dimensions we care about are 1st matrix column's and 2nd matrix row's


def matrix_multiply(matrix1: np.matrix, matrix2: np.matrix):
    '''multiplies two matrixes(or vectors) only if they are valid to be
    multiplied, otherwise throws a InvalidMatrix exception'''

    # this fuction checks that matrix1 and matrix2 have the matching
    # dimensions necessary to do matrix multiplication
    if is_mat_mult_valid(matrix1, matrix2):
        product = matrix1 * matrix2  # multiplication of the matrixes

    else:
        # if the dimesions don't match then the matrixes can't multiply
        # hence an invalid arguements error is thrown
        raise InvalidMatrix(
            "The matrixes provided don't have valid dimensions for matrix multiplication")

    return product


def get_transpose(matrix: np.matrix):
    '''unneccessary function to get the transpose of a matrix/vector'''
    return matrix.transpose


def get_inverse(matrix: np.matrix):
    '''unneccessary function to get the inverse of a matrix/vector'''
    return matrix.getI


def vector_multiply(vector1: np.matrix, vector2: np.matrix):
    '''vector multiplication'''

    if (vector1.shape[0] != 1 | vector2.shape[0] != 1 |
            vector1.shape[1] != vector2.shape[1]):
        raise InvalidMatrix(
            "The vectors provided are either not vectors, or do not have the same dimensions")
    else:
        for j in range(int(vector1.shape[1])):
            vector1[0][j] = vector1[0][j]*vector2[0][j]

    return vector1


def seven_matrix_multiply(matrix1: np.matrix, matrix2: np.matrix, matrix3: np.matrix, matrix4: np.matrix, matrix5: np.matrix, matrix6: np.matrix, matrix7: np.matrix):
    '''multiplies seven matrixes only if they are valid to be
    multiplied, otherwise throws a InvalidMatrix exception'''

    # this fuction checks that matrix1 and matrix2 have the matching
    # dimensions necessary to do matrix multiplication
    if is_mat_mult_valid(matrix1, matrix2) & is_mat_mult_valid(matrix2, matrix3) & is_mat_mult_valid(matrix3, matrix4) & is_mat_mult_valid(matrix4, matrix5) & is_mat_mult_valid(matrix5, matrix6) & is_mat_mult_valid(matrix6, matrix7):
        product = ((((((matrix1 * matrix2) * matrix3) * matrix4) * matrix5)
                   * matrix6)*matrix7)  # multiplication of the matrixes

    else:
        # if the dimesions don't match then the matrixes can't multiply
        # hence an invalid arguements error is thrown
        raise InvalidMatrix(
            "The matrixes provided don't have valid dimensions for matrix multiplication")

    return product
