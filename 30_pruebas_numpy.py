import numpy as np 
datos=np.array([10,2,11,8,20]) #array de una única dimensión.
datos2=np.array([[4,8,-1],[5,3,11]])
print(datos[0])
print=(datos2[1][1])

print(datos2[datos2>0]) #no se por qué esto da error. 

for fila in datos2:
    for celda in fila:
        print(celda)