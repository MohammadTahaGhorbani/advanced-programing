def cdf(z, mu=0.0, sigma=1.0):
    return phi((z - mu) / sigma)


z = float(input("Enter z: "))
mu = float(input("Enter mean: "))
sigma = float(input("Enter sigma: "))

if sigma <= 0:
    print("Sigma must be positive")
else:
    print(cdf(z, mu, sigma))