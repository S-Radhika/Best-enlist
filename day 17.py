#1).Finding version of database

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Rad@97"
)
import sys
cur = mydb.cursor()
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print("Database Version :",str(data))

#OUTPUT
#Database Version : ('8.0.25',)

#2).Creating table

import mysql.connector as SQLC
 
DataBase = SQLC.connect(
  host ="localhost",
  user ="root",
  password ="Rad@97"
)

Cursor = DataBase.cursor()
 
Cursor.execute("CREATE DATABASE Customers")
print("College Data base is created")

#OUTPUT
#College Data base is created

#Inserting Data

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Rad@97",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('akash', 'Lowstreet 4'),
  ('ramya', 'Apple st 652'),
  ('rithu', 'Mountain 21'),
  ('ash', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

#OUTPUT
#5 was inserted

#3).Creating Employee table

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Rad@97",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Employee1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
mycursor = mydb.cursor()

sql = "INSERT INTO Employee1 (id,name, address) VALUES (%s,%s,%s)"
val = [
  (1, 'Akash', 'Chennai 53'),
  ('112','Peter', 'Lowstreet 4'),
  ('221','Amy', 'Apple st 652'),
  ('321','Hannah', 'Mountain 21'),
  ('412','Michael', 'Valley 345'),
  ('512','Sandy', 'Ocean blvd 2'),
  ('612','Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Employee1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#OUTPUT
#(1, 'Akash', 'Chennai 53')
#(112, 'Peter', 'Lowstreet 4')
#(221, 'Amy', 'Apple st 652')
#(321, 'Hannah', 'Mountain 21')
#(412, 'Michael', 'Valley 345')
#(512, 'Sandy', 'Ocean blvd 2')
#(612, 'Viola', 'Sideway 1633')

mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM Employee1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#OUTPUT
#('Akash',)
#('Peter',)
#('Amy',)
#('Hannah',)
#('Michael',)
#('Sandy',)
#('Viola',) 
