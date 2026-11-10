import streamlit as st
import mysql.connector as con

def crear_conexion():
    return con.connect(
        host="localhost", user="root", password="root", port=3306, database="gestion_alumnos_db"
    )

st.title("Alta de Nuevos Alumnos")

#¿Creamos streamlit?
with st.container(border=True):
    txt_dni=st.text_input("Introduce el DNI (ej: 12345678A):")
    txt_nombre=st.text_input("Nombre completo:")
    txt_curso=st.selectbox("Curso:", options=["Python desde Cero", "Java Avanzado", "Bases de Datos MySQL"])
    
    boton_guardar=st.button("Registrar Alumno")

#Hacemos botoncito
if boton_guardar:
    # Verificamos que el usuario no haya dejado el DNI vacío
    if txt_dni.strip()=="":
        st.warning("Por favor, introduce un DNI válido.")
    else:
        # Abrimos conexión para comprobar si el DNI ya existe
        db=crear_conexion()
        cursor=db.cursor()
        
        sql_comprobar = "SELECT id FROM alumnos WHERE dni = %s"
        cursor.execute(sql_comprobar, (txt_dni,))
        
        #DNI
        existe=cursor.fetchone() 
        
        if existe is not None:
            # A) Si 'existe' tiene datos, significa que el DNI ya está registrado
            st.error("Error: El alumno con este DNI ya existe. No se puede duplicar.")
            db.close()
        else:
            #Aquí pasa algo??
            sql_insert = "INSERT INTO alumnos (dni, nombre, curso) VALUES (%s, %s, %s)"
            cursor.execute(sql_insert, (txt_dni, txt_nombre, txt_curso))
            db.commit()
            db.close()
            
            st.sucess("¡Estás dentro")
