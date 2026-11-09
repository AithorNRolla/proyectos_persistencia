import streamlit as st
import json 
if "lista_paises_limpia" not in st.session_state:
    
    with open("countries.json","r",encoding="utf-8") as f:
        datos_sucios=json.load(f)
    
    st.session_state["lista_paises_limpia"]=[
            {
                "name": p["name"],
                "region": p["region"],
                "population": p["population"],
                "flags": p["flags"]["png"]  #Extraemos la URL de la imagen directamente aquí
            }
            for p in datos_sucios
        ]
paises = st.session_state["lista_paises_limpia"]

tab_todos,tab_buscar,tab_poblacion=st.tabs(["Mostrar todos","Búsqueda por país","Número de habitantes"])
"""

"""
#El jodido bucle y las opciones: 
with tab_todos:
    st.title("Listado mundial de países soberanos")
    st.dataframe(
        paises, 
        column_config={"flags": st.column_config.ImageColumn("Bandera")}
    )
with tab_buscar:
    st.title("Búsqueda por nombre:")
    nombre_buscar=st.text_input("Introduce el nombre del país en inglés: ")
    if st.button("Buscar"):
        libs=list(filter(lambda lib:lib["name"].lower()==nombre_buscar.lower(),paises)) 
        if libs:
            encontrado=libs[0]
            st.success(f"País: {libs[0]['name']}, Continente:{libs[0]['region']},Población:{libs[0]['population']}")
            st.image(encontrado["flags"], width=200)
        else:
            st.error("País no encontrado/destruído")


with tab_poblacion:
    st.title("Lista máxima población")            
    
    paises_ordenados=sorted(paises, key=lambda lib: lib["population"], reverse=True)
   
      # Usamos st.dataframe en lugar de st.table para tener visuales
    st.dataframe(
        paises_ordenados,
        column_config={
            # Le decimos a Streamlit: "Trata la URL de la imagen como una foto real"
            "flags": st.column_config.ImageColumn("Bandera")
        }
    )
