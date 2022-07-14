# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define h  = Character("Hachiman Hikigaya ",color="#E82900")
define y = Character("Zeil",color= "#82E800")

# El juego comienza aquí

label start:
    #historia
    "Desde hace tiempo que he pensado algo..."
    "No sé por qué tenía que pasar aquello..."
    "Desde que él..."
    scene bg classroom
    show zeil delighted
    "Zeil" "Parece que le estoy dando muchas vueltas..."
label sprites:
    hide zeil delighted
    show zeil shocked
    "Zeil" "No fue hace tiempo que me hago la misma pregunta"
    