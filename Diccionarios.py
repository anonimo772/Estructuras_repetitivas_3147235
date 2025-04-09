#diccionario
#es una estructura o coleccion de datos
#que los almacena en pares
#clave-valor
# -un diccionario comienza y termina 
# con llaves (curly, braces)
# -la clave se separa del valor(:) 
# -y lo mismo cada elemto o propiedad
# del diccionario se separa por una coma
# -cada clave es un string 
# - el valor puede ser de caulquir tipo

#Ejemplo: diccioanrio
#que alamcene los datos de un
#pais
pais1 = {
          "nombre": 'argentina',
          "capiral": 'buenos aires',
          "moneda": 'peso argentino',
           "poblacion": {
                        "censo": 54,
                        "densidad": 29,
                      },
          "ciudades": [
                                    "cordoba",
                                    "rosario",
                                    "mendoza",
                                  ] 
       }
pais2 ={
         "nombre": 'ecuador',
         "capital": 'quito',
         "moneda": 'dolar',
          "poblacion": {
                        "censo": 67,
                        "densidad": 40,
                      },
         "ciudades principales": [
                                   "Guayaquil",
                                   "Cuenca",
                                   "Santo Domingo",
                                   "Dura",
                                   "Machala",
                                   "manta",
                                 ]

       }
pais3 ={
         "nombre": 'Bolivia',
         "Capital": 'Sucre',
         "Moneda ": 'Moneda boliviana',
         "poblacion": {
                        "censo": 46,
                        "densidad": 10,
                      },
         "ciudades": [
                       "Santa Cruz",
                       "El alto",
                       "Cochabamba",
                       "Oruro",
                       "Tarija",
                     ],
         
}

#ecceder a la informacion del pais
print  (pais1 ['moneda'])
print (pais2 ['capital'])
print (pais1 ['ciudades'] [1])
print ("------------------")
#iterar las ciudades del pais 1
for ciudad in pais1 ['ciudades']:
    print(ciudad)

## Accerder a datos poblacionales 
print ("--------------------------")
print ("censo", pais1['poblacion'],['censo'])
