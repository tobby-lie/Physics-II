from math import *

# 19.38

epsilon = 8.85E-12


def capacitance(w, h, d):
    # capacitance =  (epsilon*A)/d
    A = (w*(10**(-2)))*(h*(10**(-2)))
    return (epsilon*A)/(d*(10**(-3)))

# 16.50


def potential_difference_points(Q, r, t, s):
    E = (Q)/(pi*(r**2)*epsilon)
    v_1 = E*(((t*10**(-3))/2))
    v_2 = (t*10**(-3))/2
    v_2 += (s*10**(-3))/2
    v_2 *= E
    return -(v_2-v_1)

# 16.64


k_constant = 9E9

# a


def charge_ionize(E, L, r):
    # Q = (E*L*r)/(2*k)
    return (E*L*(10**(-2))*r*(10**(-3)))/(2*k_constant)

# b


def v_max(Q, L, r, R):
    # v_max = ((2*Q*k)/L)*ln(R/r)
    r = r*(10**(-3))
    R = R*(10**(-2))
    L = L*(10**(-2))
    v_max = (2*Q*k_constant)/L
    return v_max*log(R/r)

# 19.76


def deflection_plates(R, w, h, d, max_voltage, reach):
    capacitance = ((w*(10**(-2)))*(h*(10**(-2))))*(epsilon)/(d*(10**(-3)))
    left_side = (reach/max_voltage) - 1
    return -1*(R)*(capacitance)*log(-1*left_side)
