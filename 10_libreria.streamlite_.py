"""
Realiza un progrma para la organizacion de una libreria
un libro tiene tres propiedades: titulo, autor y precio.

Cuando se inicie el programa, se va a mostrar un menu:
1-Nuevo libro
2-Mostrar todos
3-Buscar por titulo
4-Libros por precio maximo
5-Salir

1-Se piden los datos del nuevo libro y se guardan
2-Se muestran los titulos de todos los libros
3-Se le pide el titulo y se muestran todos sus datos
4-Se le pide el precio maximo y se muestran los titulos de los libros cuyo precio sea igual o inferior al introducido
Despues de ejecutar cualquiera de las anteriores opciones, se muestra de nuevo el menu.
Asi hasta que elija la opcion 5 que sale del programa
""" 
import streamlit as st
if "lista_libros" not in st.session_state:
    
    st.session_state["lista_libros"]=[]
    
libros=st.session_state["lista_libros"]

#añadido lo de arriba para hacer otra función. 
tab_nuevo,tab_todos,tab_buscar,tab_precio,tab_tienda=st.tabs(["Nuevo libro","Mostrar todos","Búsqueda por título","Libros precio máximo","Tienda"])
"""
#Primero vamos a crear la variable tocha: esto nos permitirá almacenar la información. 
libros=[]
"""
#El jodido bucle y las opciones: 
with tab_nuevo:
    titulo=st.text_input("Introduce título: ")
    autor=st.text_input("Introduce autor: ")
    precio=st.number_input("Introduce precio: ",min_value=0.0, step=1.0)
    if st.button("Guardar libro"):
        libros.append({"titulo": titulo, "autor": autor, "precio": precio})
        st.success(f"¡Libro '{titulo}' guardado correctamente!")
with tab_buscar:
    titulo_buscar=st.text_input("Introduce el título del libro: ")
    if st.button("Buscar"):
        libs=list(filter(lambda lib:lib["titulo"].lower()==titulo.lower(),libros)) 
        if libs:
             st.success(f"Título: {libs[0]['titulo']}, Autor:{libs[0]['autor']},Precio:{libs[0]['precio']}€")
        else:
            st.error("Libro no encontrado")
with tab_todos:
    st.title("Listado de libros")
    st.table(libros)

with tab_precio:
    st.title("Lista precio máximo")
    libros_ordenados = sorted(libros, key=lambda lib: lib["precio"], reverse=True)
    st.table(libros_ordenados)
with tab_tienda:
    col_tienda,col_direccion,col_imagen=st.columns(3)
    col_tienda.write("**Nombre tienda**")
    col_direccion.write("**Dirección tienda**")
    col_imagen.write("**Foto**")
    tiendas=[{"nombre":"Cafetería","direccion":"Comfy-Lofi","foto":"tienda.jpg"}, #Cuidado, si modifico la referencia, se rompe. "foto":
             {"nombre":"tienda 2","direccion":"dir2","foto":"tienda.jpg"},
             {"nombre":"tienda 3","direccion":"dir3","foto":"tienda.jpg"}]
    for tienda in tiendas:
        col_tienda,col_direccion,col_imagen=st.columns(3)
        col_tienda.write(tienda["nombre"])
        col_direccion.write(tienda["direccion"])
        col_imagen.image(tienda["foto"]) 


        
#Hasta aquí el ejercicio ha sido escrito por mí en su totalidad. 
