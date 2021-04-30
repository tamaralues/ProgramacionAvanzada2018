# Tarea 2: DCC Casino  :school_satchel:

# Nombre : Tamara Lues Soto      Git: tamaralues

Mi tarea esta compuesta por 8 módulos.

* Acciones: Contiene la clase que hace el random entre sus unidades, es decir
            si la persona eligue jugar, llama a jugar y este retorna "ruleta" o 
            "tragamonedas".
            
* Clientes: Contiene las 5 clases de los tipos de clientes diferenciados por 
            el tipo estos heredan de la clase Humanos.
            
* Humanos: Es clase Madre de los clientes. Esta hereda de Humans (dada en en 
           entities.py)
           
* Juegos: Este módulo contiene dos clases madre, la primera es Juegos esta la
          cual hereda de Game y es la clase madre para Tragamonedas y Ruleta.
          La segunda es  NoJuegos que hereda de Building y es la clase madre 
          para las instalaciones. Aqui tambien se definen las clases de los 
          juegos e instalaciones con su respectivo funcionamiento.
          
* Main: En este módulo está la clase Main, que es mi simulación, esta la 
        funcion tick y además "armo" el casino creando las instalaciones.
        
* Parámetros: En este modulo estan definidas los parametros externos que se 
              van a utilizar a lo largo de la simulación.
              
* Trabajadores: En este módulo se definen las jornadas de trabajo, las horas 
                de trabajo y descanso.
                
* Ubicaciones_fijas: Aca tengo una lista con sub - listas las cuales definen 
                     un x y un y para la ubicación de un determinado juego o 
                     instalacion.

## Consideraciones generales :octocat:

Mi tarea contiene todo lo solicitado menos el sistema de colas, por lo tanto,
dada esta simplificacion, no hay una capacidad máxima en las instalaciones. 
Por otro lado, para generar los nombres aleatorios utilize la librería names 
la cual debe ser descargada para su uso.

Tuve problemas con el .gitignore, la primera vez que hice el push no me lo 
cosideró el cual lo hice a las 23:15. Sin embargo, me percaté del error 
posterior al plazo, y hice igual el git push de este. Dado que habia modificado 
mi código no quize hacer el git add *, por lo que tuve que eliminar manualmente 
las cosas, a pesar de esto no pude eliminar manualmente la gui. Sin embargo
cuando hice el git push de mi Readme, ahi si funcionó. Se que esto 
es un mal uso del .gitignore pero ojalá puedas tomar esto en consideración al 
momento de hacer la penalizacion por el uso de .gitignore.

### Cosas implementadas y no implementadas :white_check_mark: :x:

```
100%    es que funciona perfecto 
1-99%  tengo algo hecho, pero no todo (ESPECIFICAR)
0%      no hice esta parte
```

* `100%` Diagrama de clases:
         * `100%` Realize la entrega preeliminar
         * `100%` Entrega final

* `100%` Clientes

* `100%` Trabajadores

* `100%` Acciones

* `90%` Simulacion: Me falto hacer las colas.

* `90%` Juegos: Me falto hacer las colas

* `90%` Instalaciones: Me faltó hacer las colas

* `100%` Uso de tick

* `100%` Reloj Global: este es solicitado como input que es además de un 
         parámetro de la clase Main
            
            
## Ejecución :computer:

El módulo principal a ejecutar es Main.py. Aqui se les va solicitar el número
de días que se van a simular. Dejé el tick en el que estaba indicado cuando 
se hace el llamado a gui.run (lo deje como gui.run(tick, 50)). En el módulo 
Parametros.py estan los parámetros que se pueden modificar. Cabe destacar que
no todos tienen el nombre griego y es porque los que parecían como la letra,
le puse la letra directamente, es decir:

      - theta : parámetro externo para calcular la cantidad que apuesta el 
                cliente.
      - kappa : parámetro externo que es que se le sumará a la probabilidad 
                de ganar del jugador si el dealer y el estan coludidos.
      - eta : parámetro externo el cual se le suma a la probabilidad de irse 
              si hablo con tini.
      - epsilon : parámetro externo el cual se le resta a la ansiedad si la 
                  persona conversa.
      - gamma : parámetro externo para el calculo de la probabilidad del 
                juego en las ruletas.
      - chi : parámetro externo el cual se le suma a la deshonestidad si la 
              persona conversa.
      - alfa : parámetro externo que determina la probabilidad de ganar en el
               tragamonedas.
      - delta : parámetro externo que indica el numero máximo de que la 
                persona va a esperar para conversar si no hay nadie.
      - pi : parámetro externo para calcular
      - p : parámetro externo para hacer que entren o no nuevos clientes
      - w : parámetro externo el cual indica la probabilidad de "hagan trampa".
      - nu : parámetro externo que indica la cantidad de rondas que te tiene 
             que quedar el fisico determinista.
      - psi : parámetro externo el cual se le suma a la probabilidad de ganar.
  
## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

Por otro lado, los módulos que fueron creados fueron los siguientes:

1. math   ->  Con esta librería obtuve la funcion ceil para asi poder redondear 
              hacia arriba los números para la proxima jornada de los 
              trabajadores.
            
2. names  ->  Con esta librería genere nombres aleatorios para los cliente y 
              para los trabajadores. (Debe instalarse)
              
3. random ->  Con esta libreria pude calcular los diferentes parámetros 
              solicitados (triangular, normalvariate). Además pude obtener el 
              evento que ocurría dada una comparacion con random(). También 
              me permitió hacer elecciones aleatorias con choice. Por otr 
              lado, usando choices pude hacer esta elecciones en base a 
              objetos que tenían diferente probabilidad de ocurrencia.

## Supuestos y consideraciones adicionales :thinking:

1.  Las instalaciones no cambian de ubicacion y son una cantidad fija.
2.  El tiempo de estadia promedio es considerando el tiempo que se le da a 
    toda la simulación no por día.
3.  Hay tres tarots, un restobar y un baño, de esta manera le asigne a cada  
    Mr.T un tarot.
4.  No hay un limite de bartenders que pueden estar trabajando.
5.  Los jugadores caminan hacia su ubicacion y cuando llegan revisan que la 
    maquina este habilitada.
6.  La probabilidad de ser que un dealer sea coludido es de un 50 %
7.  La probabilidad de que un Kibitzer este prediciendo es de un 50 %
8.  La probabilida de pillar a un fisico determinista (el cual es un parámetro.
    externo), es igual a la de ser pillado si estoy coludido.
9.  Se puede hablar con Tini más de una vez.
10. El programa funciona en minutos.

## Referencias de código externo :book:

1. https://stackoverflow.com/questions/4265988/generate-random-numbers-with
   -a-given-numerical-distribution: Con este código puedo obtener la "accion"
    que va a realizar mi cliente considerando que la probabilidad de 
    ocurrencia de cada una es distinta. Utilizo este código en las lineas 386 - 
    393 del módulo Humanos.py.

2. Material complementario de simulación: Lo usé mayoritariamente para utilizar
   la lógica del random() <= problabilidad_de_ocurrencia_x_evento. El cual se
   hace refencia en muchas lineas de mi código. (Material dado en el curso)
