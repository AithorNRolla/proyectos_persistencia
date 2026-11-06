import math
#Solicitar al usuario la introducción de unas coordenadas (x,y),
#cada pareja de coordenadas se guarda en una lista. 
#Cada vez que solicitamos coordenadas
#preguntamos si quiere introducir nuevas coordenadas. 
#En caso afirmativo, se solicitan de nuevo
#si responde que no, finaliza el programa mostrando la lista 
#de coordenadas

#Las coordenadas no las debemos de tener en memoria, si no en fichero. 
""" import csv
import math """
#aquí preparamos la lista (que ya la tenía creada)
coordenadas=[]
#Esto de abajo pertenece al ejercicio 28, para no borrarlo está comentado. 
""" def distancia(punto1,punto2):
    #return math.dist(punto1,punto2)
   return math.hypot(punto1[0]-punto2[0],punto1[1]-punto2[1]) 
resp="S"
while resp=="S" or resp=="s":
    x=int(input("X de la tienda: "))
    y=int(input("Y de la tienda: "))
    coordenadas.append((x,y))
    resp=input("¿Quiere introducir nuevas coordenadas (S/N)?")
print(coordenadas) """
#Se pide al usuario su posición, después el programa
#le mostrará las coordenadas del punto 
#más cercano a su posición
""" with open('coordenadas.csv')as fichero:
    lector=csv.DictReader(fichero)
    for fila in lector:
        x_coordenada=int(fila["x"])
        y_coordenada=int(fila["y"]) #¿extraemos?
        coordenadas.append((x_coordenada,y_coordenada))
print("Coordenadas cargadas con éxito: ",coordenadas)

pos_usuario=(int(input("Tu posición x: ")),int(input("Tu posición y: "))) """#la mantenemos

#Esto de abajo también es del ejercicio 28, por lo que lo mantenemos en comentado. 
""" #En esta variable se obtendrá la distnacia más corta
distancia_corta=distancia(coordenadas[0],pos_usuario)
#En esta variable se deberá obtener la tupla de la tienda más cercana
coordenada_tienda=coordenadas[0]
#recorremos las coordenadas y para cada una de ellas,
#obtenemos la distancia con la posición del usuario. Si encontramos que esa distancia
#es inferior distancia_corta, actualizamos tanto las variables distancia_corta
#como coordenada_tienda """

""" coordenada_inicial=coordenadas[0]
distancia_corta=math.hypot(coordenada_inicial[0]-pos_usuario[0],coordenada_inicial[1]-pos_usuario[1])
#Esta parte se ha modificado para cuadrar mejor. 
for coord in coordenadas:
    dist=math.hypot(coord[0]-pos_usuario[0],coord[1]-pos_usuario[1])
    if dist<distancia_corta:
        distancia_corta,coordenada_tienda=dist,coord
print(f"La tienda mas cercana a {pos_usuario} tiene de coordenadas {coordenada_tienda}") 
 """
#Aquí abajo hay dragones: (solución profesor)

""" Se pide al usuario su posición, después el programa
le mostrará las coordenadas del punto 
más cercano a su posición
import math
import csv

def distancia(punto1,punto2):
   return math.dist(punto1,punto2)
   return math.hypot(punto1[0]-punto2[0],punto1[1]-punto2[1]) 

pos_usuario=(int(input("Tu posición x: ")),int(input("Tu posición y: ")))
dir_fichero="coordenadas.csv"
#En esta variable se obtendrá la distnacia más corta
distancia_corta=None
#En esta variable se deberá obtener la tupla de la tienda más cercana
coordenada_tienda=None
with open(dir_fichero,"r") as f:
    coordenadas=csv.DictReader(f)
    for row in coordenadas:
        coord=(int(row["x"]),int(row["y"]))
        if distancia_corta==None: #es la primera vez
            distancia_corta=distancia(coord,pos_usuario)
        if coordenada_tienda==None:
            coordenada_tienda=coord
        #recorremos las coordenadas y para cada una de ellas,
        #obtenemos la distancia con la posición del usuario. Si encontramos que esa distancia
        #es inferior distancia_corta, actualizamos tanto las variables distancia_corta
        #como coordenada_tienda
        dist=distancia(coord,pos_usuario)
        if dist<distancia_corta:
            distancia_corta,coordenada_tienda=dist,coord
print(f"La tienda mas cercana a {pos_usuario} tiene de coordenadas {coordenada_tienda}")  """

import math
import csv

pos_usuario = (int(input("Tu posición x: ")), int(input("Tu posición y: ")))

# Intentamos usar infinito, veremos qué sucede. 
# ¿eficiencia de IA?
distancia_corta = float('inf')
coordenada_tienda = None

with open("coordenadas.csv", "r") as f:
    lector = csv.DictReader(f)
    for row in lector:
        coord = (int(row["x"]), int(row["y"]))
        
        #Aquí teóricamente calcula mIm
        dist = math.dist(coord, pos_usuario)
        
        if dist < distancia_corta:
            distancia_corta, coordenada_tienda = dist, coord

print(f"La tienda mas cercana a {pos_usuario} tiene de coordenadas {coordenada_tienda}")
