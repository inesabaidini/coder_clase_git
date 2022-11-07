#Git y GitHub

#GIT
#Es un sistema de control de versiones; se entiende como todas las erramientas que nos permiten hacer modificaciones en nuestro proyecto.
#Un sistema que registra los cambios realizados sobre un archivo o conjunto de archivos a lo largo del tiempo. Podemos ver versiones y recuperar versiones anteriores casi al instante. 
 
#Estados de Git
#1er estado: working directory: git revisa y anota cuales fueron los cambios que se realizaron desde la última versión. Ssabe qué cambió y qué cambió.
#2do estado: staging area: anota ese nuevo documento con esos cambios 
#3er estado: repository: ahora si se guardan los cambios como una nueva versión en los repositorios

#GITHUB
#Sería como un google drive, es una plataforma donde podemos subir los proyectos. Servicio de alojamiento de repositorios de software con sistemas Git


#clear para limpiar el terminal
#Git ofrece 3 formas de hacerle consultas (pedir ayuda):
#git help (lo que quiero consultar) y me da la descripción de lo que pregunté
#git (comando que quiero consultar) --help y tb me trae la ayuda
#man git-(comando que quiero consultar) no es lo más recomendable, quedate con la primera
#Si quiero abrir un Git Bash desde la carpeta, hago clic dereho y voy a la opcion open git bash here y ya me abre con la unicacon de la carpeta

#REPOSITORIOS - Repository
#Como lo creo: pongo en el terminal git init (asegurate que estes trabajando con la carpeta del proyecto)
#ESTO ES IMPRESCINDIBLE! Si no hago esto no se me va a guardar nada

res = 2 + 3

#git status me va a decir q cambios hubieron dentro de la carpeta donde se encuentra el repositorio.

#hasta acá solo cree eel repositorio, pero mi archivo sigue en el working directory. Lo tengo que pasar los cambios al staging area, donde se anotaran los cambios
#comando: git add (nombre de mi archivo.py)
#acá me va a mostrar que hay cambios para ser agregados, porque todavía no se me guarda nada. Para moverlo al repositorio el comando es:
#git commit

print('Terminando problema')