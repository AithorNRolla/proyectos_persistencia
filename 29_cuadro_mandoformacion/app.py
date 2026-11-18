import streamlit as st 
import io 
import importlib #IMPORTLIB (sugerencia de la IA)
import repositorio as repo #aquí llamamos a repositorio.py
importlib.reload(repo) #IMPORTLIB obliga a python a usar siempre la versión más fresca. 
import matplotlib.pyplot as plt 
#=====Esto de arriba es la misma plantilla del anterio ejercicio, he copiado y pegado.=====#
st.set_page_config(page_title="Panel Académico",layout="wide")
#=====Ahora vamos a empezar a meter mierdas=====#
df=repo.cargar_datos()
cursos,asignaturas,grupos,evaluaciones=repo.obtener_filtros(df) #<---esto llama a repositorio.py
#=====Ahora metemos el SIDEBAR=====#
st.sidebar.markdown( 
    "<h1 style='text-align: center; font-size: 65px; margin-bottom: 0px;'>🐇</h1>", #el conejo de cabecera!!!
    unsafe_allow_html=True,
)
st.sidebar.header("Filtros Académicos 👨‍🎓")
curso_buscado=st.sidebar.selectbox("Curso",cursos)
asignatura_buscada=st.sidebar.selectbox("Asignatura",asignaturas)
grupo_buscado=st.sidebar.selectbox("Grupo",grupos)
evaluacion_buscada=st.sidebar.selectbox("Evaluación",evaluaciones)
#Esto son los cuatro desplegables. 
df_filtrado=repo.filtrar_datos(
    df,curso_buscado,asignatura_buscada,grupo_buscado,evaluacion_buscada
)
#El filtro creado. 
#=====La Mandanga=====#
st.title("Cuadro de Mando Académico 🎓") #título provisional.


#dejo espacio por que sé que aquí meteré mierdecillas. 
alumnos_eval,nota_media,nota_max,nota_min,aprobados=repo.calcular_kpis(
    df_filtrado
)
#metemos columnas: 
col1,col2,col3,col4,col5=st.columns(5)
col1.metric("Alumnos evaluados",alumnos_eval)
col2.metric("Nota media",nota_media)
col3.metric("Nota máxima",nota_max)
col4.metric("Nota mínima",nota_min)
col5.metric("Aprobados",aprobados)

st.divider()
#=====Mandanga 0.2 "Cuadro de Estadística"=====#
st.subheader("Estadística por Asignatura 📖")
if df_filtrado.height >0:
    resumen_asig=repo.tabla_por_asignatura(df_filtrado)
    st.dataframe(resumen_asig,
                use_container_width=True,
                hide_index=True,
                     column_config={
                            "asignatura": "Asignatura",
                            "alumnos_evaluados": "Alumnos Evaluados",
                            "nota_media": st.column_config.ProgressColumn(
                                "Nota Media",
                                min_value=0,
                                max_value=10,
                                format="%.2f",
                                color="#6EE7B7",
                            ),
                            "nota_maxima": "Nota Máxima",
                            "nota_minima": "Nota Mínima",
                            "aprobados": "Aprobados",
                        },
                )
else:
    st.warning("No hay datos para esta combinación de filtros.")
    
st.divider()
#Aquí metemos la tabliñas detatalladas por alumno: 
st.subheader("Detalle por Alumno 🧑‍🏫")
if df_filtrado.height>0:
    resumen_alum=repo.tabla_por_alumno(df_filtrado)
    st.dataframe(
        resumen_alum,
        use_container_width=True,
        hide_index=True,
          column_config={
            "id_alumno": "ID",
            "nombre": "Alumno",
            "curso": "Curso",
            "grupo": "Grupo",
            "nota_media": st.column_config.ProgressColumn(
                "Nota Media",
                min_value=0,
                max_value=10,
                format="%.2f",
                color="#6EE7B7",
            ),
            "asignaturas_evaluadas": "Evaluadas",
            "asignaturas_aprobadas": "Aprobadas",
        },
        ) 
st.divider()
#=====Mandanga 0.3 GRÁFICOS=====#
st.subheader("Representación Gráfica 📈")

opcion_grafico=st.selectbox(
    "Elige qué gráfico visualizar:",
    [
        "Notas por asignatura",
        "Evolución de las evaluaciones",
        "Distribución de notas",
    ],
)

if df_filtrado.height>0:
    fig,ax=plt.subplots(figsize=(8, 3.5))

    # Opción 1: Barras (Notas por asignatura)
    if opcion_grafico=="Notas por asignatura":
        
        barras=ax.bar( #añadido el barras= para que sea variable. 
            resumen_asig["asignatura"],
            resumen_asig["nota_media"],
            color="#6EE7B7",
        )
        ax.bar_label(
            barras, padding=3, color="#F3E8FF", fontweight="bold") #sugerencia IA. 
        ax.set_title("Nota Media por Asignatura", color="#F3E8FF")
        ax.set_ylabel("Nota Media")
        ax.set_ylim(0, 10.8)  # Escala fija de 0 a 10 para notas
        

    # Opción 2: Líneas (Evolución de las evaluaciones)
    elif opcion_grafico=="Evolución de las evaluaciones":
        resumen_eval=repo.datos_evolucion(df_filtrado)
        # Convertimos evaluación a texto ("1", "2") para que el eje X no ponga decimales (1.5)
        evals_texto=[str(e) for e in resumen_eval["evaluacion"]]
        ax.plot(
            evals_texto,
            resumen_eval["nota_media"],
            marker="o",
            color= "#6EE7B7",
            linewidth=2.5,
        )
        ax.set_title("Evolución de la Nota Media por Evaluación", color="#F3E8FF")
        ax.set_xlabel("Evaluación")
        ax.set_ylabel("Nota Media")
        ax.set_ylim(0, 10)

    # Opción 3: Histograma (Distribución de notas)
    elif opcion_grafico=="Distribución de notas":
        ax.hist(
            df_filtrado["nota"],
            bins=[0, 2, 4, 5, 6, 7, 8, 9, 10],
            color= "#6EE7B7",
            edgecolor="#231B36",
        )
        ax.set_title("Distribución de Notas (Histograma)", color="#F3E8FF")
        ax.set_xlabel("Rango de Nota")
        ax.set_ylabel("Cantidad de Exámenes")

    # Estilizado limpio para fondo oscuro/terracota
    ax.tick_params(colors="#FDF8F5")
    ax.yaxis.label.set_color("#FDF8F5")
    ax.xaxis.label.set_color("#FDF8F5")
    for spine in ax.spines.values():
        spine.set_color("#FDF8F5")

    # Guardamos en memoria RAM en transparente y pintamos en Streamlit
    buf=io.BytesIO()
    fig.savefig(buf, format="png", transparent=True, bbox_inches="tight")
    st.image(buf)
