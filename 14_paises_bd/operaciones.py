import mysql.connector as con 
def crear_conexion():
    return con.connect(host="localhost",
               user="root",
               password="root",
               port=3306,
               database="mundo")
    
def borrar_tablas():
    db=crear_conexion()
    cursor=db.cursor()
    cursor.execute("delete from continentes")
    cursor.execute("delete from paises")
    db.commit()
    db.close()
def crear_continentes(continentes): #["Asia","Americas",...]
    db=crear_conexion()
    cursor=db.cursor()
    sql_insert="insert into continentes(continente) values(%s)"
    for continente in continentes:
        cursor.execute(sql_insert,(continente,))
        
    db.commit()
    db.close()
def crear_paises(paises): #[Meteremos los paises]
    db=crear_conexion()
    cursor=db.cursor()
    sql_insert="insert into paises(pais,poblacion,bandera)values(%s,%s,%s)"
    for pais,poblacion,bandera in paises:
        cursor.execute(sql_insert,(pais,poblacion,bandera))
    db.commit()
    db.close()    
#esto ya es aporte del profesor
def devolver_continentes():
    sql="select * from continentes"
    db=crear_conexion()
    cursor=db.cursor(dictionary=True)
    cursor.execute(sql)
    resultado=cursor.fetchall()
    db.close()
    return resultado
