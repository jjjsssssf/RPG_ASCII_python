import pygame
import threading
pygame.mixer.init()
tocando_musica = False
def tocar_musica(caminho_musica):
    global tocando_musica
    pygame.mixer.music.load(caminho_musica)
    pygame.mixer.music.play(-1)
    tocando_musica = True
def escolher_e_tocar_musica(caminho_musica):
    parar_musica()
    threading.Thread(target=tocar_musica, args=(caminho_musica,), daemon=True).start()
def parar_musica():
    global tocando_musica
    if tocando_musica:
        pygame.mixer.music.stop()
        tocando_musica = False
