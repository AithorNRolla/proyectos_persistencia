import polars as pl
"""
    ¿Porqué polars?
    1.- Estilo y métodos más modernos
    2.- Más eficiente
    """
datos = [ 
    {"nombre": "Ana", "edad": 25, "salario": 25000,"departamento":"ventas"}, 
    {"nombre": "Luis", "edad": 32, "salario": 32000,"departamento":"informática"}, 
    {"nombre": "Marta", "edad": 28, "salario": 28000,"departamento":"informática"}, 
    {"nombre": "Pedro", "edad": 41, "salario": 41000,"departamento":"ventas"} 
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
print(df["departamento"].unique().to_list()) #muestra lista sin duplicados.

#Agrupacion en un dataframe
print( 
df.group_by("departamento").agg(pl.col("salario").mean().alias("salario medio"),
                                pl.col("nombre").count().alias("total_empleados"))
)

#Recorrido de un dataframe
for element in df.iter_rows(): #como si fuera una tupla.
    print(element)
for element in df.iter_rows(named=True): #como diccionario
    print(element)
    