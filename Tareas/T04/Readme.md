# Tarea 04: ZATAKA ic :school_satchel:

Mi tarea no cumple con todo lo pedido, es más cumple con muy poco. Esta 
consiste en dos carpetas, en las cuales se encuentan los módulos separados 
por los que le correpsonden al server y los que le corresponden al cliente.

Server:

1. server
+ la carpeta usuarios

Cliente:
1. backend
2. frontend 
3. Cliente

+ Gui
  - chatroom.gui --> es el chatroom comun
  - chatroom_master.gui --> es el chatroom del "jefe", solo el puede iniciar
  - Ingresar.gui --> si elige la opcion ingresar entra en esta ventana
  - Registrarse.gui --> si elige la opcion registrar entra en esta ventana
  - main.gui --> es el juego
  - Vantana1.gui --> es la ventana de inicio donde eleige si ingresar o 
    registrar

### Cosas implementadas y no implementadas :white_check_mark: :x:


No hice muchas cosas asi que por simplicidad voy a poner lo que si hice:

1. Sala de espera: se hace las dictinción entre el jefe y los demas.

2. Son hasta 5 usuarios los que se pueden conectar (sin embargo, si uno se 
sale, no se logra arreglar y si es el jefe no se podra inciar nunca el juego 
ya que los demas no tienen el boton).

3. Se puede ingresar a una cuenta existente y una nueva, y de haber errores 
se notifican.

4. Se puede hablar por el chat de forma dinamica

5. Si el jefe inicia el juego todos lo inicia, sin embargo to puede mandar 
las imagenes a todas las ventanas.

6. Si chocan con la pared hay error pero no esta implentada la señal.

7. En la ventana de juego tiene la opcion de para, pausar, continuar, salir o
 jugar una partida nueva.
 
8. Se hace la codificación con hash

## Ejecución :computer:

Para poder ejecutar el programa hay que inicializar el server y posterior a 
esto inicializar los clientes.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. PyQt5.QtCore 

2. os 

3. csv   

4. sys 

5. socket

6. PyQt5.QtWidgets

7. json

8. datetime 

9. hashlib


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:

1. https://github.com/mlisbit/pyqt_snake: Lo implemente en el módulo frontend 
   en la clase  MainGame (que corresponde a el juego). De este código rescate la lógica
   con la que dibuja el trace como tambien las funciones; timer Event, check 
   status, direction, keypress event , start y pause.
   
2. Ayudantía Chat con networking y la Actividad de Pacman
