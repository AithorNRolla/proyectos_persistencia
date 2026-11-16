"""
Sobre el archivo de ventas, realizar:
    
A partir del nombre de la tienda:
Mostrar sus ventas totales. 
Mostrar el mayor gasto de personal de tiendas
mostrar el mes en la que tuvo mayor facturación

"""

import pandas as pd 
df=pd.read_csv("ventas.csv") #aqui ya hacemos que lea el csv. 
tienda_buscada=input("Introduce nombre de la tienda (Centro/Norte/Sur/Este/Oeste): ")
#print("Columnas reales:", df.columns.tolist())
#print("Tiendas en el CSV:", df["nombre_tienda"].unique()) columnas chivatas recomendación de la IA para solucionar problemas que había. 
condicion=df["nombre_tienda"]==tienda_buscada
df_tienda=df[condicion]
ventas_totales=df_tienda["facturacion"].sum()
mayor_gasto=df_tienda["gastos_personal"].max()
print("Ventas totales",ventas_totales)
print("Gasto personal:",mayor_gasto)
max_facturacion=df_tienda["facturacion"].max()
condicion_mes=df_tienda["facturacion"]==max_facturacion
fila_record=df_tienda[condicion_mes]
mes_record=fila_record["mes"].values[0]
print("Mes con mayor facturación:",mes_record)





#Versión encadenada (contiene errores)
"""
import pandas as pd
df=pd.read_csv("ventas.csv)")
tienda_buscada=input("Introduce el nombre de la tienda (Centro/Norte/Sur/Este/Oeste)")
df_tienda = df[df["nombre_tienda"]==tienda_buscada]

ventas_totales=df_tienda["facturacion"].sum()
mayor_gasto=df_tienda["gastos_personal"].max()
mes_record=df_tienda[df_tienda["facturacion"] == df_tienda["facturacion"].max()]["mes"].values[0]
"""