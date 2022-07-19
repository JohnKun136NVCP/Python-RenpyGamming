# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define h  = Character("Hachiman Hikigaya ",color="#E82900")
define y = Character("Zeil",color= "#82E800")
define m = Character("Menima", color= "#95311C")

# El juego comienza aquí
label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.
    play music "audio/no-irai.mp3" fadein 1.0 volume 0.5
    scene bg train
    "Bien como comienzo..."
    "¡Ah! Sí bien ahora ya lo recuerdo todo..."
    "Por cierto, bienvenido o bienvienida, no importa, ya estamos embarcados en este lio"
    "¿Eh? Espera ¿he estado hablando conmigo todo este rato y ni siquiera me has visto?"
    "A ver, espera... ah ok era esto."

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.
    show menima ok
    "Menima" "¡Hola! ahora sí, bueno perdón por mis modales..."
    "Menima" "Mi nombre es Menima, pero me puede decir Meni."
    "Menima" "Seré tu acompañante en este taller de Renpy."
    "Menima" "No seré la única tal vez me acompañe algunas chicas o chicos que tal vez conozcas del alguna parte..."
    "Menima" "Antes que nada, gracias"
    "Menima" "¿Eh? ¿No aparecido Zeil? Bueno me tocaba la presentación, pero ella la siguiente parte, me enojaré si no se presenta"
    "Menima" "Ey Zeil ven para acá ya te vi"

    #show y yukino happy
label sprites:
    show zeil shocked at right
    "Zeil" "Perdón estaba viendo si funcionaba todo bien"
    hide zeil shocked
    show zeil delighted at right
    "Zeil" "Meni puede ser un poco enoja pero es una gran amiga"
    hide zeil delighted
    show zeil smile at right
    "Zeil" "Bueno, bueno, ya comencemos"

    stop music fadeout 1.0