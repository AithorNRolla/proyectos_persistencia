#----------Esto es una modificación del ejercicio 23 o 24--------------------------


#Al iniciar el programa se debe mostrar el siguiente menú:
#1 - Añadir nota.
#2 - Mostrar notas extremas. 
#3 - Total de aprobados. 
#4 - Nota media. 
#5 - Mostrar todas.
#6 - Salir. 

#El usuario elige una opción (1 al 6) y el programa le muestra
#los datos necesarios para llevar a cabo la acción. Después, vuelve a salir el menú. 
#Así hasta que elija la opción de salir. 
#LAS NOTAS SE GUARDAN EN UN FICHERO
def guardar_nota_en_fichero(nota):
    """Abre el archivo en modo 'a' (añadir) para no borrar lo anterior 
    y guarda la nota con un salto de línea."""
    with open("notas.txt","a") as f:
        f.write(str(nota)+"\n")
def cargar_notas_del_fichero():
    """Abre el archivo en modo 'r', lee las líneas, las limpia de saltos 
    de línea con .strip() y las convierte a números reales (float)."""
    try:
        with open("notas.txt","r") as f:
            lineas=f.readlines()
            return[float(linea.strip())for linea in lineas]
    except FileNotFoundError:
        return[] 
        
    
opcion=0
while opcion!=6: #Recordemos que la ! signifira "diferente de". 
    print("\n Menú de notas")
    print("1: Añadir nota")
    print("2: Mostrar nota extremas")
    print("3: Total de aprobados")
    print("4: Nota media")
    print("5: Mostrar todas")
    print("6: Salir")
    opcion=int(input("Elija una opción del 1 al 6   "))
    if opcion==1:
        nueva_nota=float(input("Añadir nota: "))
        guardar_nota_en_fichero(nueva_nota)
        print("Nota guardada ")
    elif opcion==2:
        notas=cargar_notas_del_fichero()
        if len(notas)==0:
            print("Todavía no hay notas extremas")
        else:
            nota_extrema=max(notas)
            nota_minima=min(notas)
            print(f"Notas extremas {nota_extrema}")
            print(f"Notas mínimas {nota_minima}")
    elif opcion==3:
        notas=cargar_notas_del_fichero()
        if len(notas)==0:
            print("Todavía no hay aprobados")
        else:
            total_aprobados=0
            for num in notas:
                if num >5:
                    total_aprobados=total_aprobados+1         
            print(f"Total de aprobados: {total_aprobados}")
    elif opcion==4:
        notas=cargar_notas_del_fichero()
        if len(notas)==0:
            print("Todavía no hay notas medias")
        else:
            media=sum(notas)/len(notas)
            print(f"La nota media es {media}")
    elif opcion==5:
        notas=cargar_notas_del_fichero()
        if len(notas) ==0:
            print("Todavía no hay notas")
        else:
         print(f"Mostrar todas {notas} ")
    elif opcion==6:
        print("Salir")

#Aquí abajo es el codigo del profesor: 

#Al iniciar el programa se debe mostrar el siguiente menú:
#1.- Añadir nota
#2.- Mostrar notas extremas
#3.- Total de aprobados
#4.- Nota media
#5.- Mostrar todas
#6.- Salir

#El usuario elige una opción (1 al 6) y el programa le muestra o le pide
#los datos necesarios para llevar a cabo ea acción. Despues, vuelve a salir el menú
#y así hasta que elija la opción de salir. 
#Las notas se guardan en un fichero
"""
dir_fichero="notas.txt"
"""
#funciones propias
"""
def menu():
    print("1.- Añadir nota")
    print("2.- Mostrar notas extremas")
    print("3.- Total de aprobados")
    print("4.- Nota media")
    print("5.- Mostrar todas")
    print("6.- Salir")
def nueva_nota(nota):
    with open(dir_fichero,"a") as f:
        f.write(nota+"\n")
        
def aprobados():
    with open(dir_fichero,"r") as f:      
        aprobados=0
        linea=f.readline()
        while(linea!=""):
            if int(linea.strip())>=5:
                aprobados+=1
            linea=f.readline()
    return aprobados
def nota_baja():
    with open(dir_fichero,"r") as f:
        notas=f.readlines()
    return min(notas,key=lambda n:int(n.strip()))
def nota_alta():
    with open(dir_fichero,"r") as f:
        notas=f.readlines()
    return max(notas,key=lambda n:int(n.strip()))
def media():
    with open(dir_fichero,"r") as f:
        notas=f.readlines()
    if not notas:
        return 0
    return sum([int(n.strip()) for n in notas])/len(notas)
def mostrar_notas():
    with open(dir_fichero,"r") as f:
        linea=f.readline()
        while linea!="":
            print(linea.strip())
            linea=f.readline()
#programa principal
opcion_elegida=0
while opcion_elegida!=6 :
    menu()
    opcion_elegida=int(input("Elige opción: "))
    match opcion_elegida:
        case 1:
            nueva_nota(input("Introduce nota "))
        case 2:
            print(f"nota más alta {nota_alta()}")
            print(f"nota más baja {nota_baja()}")
        case 3:
            print(f"total de aprobados {aprobados()}")
        case 4:
            print(f"La nota media es {media()}")
        case 5:
            mostrar_notas()
        case 6:
            print("Fin del programa!")
        case _:
            print("opción no válida") 
"""