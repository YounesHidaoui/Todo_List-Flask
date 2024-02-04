import mysql.connector 

db = mysql.connector.connect(
    host="localhost",
    username="root",
    passwd=""
)
mycursor = db.cursor()
mycursor.execute("CREATE DATABASE todolist")
mycursor.execute("SHOW DATABASES")


for i in mycursor :
    print(i,'database')