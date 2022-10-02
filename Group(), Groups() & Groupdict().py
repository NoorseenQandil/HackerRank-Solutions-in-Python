# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
a = re.findall(r"([A-Za-z0-9])\1+",
input()) 
if a: 
    print(a[0]) 
else: 
    print(-1)
