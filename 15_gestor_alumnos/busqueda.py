import streamlit as st 
import mysql.connector as con 

def crear_conexion():
    return con.connect(
        host="localhost", 
        user="root", 
        password="root", 
        port=3306, 
        database="gestion_alumnos_db")

st.title("Panel de Búsqueda y Gestión de Alumnos")
ventana_dni, ventana_curso = st.tabs(["Buscar por DNI", "Buscar por Curso"])

#Metemos la primera busqueda:
with ventana_dni:
    txt_dni=st.text_input("Introduce el DNI a buscar:")
    boton_buscar_dni=st.button("Buscar Alumno")
    
    if boton_buscar_dni:
        if txt_dni.strip()=="":
            st.warning("Introduce un DNI para buscar.")
        else:
            db=crear_conexion()
            cursor=db.cursor(dictionary=True)
            sql="SELECT * FROM alumnos WHERE dni = %s"
            cursor.execute(sql, (txt_dni.strip(),))
            alumno = cursor.fetchone() # ¿Qué método extrae este único alumno?
            db.close()
            
            if alumno is not None:
                with st.container(border=True):
                    st.write(f"**Nombre:** {alumno['nombre']}")
                    st.write(f"**Curso:** {alumno['curso']}")
            else:
                # ¿Qué componente pinta la alerta roja de advertencia?
                st.error("El DNI no existe.")

#Segunda busqueda:
with ventana_curso:
    curso_seleccionado=st.selectbox(
        "Selecciona el curso:", 
        options=["Python desde Cero", "Java Avanzado", "Bases de Datos MySQL"]
    )
    
    db=crear_conexion()
    cursor=db.cursor(dictionary=True)
    sql_curso="SELECT id, dni, nombre FROM alumnos WHERE curso = %s"
    cursor.execute(sql_curso, (curso_seleccionado,))
    lista_alumnos=cursor.fetchall()
    db.close()
    
    if lista_alumnos:
        # Añadimos una columna virtual de tipo "botón" llamada 'Borrar' a cada fila
        config_columnas={
            "id": None, # Ocultamos el ID en la web
        }
        
        # Para capturar qué fila ha sido clickeada, usamos st.data_editor!!!
        tabla_interactiva = st.data_editor(
            lista_alumnos,
            column_config=config_columnas,
            use_container_width=True,
            num_rows="dynamic",
            key="editor_alumnos"
        )
        
        # Si el usuario interactúa con la tabla (borra o edita)
        if st.session_state.editor_alumnos["deleted_rows"]:
            # Capturamos el índice de la fila que se quiere eliminar
            indice_borrar=st.session_state.editor_alumnos["deleted_rows"][0]
            id_a_eliminar=lista_alumnos[indice_borrar]["id"]
            
            # Conexión relacional para ejecutar el borrado físico
            db=crear_conexion()
            cursor=db.cursor()
            sql_delete="delete FROM alumnos WHERE id = %s"
            cursor.execute(sql_delete, (id_a_eliminar,))
            db.commit()
            db.close()
            
            st.success("Alumno eliminado correctamente.")
            st.rerun
    else:
        st.info("No hay alumnos inscritos en este curso todavía.")