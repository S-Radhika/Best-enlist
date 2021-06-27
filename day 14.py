#1). Error & Exception

try:
  print(a)
except:
  print("An exception occurred")

#OUTPUT
#An exception occurred

#2). Calculator

a=int(input("Enter 1st Number "))
b=int(input("Enter 2nd number "))

c=input("Enter operation ")
try:
    if(c=='+'):
        print(a+b)
    elif(c=='-'):
        print(a-b)
    elif(c=='*'):
        print(a*b)
    elif(c=='/'):
        print(a/b)
except:
    print("Wrong sign")
finally:
    print("Thank you for using our calculator ")

#OUTPUT
#Enter 1st Number 5
#Enter 2nd number 6
#Enter operation *
#30
#Thank you for using our calculator

#3).Name Error

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#OUTPUT
#Variable x is not defined

#4).When try error is not needed

print("Try catch is needed only if expected error is small and does not affect the program, in case of fatal errors try catch block is not recommended")

#5).Getting input inside try catch block

try:
 name=input("Enter the Name : ")
 print("Hi ",name)
except:
  print("Name not defined")

#OUTPUT
#Enter the Name : Radhika
#Hi  Radhika
