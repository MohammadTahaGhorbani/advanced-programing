import math

def hypot(a, b):
    return math.sqrt(a*a + b*b)


a = float(input("Enter a: "))
b = float(input("Enter b: "))

print(hypot(a, b))