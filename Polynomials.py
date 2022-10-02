# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n = list(map(float,input().split()));
m = input();
print(numpy.polyval(n,int(m)));
