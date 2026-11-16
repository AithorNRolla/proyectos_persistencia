import polars as pl #NO DARLE AL PLAY, DARÁ ERROR, ESTO ES SOLO UNA CHULETA DE APUNTES. 

# ==============================================================================
# 1. ENTRADA Y SALIDA DE DATOS (I/O)
# ==============================================================================
df = pl.read_csv("archivo.csv")       # Carga inmediata en memoria (Eager)
lf = pl.scan_csv("archivo.csv")       # Carga diferida/planificada (Lazy)
df_json = pl.read_json("archivo.json")

df.write_csv("salida.csv")            # Exportar a CSV


# ==============================================================================
# 2. INSPECCIÓN RÁPIDA DE LA TABLA
# ==============================================================================
print(df.head(5))       # Primeras 5 filas
print(df.tail(5))       # Últimas 5 filas
print(df.shape)         # (filas, columnas)
print(df.columns)       # Lista con nombres de columnas
print(df.dtypes)        # Tipos de datos de cada columna
print(df.describe())    # Estadísticas resumen (media, min, max, etc.)


# ==============================================================================
# 3. SELECCIONAR COLUMNAS (.select) Y EXPRESIONES (pl.col)
# ==============================================================================
# Seleccionar columnas concretas
df_sel = df.select([
    pl.col("columna_a"),
    pl.col("columna_b")
])

# Seleccionar por tipo de dato
df_numeros = df.select(pl.col(pl.Int64, pl.Float64))


# ==============================================================================
# 4. FILTRAR FILAS (.filter)
# ==============================================================================
# Condición simple
df_filtrado = df.filter(pl.col("edad") >= 18)

# Condición múltiple (& = Y, | = O, ~ = NO)
df_complejo = df.filter(
    (pl.col("edad") >= 18) & (pl.col("ciudad") == "Madrid")
)

# Filtrar por lista de valores (.is_in)
df_varios = df.filter(pl.col("ciudad").is_in(["Madrid", "Barcelona"]))


# ==============================================================================
# 5. CREAR O MODIFICAR COLUMNAS (.with_columns)
# ==============================================================================
# .alias() bautiza la nueva columna
df_nuevo = df.with_columns([
    (pl.col("precio") * 1.21).alias("precio_con_iva"),
    (pl.col("ingresos") - pl.col("gastos")).alias("beneficio")
])


# ==============================================================================
# 6. ORDENAR (.sort)
# ==============================================================================
df_ordenado = df.sort("precio", descending=True)                  # Una columna
df_multi_orden = df.sort(["ciudad", "precio"], descending=[False, True])


# ==============================================================================
# 7. AGRUPAR Y RESUMIR (.group_by + .agg)
# ==============================================================================
resumen = df.group_by("categoria").agg([
    pl.len().alias("total_filas"),               # Contar registros
    pl.col("ventas").sum().alias("suma_ventas"), # Sumar
    pl.col("ventas").mean().alias("media"),      # Promedio
    pl.col("ventas").max().alias("maximo"),      # Máximo
    pl.col("ventas").min().alias("minimo")       # Mínimo
])


# ==============================================================================
# 8. LIMPIEZA DE DATOS NULOS (null / NaN)
# ==============================================================================
nulos = df.null_count()                                  # Contar nulos por columna
df_sin_nulos = df.drop_nulls()                           # Borrar filas con nulos
df_relleno = df.with_columns(pl.col("ventas").fill_null(0)) # Rellenar nulos con 0


# ==============================================================================
# 9. EJECUCIÓN PEREZOSA (LAZY API)
# ==============================================================================
plan = (
    pl.scan_csv("archivo.csv")
    .filter(pl.col("ventas") > 1000)
    .group_by("categoria")
    .agg(pl.col("ventas").sum().alias("total"))
    .sort("total", descending=True)
)

resultado = plan.collect()  # Ejecuta todo el plan optimizado en paralelo
