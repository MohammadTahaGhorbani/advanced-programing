import math

def phi(z):
    if z < -8.0:
        return 0.0

    if z > 8.0:
        return 1.0

    total = 0.0
    term = z
    i = 3

    while total != total + term:
        total += term
        term *= z * z / float(i)
        i += 2

    return 0.5 + (
        math.exp(-z*z/2) / math.sqrt(2*math.pi)
    ) * total


z = float(input("Enter z: "))
print(phi(z))