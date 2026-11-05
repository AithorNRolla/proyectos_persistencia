
import csv
"""
with open("empleados.csv","r") as f:
    datos=csv.reader(f,delimiter=",")
    for row in datos:
        print(row)
with open("empleados.csv","r") as f:
    datos=list(csv.reader(f))
    print(datos)
with open("empleados.csv","r") as f:
    datos=list(csv.DictReader(f))
    print(datos)
"""   

#Solicita la introducción de un departamento y que te muestre
#los hombres de las personas de este departamento. 

def buscar_por_departamento(lista_empleados,departamento):
    print(f"Empleados del departamento de {departamento}")
    encontrado=False
    for persona in lista_empleados:
        if persona ["departamento"]==departamento:
            print(f"{persona["empleado"]}")
            encontrado=True 
    if not encontrado:
        print(f"No se encuentran personas de este departamento.")

with open("empleados.csv","r",encoding="utf-8")as f:
    datos_empleados=list(csv.DictReader(f))
    busqueda=input("Introduzca el departamento a buscar: ")
buscar_por_departamento(datos_empleados, busqueda)

#Solicita el nombre del empleado con mayor salario: 
salario_alto=0.0
nombre_empleado=""
for empleado in datos_empleados:
    salario_actual=float(empleado["salario"])
    if salario_actual>salario_alto:
        salario_alto=salario_actual
        nombre_empleado=empleado["empleado"]
print("Analisis Salarios")
print(f"La persona con el salario más alto es {nombre_empleado}")