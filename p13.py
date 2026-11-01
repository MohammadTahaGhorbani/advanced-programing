x = float(input("x: "))
y = float(input("y: "))
s=0
for n in range (101):
    s=s+1 /(x+y)**n
print(s)    
