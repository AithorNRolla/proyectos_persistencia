"""
Sobre el archivo de ventas.csv, realizar:
    
A partir del nombre de la tienda:
Mostrar sus ventas totales. 
Mostrar el mayor gasto de personal de tiendas
mostrar el mes en la que tuvo mayor facturación

"""
import polars as pl 
#df=pl.read_csv("ventas.csv")
df=pl.read_csv("ventas.csv")
tienda_buscada=input("Introduce nombre de la tienda (Centro/Norte/Sur/Este/Oeste): ") #la misma del 23.
#===============================================DF TIENDA==============================================
condicion=pl.col("nombre_tienda")==tienda_buscada
df_tienda=df.filter(condicion)
#df.group_by("nombre_tienda").agg(pl.col("gastos_personal").sum()).select(pl.col("gastos_personal").max()).item()) [GRUPO TOTAL, iria fuera seguramente]
#A partir de aquí calculamos en base a df_tienda 
ventas_totales=df_tienda.select(pl.col("facturacion").sum()).item()
print("Ventas totales:",ventas_totales)
mayor_gasto=df_tienda.select(pl.col("gastos_personal").max()).item() #¿Solo una tienda?
print("Mayor gasto de personal:",mayor_gasto)
tabla_ordenada=df_tienda.sort("facturacion",descending=True)
fila_record=tabla_ordenada.head(1)
mes_record=fila_record.select(pl.col("mes")).item()
print("Mes con mayor facturación:",mes_record)
#===========================================CALCULO GLOBAL=============================================
#gasto_global=df.group_by("nombre_tienda").agg(pl.col("gastos_personal").sum()).select(pl.col("gastos_personal").max()).item()
#print("Mayor gasto global:",gasto_global)
# 2. Tienda con mayor gasto de personal acumulado (nombre e importe total)
fila_max_gasto = (
    df.group_by("nombre_tienda")
    .agg(pl.col("gastos_personal").sum())
    .sort("gastos_personal", descending=True)
    .row(0, named=True)
)

print(
    f"Tienda con mayor gasto de personal: {fila_max_gasto['nombre_tienda']}"
    f" ({fila_max_gasto['gastos_personal']})"
)#Arriba lo que hizo Vicente por que funciona muy bien. Abajo le copiamos para aprender:

fila_record_global=(
    df.sort("facturacion",descending=True).row(0,named=True)
    
)
print(
    f"Record:{fila_record_global['nombre_tienda']}"
    f" con facturación de {fila_record_global['facturacion']}€" #ponemos espacio por que sigue la frase.
    f" en el mes de {fila_record_global['mes']}"                #ponemos espacio por que sigue la frase.
)
""" df_ordenadoventas=df.sort("facturacion",descending=True) 
fila_record_global=df_ordenadoventas.row(0,named=True)
tienda_ganadora=fila_record_global["nombre_tienda"]
mes_ganador=fila_record_global["mes"]
dineroG=fila_record_global["facturacion"]
print(f"Récord:{tienda_ganadora} con facturación de {dineroG}€ en el mes de {mes_ganador}") """
#======================================================================================================
#=======================================BENEFICIOS Y RANKING===========================================
restamos=pl.col("facturacion")-pl.col("gastos_personal")
columna_beneficio=restamos.alias("beneficio_neto")
df=df.with_columns(columna_beneficio)
#Aquí metemos las tiendas de los cojones
grupos_tiendas=df.group_by("nombre_tienda")
resumen_beneficios=grupos_tiendas.agg(pl.col("beneficio_neto").sum())
print("Beneficio por tienda:")
print(resumen_beneficios) #se nos olvida el print!
#Prepramos el ranking ^-^
ranking_tiendas=resumen_beneficios.sort("beneficio_neto",descending=True)
print("Ranking de beneficios (de mayor a menor):")
print(ranking_tiendas)