import streamlit as st 
with st.sidebar:
    st.write("Menú navegación")
    st.text_input("Dato:")
    if st.button("pulsar"):
        saludo="Estoy en navegación"
st.write(saludo)

    """
    Tenemos que hacer una app con un sidebar a la izquierda con dos desplegables (tienda y mes) VENTAS.CSV
    Al seleccionar una tienda se ha de mostrar a la derecha:
    - Una tabla que contenga un total de facturacion/total de gastos de personal/mes con mayor facturacion
    Al seleccionar un mes se ha de mostrar a la derecha:
    - Una tabla con información de dicho mes de todas las tiendas (facturacion seguramente)
    - Una tabla con los datos de ese mes (facturacion/total gastos de personal)
    - Debajo de estas tablas una media de facturación de todas las tablas
    - Una tabla con la tienda que tenga el mayor gasto de personal de dicho mes
    
    """