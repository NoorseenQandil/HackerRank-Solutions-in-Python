# Enter your code here. Read input from STDIN. Print output to STDOUT
lower = []
upper = []
odd = []
even = []
for i in input():
    try:
        if int(i)/2 != round(int(i)/2):
            odd.append(i)
        elif int(i)/2 == round(int(i)/2):
            even.append(i)
    except:
        if i == i.lower():
            lower.append(i)
        else:
            upper.append(i)
print(*(sorted(lower) + sorted(upper) + sorted(odd) + sorted(even)), sep = '')
