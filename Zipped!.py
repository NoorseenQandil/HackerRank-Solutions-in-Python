# Enter your code here. Read input from STDIN. Print output to STDOUT
marks = [[float(j) for j in input().split()] for i in range(int(input().split()[1]))]
for i in zip(*marks):
    print(sum(i)/len(i))
