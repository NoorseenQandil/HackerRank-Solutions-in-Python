# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string = input()
pattern = re.finditer(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', string)
match = [i for i in map(lambda x: x.group(), pattern)]
print(*match, sep='\n') if match != [] else print(-1)
