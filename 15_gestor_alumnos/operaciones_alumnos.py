import mysql.connector as con 

def crear_conexion():
    return con.connect(
        host="localhost", 
        user="root", 
        password="root", 
        port=3306, 
        database="gestion_alumnos_db"
    )

def existe_dni(dni):
    with crear_conexion() as db:
        with db.cursor() as cursor:
            sql = "SELECT id FROM alumnos WHERE dni = %s"
            cursor.execute(sql, (dni,))
            return cursor.fetchone() is not None 

def insertar_alumno(dni, nombre, curso):
    with crear_conexion() as db:
        with db.cursor() as cursor:
            sql = "INSERT INTO alumnos (dni, nombre, curso) VALUES (%s, %s, %s)"
            cursor.execute(sql, (dni, nombre, curso))
            db.commit()

def obtener_alumnos_por_curso(curso):
    with crear_conexion() as db:
        with db.cursor(dictionary=True) as cursor:
            sql = "SELECT id, dni, nombre, curso FROM alumnos WHERE curso = %s"
            cursor.execute(sql, (curso,))
            return cursor.fetchall()

def obtener_alumno_por_dni(dni):
    with crear_conexion() as db:
        with db.cursor(dictionary=True) as cursor:
            sql = "SELECT id, dni, nombre, curso FROM alumnos WHERE dni = %s"
            cursor.execute(sql, (dni,))
            return cursor.fetchone() # Devuelve el diccionario del alumno o None

def eliminar_alumno(id_alumno):
    with crear_conexion() as db:
        with db.cursor() as cursor:
            sql = "DELETE FROM alumnos WHERE id = %s"
            cursor.execute(sql, (id_alumno,))
            db.commit()
