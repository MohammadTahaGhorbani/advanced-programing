def harmonic(n, m=1):
    total = 0.0

    for i in range(1, n+1):
        total += 1.0 / (i ** m)

    return total


n = int(input("Enter n: "))
m = int(input("Enter m: "))

print(harmonic(n, m))