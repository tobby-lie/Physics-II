# 20.31

# b


def potential_difference_12_V1(w, B):
    m = 1.66E-27
    w *= .01
    R = w/2
    return ((1.6E-19)*(R**2)*(B**2))/(2*12*m)


def potential_difference_12_V2(w, B, L):
    L *= .01
    m = 1.66E-27
    w *= .01
    R = w/2
    return ((1.6E-19)*R*L*(B**2))/(12*m)

# c


def potential_difference_14_V1(w, B):
    m = 1.66E-27
    w *= .01
    R = w/2
    return ((1.6E-19)*(R**2)*(B**2))/(2*14*m)


def potential_difference_14_V2(w, B, L):
    L *= .01
    m = 1.66E-27
    w *= .01
    R = w/2
    return ((1.6E-19)*R*L*(B**2))/(14*m)

# 20.56

# b


def drift_speed_v(V, L, B):
    L *= .01
    return abs(V/L)/B

# c


def mobility_u(v, V, L):
    L *= .01
    return v/(abs(V)/L)

# d


def mobile_charges(I, w, h, V_f):
    h *= .01
    w *= .01
    return I/((1.6E-19)*w*h*V_f)

# e


def resistance(V, I):
    return V/I

# 20.63

# 3


def F_net(V, B):
    return (V*B)*1.6E-19

# 4


def F_mag(V, B):
    return (V*(1.6E-19)*B)

# 5


def potential_difference(B, V, L):
    return (B*V*L)
