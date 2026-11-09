import mysql.connector as con 
db=con.connect(host="localhost",
               user="root",
               password="root",
               port=3306,
               database="universidad")
print("¡Conexión realizada!")