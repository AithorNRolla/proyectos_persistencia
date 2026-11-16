import polars as pl

df=pl.scan_csv("houses.csv")
#print(df)
filtro=df.filter(pl.col("rooms")>2)
print(
filtro.select
(pl.col("price").mean())
      .collect()) 