
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