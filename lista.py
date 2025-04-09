

#diccionario
# Coleccion de datos que los
# almacena en pares clave-valor
# -un diccionario comienza y termina
# con llaves(curly braces)
# -la clave se separa del valor 
# por dos puntos(:)
# -cada clave es un string
# -el valor puede ser cualquier tipo
# -cada elemento(propeidad) del
# diccionario se separa por una coma

#EJEMPLO: diccionario
# que almacene los datos de un pais
pais1 = {
            "nombre": "Argentina",
            "capital": "Buenos Aires",
            "moneda": "peso argentina",
            "idioma": "español",  
            "poblacion": 44938783,
            "ciudades principales": [
                                        "Buenos Aires",
                                        "Córdoba",
                                        "Mendoza",
                                        "Rosario",
                                        "La Plata",
                                        "Santa Fe",
                                        "Tucumán",
                                        "Quilmes",
                                        "San Juan",
                                        "Mar del Plata",

                                ]
                                
        }
pais2 = {
            "nombre": "Ecuador",
            "capital": "Quito",
            "moneda": "Dolar",
            "idioma": "Ecuatoriano",  
            "poblacion": 18373000,
            "ciudades": [
                            "Quito",
                            "Guayaquil",
                            "Cuenca",
                            "Manta",
                            "Ambato",
                            "Loja",
                            "Ibarra",
                            "Santo Domingo de los Colorados",
                            "Riobamba",
                        ]
        }

pais3 = {
            "nombre": "haiti",
            "capital": "Puerto Príncipe",
            "moneda": "Gourde Haitiano",
            "idioma": "Francés",
            "ciudades": [
                        "Puerto Príncipe",
                        "Cap Haitien",
                        "Gonaives",
                        "Jacmel",
                        "Les Cayes"
                        ]

                        

        }
# Acceder a la informacion del pais
print(pais1["moneda"])
print(pais2["capital"])
# Acceder a una ciudad del pais1
print(pais1["ciudades principales"][2])

# iterar sobre las ciudades de un 
print ("----------------------------")
for ciudad in pais1["ciudades principales"]:
    print(ciudad)
# acceder a datos poblacionales
print ("-----------------------------")
print(pais1["poblacion"])