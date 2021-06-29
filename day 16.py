#multiply argument x with y
a=lambda x,y:x*y
print(a(5,6))

#output
'''
30
'''
#create fibonacci series

from functools import reduce
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])
print(fib(5))
'''
output
[0, 1, 1, 2, 3]
'''


#counting even numbers in a list
# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]
even_count = len(list(filter(lambda x: (x%2 == 0) , list1)))
print("Even numbers in the list: ", even_count)
'''
output
Even numbers in the list: 3
'''

#divisible by 9
num_list = [45, 55, 60, 37, 100, 105, 220]
result = list(filter(lambda x: (x % 9 == 0), num_list))
print("Numbers divisible by 9 are",result)

'''
output
Numbers divisible by 9 are [45]
'''

#multiply each number of a list by a given number
nums = [2, 4, 6, 9 , 11]
n = 2
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))

'''
output
Original list:  [2, 4, 6, 9, 11]
Given number:  2
Result:
4 8 12 18 22
'''
