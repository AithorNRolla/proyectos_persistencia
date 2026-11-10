import json 
def continentes():
    with open("countries.json","r") as f: 
        return list(set(map(lambda p:p["region"],json.load(f))))
def paises():
       with open("countries.json","r") as f: 
            return json.load(f)

"""
import json 

def continentes():
    with open("countries.json", "r", encoding="utf-8") as f: 
        # Extrae las regiones únicas eliminando duplicados mediante un conjunto (set)
        return list(set(map(lambda p: p["region"], json.load(f))))

def paises():
    with open("countries.json", "r", encoding="utf-8") as f: 
        return json.load(f)
    """

#Esto de aquí arriba está limpiado con la IA. 