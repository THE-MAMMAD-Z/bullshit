# f = open("note.txt", "a")
# f.write("lal lala la lal lala lalal")
# f = open("note.txt" , "rt")
# print(f.read())
# f.close()

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sezar1381"
)
asfasdfsafzvczv
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
zvzcvzvzv
derlkewrk
fodaiperi
for x in mycursor:
  print(x)