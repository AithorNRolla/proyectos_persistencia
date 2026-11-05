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
   # print(f.readlines()) #Añadimos el print con readlines. 
   lista_dias=f.readlines()
#print(lista_dias) aquí me sale la lista en sucio. 
#Aquí abajo es el ejercicio como tal, corrigiendo el texto en dias.txt:
lista_limpia=[dia.strip("\n")for dia in lista_dias] #metodo ia (strip directo)
print(lista_limpia)
lista_limpia=list(map(lambda a:a.strip(),lista_dias)) #metodo profesor. 
print(lista_limpia)
#texto="aaa \n \t" 
#texto_limpio=texto.strip()
#print(texto)
#print(texto_limpio)
