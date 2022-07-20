# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define z = Character("Zeil",color= "#82E800")
define i = Character("Nakano Itsuki",color="#F72C00")
# El juego comienza aquí
label start:
    show zeil laugh
    z "¡Hola de nuevo! Mi nombre es Zeil, mucho gusto como verás no tenemos fondo de pantalla ¿Verdad? Pues comencemos por el principio ¿Qué te parece? Hoy hablaremos sobre como me definí como caracter y como puedes crear los tuyos"
    hide zeil laugh
    show zeil delighted
    z "Para empezar en la parte superior del juego debes declarar la palabra reservada {b} define + letra del personaje = ('Nombre personaje', color =hexadecimal en html){\b}"
    hide zeil delighted
    show zeil sad
    z "Por cierto, John-Kun les explicará está parte de los colores html ya que no los rescuerdo bien..."
    hide zeil sad
    show zeil delighted
    z "Pero no estemos tristes por ello ya que el siguiente tema le toma a mi mejor amiga, es un poco timida pero es muy linda"
    z "¡Oh! Por cierto, aquí está"
    z "¡Ven, Itsuki! ¡Ven, Itsuki!"
    hide zeil delighted
    show itsuki hello
    i "¡Hola! Mi nombre es Nakano Itsuki, gusto en conocerte."
    i "Espero que nos llevemos bien, ah sí te explicaré lo siguiente {b}iniciar un juego{\b}"
    hide itsuki hello 
    show itsuki happy
    i "Para iniciar o empezar escribir tu novela necesitaremos que primero se inicialice con un {b}label start{\b} después la identación de 4 espacios o un tab."
    i "Para poner mostrar un personaje que como ahorita me muestro necesitamos un sprite o una imagen .png o .gif. Pero primero los dialogos. ¿Te acuerdas que iniciaste el personaje con una letra o con el nombre? Lo usaremos."
    i "Inicializamos un dialogo con {b}'letra o nombre del personaje'{\b} más las comillas dobles donde va el texto"
    hide itsuki happy
    show itsuki hello
    i "Intentalo, es divertido. Abajo de esta linea estará un comentario que se verá el archivo {i}script.rpy{\i} donde si quieres te puedo saludar."
    #i "Hola Escribre_tu_nombre"
    hide itsuki hello
    show itsuki happy
    i "Ahora pasaremos al fondo de pantalla que esto se ve muy vacio."
    i "Para ello si vas a ocupar un fondo de pantalla debe iniciar scene bg nombre_imagen (John-Kun se los explicará mejor) ya que eso es un identificador para Renpy."
    i "Vamos a ver uno de Japón donde vivo."
    scene bg japan1
    show itsuki hello
    i "Ya ves, se ve hermoso"
    i "¿Y si cambiamos el escenario a otro?"
    scene bg japan3
    show itsuki angry
    i "¡Wow! Es muy bonito ¿Verdad?"
    hide itsuki angry
    show itsuki shame
    i "¡Ups! Me dio hambre, lamento mucho, me dio un poco de vergüenza"
    i "Lo siento mucho, otra vez, bueno continuemos..."
    hide itsuki shame
    show itsuki happy
    i "Por cierto, también podemos cambiar a México"
    scene bg mexico
    show itsuki hello
    i "¡Es hermoso! Espero igual después visitar pronto este lugar, entonces ya sabemos como cambiar fondos de pantalla."
    i "Si te es que te gustó otro fondo puedes revisar la carpeta de {i}images{\i} y ver cual te gustó más."
    hide itsuki hello
    show itsuki sad
    i "¡Por cierto! Si decides cambiar de fondo es importante poner después de {b}scene bg_fondo{\b} después de ello {i}show itsuki happy{\i}. Claro es opcional, si ya no me queres ver..."
    #opcional. Para cambiar el fondo:
    #scene bg imagen
    #show itsuki happy
    #Si decides cambiarlo borra las 2 lineas siguientes 
    hide itsuki sad
    show itsuki hello
    i "Bueno antes de irme, te deseo buena suerte y gracias por haberme escuchado."
    i "Por aquí viene mi amigo Kirigaya Kazuto, estará explicando (eso espero los siguientes temas)"
