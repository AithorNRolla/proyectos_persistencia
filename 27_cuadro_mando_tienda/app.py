import streamlit as st 
import io 
import importlib #IMPORTLIB (sugerencia de la IA)
import tiendas_repository as repo #aquí llamamos a tiendas_repository.py
importlib.reload(repo) #IMPORTLIB obliga a python a usar siempre la versión más fresca. 
import matplotlib.pyplot as plt 


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
#Aquí vamos a jugar con los gráficos:
total_fact=tabla_tienda["Total facturación"].item()
total_gast=tabla_tienda["Total gastos personal"].item()
#metemos cañita!!!!!!
valores_tienda=[total_fact, total_gast]
etiquetas_tienda=["Total Facturación", "Gastos Personal"]
#grafico:
fig_tienda, ax_tienda=plt.subplots(figsize=(5, 4))
ax_tienda.pie(
    valores_tienda,
    labels=etiquetas_tienda,
    autopct="%1.1f%%",
    colors=["#F4A261", "#B892FF"],
    textprops={"color": "#FDF8F5", "fontsize": 10, "weight": "bold"}
)
ax_tienda.set_title(f"Balance: {tienda_buscada}", color="#FDF8F5", fontsize=12, weight="bold")
buf_tienda=io.BytesIO()
fig_tienda.savefig(buf_tienda, format="png", transparent=True, dpi=200)
st.image(buf_tienda)
plt.close(fig_tienda)

st.divider() #dibuja
#=============== tablas derecha zona mes ===============
st.subheader(f"Análisis detallado del mes:{mes_buscado}")
st.write("1º - Información general de todas las tiendas en este mes:") #TABLA 1
tabla_mes_completa=repo.info_mes_completo(mes_buscado)
st.dataframe(tabla_mes_completa,hide_index=True,use_container_width=True,column_config=config_columnas)
#========================================================
tiendas_x=tabla_mes_completa["nombre_tienda"].to_list()
facturacion_y=tabla_mes_completa["facturacion"].to_list()
gastos_y=tabla_mes_completa["gastos_personal"].to_list()
fig_mes_linea, ax_mes_linea=plt.subplots(figsize=(8, 3.2))
ax_mes_linea.plot(tiendas_x, facturacion_y, marker="o", linewidth=2.5, color="#F4A261", label="Facturación")
ax_mes_linea.plot(tiendas_x, gastos_y, marker="s", linewidth=2.5, color="#B892FF", label="Gastos Personal")
ax_mes_linea.set_title(f"Comparativa lineal - {mes_buscado}", color="#FDF8F5", fontsize=12, weight="bold")
ax_mes_linea.tick_params(colors="#FDF8F5") # Letras de los ejes en blanco marfil
ax_mes_linea.grid(True, linestyle="--", alpha=0.2) # Cuadrícula suave
ax_mes_linea.legend()
buf_mes_linea = io.BytesIO()
fig_mes_linea.savefig(buf_mes_linea, format="png", transparent=True, dpi=200)
st.image(buf_mes_linea)
plt.close(fig_mes_linea)
#========================================================
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
    color="#B892FF"
)
#Ahora metemos gráficas circulares de porcentaje:
st.write(":material/pie_chart: Porcentaje de facturación por tienda este mes.")
nombres_tiendas=tabla_economica["nombre_tienda"].to_list()
valores_facturacion=tabla_economica["facturacion"].to_list()
#Aquí creamos el lienzo:
fig,ax=plt.subplots(figsize=(6, 6))
#==========================
ax.pie(
    valores_facturacion,
    labels=nombres_tiendas,
    autopct="%1.1f%%",
    colors=["#E07A5F", "#F4A261", "#E9C46A", "#B892FF", "#81B29A"],
    textprops={"color": "#F0F7F4", "fontsize": 11, "weight": "bold"}
)
ax.set_title(f"Reparto de facturación - {mes_buscado}", color="#F0F7F4", fontsize=14, weight="bold")
buf=io.BytesIO() #creamos el espacio en RAM. 
fig.savefig(buf, format="png", transparent=True, dpi=200) #esto hace transparente el fondo del gráfico. 
st.image(buf)
st.divider()

st.subheader(f"Media Global de Facturación")
tabla_media=repo.media_facturacion_global()
st.dataframe(tabla_media,hide_index=True,use_container_width=True,column_config=config_columnas)



#Enunciado:


