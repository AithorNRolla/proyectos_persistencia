import streamlit as st  
import csv 

if "lista_casas" not in st.session_state:
    viviendas=[]
    with open("houses.csv", "r",encoding="utf-8") as f:
        lector=csv.DictReader(f)
        for fila in lector:
             viviendas.append({
                "size": int(fila["size"]),
                "rooms": int(fila["rooms"]),
                "age": int(fila["age"]),
                "location": int(fila["location"]),
                "price": int(fila["price"]) * 1000  # Multiplicamos por 1000 para tener euros reales (entre comillas)
            })
    st.session_state["lista_casas"] = viviendas
casas=st.session_state["lista_casas"]
    
st.title("Buscador inmobilaria de CSV")
    
presupuesto_max=st.slider("¿Presupuesto máximo(€)?", min_value=50000, max_value=500000, value=250000, step=10000)
habitaciones_min=st.number_input("Número mínimo de habitaciones:", min_value=1, max_value=5, value=2)
    
if st.button("Buscar casas disponibles"):
        casas_filtradas=list(filter( lambda c:c["price"]<= presupuesto_max and c["rooms"]>= habitaciones_min, casas))
        if casas_filtradas:
         st.success(f"¡Hemos encontrado {len(casas_filtradas)} opciones para ti!")
         st.dataframe(casas_filtradas)
        else:
         st.error("No hay ninguna casa en el CSV que coincida con tu presupuesto o criterios actuales.")