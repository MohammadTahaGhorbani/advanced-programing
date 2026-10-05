import sys
year= int(sys.argv[1])
leap=(year%4==0)
leap=leap and (year%100!=0)
leap=leap or (year%400==0)
print (leap)