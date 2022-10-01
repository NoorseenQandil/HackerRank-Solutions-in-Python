# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter
x = int(input())
sizes = list(map(int,input().split()))
n = int(input())
sizes = Counter(sizes)
pr = 0
for i in range(n):
    sz,pz = map(int,input().split())
    if(sizes[sz]):
        sizes[sz] -= 1
        pr += pz
print(pr)
