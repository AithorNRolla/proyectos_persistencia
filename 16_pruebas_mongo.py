import pymongo as pm 
url="mongodb://localhost:27017"
serv=pm.MongoClient(url)
libros=serv.librería.libros.find() #Cuidado con las tildes, hay que poner el MISMO nombre de la base de datos. 
for lb in libros:                  #Que es lo que me ha pasado con "librería", CON TILDE. 
    print(lb)
serv.close()