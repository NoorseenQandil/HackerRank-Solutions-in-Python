# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

m, n = map(int, input().split())
a = np.array([list(map(int, input().split())) for _ in range(m)], np.int64)
b = np.array([list(map(int, input().split())) for _ in range(m)], np.int64)
print(f"{a+b}\n{a-b}\n{a*b}\n{a//b}\n{a%b}\n{a**b}")
