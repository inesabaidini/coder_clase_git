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


#git commit -m 'Mensaje que quiero dejar'. Este menssaje está bueno para yo decir qué cambios hice en esta nueva versión, agregué x clase, hice esto o aquello, etc.
#Después de cada cambio voy a tener que hacer el git add y el git commit si o si, y ahi listo, voy a tener todo em el repositorio

#Para ver los cambios, comando> git log
#Esto me muestra el commit seguido de un hash (clave alfanumerica larga al lado del commit)
#Abajo me muestra quien hizo el cambio, a que hora, y el texto q indica de q se trataba el cambio q hice.
#wq oara salir, después de los :

#Podria crear distintas ramas:
#quiero probar cosas, ver de agregar cosas a ver q onda. se me agregan las ramas para desarrollo, y me ahorro de perder o romper mi codigo. Esta sería ponele mi rama principal. o
#rama MASTER. Cómo creo las ramas: git branch me dice cual rama estoy
#git branch -l me va a mostrar la rama en la q estoy yo y las otras ramas q hay
#git checkout (nombre de la rama a la que me quiero ir a trabajar ahora)
#Y pruebo hacer cambios, para ver que el documento que tenía en la main no se modifica pero se crea otro igual en la pruebas_random donde se van quedando los cambios

#FLASHERÍSIMO HERMANO, si me vuelvo al checkout main se me pierde todo q loco

#git branch -D (rama que quiero borrar) y me la borra toda a la re verga
#git log --oneline me muestra de forma más resumida los cambios




#Si me quiero mover al commit anterior, git checkout y le copio los primeros 7 caracteres del hash
#si quiero volver al ultimo, git checkout master y bye, vuelvo a la principio

#si ahora lo que quiero es que lo q hice en una tarea, q me salio de 10, se me agregue al master
#bueno me cambio a mi otra rama TAREA, creo mi archivo persona esto aquello, y ahora como funciono perfecto lo tengo q pasar a master para q entre en operacion