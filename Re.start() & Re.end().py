# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s=input()
k=input()

if (k not in s):
    print("(-1, -1)")
else:
    start_index=0
    while (len(s) > 0):
        m = re.search(f"({k})", s)
        if m:
            not_found=None
            print("(" + str(m.start()+start_index) + ", " + str(m.end()+start_index-1) + ")")
            start_index=start_index+m.start()+1
            s=s[m.start()+1:]
        else:
            break
