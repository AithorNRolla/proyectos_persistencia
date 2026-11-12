import pymongo as pm 
url="mongodb://localhost:27017"
serv=pm.MongoClient(url)
#Cuidado con las tildes, hay que poner el MISMO nombre de la base de datos.
#Que es lo que me ha pasado con "librería", CON TILDE. 
col_libros=serv.librería.libros
#col_libros.insert_one({'isbn': 'yu12', 'titulo': 'C++', 'paginas': 520, 'categoria': 'programación', 'precio': 40.7}) #Añadimos este a mongo!
col_libros.update_one({"isbn":"1111A"},{"$inc":{"precio":20}})
libros=serv.librería.libros.find({"categoria":"programación"})  
for lb in libros:                  
    print(lb)
serv.close()
