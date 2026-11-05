
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