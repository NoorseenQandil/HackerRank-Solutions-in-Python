# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n=int(input())
for _ in range(n):
    cc=input()
    if (re.fullmatch(r"^[456]\d{3}(-?\d{4}){3}$", cc) and \
         not re.search(r"([0-9])(-?\1){3}", cc)):
        print("Valid")
    else:
        print("Invalid")
