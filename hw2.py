from math import *
import numpy as np

k_constant = 9E9

# 13.47


def electric_field(q, location_1, location_2):
    # a & b
    # E = (k*(q/(r^2)))*r_hat
    # micro-C = 1E-6C
    q = q*(1E-6)
    r_vector = np.array(
        [a_i*.01 - b_i*.01 for a_i, b_i in zip(location_1, location_2)])
    sum_of_squares = sum([(point**2) for point in r_vector])
    distance = ((sqrt(sum_of_squares)))
    r_hat = r_vector/distance
    print(r_hat)
    return ((k_constant*(q/(distance**2)))*r_hat)


def net_electric_field(electric_fields):
    electric_fields = [np.array(electric_field)
                       for electric_field in electric_fields]
    return sum(electric_fields)


def net_force(q, E_net):
    q = q*(1E-6)
    E_net = np.array(E_net)
    return q*E_net

# 13.49

# 15.22

# 15.28

# 15.26
