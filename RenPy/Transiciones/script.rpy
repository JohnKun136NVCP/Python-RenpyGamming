# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define k = Character("Kirigaya Kazuto",color= "#AEAEAE")
define y = Character("Yui",color="#FFFFFF")
# El juego comienza aquí
label start:
    scene bg aincrad
    transform slighright:
        xalign 0.75
        yalign -0.25
    transform slighleft:
        xalign 0.25
        yalign -0.50
    transform slighcenter:
        xalign 0.5
        yalign -0.50
    show kirito happy at slighleft:
    k "¡Hey! ¿Qué tal? Bienvenido a Aincrad bueno está en 2D pero tampoco está mal."
    k "Mi nombre es Kiragaya Kazuto, pero mucha gente me conoce como Kirito."
    k "Estaré enseñando lo que sé para los juegos 2D en Renpy. Pero no estaré solo ¡Yui! ¡Yui!"
    show yui eating at slighright
    y "Papá, es la primera vez que salgo en un programa en 2D más siendo una IA..."
    k "Oye Yui ¿Ese no es el emparedado que Asuna preparó en la mañana?"
    y "Sí, lo es, además mamá me lo dio. Pero no deberíamos estar hablando de comida sino vamos a ponernos a trabajar"
    k "¡Ah cierto! Bueno... Bueno..."
    y "¿En serio papá se te olvidó lo que ibas a enseñar?"
    k "¡No!¡No! Nada más que es raro estar en un juego 2D. Bueno vamos a comenzar antes que tu mamá me regañe"
    hide yui eating
    show kirito happy at slighcenter
    k "Bien, hablaré de la posición de las imagenes y también de cambios de escena"
    k "Cambiemos esta escena de una manera no tan brusca de manera que se pueda ver mejor"
    scene bg aincrad
    with Dissolve(.5)
    pause .5
    scene bg classroom
    show kirito happy at slighcenter
    with Dissolve(.5)
    k "Como verás andamos ahora en un salon de clases pero con el fondo que se desapareciera no de manera brusca sino de manera más paulatina."
    k "Además no es la única hay toda una sección de transiciones simples."
    k "Por ejemplo, {i}fade{\i}"
    show bg train 
    with fade
    k "Como se puede apreciar nada más el fondo de pantalla"
    show kirito happy at slighcenter
    k "Si queremos un gran flash también existe esta parte en Renpy."
    define flashing = Fade(0.2,0.0,0.8,color="#fff")
    show bg japan1
    with flashing
    show kirito happy at slighcenter
    k "Ahora visto esto vamos a probar otra cosa."
    k "Vamos a movernos de una manera diferente."
    show kirito happy at slighleft with move
    k "Me he movido hacia la izquierda."
    show kirito happy at slighleft with move
    k "Me he movido hacia la derecha."
    show kirito happy at slighcenter with move
    k "Me he movido al centro."
    scene bg aincrad
    show kirito happy at slighcenter
    with Dissolve(0.5)
    k "Otra vez, estamos de regreso."
    k "Bueno creo que con los ejemplos basta..."
    y "¡Eh! Espera papá..."
    y "Pero si nada más pusiste los ejemplos pero no explicaste cómo se hacia."
    y "Está bien solamente porque mamá te regaña explicaré lo que acabas de mostrar."
    y "Nada más explicaré en una forma que puedan entender bien."
    transform upright:
        xalign 1.0
        yalign 0.25
    hide kirito happy 
    with moveoutleft
    show yui happy at upright
    
    y "¡Hola! Disculpen a mi papá pero es un poco distraido a veces."
    y "Dejen me presento otra vez, me llamo Yui y son una IA creada por Akihiko Kayaba. Pero realmente mi papá es el quien conocieron hace poco y mi madre que ahorita no está aquí pero se llama Asuna, dejemos de presentaciones y vamos al grano."
    y "Cuando nos presentamos por primera vez se tuvieron que hacer algunos ajustes a la pantalla ya que si dejaban nuestros {b}sprites{\b} así como están nos veriamos fuera del juego."
    y "En Renpy podemos crear 'funciones' que podrán ser de utilidad al momento de usar sprites. Veamos las primera función."
    show code ok:
        xalign 0.25
        yalign 0.25
    y "Como podemos ver para acomodar imagenes en usaremos {b}xalign{\b} y {b}yalign{\b} que nos iremos a una posición de la pantalla, en este caso se definió para que papá y yo estuvieramos casi juntos y que no se viera complementamente los springs."
    hide code ok with moveoutleft
    y "Finalmente para usar esas {b}transformaciones{\b} solamente las enviaremos a llamar a la función, como se muestra."
    show code ok2:
        xalign 0.25
        yalign 0.5
    y "Así es la primera parte que explicó papá con sus ejemplos."
    y "Hablaré sobre los cambios de escena para ello existe el {i}Disolve{\i},{i}fade{\i} como se los mostraron."
    hide code ok2 with moveoutleft
    y "Mostaré el código que se aplicó."
    show code ok3:
        xalign 0.25
        yalign 0.5
    y "Vemos que está la escena de Aincrad después se aplica el efecto de Disolve (tiempo), dejamos pasar {b}pause{\b} la mitad de un segundo y finalmente aparece papá con la nueva escena."
    y "Para {b}fade{\b} es el mismo código nada más sin darle un tiempo, pero explicaremos el de 'flash'."
    hide code ok3 with moveoutleft
    show code ok4:
        xalign 0.25
        yalign 0.5
    y "Como vemos igual que los personajes tenemos que definir una variable que se llama {i}flashing{\i} y también con la función {i}Fade{\i}."
    y "Esta recibe {i}Fade(time_out,hold_time,in_time,color ='HTML COLOR'){\i}, donde es tiempo de salida, cuanto tiempo estará, timepo de entrada y finalmente un color de flash."
    hide code ok4 with moveoutleft
    y "Finalmente me falta los movimientos que han estado apareciendo"
    y "Para mover a los personajes o {i}sprites{\i} se usa la palabra reservada {b}move{\b}."
    show code ok5:
        xalign 0.25
        yalign 0.5
    y "Podemos dar una posición y que se mueva, como se ve en el ejemplo."
    hide code ok5 with moveoutleft
    show code ok6:
        xalign 0.25
        yalign 0.5
    y "Finalmente, podemos también sacar un {i}sprite{\i} de la pantalla como se muestra aquí."
    hide yui happy
    hide code ok6
    show yui eating at slighcenter
    y "Eso fue una breve explicación de como funciona las {i}transiciones{\i}."
    y "Fue gusto en conocernos."
