import streamlit as st 
import importlib #IMPORTLIB (sugerencia de la IA)
import tiendas_repository as repo #aquí llamamos a tiendas_repository.py
importlib.reload(repo) #IMPORTLIB obliga a python a usar siempre la versión más fresca. 

st.title("Panel de Control de Tiendas")

# Molde reutilizable de cabeceras profesionales
config_columnas = {
    "nombre_tienda": st.column_config.TextColumn("🏪 Tienda"),
    "Tienda": st.column_config.TextColumn("🏪 Tienda"),
    "mes": st.column_config.TextColumn("📅 Mes"),
    "Mes con mayor facturación": st.column_config.TextColumn("🏆 Mes Récord"),
    "facturacion": st.column_config.NumberColumn("💶 Facturación", format="%d €"),
    "Total facturación": st.column_config.NumberColumn("💶 Total Facturación", format="%d €"),
    "gastos_personal": st.column_config.NumberColumn("👥 Gastos Personal", format="%d €"),
    "Total gastos personal": st.column_config.NumberColumn("👥 Total Gastos Personal", format="%d €"),
    "año_apertura": st.column_config.NumberColumn("🏛️ Año Apertura", format="%d"),
    "Media facturación global": st.column_config.NumberColumn("📈 Media Global", format="%.2f €")
}


listas_tiendas=repo.obtener_tiendas()
listas_meses=repo.obtener_meses()
#==================== sidebar ==========================
st.sidebar.title(":material/dashboard: Gestión Comercial") #añadido detallles
st.sidebar.divider() #añadido detallles
st.sidebar.header("Filtros de Búsqueda")
tienda_buscada=st.sidebar.selectbox(                       #("Selecciona una tienda:",listas_tiendas) la anterior. 
    "Selecciona una tienda:",
    listas_tiendas,
    ) 
mes_buscado=st.sidebar.selectbox(                          #("Selecciona un mes:",listas_meses) la anterior.
    "Selecciona un mes:",
    listas_meses,
    )
#=================== tablas derecha ====================
st.subheader(f"Resumen económico:{tienda_buscada}") #nos metemos con las tiendas!!!
tabla_tienda=repo.resumen_por_tienda(tienda_buscada) #polars?
st.dataframe(tabla_tienda,hide_index=True,use_container_width=True,column_config=config_columnas)#el hide_index oculta la fila 0, ayudita IA. 
st.divider() #dibuja
#=============== tablas derecha zona mes ===============
st.subheader(f"Análisis detallado del mes:{mes_buscado}")
st.write("1º - Información general de todas las tiendas en este mes:") #TABLA 1
tabla_mes_completa=repo.info_mes_completo(mes_buscado)
st.dataframe(tabla_mes_completa,hide_index=True,use_container_width=True,column_config=config_columnas)
st.write("2º - Desglose de facturación y gasto del personal:")
tabla_economica=repo.datos_economicos_mes(mes_buscado)
st.dataframe(tabla_economica,hide_index=True,use_container_width=True,column_config=config_columnas) #TABLA 2
st.bar_chart(
    tabla_economica,
    x="nombre_tienda",
    y=["facturacion","gastos_personal"],
    color=["#E07A5F", "#F2CC8F"] 
)
st.write("3º - Tienda con mayor gasto de personal del mes:")
tabla_mayor_gasto=repo.mayor_gasto_mes(mes_buscado)
st.dataframe(tabla_mayor_gasto,hide_index=True,use_container_width=True,column_config=config_columnas) #TABLA 3
st.write(":material/bar_chart: Comparativa de gastos personal de tiendas")
st.bar_chart(
    tabla_economica,
    x="nombre_tienda",
    y="gastos_personal",
    color="#C084FC"
)
st.divider()

st.subheader(f"Media Global de Facturación")
tabla_media=repo.media_facturacion_global()
st.dataframe(tabla_media,hide_index=True,use_container_width=True,column_config=config_columnas)



#Enunciado:
 """
    Tenemos que hacer una app con un sidebar a la izquierda con dos desplegables (tienda y mes) VENTAS.CSV
    Al seleccionar una tienda se ha de mostrar a la derecha:
    - Una tabla que contenga un total de facturacion/total de gastos de personal/mes con mayor facturacion
    Al seleccionar un mes se ha de mostrar a la derecha:
    - Una tabla con información de dicho mes de todas las tiendas (facturacion seguramente)
    - Una tabla con los datos de ese mes (facturacion/total gastos de personal)
    - Debajo de estas tablas una media de facturación de todas las tablas
    - Una tabla con la tienda que tenga el mayor gasto de personal de dicho mes
    
    """

