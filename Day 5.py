#1).Creating a List
a = [1,2,3]
print ("list = " ,a)
a.append(11)                                  #Appending a value
print ("list = " ,a)
b= [12,13,14,15]
a.extend(b)                               #Adding another items from list
print ("list = " ,b)
a.insert(0,0)                                 #Appending value at a particular index
print ("list = " ,a)                         

del a[0]                                      #Deleting a value
print ("list = " , a)
Popped_Number = a.pop()                       #Deleting using Pop function
print ("list = " , a)
print ("Popped_Number =" , Popped_Number)

Smallest_Number = min(a)                      #Identifying minimum value
print ("Smallest_Number = " , Smallest_Number)
Largest_Number = max(a)                       #Identifying maximum value
print ("Largest_Number = " , Largest_Number) 



#2).Creating a Tuple and Reversing it

s= (7,'apple',3,'orange',5,'mango',11,'strawberry',9,'cherry')     #Creating a Tuple
print ("Tuple :")
print(s)
rev_tuple = reversed(s)                         #Reversing the Tuple
print ("Reversed_Tuple :" ) 
print (tuple(rev_tuple))

#3).Converting Tuple to List

tup = list(s)                                             #Converting Tuple to List
print ("List = ", tup)
