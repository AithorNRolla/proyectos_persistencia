from pathlib import Path
import polars as pl

CARPETA_ACTUAL=Path(__file__).parent


def cargar_datos():
    df_notas=pl.read_csv(CARPETA_ACTUAL / "notas.csv").drop_nulls()
    df_alumnos=pl.read_csv(CARPETA_ACTUAL / "alumnos.csv").drop_nulls()
    df_notas=df_notas.with_columns(
        pl.col("nota")
        .cast(pl.String)
        .str.strip_chars()
        .str.replace(",", ".")
        .cast(pl.Float64, strict=False)
    ).drop_nulls()
    df=df_notas.join(df_alumnos, on="id_alumno", how="left")
    return df
#===== Todo este bloque de arriba es para que se cargue dónde está almacenado, sugerencia de la IA=====#
#======================================================================================================#
#df=pl.read_csv("notas.csv","alumnos.csv") [no me sirve por que hace dos instrucciones]
"""
def cargar_datos():
    df_notas=pl.read_csv("notas.csv")
    df_alumnos=pl.read_csv("alumnos.csv")
    df=df_notas.join(df_alumnos,on="id_alumno",how="left") #esto hace que me busque el alumno. 
    return df
"""
def obtener_filtros(df): #metemos ["Todos"] para que salga esa opción. 
    cursos=["Todos"]+df["curso"].unique(maintain_order=True).to_list()
    asignaturas=["Todos"]+df["asignatura"].unique(maintain_order=True).to_list()
    grupos=["Todos"]+df["grupo"].unique(maintain_order=True).to_list()
    evaluaciones=["Todos"]+df["evaluacion"].unique(maintain_order=True).to_list()
    return cursos,asignaturas,grupos,evaluaciones
def filtrar_datos(
    df,curso_buscado,asignatura_buscada,grupo_buscado,evaluacion_buscada
):
    df_filtrado=df
    if curso_buscado!="Todos":
        df_filtrado=df_filtrado.filter(pl.col("curso")==curso_buscado)
    if asignatura_buscada!="Todos":
        df_filtrado=df_filtrado.filter(pl.col("asignatura")==asignatura_buscada)
    if grupo_buscado!="Todos":
        df_filtrado=df_filtrado.filter(pl.col("grupo")==grupo_buscado)
    if evaluacion_buscada!="Todos":
        df_filtrado=df_filtrado.filter(pl.col("evaluacion")==evaluacion_buscada)
    return df_filtrado
def calcular_kpis(df_filtrado):
    # Si el filtro deja 0 resultados, devolvemos ceros para evitar errores!!!!
    if df_filtrado.height==0:
        return 0, 0.0, 0.0, 0.0, 0

    alumnos_eval=df_filtrado["id_alumno"].n_unique()
    media_cruda=df_filtrado["nota"].mean()
    nota_media=round(media_cruda, 2) if media_cruda is not None else 0.0   #(df_filtrado["nota"].mean(), 2)
    nota_max=df_filtrado["nota"].max()or 0.0
    nota_min=df_filtrado["nota"].min()or 0.0
    aprobados=df_filtrado.filter(pl.col("nota") >= 5).height
    
    return alumnos_eval,nota_media,nota_max,nota_min,aprobados
def tabla_por_asignatura(df_filtrado): #asigna las asignaturas y las enlaza con las notas. 
    # Las mismas 5 opciones:
    resumen_asig=df_filtrado.group_by("asignatura",maintain_order=True).agg(
        [
            pl.col("id_alumno").n_unique().alias("alumnos_evaluados"),
            pl.col("nota").mean().round(2).alias("nota_media"),
            pl.col("nota").max().alias("nota_maxima"),
            pl.col("nota").min().alias("nota_minima"),
            (pl.col("nota") >= 5).sum().alias("aprobados"),
        ]
    )
    return resumen_asig


def tabla_por_alumno(df_filtrado):
    # Las 7 columnas exactas agrupadas por alumno
    resumen_alum=(
        df_filtrado.group_by(
            ["id_alumno", "nombre", "curso", "grupo"], maintain_order=True
        )
        .agg([
            pl.col("nota").mean().round(2).alias("nota_media"),
            pl.col("asignatura").count().alias("asignaturas_evaluadas"),
            (pl.col("nota") >= 5).sum().alias("asignaturas_aprobadas"),
        ])
        .sort("id_alumno")
    )
    return resumen_alum
def datos_evolucion(df_filtrado): #lo último a añadir. 
    resumen_eval=(
        df_filtrado.group_by("evaluacion")
        .agg(pl.col("nota").mean().round(2).alias("nota_media"))
        .sort("evaluacion")
    )
    return resumen_eval