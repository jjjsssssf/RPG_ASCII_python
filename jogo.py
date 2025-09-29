from classe_do_jogador import jogador
from classe_do_inimigo import inimigo
import time, random, os
from batalha import batalha
from classe_arts import draw_window, term, clear, art_ascii, Cores
from mm import tocar_musica, escolher_e_tocar_musica, parar_musica, tocando_musica
ascii = art_ascii()
C = Cores()
player = jogador(nome="", hp_max=100, atk=15, niv=1, xp_max=100, defesa=10, gold=0, stm_max=100, intt=10, mn_max=100,d_m=20, art_player=ascii.necro, skin="0")
enimy = inimigo(nome="", hp_max=0, atk=0, niv=0, xp=0, defesa=0, gold=0, art_ascii="",atk1="",atk2="")
def vila():
    draw_window(term, x=0, y=0, width=30, height=8, text_content=ascii.vila1)
    with term.location(x=0, y=9):
        escolha = input("Você quer entrar nessa vila\n[S] [N]: ")
    if escolha == "S":
        while True:
            clear()
            esc = "[1]Mercado  [2]Dormir\n[3]Conversar [4]Sair"
            draw_window(term, x=0, y=0, width=30, height=8, text_content=ascii.vila1)
            draw_window(term, x=0, y=8, width=30, height=5, text_content=esc)
            with term.location(x=2, y=11):
                escolha = input(">")
            if escolha == "1":
                player.gerenciar_loja(x_pos=32, y_pos=0, herd=7, x_loq=31, y_loq=0)
            elif escolha == "2":
                player.hospital(x_=31, y_=0)
            elif escolha == "3":
                pass
            elif escolha == "4":
                break
    elif escolha == "N":
        return

INTERACOES = {
    'V': vila,
}

def centralizar_camera(player, mapa_art, cam_width, cam_height):
    half_w = cam_width // 2
    half_h = cam_height // 2
    max_y = len(mapa_art)
    max_x = len(mapa_art[0])

    camera_x = max(0, min(player.x_mapa - half_w, max_x - cam_width))
    camera_y = max(0, min(player.y_mapa - half_h, max_y - cam_height))
    return camera_x, camera_y    

def mini_mapa(x_l, y_l, player, ascii):
    if player.locais["Vila"] == True:
        player.x_mapa = 3
        player.y_mapa = 2
        mapa_art = [linha.rstrip() for linha in ascii.mini_mapa.split('\n') if linha] 
    elif player.locais["Farol"] == True:
        player.x_mapa = 3
        player.y_mapa = 2
        mapa_art = [linha.rstrip() for linha in ascii.mini_mapa2.split('\n') if linha]
    OBSTACULOS = ['=', '|']
    INTERACOES = {}
    feedback_message = ""
    CAM_WIDTH = 30
    CAM_HEIGHT = 8
    parar_musica()
    escolher_e_tocar_musica("Menu_som_baia.mp3")
    while True:
        clear()
        print(term.home + term.clear)
        camera_x, camera_y = centralizar_camera(player, mapa_art, CAM_WIDTH, CAM_HEIGHT)
        mapa_visivel = [
            linha[camera_x:camera_x + CAM_WIDTH]
            for linha in mapa_art[camera_y:camera_y + CAM_HEIGHT]
        ]
        mini_mapa_render = "\n".join(mapa_visivel)
        draw_window(term, x=x_l, y=y_l, width=CAM_WIDTH+2, height=CAM_HEIGHT+2, text_content=mini_mapa_render)
        rel_x = player.x_mapa - camera_x
        rel_y = player.y_mapa - camera_y
        with term.location(x_l + 1 + rel_x, y_l + 1 + rel_y):
            print(term.bold_yellow(player.skin) + term.normal)
        try:
            caractere_atual = mapa_art[player.y_mapa][player.x_mapa]
        except IndexError:
            caractere_atual = ' '
        if caractere_atual == '.':
            draw_window(term, x=x_l, y=y_l-8, width=30, height=8, title="Estrada", text_content=ascii.caminho)
            if random.randint(1, 100) < 25:
                batalha(player_b=player, inimigo_b=enimy)
                escolher_e_tocar_musica("Menu_som_baia.mp3")
        elif caractere_atual == '~':
            draw_window(term, x=x_l, y=y_l-8, width=30, height=8, title="Rio", text_content=ascii.agua)
        elif caractere_atual == '#':
            draw_window(term, x=x_l, y=y_l-8, width=30, height=8, title="Montanha", text_content=ascii.montaha)
        elif caractere_atual == 'V':
            draw_window(term, x=x_l, y=y_l-8, width=30, height=8, title="Vila", text_content=ascii.vila1)
        elif caractere_atual == '*':
            draw_window(term, x=x_l, y=y_l-8, width=30, height=8, title="Deserto", text_content=ascii.deserto)
        if feedback_message:
            with term.location(0, CAM_HEIGHT + y_l + 4):
                print(term.red(feedback_message))
                feedback_message = ""
        with term.location(x=x_l, y=CAM_HEIGHT + y_l + 2):
            print(term.clear_eol + "Digite (w/s/a/d [n]):")
        with term.location(x=x_l+21,y=CAM_HEIGHT+y_l +2):
            entrada = input(">").strip().split()
        if not entrada:
            continue
        try:
            movi = entrada[0].lower()
            quant = int(entrada[1]) if len(entrada) > 1 else 1
        except (ValueError, IndexError):
            continue
        novo_x = player.x_mapa
        novo_y = player.y_mapa
        if movi == "w":
            novo_y -= quant
        elif movi == "s":
            novo_y += quant
        elif movi == "a":
            novo_x -= quant
        elif movi == "d":
            novo_x += quant
        elif movi == "menu":
            player.menu(x_janela=0, y_janela=8)
            continue
        else:
            feedback_message = f"Comando '{movi}' inválido. Use w/a/s/d."
            continue

        if 0 <= novo_y < len(mapa_art) and 0 <= novo_x < len(mapa_art[0]):
            caractere = mapa_art[novo_y][novo_x]
            if caractere not in OBSTACULOS:
                player.x_mapa = novo_x
                player.y_mapa = novo_y
                if caractere in INTERACOES:
                    INTERACOES[caractere]()

mini_mapa(x_l=0, y_l=8, player=player, ascii= ascii)