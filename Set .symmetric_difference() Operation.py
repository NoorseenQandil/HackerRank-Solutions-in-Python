# Enter your code here. Read input from STDIN. Print output to STDOUT
n1=input()
li1 = input().split()
s1 = set(li1)
n2=input()
li2 = input().split()
s2 = set(li2)
s1s2 = s1.symmetric_difference(s2)
print(len(s1s2))
