# Como correr una aplicación con arduino
## Instalar python
Ir al siguiente enlace y descargar la versión más reciente de Python. En este caso debería ser la versión 3.7
[Python Official download](https://www.python.org/downloads/)
Ejecuta el archivo descargado y sigue las instrucciones en pantalla. Las siguientes opciones que están marcadas deben estar habilitadas. Las demás no son primordiales para este ejercicio pero mejor tenerlas...
[Py install 1](https://i.imgur.com/ceP7qkR.png "Py install 1")

[Py install 2](https://i.imgur.com/ceP7qkR.png "Py install 2")

## Descargar el repositorio
[Descargar zip](https://github.com/NotZombieFood/Flask-App-with-Arduino-support/archive/master.zip)
Descomprimelo en el lugar de tu preferencia.
Copia la ruta de la carpeta, ejemplo:
C:\Users\notZombieFood\Documents\LDI\Flask-App-with-Arduino-support
Así deberían de ver el contenido del folder:
[folder](https://i.imgur.com/kax7kV1.png "folder")


## Abrir terminal
Este paso lo repetiremos muy seguido, entonces es bueno tomar nota para que quede claro.
### En caso de ser usuario de Windows:
Buscamos Command prompt, CMD o Consola, y nos tendrá que salir esta aplicación:
[cmd](https://i.imgur.com/N12iWBo.png "cmd")
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
[cd](https://i.imgur.com/wnKtwnh.png "cd")
[Imgur](https://i.imgur.com/wnKtwnh.png)
## Instalar librerías 
Correr el siguiente comando:
pip -r requirements.txt

## Correr programa 
Usar el siguiente comando 
python server.py

## ¿Y esto de que sirve?


