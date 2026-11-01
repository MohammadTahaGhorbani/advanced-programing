a=[1]
for i in range(9):
    print(a)
    b=[1]
    for j in range (len(a)-1):
        b.append(a[j]+a[j+1])
    b.append(1)
    a=b