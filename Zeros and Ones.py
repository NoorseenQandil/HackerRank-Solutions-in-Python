# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
nums = tuple(map(int, input().split()))
print (numpy.zeros(nums, dtype = numpy.int))
print (numpy.ones(nums, dtype = numpy.int))
