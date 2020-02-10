from math import *

# 16.35


def max_potential_difference(E, d):

    # E = V/d
    # V = E*d
    return E * (d * (10**(-3)))


epsilon = 8.85e-12

# 16.66


def field_in_capacitor(Q, r):
    # a
    # E = Q/(epsilon*A)
    # A = pi*r^2

    return (Q*(10**(-6)))/(epsilon*(pi*(r**(2))))


def potential_difference(E, s1):
    # b
    # deltaV_AB = -E * s1
    return -E * s1


def potential_difference_C_to_A(L_x, E_x):
    # d
    return -E_x * L_x

# 18.25


def absolute_val_I2(I1, I3, I4):
    # a
    # I1 + I4 = I2 + I3
    # I2 = I1 + I4 - I3
    return I1 + I4 - I3


D_molecules = 3.011e23
qe = 1.6e-19


def hours_light_lit(I):
    # b
    n = I/qe
    T = D_molecules/n
    return T/3600
