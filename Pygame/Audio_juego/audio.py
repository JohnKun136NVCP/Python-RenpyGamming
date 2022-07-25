import pygame as pg#Importe del modulo pygame
import os #Para archivos
"""
Canción original: "Bojji to Kage no Yujyo"
Autor original:  MAAYUKO.
Productora: 2022 Aniplex, Inc.
Anime original: "Ōsama Ranking".
Esta canción está reservada nada más para fines educativos, no para uso comercial.
"""

def Reproducir_musica(): #Función para reproducción de música.
    pg.mixer.music.load("Bojjito.mp3") #Cargar primero la música.
    pg.mixer.music.set_volume(0.7) #Ajustar el volumen.
    pg.mixer.music.play()#Reproduce la música.
def Pausa_musica():
    pg.mixer.music.pause() #Pausa la música que se esté en ese momento.
def Parar_musica():
    pg.mixer.music.stop() #Para la reproducción total de la música.

while True:
    pg.mixer.init() #Para inicializar la reproducción de música.
    """
    from pygame import mixer
    """
    Reproducir_musica()
    print("Pulse p para pausar")
    print("pulse s para parar")
    op = input("=> ")
    if op =='p':
        Pausa_musica()
    elif op =='s':
        Parar_musica()
        break
    else:
        print("Opcion no valida")