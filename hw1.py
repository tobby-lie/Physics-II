from math import *

proton_mass = 1.67262158E-27
proton_charge = 1.602E-19
electron_charge = 1.602E-19
the_constant = 9E9


def unitVec(vec):
    sum = 0
    for point in vec:
        sum += point**2
    mag_electric_field = sqrt(sum)

    unitVec = []
    for point in vec:
        unitVec.append(point/mag_electric_field)

    return unitVec


def electric_force(charge, vec):
    # F = qE
    return [(charge)*point for point in vec]


def magnitude_electric_field(charge, distance):
    the_constant = 9E9
    return "{:e}".format(the_constant*(charge/(distance**2)))


def magnitude_electric_field_location(charge, acceleration, mass):
    # F = ma
    # E = F/q
    F = mass*acceleration
    return F/charge


# Essential skills


def get_y_component(S, P):
    sum = 0
    vector_r = []
    for s, p in zip(S, P):
        sum += (s-p)**2
        vector_r.append(p-s)
    mag_r = sqrt(sum)
    return [r/mag_r for r in vector_r]


def distance_between(S, P):
    sum = 0
    for s, p in zip(S, P):
        sum += (s-p)**2
    return sqrt(sum)


def electrons_lost(net_charge, charge):
    # number of electrons lost n = net-charge/charge
    return (net_charge/charge)*(10**-12)


def two_point_particles(distance, q1, q2):
    the_constant = 9E9
    return (((the_constant)*(q1*(10**-9))*(q2*(10**-9)))/((distance*.01)**2))*(1E+6)


def test_charge(force, charge):
    return ((force)*(10**-6))/((charge)*(10**-9))
