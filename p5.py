import sys
n = int(sys.argv[1])
binary = ""
while n > 0:
    remainder = n % 2
    binary =  str(remainder) + binary 
    n = n // 2
print(binary)