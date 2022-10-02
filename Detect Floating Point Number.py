# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    if re.match('^[+-]{0,1}[\d]{0,}\.\d+$', input()):
        print(True)
    else:
        print(False)
