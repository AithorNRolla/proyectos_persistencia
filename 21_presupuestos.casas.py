""" 
Solicitamos presupuesto y mostramos datos a patir del ficho houses.csv,
además se ordenará de mayor a menor precio. 

"""
import pandas as pd

df=pd.read_csv("houses.csv") #al loro con la variable, df= "metemos aquí el pd"
presupuesto=float(input("Introduce tu presupuesto máximo: "))
filtro_presupuesto=(df["price"]<=presupuesto)
casas_posibles=df[filtro_presupuesto]
casas_ordenadas=casas_posibles.sort_values(by="price",ascending=False)
#Seguramente se pueda hacer más resumido, poco a poco. 
print("Casas disponibles (de mayor a menor)")
print(casas_ordenadas)
print(f"Total de casas encontradas: {len(casas_ordenadas)}")

#"LO DE ABAJO ES LA FORMA RESUMIDA" que es más profesional. 
"""
import pandas as pd "LO DE ABAJO ES LA FORMA RESUMIDA"

df = pd.read_csv("houses.csv")
presupuesto = float(input("Introduce tu presupuesto máximo: "))

# Filtramos y ordenamos de golpe en una sola tubería
resultado = df[df["price"] <= presupuesto].sort_values(by="price", ascending=False)

print("Casas disponibles (de mayor a menor)")
print(resultado)
print(f"Total de casas encontradas: {len(resultado)}")
""" 
