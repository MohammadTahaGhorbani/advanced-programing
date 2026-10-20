import sys
import random
n = int(sys.argv[1])
a = [random.randint(0,100) for i in range(n)]
print(a)
for v in a :
    print(v)