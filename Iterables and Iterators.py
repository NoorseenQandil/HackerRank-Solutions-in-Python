# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
N = int(input())
s = input().replace(' ', '')
k = int(input())
c = list(combinations(s, k))
a = [i for i in c if "a" in i]
print(len(a)/len(c))
