#program to loop through a list of numbers and add +2 to every value to elements in list
a=[1,2,3,4,5,6]
for i in range(len(a)):
    a[i]+=2
print("result=",a)

#output
'''
result= [3, 4, 5, 6, 7, 8]
'''

#pattern printing

n=int(input("Enter no.of.rows"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end="")

    print()
#output
'''
Enter no.of.rows5
54321
4321
321
21
1
'''

#fibonacci series

l=int(input("enter the length of fibonacci series"))
n1,n2=0,1
count=0
if l<=0:
    print("invalid input")
elif l==1 :
    print(n1)
else:
    print("the length of fibonacci sequence is",l)
while(count<l):
      print(n1)
      n=n1+n2
      n1=n2
      n2=n
      count=count+1
#output
'''
enter the length of fibonacci series7
the length of fibonacci sequence is 7
0
1
1
2
3
5
8
'''
#multiplication table of 9

s=int(input("enter the no .of.multiples"))
number=9
for i in range(1,s+1):
    print("the multiples of 9 are ",number*i)

#output
'''
enter the no .of.multiples5
the multiples of 9 are  9
the multiples of 9 are  18
the multiples of 9 are  27
the multiples of 9 are  36
the multiples of 9 are  45
'''

#check whether a number is positive or not

number=float(input("Enter a number"))
if(number>0):
    print("the given number",number,"is positive")
elif(number<0):
    print("the given number",number,"is negative")
else:
    print("zero")

#output
'''
Enter a number-2
the given number -2.0 is negative
'''

#check armstrong number

num=int(input("enter the number"))
order=len(str(num))
sum=0
temp=num
while temp>0:
    dig=temp%10
    sum+=dig**order
    temp=temp//10
if(sum==num):
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")

#output
'''
enter the number153
153 is an armstrong number
'''

#convert no of days to ages

days=int(input("enter the no.of.days"))
Age=days/365
print("Age is",Age)

#output
'''
enter the no.of.days456
Age is 1.2493150684931507
'''

#trigonometric problem solving using math function

import math 
x = 0.75 
print("math.cos(",x,"): ", math.cos(x));

#output
'''
math.cos( 0.75 ):  0.7316888688738209
'''
#calculator
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")

#output
'''
Select operation.
1.Add
2.Subtract
3.Multiply
4.Divide
Enter choice(1/2/3/4): 2
Enter first number: 5
Enter second number: 4
5.0 - 4.0 = 1.0
'''





























    
