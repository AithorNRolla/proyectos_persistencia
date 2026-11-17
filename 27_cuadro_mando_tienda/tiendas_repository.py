#Aquí las funciones de acceso a datos a través de Polars (ventas.csv)
import polars as pl 
df=pl.read_csv("ventas.csv") #leemos el archivo. 
#==================== funciones principales ====================
def obtener_tiendas():
    tiendas=df["nombre_tienda"].unique(maintain_order=True).to_list()
    return tiendas
def obtener_meses():
    meses=df["mes"].unique(maintain_order=True).to_list()
    return meses 
#==================== funciones secundarias ====================
def resumen_por_tienda(tienda_buscada):
    df_tienda=df.filter(pl.col("nombre_tienda")==tienda_buscada)
    
    total_facturacion=df_tienda["facturacion"].sum()
    total_gastos=df_tienda["gastos_personal"].sum()
    #Aquí debería de funcionar para calcular esto, quizá se podría resumir como lo de vicente. 
    fila_record=df_tienda.sort("facturacion",descending=True).row(0,named=True)
    mes_record=fila_record["mes"]
    #Ahora metemos polars:
    tabla_resumen=pl.DataFrame({
        "Tienda":[tienda_buscada],
        "Total facturación":[total_facturacion],
        "Total gastos personal":[total_gastos],
        "Mes con mayor facturación":[mes_record]
    })
    return tabla_resumen
#================== funciones para el mes ======================
def info_mes_completo(mes_buscado):
    df_mes=df.filter(pl.col("mes") == mes_buscado)
    return df_mes
def datos_economicos_mes(mes_buscado):
    df_mes=df.filter(pl.col("mes")==mes_buscado)
    df_reducido=df_mes.select(["nombre_tienda","facturacion","gastos_personal"])
    return df_reducido
def mayor_gasto_mes(mes_buscado):
    df_mes=df.filter(pl.col("mes")==mes_buscado)
    df_ordenado=df_mes.sort("gastos_personal",descending=True)
    df_top_gasto=df_ordenado.head(1) #esto me ayudará a que solo salga una fila. 
    return df_top_gasto
def media_facturacion_global():
    media=df["facturacion"].mean()
    tabla_media=pl.DataFrame({ #esto saldrá en streamlit como una jodida tabla. 
        "Media facturación global":[round(media,2)]
    })
    return tabla_media
