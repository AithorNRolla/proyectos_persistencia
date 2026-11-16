import polars as pl
"""
    ¿Porqué polars?
    1.- Estilo y métodos más modernos
    2.- Más eficiente
    """
datos = [ 
    {"nombre": "Ana", "edad": 25, "salario": 25000}, 
    {"nombre": "Luis", "edad": 32, "salario": 32000}, 
    {"nombre": "Marta", "edad": 28, "salario": 28000}, 
    {"nombre": "Pedro", "edad": 41, "salario": 41000} 
] 
df = pl.DataFrame(datos) 
print(df)
#Acceso a filas y columnas
print(df["edad"].to_list()) #columna en lista de valores
print(df.row(0,named=True)) #diccionario con los datos de la fila
#Transformación en diccionarios
print(df.to_dicts()) #Convierte todo el dataframe en una lista de diccionarios

#Filtrado
print(df.filter(pl.col("salario")>30000))
print(df.filter((pl.col("salario")>30000) & (pl.col("edad")<50)))

#ordenación
print(df.sort(by="edad",descending=False))
print(df
      .sort("salario",descending=True) #ordena descendente en salario
      .row(0)[0]) #se queda con la primera fila, y de esta, con el primer elemento

#funciones para cálculos min(),max(),mean(),count(),unique()

print("Salario más alto",df["salario"].max())
print("Edad más baja",df["edad"].min())

#selección
resultado=df.select
(pl.col("salario").mean().alias("salario medio"),pl.col("edad").mean().alias("media edad"))
print(resultado) 