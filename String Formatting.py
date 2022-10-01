def print_formatted(number):
    # your code goes here
    d = len(bin(number)[2:])
    for i in range(1, number+1):
        on = oct(i)[2:]
        hn = hex(i)[2:].upper()
        bn = bin(i)[2:]
        print(str(i).rjust(d), on.rjust(d),hn.rjust(d), bn.rjust(d))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
