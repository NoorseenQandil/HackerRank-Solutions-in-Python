# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
k,rooms=int(input()),Counter(list(map(int, input().rsplit())))
[print(i) for i,j in rooms.items() if j==1]
