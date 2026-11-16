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
#condicion=df["nombre_tienda"]==tienda_buscada |comentado por añadir query| 
#df_tienda=df[condicion] |comentado por añadir query|
df_tienda=df.query("nombre_tienda==@tienda_buscada")
ventas_totales=df_tienda["facturacion"].sum()
mayor_gasto=df_tienda["gastos_personal"].max()
print("Ventas totales",ventas_totales)
print("Gasto personal:",mayor_gasto)
max_facturacion=df_tienda["facturacion"].max()
condicion_mes=df_tienda["facturacion"]==max_facturacion
#fila_record=df_tienda[condicion_mes] |comentado por añadir query| 
fila_record=df_tienda.query("facturacion==@max_facturacion")
mes_record=fila_record["mes"].values[0]
print("Mes con mayor facturación:",mes_record)
#-----Aquí he añadido por mi cuenta más cosas, como el beneficio o el ranking. 
df["beneficio_neto"]=df["facturacion"]-df["gastos_personal"]
grupos_tiendas=df.groupby("nombre_tienda")
resumen_beneficios=grupos_tiendas["beneficio_neto"].sum()
#-----Aquí metemos la tabla: 
tabla_limpia1=resumen_beneficios.reset_index()
print("Beneficio por tienda:")
print(tabla_limpia1)
ranking_tiendas=resumen_beneficios.sort_values(ascending=False)
#print(ranking_tiendas)
tabla_limpia=ranking_tiendas.reset_index() #recuerda que la variable va de la mano con lo que queremos pedir joder!
print("Ranking de beneficio de mayor a menor:")
print(tabla_limpia)
#-----Aquí abajo añadimos la tienda más vieja. 
edad_vieja=df["año_apertura"].min() #el año
condicion_vieja=df["año_apertura"]==edad_vieja #filtramos
tienda_vieja=df[condicion_vieja] #filas
nombre_tienda_vieja=tienda_vieja["nombre_tienda"].unique()[0] #usamos unique para que no se repita!!! (si no, se me repite 6 veces)
print(f"La tienda más antigua es {nombre_tienda_vieja},inaugurada en el año {edad_vieja}")