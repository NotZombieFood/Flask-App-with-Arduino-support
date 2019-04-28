# Como correr una aplicación con arduino
## Instalar python
Ir al siguiente enlace y descargar la versión más reciente de Python. En este caso debería ser la versión 3.7
[Python Official download](https://www.python.org/downloads/)
Ejecuta el archivo descargado y sigue las instrucciones en pantalla. Las siguientes opciones que están marcadas deben estar habilitadas. Las demás no son primordiales para este ejercicio pero mejor tenerlas...
Da clic en las imagenes para verlas
[imagen 1](https://i.imgur.com/ceP7qkR.png "imagen 1")

[imagen 2](https://i.imgur.com/ceP7qkR.png "imagen 2")

## Descargar el repositorio
[Descargar zip](https://github.com/NotZombieFood/Flask-App-with-Arduino-support/archive/master.zip)
Descomprimelo en el lugar de tu preferencia.
Copia la ruta de la carpeta, ejemplo:
C:\Users\notZombieFood\Documents\LDI\Flask-App-with-Arduino-support
Así deberían de ver el contenido del folder:
Da clic en las imagenes para verlas
[imagen](https://i.imgur.com/kax7kV1.png "imagen")


## Abrir terminal
Este paso lo repetiremos muy seguido, entonces es bueno tomar nota para que quede claro.
### En caso de ser usuario de Windows:
Buscamos Command prompt, CMD o Consola, y nos tendrá que salir esta aplicación:
Da clic en las imagenes para verlas
[imagen](https://i.imgur.com/N12iWBo.png "imagen")
Le damos clic secundario y le damos run as administrator. 
### En caso de ser usuario de MacOs:
No tiene screenshot porque no tengo Mac :P Pero usando el finder o como se llame la cosa que sale con CMD + space. Escriben terminal y abren el que salga.

### Ahora paso para Windows y MacOS
Se acuerdan de la ruta que sacamos en el paso anterior. Que en mi ejemplo fue la siguiente:
C:\Users\notZombieFood\Documents\LDI\Flask-App-with-Arduino-support

Vamos a retomarla y vamos a escribir el siguiente comando en la terminal que abrieron.
cd ruta_del_folder
Siguiendo el ejemplo, sería así:
cd C:\Users\notZombieFood\Documents\LDI\Flask-App-with-Arduino-support
Deberían ver algo parecido a lo siguiente:
El comando "cd" es usado para movernos a un folder. 
Da clic en las imagenes para verlas
[imagen](https://i.imgur.com/wnKtwnh.png "imagen")
## Instalar librerías 
Correr el siguiente comando:
pip -r requirements.txt

## Correr programa 
Usar el siguiente comando 
python server.py

## ¿Y esto de que sirve?
En la siguiente imagen puedes ver la información que sale al correr el programa, podemos observar en un recuadro azul la información importante.
[imagen](https://i.imgur.com/DoYM2sG.png "imagen")

Teniendo nuestro celular y computadora dentro de la misma red, solo basta con escribir en el navegador la dirección IP que observamos en el recuadro (será distinta cuando ustedes lo corran, pero la idea es la misma).
Deberíamos ver lo siguiente en el navegador:
[imagen](https://i.imgur.com/TAfRdti.jpg "imagen")

Y en el navegador de nuestra computadora, escribimos 
localhost
en la barra de direcciones y deberíamos ver lo mismo que en el movil.
[imagen](https://i.imgur.com/5ffhkWO.png "imagen")

## Conectar PC con Arduino
- Abrir menu de bluetooth y buscar el modulo, saldrá como HC-04.
- Emparejar, la contraseña será 1234.
- En configuración de Bluetooth avanzada, buscar la parte donde diga Puertos COM y anotar cual es el puerto entrante.
- Anotar en la linea que diga lo siguiente 'arduino = serial.Serial("COM3",9600,timeout = 2)', y cambiar COM3 por el COM que encontramos.

## Cargar el programa del arduino
Programa que se llama example.ino

# Rutas importantes
## /graph
Muestra una gráfica de los valores que ha recibido el sensor.

## /monitor 
Monitorea los valores actuales del sensor, recibe alertas.