# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n,_ = map(int,input().split())
my_array = np.array([list(map(int,input().split())) for _ in range(n)])
print(np.mean(my_array,1), np.var(my_array,0), round(np.std(my_array),11), sep = "\n") 
