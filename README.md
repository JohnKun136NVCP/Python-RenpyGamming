# Taller de Creación de Videojuegos 🕹️🎮.

<p align = "right">
<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"
    width = "40px"
    align = "right"
    />
</p>


# Lenguaje de programación Python. 
    
    1. Renpy (Juegos de citas en 2D). <-Taller.
    2. Pygame.
    3. Panda3D (Es necesario saber C++).



## RenPy.
<p align = "center">
<img src = "https://upload.wikimedia.org/wikipedia/commons/7/7e/Ren%E2%80%99Py_Logo_6-13-6_200x307px.png"
    width = ""
    align = "center"/>
</p>

### ¿Qué es RenPy?
Si has jugado los juegos de citas tanto en PC como en un dispositivo electrónico en conquistar chicas o personajes que podrás desbloquear fondos lindos pues a esto es posible combinando la programación en Python y también el juego de citas. Renpy puedes hacer tu novela romántica en 2D y también exportarlo para Windows, Linux, MacOS, Android.


<p align = "center">
<img src = "https://cdn.akamai.steamstatic.com/steam/apps/698780/ss_c60999c236a809c04321017aa14e97e5ac9856a1.1920x1080.jpg?t=1586800322"
    width = ""
    align = "center"/>
</p>

#### Requisistos.
<p align = "right">
<img src = "https://upload.wikimedia.org/wikipedia/commons/c/c7/Windows_logo_-_2012.png"
    width = "35px"
    align = "right"/>
</p>

1. Windows
    - Versión: Windows XP o superior. (A partir de la versión 7.4 no es compatible con Windows XP).
    - CPU: 2.0 GHz Core 2 Duo.
    - RAM: 2.0 GB.
    - Gráficos: OpenGL 2.0 or DirectX 9.0c.
<p align = "right">
<img src = "https://upload.wikimedia.org/wikipedia/commons/d/dd/Linux_logo.jpg"
    width = "35px"
    align = "right"/>
</p>

2. Linux.
    - Versión: Ubuntu 12.04+.
    - CPU: 2.0 GHz Core 2 Duo.
    - RAM: 2.0 GB.
    - Gráficos: OpenGL 2.0.

<p align = "right">
<img src = "https://upload.wikimedia.org/wikipedia/commons/2/22/MacOS_logo_%282017%29.svg"
    width = "45px"
    align = "right"/>
</p>

3. MacOS. 
    - Versión: 10.6+.
    - CPU: 2.0 GHz Core 2 Duo (solo 64 bit).
    - RAM: 2.0 GB.
    - Gráficos: OpenGL 2.0

<p align = "right">
<img src = "https://upload.wikimedia.org/wikipedia/commons/3/3b/Android_new_logo_2019.svg"
    width = "95px"
    align = "right"/>
</p>

4. Android. (Para jugar.)
    - Versión: Android 5.0 Lollipop+.
    - CPU: 2.0 GHz
    - RAM: 2GB.
    - Gráficos: OpenGL 2.0.

Fuente: [Wikipedia](https://es.wikipedia.org/wiki/Ren%27Py)

En las actualizaciones recientes se ha implementado para *iOS* y también como test en *Html*.

#### Instalación RenPy versión 8. 🔨

1. [Windows](https://www.renpy.org/latest.html) en la extención ***.exe***.
2. [MacOs](https://www.renpy.org/latest.html) en la extención ***.dmg***.
3. [Linux](https://www.renpy.org/latest.html) en la extención ***tar.bz2***.
4. [Linux RaspberryPi and Chromebook](https://www.renpy.org/latest.html) en extención ***tar.bz2***.

Para el curso de **RenPy**, por favor ver la carpeta donde dice **RenPy**.

## Pygame. 


<p align = "center">
<img src = "https://upload.wikimedia.org/wikipedia/commons/a/a9/Pygame_logo.gif"
    width = ""
    align = "center"/>
</p>

Si uno quiere desarrollar juegos sencillos. Sencillos me refiero como juegos en 2D no un *Mortal Kombat X*, tal vez un *Mortal Kombat 1 del 1992*. Sí es la desventaja de *Pygame*. Sin embargo, hay cosas curiosas que se puede hacer con *Pygame*. Al igual que *RenPy* usa manejo de Sprites pero de una manera que puedas programarlo por tu cuenta y no tanto que lo haga *RenPy* por ti.

#### Instalación.
1. **Windows**. Solamente se tiene que escribir el siguiente comando:

    ```python
        py -m pip install  -U pygame --user
    ```
    O también
    ```python
        pip3 install pygame --user
    ```
    Para comprobar que sí se instaló correctamente se debe poner este comando como de prueba.
    
    ```python
        py -m pygame.examples.aliens
    ```

    <p align = "center">
    <img src="img/aliens.png" 
        aling = "center">
    </p>

2. **MacOs**. 

    ```python
        python3 -m pip install -U pygame --user
    ```
    Para **Anaconda**:
    ```python
        pythonw

    ```
    En vez de:
    ```python
        python

    ```
3. **Linux**
    - Debian/Ubuntu/Mint
    ```python
        sudo apt-get install python3-pygame
    ```
    - Fedora/Red hat.
    ```python
        sudo yum install python3-pygame
    ```
    - OpenSUSE
    ```python
        sudo yum install python3-pygame
    ```
    - Arch/Manjaro
    ```python
        sudo pamac install python-pygame
    ```
## Pandas3D
Motor de videojuegos que incluye graficos más avanzados, audio y detección de colisiones para ahora videojuegos 3D. Es de código abierto y libre software.

<p align = "center">
<img src ="https://upload.wikimedia.org/wikipedia/fr/thumb/1/11/Panda3D_Logo.png/220px-Panda3D_Logo.png"
align = "center"
width = "150px">
</p>

### Instalación Pandas3D con pip

```python
    pip install panda3d==1.10.11
```
Descargando el SDK para: 
1. [Windows](https://www.panda3d.org/download/sdk-1-10-11/) 64-bit y 32-bit.
2. [macOs](https://www.panda3d.org/download/sdk-1-10-11/) para macOS OS X10.9+ y OS X 10.6+
3. [Linux](https://www.panda3d.org/download/sdk-1-10-11/) distribuciones de Ubuntu.