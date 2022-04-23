import mariadb

mydb = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="mysql"

    )

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM user")

for x in mycursor:
    print(x) 