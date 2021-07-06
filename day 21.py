# 1. Write a program using zip() function and list() function, create amerged list of tuples from the two lists given.

def merge(list1, list2):
      
    merged_list = tuple(zip(list1, list2)) 
    return merged_list
      
list1 = ['Sachin','Ms','Suresh']
list2 = ['Tendulkar', 'Dhoni', 'Raina']
print(merge(list1, list2))
'''
o/p

(('Sachin', 'Tendulkar'), ('Ms', 'Dhoni'), ('Suresh', 'Raina'))
'''
# 2.First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuple
R = list(range(1,8))

L=["One", "Two", "Three", "Four", "Five", "Six", "Seven"]

lst = tuple(zip(R,L))

print(lst)

'''
o/p
((1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five'), (6, 'Six'), (7, 'Seven'))
'''

# 3. Using sorted() function, sort the list in ascending order.

lst2 = ("h", "b", "a", "c", "f", "d", "e", "g")

Sorted_list = sorted(lst2)

print(Sorted_list)

'''
0/p
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
'''
# 4.Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list.

lst3 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 

new_list = filter(lambda x: x % 2 == 1, lst3)

print(list(new_list))
'''
o/p
[1, 3, 5, 7, 9, 11, 13, 15]
'''
