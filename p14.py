import random
import math

a = []

for i in range(10):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    a.append((x, y))

f = 1000

for i in range(10):
    for j in range(i+1, 10):
        d = math.sqrt((a[i][0]-a[j][0])**2 + (a[i][1]-a[j][1])**2)

        if d < f:
            f = d

print(a)
print(f)