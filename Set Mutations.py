# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    coms = list(input().split())
    a = set(map(int, input().split()))
    if coms[0] == 'intersection_update' or 'update' or 'symmetric_difference_update' or 'difference_update':
        eval(f"s.{coms[0]}(a)")

print(sum(s))
