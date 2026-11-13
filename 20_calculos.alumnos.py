"""""
Calcular media, mostrar nota mas alta, total de alumnos. (a partir del archivo alumnos.json)

"""
import pandas as pd

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