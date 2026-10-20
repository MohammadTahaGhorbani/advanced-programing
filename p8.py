import sys
import random
n = int(sys.argv[1])
a = [random.randint(0,100) for i in range(n)]
print(a)
average = float(sum(a)) / len(a)
print('average:' + str(average))