#!/usr/bin/env python
# coding: utf-8

# In[12]:


import mariadb

mydb = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="mysql"

    )

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

for x in mycursor:
    print(x) 


# In[9]:


import mariadb

mydb = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="mysql"

    )

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers(Membership_ID INT NOT NULL, Full_Names VARCHAR (20) NOT NULL, Physical_Address CHAR (25), Salutation_ID INT NOT NULL)")


# In[11]:


import mariadb

mydb = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="mysql"

    )

mycursor = mydb.cursor()


sql = "INSERT INTO customers (Membership_ID, Full_Names, Physical_Address, Salutation_ID) VALUES (%d, %s, %s, %d)"
val = [
  ('1', 'Janet Jones', 'First Street Plot No 4', '2'),
  ('2', 'Robert Phil', '3rd Street 24', '1'),
  ('3', 'Robert Phil', '5th Avenue', '1')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


# In[13]:


import mariadb

mydb = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="mysql"

    )

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE movies(Membership_ID INT NOT NULL, Movies_Rented VARCHAR (20) NOT NULL)")


# In[20]:


import mariadb

mydb = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="mysql"

    )

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE movies MODIFY Movies_Rented LONGTEXT")


# In[21]:


import mariadb

mydb = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="mysql"

    )

mycursor = mydb.cursor()


sql = "INSERT INTO movies (Membership_ID, Movies_Rented) VALUES (%d, %s)"
val = [
  ("1", "Pirates of the Caribbean"),
  ("1", "Clash of the Titans"),
  ("2", "Forgetting Sarah Marshal"),
  ("2", "Daddy's Little Girl"),
  ("3", "Clash of the Titans")
]

mycursor.executemany(sql, val)


mydb.commit()

print(mycursor.rowcount, "was inserted.") 


# In[22]:


import mariadb

mydb = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="mysql"

    )

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE salutation(Salutation_ID INT NOT NULL, Salutation VARCHAR (20) NOT NULL)")


# In[24]:


import mariadb

mydb = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="mysql"

    )

mycursor = mydb.cursor()


sql = "INSERT INTO salutation (Salutation_ID, Salutation) VALUES (%d, %s)"
val = [
  ("1", "Mr."),
  ("2", "Ms."),
  ("3", "Mrs."),
  ("4", "Dr.")
]

mycursor.executemany(sql, val)


mydb.commit()

print(mycursor.rowcount, "was inserted.") 


# In[10]:


import mariadb

mydb = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="mysql"

    )

mycursor = mydb.cursor()

sql = "SELECT customers.Full_Names, movies.Movies_Rented FROM customers JOIN movies ON customers.Membership_ID = movies.Membership_ID WHERE customers.Full_Names ='Janet Jones'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


# In[11]:


import datetime

x = datetime.datetime.now()
print(x) 


# In[ ]:




