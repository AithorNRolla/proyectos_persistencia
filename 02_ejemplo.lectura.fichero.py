"""""
f=open("dias.txt","r")
linea=f.readline()
while linea!="":
    print(linea)
    linea=f.readline()
f.close()
"""
#Arriba el primer ejemplo usado. Abajo es con "with"
with open("dias.txt","r") as f:
    linea=f.readline()
    while linea!="":
     print(linea)
     linea=f.readline()
with open("dias.txt","r") as f: #copiamos esto y lo pegamos. 
    print(f.readlines()) #Añadimos el print con readlines. 