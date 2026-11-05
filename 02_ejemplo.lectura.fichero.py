f=open("dias.txt","r")
linea=f.readline()
while linea!="":
    print(linea)
    linea=f.readline()
f.close()