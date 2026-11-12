"""
-Alta de nuevos empleados
-Filtrar empleados: opcion por departamento o rango salarial.
Si se elige departamento, se muestra combo con departamentos y al
seleccionar uno muestra empleados. Si se elige rango salarial,
aparecen dos campos de textos (min y max) y un botón que al pulsarlo
muestra empleados 
"""
#Aquí podríamos meter el streamlit

import streamlit as st
import pymongo as pm
url="mongodb://localhost:27017"
serv=pm.MongoClient(url)

col_empresa=serv.empresa.empleados

st.title("Panel de Gestión de Empleados")
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

opcion=st.radio("Filtrar por:", ["Departamento", "Rango salarial"])
if opcion=="Departamento":
    lista_deptos=col_empresa.distinct("departamento")
    depto_elegido=st.selectbox("Selecciona un departamento:", lista_deptos)
    cursor_deptos=col_empresa.find({"departamento": depto_elegido},{"_id": 0})
    #Aquí deberia de cambiar cosas:
    lista_empleados=list(cursor_deptos)
    st.dataframe(lista_empleados)
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
                cursor_salario = col_empresa.find(filtro_salario)
                lista_empleados = list(cursor_salario)
                st.dataframe(lista_empleados)
