def cube(i):
    j = i * i * i
    return j


n = int(input('n: '))

for i in range(1, n+1):
    print("%s %s" % (i, cube(i)))