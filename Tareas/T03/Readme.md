# Tarea 03: DCC Electromatic :school_satchel:

Mi tarea cumple con lo pedido pero no en su totalidad. Me faltó hacer una 
consulta y mitad del testing.

Esta consiste en 8 módulos:

1. Consultas
2. Elementos grafo
3. Exceptions
4. Grafo
5. Lectura_archivos
6. Main
7. Not_things
8. Testing

## Consideraciones generales :octocat:

Como mencioné mi tarea no hace la consulta de perdidade energía ni la parte 
de testing para las excepciones. Mi main no funciona muy bien para el large, 
y se demora aproximadamente 1 hora en carga el grafo. Esto se debe a que mi 
codigo no es muy eficiente y recorre muchas veces mi lista para poder 
realizar su función. Por otra parte, esto empeoró cuando vi la issue de la 
prohibición del range y no estaba muy segura de lo del yield si era prohibido
 o no asi que preferi optar por lo que si sabia que estaba permitido.
 
En el testing, para el mayor y menor consumo puse como ejemplo uno basado en 
la base small sin embargo, en esta base el flujo me bada cero para las casa 
ya que no les llegaba energía.

Otra cosideración importante es que cuando se pida el tipo en el main y deba 
ser asociado a un id, el tipo se debe escribir como: casas, distribucion, 
centrales, transminision, elevadoras. De no ser asi será un input inválido.

### Cosas implementadas y no implementadas :white_check_mark: :x:

```
100%    es que funciona perfecto 
1-99%  tengo algo hecho, pero no todo (ESPECIFICAR)
0%      no hice esta parte
```

* `80%` Consultas:
         * `100%` Consumo por comuna
         * `100%` Consumo por distribudora
         * `100%` Casa que más consume
         * `100%` Casa que menos consume
         * `0%` Energia perdida

* `80%` Main: Pongo 80% ya que no pude corroborar que todo funcionara.

* `100%` Lectura archivos: Puedo desempaquetar tanto la base large como la 
         base small.

* `90%` Grafo: Puedo generar los grafos para ambas bases de datos sin 
        embargo, al momento de modificar no restringo que no se pueda eliminar 
        una elevadora si la comuna no tiene una.

* `80%` Tiempos de ejecución: Para el archivo más grandes se demora mucho en 
        abrir. 
        
* `50%` Testing: No hice el testing de la excepciones. 

*  `100%` Implementación de mis propias estructura de datos: No utilize 
          ninguna EDD de python e implemente las mias.

           
## Ejecución :computer:

El módulo principal a implementar es el Main.py. Sin embargo, también incluí 
en la mayoría de los módulos un main con ejemplos para que se pueda probar 
las diferentes funciones ya que como mi código se demoraba mucho no pude 
probar todas sus funcionalidades.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. unittest -> Implementado en el módulo Testing. Lo hago para poder generar 
               los test.
2. copy -> Está implementado en el módulo Main.py.Lo utilizo para hacer una 
           copia preeliminar del grafo, despues el usuario puede volver a esa
           version o recuperar la anterior que fué copiada.
3. csv ->  La uso en el módulo Lectura_archivos, para poder leerlos. Aqui 
           también los desempaqueto y los paso a la estructura de datos 
           implementada por mi.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. El archivo inicial no va a tener un electrical overload desde un comienzo
2. Sin la energía es suficiente se distribuye equitativamente
3. Me base en al issue #641 donde sale que el consumo por comuna es casa y 
   distribudoras.
4. Redirijo todo al menu principal si el usuario se equivoca
5. Si un nodo se agrega y no se une a la red no afecta el flujo
6. La casa se puede conectar a casas o distruibuidoras.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1.https://www.codefellows.org/blog/implementing-a-singly-linked-list-in
   -python/ y https://dbader.org/blog/python-linked-list: esta implementado 
   en el módulo Not_things.py y corresponde a la función insert y size de mi 
   clase NotList() y NotDict(). Con estas dos funciones puedo insertar un 
   elemento en mi lista o diccionario y con size puede obtener el tamaño de 
   ella. (insert esta bajo el nombre agregar en NotDict())
   
2. https://dbader.org/blog/python-linked-list: esta implementado en el módulo
   Not_things.py. Corresponde a la función remove, tanto de NotDict() como de
   NotList().

3. https://docs.python.org/2/library/csv.html: Esta implementado en el módulo
   Lectura_archivos lo use en las lineas 20 a la 22. Este código me permite 
   abrir mis archivos correctamente.

4. Ayudantía 6 y 7: Me base en el código propuesto para realizar mi lista, 
   diccionario y mi grafo. Esto es los módulo Not_things y Grafo. 
