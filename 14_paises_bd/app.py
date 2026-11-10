"""
Utilizando los archivos de funciones definidos, hará lo siguiente:
-Borrará las tablas de la base de datos.
-Recuperará continentes y países del JSON.
-Preparará los datos anteriores, para poder enviarlos a las funciones de base de datos. 
-Llamará a las funciones para guardar continentes y guardar paises. 

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


# TAREA 4: Llamar a las funciones para guardar en MySQL
op.crear_continentes(lista_continentes_limpia)
op.crear_paises(lista_paises_limpia)

print("¡Proceso completado madafaka!")