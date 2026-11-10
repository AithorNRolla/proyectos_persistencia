"""
Utilizando los archivos de funciones definidos, hará lo siguiente:
-Borrará las tablas de la base de datos.
-Recuperará continentes y países del JSON.
-Preparará los datos anteriores, para poder enviarlos a las funciones de base de datos. 
-Llamará a las funciones para guardar continentes y guardar paises. 

"""
"""
import json
import operaciones as op
op.borrar_tablas()

with open("datos.json","r",encoding="utf-8") as archivo: #¿Cargamos el json?
    datos_json = json.load(archivo)
    
#Listas vacías listas para ser preparadas
lista_continentes_limpia=[]
lista_paises_limpia=[]

#metemos pasos anteriores ^-^ 
for item in datos_json:
    #Extraermos el continente. 
    nom_continente = item["continente"]
    
    # Evitamos duplicados en la lista de continentes antes de enviarla?
    if nom_continente not in lista_continentes_limpia:
        lista_continentes_limpia.append(nom_continente)
        
    #Extraemos los 3 datos del país
    #Ejemplo: item["name"], item["population"], item["flags"]["png"] (ejemplo de la IA)
    nom_pais = item["pais"]
    poblacion = item["poblacion"]
    url_bandera = item["bandera"] 
    
    #¿Guardamos?
    lista_paises_limpia.append((nom_pais, poblacion, url_bandera))


#Llamar a las funciones para guardar en MySQL
op.crear_continentes(lista_continentes_limpia)
op.crear_paises(lista_paises_limpia)

print("¡Proceso completado madafaka!")
"""
#Arriba está lo que yo he escrito mientras que abajo está lo del profesor. 
import operaciones_bd as opbd
import operaciones_json as opjs

    
opbd.borrar_tablas()
continentes=opjs.continentes() #["Asia","Europe",.]
opbd.crear_continentes(continentes)
continentes_bd=opbd.devolver_continentes() #[{"continente":"Asia",idContinente":3},.]
paises=opjs.paises() #[{"name":"España","region":"Europe"}]
def obtener_idcontinente(continente):
    return [c["idContinente"] for c in continentes_bd if c["continente"]==continente][0]
#formateamos la lista de paises tal y como lo espera la función crear_paises
paises_para_bd=[{"pais":p["name"],
                 "poblacion":p["population"],
                 "bandera":p["flags"]["png"],"idContinente":obtener_idcontinente(p["region"])} for p in paises]
opbd.crear_paises(paises_para_bd)
print("Datos almacenados!!!") 

#Aquí abajo es código limpiado con la IA de lo de más arriba mío pero no funciona: 
""""
import streamlit as st
import operaciones as opbd

#Config
st.set_page_config(page_title="Visor Mundial", page_icon="🌎", layout="wide")

st.title("🌎 Visor Mundial de Países Full-Stack")
st.subheader("Datos relacionales en tiempo real desde MySQL")

#Empezamos los continentes:
continentes_bd = opbd.devolver_continentes()

#Creamos una lista limpia con los nombres de los continentes para mostrar en el wombocombo
nombres_continentes = [c["continente"] for c in continentes_bd]

#Cabecera visual?
continente_seleccionado = st.selectbox(
    "Selecciona un continente para filtrar los países:", 
    options=nombres_continentes
)

#Buscamos la ID.
id_continente_actual = None
for c in continentes_bd:
    if c["continente"] == continente_seleccionado:
        id_continente_actual = c["idContinente"]
        break

#Mezclamos lo del profe.
if id_continente_actual is not None:
    # Trae la lista de diccionarios de los países filtrados por WHERE idContinente = %s
    datos_paises = opbd.paises_por_continente(id_continente_actual)
    
    #Aquí hacemos cuatro mierdas:
    configuracion_columnas = {
        "idPais": None,          #Ocultamos la columna del ID primario para que quede limpio
        "idContinente": None,    #Ocultamos la columna de la clave foránea
        "pais": st.column_config.TextColumn(title="Nombre del País"),
        "poblacion": st.column_config.NumberColumn(title="Habitantes", format="%d"),
        "bandera": st.column_config.ImageColumn(title="Bandera Oficial") # Transforma la URL en foto
    }
    #Definimos.
    orden_columnas = ["bandera", "pais", "poblacion"] 
    
    #¿El dataframe?
    if datos_paises:
        st.dataframe(
            datos_paises,
            column_config=configuracion_columnas,
            column_order=orden_columnas,
            use_container_width=True
)
    else:
        st.warning("No se encontraron países registrados para este continente.")
"""
#Este código tampoco funciona