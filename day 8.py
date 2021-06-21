  
#1). Merging Two Dictionaries

d1 = {'hat': 1, 'watch':2 }
print ("Dictionary 1 = " , d1)

d2 = {'car': 3, 'key': 4}
print ("Dictionary 2 = " , d2)

d = d1.copy()
d.update(d2)
print("Combined Dictionary = " , d)

#2). Sorting in Descending and Converting List to Set

numbers = [1, 3, 4, 2,7,9,5,10,8,6]
print("List =" , numbers)
numbers.sort(reverse = True)
print("Sorted List =",numbers)
set1=set(numbers)
print("Converted Set =" , set1)

#3). Sorting Dictionary

test_dict = {'gfg': [7, 6, 3], 
             'is': [2, 10, 3], 
             'best': [19, 4]}
  
print("The original dictionary is : " + str(test_dict))
  
res = {key : sorted(test_dict[key]) for key in sorted(test_dict)}
  
print("The sorted dictionary : " + str(res))

#4).Changing Certain Index with specific Value 

String1=input("Enter the String : ")
n=int(input("Enter the index to be replaced : "))
String2=String1.replace(String1[n],"X")
print("After Replacing : " , String2)


#5). Changing Case of First letter of the String

String1=input("Enter the String : ")
n=int(input("Enter the index to be replaced : "))
String2=String1.replace(String1[n],"X")
print("After Replacing : " , String2)

#6). Finding the repeated items of a list

from collections import Counter
 
l1 = [1,2,3,3,4,5,6,6,7,8,9,9,9]
d = Counter(l1)
print(d)
 
new_list = list([item for item in d if d[item]>1])
print("Repeated Items in the list : " , new_list)


#7). Checking the sum of three elements and dividing by a value which is given as an input by the user

a=59
b=76
c=35
Sum = a+b+c
print("The Sum of 3 Numbers is :" ,Sum)

Divisor=int((input("Enter the divisor : ")))
val= Sum / Divisor

print("After divison : " , val )

#8). Finding the Mean,median,mode among three given numbers

import statistics
list1 = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    number = int(input())
  
    list1.append(number) # adding the element
          
print("The three Numbers is :", list1)

print("Mean of three numbers is : " , statistics.mean(list1))
print("Median of three numbers is : " , statistics.median(list1))
print("Mode of three numbers is : " , statistics.mode(list1))

#9). Swapping cases of a given string

Input_string = input("Enter The String : ")
  
print("After Swapping : " , Input_string.swapcase())

#OUTPUT
#Enter The String : Best Enlist
#After Swapping All the Cases :  bEST eNLIST

#10). Converting an integer to binary & octa decimal
a=int(input("Enter the value of the Integer : "))
print("Binary Value = ", bin(a))
print("Octa Decimal Value = ", oct(a))
