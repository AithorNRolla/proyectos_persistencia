
"""""
import operaciones as op
#op.crear_continentes(["con1","con2","con3"])
op.borrar_tablas()
op.crear_continentes(["con1","con2","con3"])
print(op.devolver_continentes())
op.borrar_tablas()
op.crear_paises(["pais","poblacion","bandera"])

#Esto no sale como debería. 
print("Países en DB:", op.devolver_paises()) 
"""
#Esto está limpiado con IA con lo de arriba:
import operaciones as opbd
import operaciones_json as opjs

# 1. Limpiamos las tablas de MySQL en el orden correcto
opbd.borrar_tablas()

# 2. Extraemos e insertamos los continentes únicos del JSON
continentes_del_json = opjs.continentes() 
opbd.crear_continentes(continentes_del_json)

# 3. Descargamos los continentes de MySQL para conocer sus IDs asignados automáticamente
continentes_en_bd = opbd.devolver_continentes() 

# 4. Función relacional: Busca en memoria el ID que MySQL le dio a una región
def obtener_idcontinente(nombre_region):
    for c in continentes_en_bd:
        if c["continente"] == nombre_region:
            return c["idContinente"]
    return None

# 5. Extraemos los países y preparamos sus datos acoplando la clave foránea
paises_del_json = opjs.paises()
paises_listos_para_bd = []

for p in paises_del_json:
    # Cruzamos el nombre de la región con nuestra función para hallar su ID
    id_del_continente = obtener_idcontinente(p["region"])
    
    # Extraemos las llaves del JSON (name, population, flag)
    # y añadimos el id_del_continente al final de la tupla
    paises_listos_para_bd.append((p["name"], p["population"], p["flag"], id_del_continente))

# 6. Guardamos los países con sus relaciones en la base de datos
opbd.crear_paises(paises_listos_para_bd)

# 7. Verificación final en consola
print("\n🟢 ¡PROCESO COMPLETADO MADAFAKA!")
print(f"Continentes guardados: {len(continentes_del_json)}")
print(f"Países relacionados guardados: {len(paises_listos_para_bd)}")
print("\nMuestra de países en DB:", opbd.devolver_paises()[:2]) # Muestra solo los primeros 2
