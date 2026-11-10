import operaciones as op
#op.crear_continentes(["con1","con2","con3"])
op.borrar_tablas()
op.crear_continentes(["con1","con2","con3"])
print(op.devolver_continentes())
op.borrar_tablas()
op.crear_paises(["pais","poblacion","bandera"])

#Esto no sale como debería. 
print("Países en DB:", op.devolver_paises()) 
