# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=list(map(int,input().split()))#getting Values

for x in range(1,n,2):
    print((".|."*x).center(m,"-"))

print("WELCOME".center(m,"-"))

for x in range(n-2,0,-2):
    print((".|."*x).center(m,"-"))
