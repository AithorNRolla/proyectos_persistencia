import numpy as np
from pymongo import MongoClient
from pathlib import Path
#===== BLOQUE 1: LA CONEXIÓN =====#
cliente=MongoClient("mongodb://localhost:27017/")
db=cliente["empresa"]
coleccion=db["empleados"]
documentos=list(coleccion.find())

##esto de aquí abajo pertenece si quiero conectar con el empleados.csv
""" CARPETA_ACTUAL=Path(__file__).parent
ruta_csv=CARPETA_ACTUAL/"empleados.csv" """
#===== BLOQUE 2: POSTURA =====#
edades=np.array([doc["edad"] for doc in documentos], dtype=int)
salarios=np.array([doc["salario"] for doc in documentos], dtype=float)
departamentos=np.array([doc["departamento"] for doc in documentos], dtype=str)

##esto de aquí abajo pertenece si quiero conectar con el empleados.csv
""" edades=np.genfromtxt(ruta_csv,delimiter=",",skip_header=1,usecols=1,dtype=int)
salarios=np.genfromtxt(ruta_csv,delimiter=",",skip_header=1,usecols=2,dtype=float)
departamentos=np.genfromtxt(
    ruta_csv,delimiter=",",skip_header=1,usecols=3,dtype=str,encoding="utf-8"
) """
#===== BLOQUE 3: SABER ESTAR ======#
departamentos_limpios=np.char.strip(departamentos)
#calculamos todo:
salario_medio=np.mean(salarios)
edad_mayor=np.max(edades)
lista_departamentos=np.unique(departamentos_limpios)
#patallica rica:
print(f"Salario medio: {salario_medio:.2f} €")
print(f"Edad mayor: {edad_mayor} años")
print(f"Lista de departamentos: {lista_departamentos.tolist()}")
