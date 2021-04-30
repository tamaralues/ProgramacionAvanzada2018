# Tarea 1: Tamara Lues :school_satchel:

## Consideraciones generales :octocat:

Mi tarea esta compuesta por 6 módulos.

* consultas_dict: Estan las consultas que hacen generadores.
* consultas_gen: Las consultas que no hacen bases de datos.
* consola: Recursion de la consola.
* lectura_csv: Funciones que abren los archivos.
* main: La consola.
* check_filter: Chequea los filtros y el formato.
   
Cumpli con los requerimientos de funcionalidad, uso de loops y también con el
requisito de las lineas máxima en las funciones. Sin embargo por temas de tiempo 
no alcanze a hacer todo lo solicitado.La tarea es capaz de hacer todas las
consultas menos popular airports, que la hice pero esta mala, además falla en
la impresión y guardado de las consultas cuando son listas. Tampoco pueden 
hacer consultas anidadas ya que dirá que la consulta no es válida.

### Cosas implementadas y no implementadas :white_check_mark: :x:

```
100%    es que funciona perfecto 
1-99%  tengo algo hecho, pero no todo (ESPECIFICAR)
0%      no hice esta parte
```

* `100%` Consultas que retornan base de datos:
         * `100%` load_database
         * `100%` filter_flights
         * `100%` filter_passengers
         * `100%` filter_passengers_by_age
         * `100%` filter_airports_by_country
         * `100%` filter_airports_by_distance

* `80%` Consultas que no retornan base de datos:
         * `100%` favourite_airports
         * `100%` passenger_miles
         * `0%` popular_airports
         * `100%` airport_passengers
         * `100%` furthest distance

* `85%` Consola:
         * `100%` Abrir archivo de cosultas
         * `100%` Elegir consulta existente o varias
         * `60%` Ejecutar consulta que ya existe o varias: Cuando son varias 
                 hay no funciona guardarla con el formato correcto en output.
         * `60%` Ejecutar consula existe o varias: Cuando son varias hay 
                 no funciona guardarla con el formato correcto en output.
         * `50%` No se realizan correctamente las consultas anidadas.
         * `80%` Ponerle número a la consulta: sigo el formato menos el 
                  número.
         * `70%` Impresión del resultado en pantalla: Para la mayoría de los 
                 caso funciona pero cuando es una lista imprime el tipo no los 
                 datos.
         * `90%` Ejecutar consultas nuevas de lista y simples: las hace pero 
                 imprime mal.
         * `100%` Eliminar consultas

* `70%` Recursion:
         * `80%` Volver atras: Siempre se la opcion de volver a inicio pero 
                 no al anterior y si se hace algo mal también.
         * `60%` Caida del programa: Hago chequeos que evitan algunas 
                 posibles caidas del programa pero si en el programa se pone en 
                 alguna variables algo que no es del tipo que debe ser se va a 
                 caer.

* `66%` Tiempos de ejecución: Para el archivo más grandes se demora mucho en 
        abrir. 
            

## Ejecución :computer:

El módulo de ejercicio a ejecutar es main.py y los datos deben estar en una 
carpeta llamada data y dentro de ella las carpetas; small, medium y large, 
con los archivos en cada uno de ellos segun su tamaño, es decir, igual al 
formato de la carpeta que nos dieron. Además debe haber otro archivo que es 
queries que es el archivo de las consultas validas, que debe estar en la 
carpeta data.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1.  pprint
2.  math -> sin, asin, sqrt, pow
3.  datetime -> datetime

## Supuestos y consideraciones adicionales :thinking:

Los supuestos que realicé durante la tarea son los siguientes:

1. Se van a poner correctamente las consultas: Con esto me refiero que las 
   variables seran del tipo del enunciado.
   
2. En el archivo outputs debe ir la consulta, el tipo y el resultado: Esto lo
 hice asi ya que leyendo los issues no me quedo muy claro a que se referian 
 por resultado.

3. El usuario debe ingresar a en lectura_csv.py el tamaño del archivo que 
   quiere leer.

4. El keys de passenger miles son los nombres.
   
   
## Referencias de código externo :book:

Para realizar mi tarea saqué código de:

1. https://stackoverflow.com/questions/4913349/haversine-formula-in-python-be
   aring-and-distance-between-two-gps-points: use este codigo para calcular 
   las millas, es basicamente la formula descompuesta. Este código lo usé en 
   el módulo consultas_gen en las lines 89-97. Es una función bajo el nombre 
   formula_
   
2. generadoreshttps://stackoverflow.com/questions/9708902/in-practice-what-are-t
   he-main-uses-for-the-new-yield-from-syntax-in-python-3: Con este codigo 
   puedo anidar dos funciones. Este lo usé en el módulo consultas_gen en la 
   las lineas 28-53, son dos funciones que estan bajo el nombre 
   wrapper_flights y wrapper_passengers.
   
3. https://stackoverflow.com/questions/9708902/in-practice-what-are-the-main-use
   s-for-the-new-yield-from-syntax-in-python-3: Este link lo utilize para 
   aprender a usar yield. 
   
4. https://stackoverflow.com/questions/3545331/how-can-i-get-dictionary-key
   -as-variable-directly-in-python-not-by-searching-fr: este codigo permite 
   obteer el key directamente como una variable, este código lo use a lo 
   largo de las funciones en el módulo check_filter 
 
5. https://stackoverflow.com/questions/6987285/python-find-the-item-with-maxim
   um-occurrences-in-a-list#comment8338917_6987358:  Este código lo use en la
   linea 17 del módulo consultas_dict. Lo utilize para calcular el máximo de 
   aparencias de un vuelo en una lista y darsela como value al pasajero.
   
6. https://stackoverflow.com/questions/26151669/valueerror-max-arg-is-an-empty
   -sequence:  Este codigo lo en la linea 18 y 26 del módulo consultas_dict. 
   Lo utilize para que no hubiera error cuando el value no se pudiera operar 
   por no ser del tipo operable según la función que le di.

7. https://stackoverflow.com/questions/20489609/dictionary-comprehension-in-pyt
   hon-3 diccionarios por compresion de una generador: me base en este código
   para aprender a hacer los diccionarios por compresión.

8. https://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-list
   s-tuples: Este codigo lo uso en la linea 116, 122, 216 y 222 del módulo 
   consultas_dict. Sirve para ordenar una con el criteria de forma creciente. 

9. Utilize el código dado como apoyo para esta tarea que es parse.

## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).