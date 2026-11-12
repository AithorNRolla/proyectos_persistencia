
"""
-Alta de nuevos empleados
-Filtrar empleados: opcion por departamento o rango salarial.
Si se elige departamento, se muestra combo con departamentos y al
seleccionar uno muestra empleados. Si se elige rango salarial,
aparecen dos campos de textos (min y max) y un botón que al pulsarlo
muestra empleados 
"""
#Aquí importaremos los datos de la empresa. 

import pymongo as pm 
url="mongodb://localhost:27017"
serv=pm.MongoClient(url)
#Cuidado con las tildes, hay que poner el MISMO nombre de la base de datos.
#Que es lo que me ha pasado con "librería", CON TILDE. 
col_empresa=serv.empresa.empleados
lista_deptos=col_empresa.distinct("departamento") #lista
print("Departamentos:",lista_deptos)
empleados_deptos=col_empresa.find({"departamento":"RRHH"}) #buscamos departmento
for emp in empleados_deptos:
    print(emp)
print("Empleados por salario")
filtro_salario={
    "salario":{
        "$gte":1500,
        "$lte":2500
    }
}

empleados_salario=col_empresa.find(filtro_salario) 
for emp in empleados_salario:                  
    print(emp)
serv.close()

