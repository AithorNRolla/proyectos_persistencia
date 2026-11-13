"""
-Alta de nuevos empleados
-Filtrar empleados: opcion por departamento o rango salarial.
Si se elige departamento, se muestra combo con departamentos y al
seleccionar uno muestra empleados. Si se elige rango salarial,
aparecen dos campos de textos (min y max) y un botón que al pulsarlo
muestra empleados 
"""
#streamlit run C:\Users\Tardes\Desktop\Curso_TARDE\proyectos_persistencia\17_empleados_app\app.py
#Aquí podríamos meter el streamlit

import streamlit as st
import pymongo as pm
from bson.objectid import ObjectId #añadido para blindar la _id de mongo (quiere hojas verdes). 
url="mongodb://localhost:27017"
serv=pm.MongoClient(url)

col_empresa=serv.empresa.empleados

st.title("Panel de Gestión de Empleados")
#Añado imagen aunque no está entro del ejercicio. Como tampoco el botón. 
#st.image("https://www.nuevatribuna.es/asset/thumbnail,992,558,center,center/media/nuevatribuna/images/2017/01/11/2017011111274767744.jpg",width=698) trabajadores
#st.image("https://media1.tenor.com/m/_BiwWBWhYucAAAAd/what-huh.gif",width=500) gif travolta
st.image("https://i.pinimg.com/originals/f4/75/e1/f475e17d2d74c96d45ac92b14de16da5.gif",width=360)
st.header("1. Alta de nuevo empleado")

#Probamos el paso 4, puede que de error. 
nombre=st.text_input("Nombre del empleado")
edad=st.text_input("Edad")
salario=st.text_input("Salario")
depto=st.text_input("Departamento")

if st.button("Dar de alta"):
    #¿Documentación?
  if nombre.strip()==""or edad.strip()==""or salario.strip()==""or depto.strip()=="": 
        st.warning("Por favor, rellena todos los campos")                                           
  else: #cuidado con tanto espacio por que un ligero cambio puede hacer destrozos.                                                                                           
    try:                                                                                        
        nuevo_empleado = {
                "empleado": nombre.strip(),      
                "edad": int(edad),               
                "salario": int(salario),         
                "departamento": depto.strip()    
            }  
        col_empresa.insert_one(nuevo_empleado)
        st.success("Empleado guardado correctamente")
    except ValueError:                                                                          
                st.error("La **edad** y el **salario** deben ser __números enteros__ madafaka") 

st.divider()
st.header("2. Filtrar empleados")
#Aquí podemos poner otra imagen por los JAJAS
opcion=st.radio("Filtrar por:", ["Departamento", "Rango salarial"])
if opcion=="Departamento":
    deptos_mongo=col_empresa.distinct("departamento")
    lista_deptos=["Todos"]+deptos_mongo
    depto_elegido=st.selectbox("Selecciona un departamento:", lista_deptos)
    if depto_elegido=="Todos":
        cursor_deptos=col_empresa.find({}) #quitamos el {"_id": 0} para que mongo no lo traiga. 
    else:
        cursor_deptos=col_empresa.find({"departamento": depto_elegido}) #quitamos el {"_id": 0} por lo mismo. 
    #Aquí deberia de cambiar cosas:
    lista_empleados=[] # lista_empleados=list(cursor_deptos) la que estaba. 
    for emp in cursor_deptos: #st.dataframe(lista_empleados) lo que estaba antes. 
        emp["_id"]=str(emp["_id"])
        lista_empleados.append(emp) 
    tabla_editada=st.data_editor(
        lista_empleados,
        column_order=["empleado","edad","salario","departamento"],
        num_rows="dynamic",
        #disabled=["_id"], lo quitamos por ahora. 
        key="editor_empleados"
    )
    cambios=st.session_state.get("editor_empleados",{})
    filas_borradas=cambios.get("deleted_rows",[])
    if len(filas_borradas)>0:
        for indice in filas_borradas:
            emp_a_borrar=lista_empleados[indice]
            id_real=ObjectId(emp_a_borrar["_id"])
            col_empresa.delete_one({"_id":id_real})
        st.success("Empleado eliminado en Mongo")
        st.rerun()
    if st.button("Guardar cambios"):
        for fila in tabla_editada:
            id_real=ObjectId(fila["_id"])
            col_empresa.update_one(
                {"_id":id_real},
                {"$set":{
                    "empleado":fila["empleado"],
                    "edad":int(fila["edad"]),
                    "salario":int(fila["salario"]),
                    "departamento":fila["departamento"]
                }}
            )
        st.success("**Cambios guardados en Mongo** -mongo quiere hojas verdes")
        st.rerun()
         
elif opcion=="Rango salarial":
    min_sal=st.text_input("Salario mínimo")
    max_sal=st.text_input("Salario máximo")

if st.button("Buscar"):
    if min_sal.strip()==""or max_sal.strip()=="":
            st.warning("Introduzca ambos salarios")
    else:
            filtro_salario={      #Copio lo mismo del otro, modifico parámetros. 
                "salario": {
                "$gte": int(min_sal),
                "$lte": int(max_sal)
                    }
                }
            cursor_salario=col_empresa.find(filtro_salario,{"_id": 0})#aquí añadiremos el {"_id": 0}
            lista_empleados=list(cursor_salario)
            st.dataframe(lista_empleados)
st.image("https://media.tenor.com/WYcP64486i8AAAAM/h2di-michael-shocked-happy.gif",width=380)
#st.image("https://e01-phantom-elmundo.uecdn.es/6325c1e69d0fbc008e944ef214171165/f/webp/assets/multimedia/imagenes/2019/01/28/15486725361120.jpg",width=230) 500€