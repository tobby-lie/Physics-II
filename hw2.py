from math import *
import numpy as np
from operator import add
from termcolor import colored, cprint

k_constant = 9E9
epsilon = 8.85e-12

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
    q = q*(1E-9)
    E_net = np.array(E_net)
    return q*E_net

# 13.49


def electric_field_by_ion(q, distance):
    # beginning of all parts
    return k_constant*(q/(((distance*(10**-9))**2)))


def net_field(section, q1, q2, r, total_distance):
    if (section == 'a'):
        E1 = electric_field_by_ion(q1, (total_distance-r))
        E2 = electric_field_by_ion(q2, r)
        return E1 + E2
    elif (section == 'b'):
        E1 = electric_field_by_ion(q1, (total_distance+r))
        E2 = electric_field_by_ion(q2, r)
        return E1 - E2


def force_electron(q, E):
    return q*E

# 15.22


def length_piece(total_length, pieces):
    # a
    return total_length/pieces

# b just do by hand


def charge_piece(total_charge, pieces):
    # c
    return total_charge/pieces


def electric_field_piece(x, y, charge, pieces):
    r = sqrt(((x)**2)+((y)**2))
    print(r)
    print(x)
    print(y)
    q = charge
    r_vec = np.array([x, y, 0])
    r_hat = r_vec/r
    print(r_hat)
    return ((k_constant)*(q/((r)**2)))*r_hat

# 15.28


def electric_field_piece_1(length, net_charge, location_vec):
    # a
    x_component = ((9e9)*(length/3)*(net_charge*(10**-9))) / \
        (3*((((length/3)**2)+(location_vec[1]**2))**(3/2.)))
    y_component = ((9e9)*(location_vec[1])*(net_charge*(10**-9))) / \
        (3*((((length/3)**2)+(location_vec[1]**2))**(3/2.)))
    return [x_component, y_component]


def electric_field_piece_2(length, net_charge, location_vec):
    # b
    return ((9e9)*(net_charge*(10**-9)))/(3*(location_vec[1]**2))


def electric_field_piece_3(length, net_charge, location_vec):
    # c
    x_component = (-(9e9)*(length/3)*(net_charge*(10**-9))) / \
        (3*((((length/3)**2)+(location_vec[1]**2))**(3/2.)))
    y_component = ((9e9)*(location_vec[1])*(net_charge*(10**-9))) / \
        (3*((((length/3)**2)+(location_vec[1]**2))**(3/2.)))
    return [x_component, y_component]


def net_electric_field_at_A(E1, E2, E3):
    # d
    return [sum(x) for x in zip(E1, E2, E3)]

# 15.26


def initial_acceleration_coal_dust(times, L, Q, d, alpha, m):
    # a & b
    a_d = (((Q**2)*alpha)/((4)*(pi**2)*(epsilon**2)*(L**2)*(m)*((times*d*.01)**3)))
    a = (((Q**2)*alpha)/((4)*(pi**2)*(epsilon**2)*(L**2)*(m)*((d*.01)**3)))
    print("Initial acceleration = {}".format(colored(str(a), 'red')))
    cprint("If the speck of coal dust were initially {} times as far from the charged wire, the initial acceleration of the speck would be {} times smaller".format(
        colored(str(times), 'red'), colored(str(a_d/a), 'red')))
