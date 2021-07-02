import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="Rad@97",
)

mycursor = mydb.cursor()
print(mydb)


#creating database 
dbse = mydb.cursor()

dbse.execute("CREATE DATABASE Employee_Mangement")

dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for entry in dbse:
    print(entry)

'''
('customers',)
('employee_mangement',)
('information_schema',)
('mysql',)
('performance_schema',)
('sakila',)
('sys',)
('world',)
'''
dbse = mydb.cursor()

dbse.execute("CREATE TABLE Employeee (emp_id INT , EMP_NAME VARCHAR(255),EMP_SALARY DOUBLE )")
dbse = mydb.cursor()

sql = "INSERT INTO employeee(emp_id , EMP_NAME , EMP_SALARY) VALUES (%s,%s,%s)"
val = [
  ('1','SARA','10000.0'),
    ('2','ANU','15000.0'),
    ('3','PRIYA','70800.0'),
    ('4','VIBAV','80000.0'),
    ('5','ANURAG','89000.0'),
    ('6','KUHU','50000.0'),
    ('7','KUNAL','56000.0'),
    ('8','ABIR','47000.0'),
    ('9','MAYA','26000.0'),
    ('10','RANA','15000.0'),
    ('11','LAKSHANYA','50500.0'),
    ('12','PRERNA','40500.0'),
    ('13','MISTI','25000.0'),
    ('14','POOJA','20500.0'),
    ('15','ARJUN','100600.0')
       
]
dbse.executemany(sql, val)

mydb.commit()

print(dbse.rowcount, "was inserted.")

'''
15 was inserted.
'''


# to find min and max salary of an employee



mycursor = mydb.cursor()

mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM employeee where EMP_SALARY = (select max(EMP_SALARY) from employee)")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
'''
('ARJUN', 100600.0)
'''
mycursor = mydb.cursor()

mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM employeee where EMP_SALARY = (select min(EMP_SALARY) from employee)")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

'''
o/p
('SARA', 10000.0)
'''
# to find no of employees working

mycursor = mydb.cursor()

mycursor.execute("SELECT COUNT(*) from employeee")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
'''
o/p
(15,)
'''
#to get first 3 characters of first name from employees table
mycursor = mydb.cursor()

mycursor.execute("SELECT * from employeee WHERE EMP_NAME LIKE('ANU%')")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
'''
o/p
(2, 'ANU', 15000.0)
(5, 'ANURAG', 89000.0)
'''






