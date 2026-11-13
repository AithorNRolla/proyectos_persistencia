import pandas as pd
lista_reproduccion=[
    {"titulo":"cancion inventada","duracion":3.20,"valoracion":4},
    {"titulo":"Bohemian Rhapsody","duracion":5.40,"valoracion":10},
    {"titulo":"Green summer","duracion":4.10,"valoracion":7}
]
#df=pd.DataFrame(lista_reproduccion)
#print(df)
df=pd.read_csv("empleados.csv",encoding="utf-8")
print(df)