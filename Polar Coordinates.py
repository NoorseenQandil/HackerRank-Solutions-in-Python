# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan2

z = complex(input())
x,y = z.real, z.imag
r = (x**2+y**2)**.5
phi = atan2(y,x)

print(r)
print(phi)
