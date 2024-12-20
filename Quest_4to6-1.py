
from array import array
import numpy as np


def RotX(theta: float):
    '''retursn a Rotation Matrix for X-axis rotations given theta'''

    myCos = round(np.cos(theta), 3)
    mySin = round(np.sin(theta), 3)

    rot = np.mat([[1, 0, 0], [0, myCos, -mySin],
                  [0, mySin, myCos]])
    return rot


def RotY(theta: float):
    '''returns a Rotation Matrix for Y-axis rotations given theta'''

    myCos = round(np.cos(theta), 3)
    mySin = round(np.sin(theta), 3)

    rot = np.mat([[myCos, 0, mySin], [0, 1, 0],
                  [-mySin, 0, myCos]])
    return rot


def RotZ(theta: float):
    '''returns a Rotation Matrix for Z-axis rotations given theta'''

    myCos = round(np.cos(theta), 3)
    mySin = round(np.sin(theta), 3)

    rot = np.mat([[myCos, -mySin, 0], [mySin, myCos, 0],
                  [0, 0, 1]])
    return rot


def Euler(theta1, theta2, theta3):
    '''A common method of specifying a rotation matrix in terms of three independent quantities
    ZYZ. theta1 = phi, theta2 = theta, theta3 = psi'''
    c_phi = round(np.cos(theta1), 3)
    c_the = round(np.cos(theta2), 3)
    c_psi = round(np.cos(theta3), 3)

    s_phi = round(np.sin(theta1), 3)
    s_the = round(np.sin(theta2), 3)
    s_psi = round(np.sin(theta3), 3)

    euler = np.mat([[c_phi*c_the*c_psi - s_phi*s_psi, -c_phi*c_the*s_psi - s_phi*c_psi, c_phi*s_the],
                    [s_phi*c_the*c_psi + c_phi*s_psi, -s_phi * c_the*s_psi + c_phi*c_psi, s_phi*s_the], [-s_the*c_psi, s_the*s_psi, c_the]])

    return euler


def RPY(theta1, theta2, theta3):
    '''A rotation matrix R can also be described as a product of successive rotations about the principal coordinate axes x0, y0, and z0 taken in a specific order
    XYZ in the fixed frame. theta1 = phi, theta2 = theta, theta3 = psi'''
    c_phi = round(np.cos(theta1), 3)
    c_the = round(np.cos(theta2), 3)
    c_psi = round(np.cos(theta3), 3)

    s_phi = round(np.sin(theta1), 3)
    s_the = round(np.sin(theta2), 3)
    s_psi = round(np.sin(theta3), 3)

    rpy = np.mat([[c_phi*c_the, -s_phi*c_psi + c_phi*s_the*s_psi, s_phi*s_psi + c_phi*s_the*c_psi],
                  [s_phi*c_the, c_phi*c_psi + s_phi*s_the*s_psi, -c_phi*s_psi + s_phi*s_the*c_psi], [-s_the, c_the*s_psi, c_the*c_psi]])

    return rpy


def FK(DH: array):
    '''DH contains the DH parameters which are link length, link twist, link offset, and joint angle'''
    a_len = DH[0]
    a_alp = DH[1]
    d_off = DH[2]
    t_the = DH[3]

    c_alp = round(np.cos(a_alp), 3)
    s_alp = round(np.sin(a_alp), 3)
    c_the = round(np.cos(t_the), 3)
    s_the = round(np.sin(t_the), 3)

    fk = np.mat([[c_the, -s_the*c_alp, s_the*s_alp, a_len*c_the],
                 [s_the, c_the*c_alp, -c_the*s_alp, a_len*s_the], [0, s_alp, c_alp, d_off], [0, 0, 0, 1]])

    return fk


def main():
    '''main where we call functions to test them'''
    theta = np.pi / 2
    print("Theta is: " + str(round(theta, 3)))

    print("Rotation in X:")
    R = RotX(theta)
    print(R)
    print("Rotation in Y:")
    R = RotY(theta)
    print(R)
    print("Rotation in Z:")
    R = RotZ(theta)
    print(R)
    print()

    print("Euler Rotation:")
    print("Input: 0, " + str(round(theta, 3)) + ", 0")
    R = Euler(0, theta, 0)
    print(R)
    print()

    print("Roll Pitch Yaw Rotation:")
    print("Input: " + str(round(theta, 3)) + ", " +
          str(round(theta, 3)) + ", " + str(round(theta, 3)))
    R = RPY(theta, theta, theta)
    print(R)
    print()

    print("Input: a=" + str(1) + ", alpha=" + str(round(theta, 3)) +
          ", d=" + str(1) + ", theta=" + str(round(theta, 3)))
    DH = [float(1), float(theta), float(1), float(theta)]
    R = FK(DH)
    print(R)
    print()


main()
