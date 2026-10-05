import sys
import math
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
delta = b**2 - 4*a*c
if delta>=0:
    print((-b + (math.sqrt(delta)))/ (2*a))
    print((-b - (math.sqrt(delta))) / (2*a))
elif delta<0:
    print (-b + ( 1j * (math.sqrt(-(delta))))/ 2*a)
    print('hi')