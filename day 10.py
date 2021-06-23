# Python program to create Bankaccount class
class Bank_Account:
	def __init__(self):
		self.balance=0
		print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\n Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("\n You Withdrew:", amount)
		else:
			print("\n Insufficient balance ")

	def display(self):
		print("\n Net Available Balance=",self.balance)
s = Bank_Account()
s.deposit()
s.withdraw()
s.display()

#output
'''
Hello!!! Welcome to the Deposit & Withdrawal Machine
Enter amount to be Deposited: 1000

 Amount Deposited: 1000.0
Enter amount to be Withdrawn: 300

 You Withdrew: 300.0

 Net Available Balance= 700.0
'''



