"""""
Calcular media, mostrar nota mas alta, total de alumnos. (a partir del archivo alumnos.json)

"""
import json
import pandas as pd
#Solución sacada de la IA abajo: 
"""
# 1. Abrimos el archivo con Python puro (como ya sabías hacer)
with open("alumnos.json", "r", encoding="utf-8") as archivo:
    datos_lista = json.load(archivo)

# 2. Aquí es donde entra pd.DataFrame(): convierte tu lista en tabla de Pandas
df = pd.DataFrame(datos_lista)
"""
#Arriba está una forma de hacerlo, con Dataframe. 
df=pd.read_json("alumnos.json", encoding="utf-8") 
print("Tabla de Alumnos")
print(df)
print()
#df=pd.DataFrame("Índice","nombre","curso","nota") esta línea sobra, ya que "read_json" ya me hace dataframe. 

columna_notas=df["nota"]
media_notas=columna_notas.mean()
nota_maxima=columna_notas.max()
filtro_mejor=(df["nota"]==nota_maxima)
mejor_alumno=df[filtro_mejor]
print("La nota más alta es: ")
print(mejor_alumno)
total_alumnos=len(df)
print("--- RESULTADOS ---")
print(f"Total de alumnos: {total_alumnos}")
print(f"Nota media: {round(media_notas, 2)}")
print(f"Nota más alta: {nota_maxima}")