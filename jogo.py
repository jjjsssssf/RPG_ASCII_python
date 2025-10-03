from classe_do_jogador import jogador
from classe_do_inimigo import inimigo
import time, random, os
from batalha import batalha, batalha_cut
from classe_arts import draw_window,term, clear, art_ascii, Cores, mini_mapa_, dialogos, clear_region_a
from mm import tocar_musica, escolher_e_tocar_musica, parar_musica, tocando_musica
from classe_do_inventario import TODOS_OS_ITENS, Item
mapas = mini_mapa_()
dialogo = dialogos()
ascii = art_ascii()
C = Cores()
player = jogador(nome="", hp_max=100, atk=15, niv=1, xp_max=100, defesa=10, gold=0, stm_max=100, intt=10, mn_max=100,d_m=20, art_player=ascii.necro, skin="@")
enimy = inimigo(nome="", hp_max=0, atk=0, niv=0, xp=0, defesa=0, gold=0, art_ascii="",atk1="",atk2="")
def vila():
    draw_window(term, x=0, y=0, width=30, height=8, text_content=ascii.vila1)
    with term.location(x=31, y=0):
        escolha = input("Você quer entrar nessa vila [S] [N]:")
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

def mini_mapa(x_l, y_l, player,ascii, mapas_, camera_w, camera_h, x_p, y_p, menager):
    raw_map_lines = mapas_
    max_width = max(len(l) for l in raw_map_lines if l.strip())
    mapa_art = [l.ljust(max_width) for l in raw_map_lines if l.strip()]
    player.x_mapa = x_p
    player.y_mapa = y_p
    OBSTACULOS = ['#', '.']
    INTERACOES = {'v':vila}
    feedback_message = ""
    MAP_WIDTH = max_width
    MAP_HEIGHT = len(mapa_art)
    CAMERA_WIDTH = camera_w
    CAMERA_HEIGHT = camera_h
    camera_x = max(0, player.x_mapa - CAMERA_WIDTH // 2)
    camera_y = max(0, player.y_mapa - CAMERA_HEIGHT // 2)
    def atualizar_camera():
        nonlocal camera_x, camera_y
        margem = 2
        if player.x_mapa - camera_x < margem:
            camera_x = max(0, player.x_mapa - margem)
        elif player.x_mapa - camera_x > CAMERA_WIDTH - margem - 1:
            camera_x = min(MAP_WIDTH - CAMERA_WIDTH, player.x_mapa - (CAMERA_WIDTH - margem - 1))
        if player.y_mapa - camera_y < margem:
            camera_y = max(0, player.y_mapa - margem)
        elif player.y_mapa - camera_y > CAMERA_HEIGHT - margem - 1:
            camera_y = min(MAP_HEIGHT - CAMERA_HEIGHT, player.y_mapa - (CAMERA_HEIGHT - margem - 1))
    parar_musica()
    escolher_e_tocar_musica("music_back.mp3")
    while True:
        clear()
        atualizar_camera()
        janela_mapa = [
            linha[camera_x:camera_x + CAMERA_WIDTH]
            for linha in mapa_art[camera_y:camera_y + CAMERA_HEIGHT]
        ]
        mini_mapa_render = "\n".join(janela_mapa)
        draw_window(term, x=x_l, y=y_l, width=CAMERA_WIDTH + 4, height=CAMERA_HEIGHT + 2, text_content=mini_mapa_render)
        CORES = {
            '.': C.VERDE,
            ':': term.black,
            'O': term.bold_blue_on_black,
            '@': term.bold_red_on_black,
            'B': term.bold_brown_on_brown,
            '#': term.bold_magenta_on_black,
            'X': term.bold_red_on_white,
            'P': term.blue_on_white
        }
        draw_window(term, x=x_l, y=y_l, width=CAMERA_WIDTH + 4, height=CAMERA_HEIGHT + 2)
        draw_window(term, x=x_l+CAMERA_WIDTH+5, y=y_l, width=CAMERA_WIDTH+2, height=CAMERA_HEIGHT+2, text_content=menager)
        player.barra_de_vida(x_l+CAMERA_WIDTH+6, y_l=CAMERA_HEIGHT-8)

        for j, linha in enumerate(mapa_art[camera_y:camera_y + CAMERA_HEIGHT]):
            for i, ch in enumerate(linha[camera_x:camera_x + CAMERA_WIDTH]):
                cor = CORES.get(ch, "")
                with term.location(x_l + 2 + i, y_l + 1 + j):
                    print(cor + ch + C.RESET, end="")
        with term.location(x_l + 2 + player.x_mapa - camera_x, y_l + 1 + player.y_mapa - camera_y):
            print(term.bold_yellow(player.skin) + term.normal)
        try:
            caractere_atual = mapa_art[player.y_mapa][player.x_mapa]
        except IndexError:
            caractere_atual = ' '
        if caractere_atual == ':':
            with term.location(x=x_l+CAMERA_WIDTH+6, y=CAMERA_HEIGHT-1):
                print("Você está Em uma sala")
        elif caractere_atual == "@":
            musumano = inimigo(nome='Muçumano', hp_max=50, atk=5, niv=1, xp=50, defesa=0, gold=10, art_ascii=ascii.musumano, atk1="Avansar", atk2="Espada")
            batalha_cut(player_b=player, inimigo_b=musumano)
            if musumano.hp <= 0:
                novo_char = "X"
                linha_antiga = mapa_art[player.y_mapa]
                mapa_art[player.y_mapa] = (
                    linha_antiga[:player.x_mapa] + 
                    novo_char + 
                    linha_antiga[player.x_mapa + 1:]
                )
        elif caractere_atual == "O":
            with term.location(x_l+CAMERA_WIDTH+6, y=CAMERA_HEIGHT-3):
                print("Você deseja ajudar seu amigo:S/N")
            with term.location(x_l+CAMERA_WIDTH+6, y=CAMERA_HEIGHT-2):
                escolha = input(">")
            if escolha == "S":
                novo_char = 'E'
                linha_antiga = mapa_art[player.y_mapa]
                mapa_art[player.y_mapa] = (
                    linha_antiga[:player.x_mapa] + 
                    novo_char + 
                    linha_antiga[player.x_mapa + 1:]
                )
        elif caractere_atual == "B":
            with term.location(x=x_l+CAMERA_WIDTH+6, y=CAMERA_HEIGHT-2):
                print("Você Encontrou um Bau")
            itens = 'Espada', 'Escudo', 'Suco', 'Poção de Cura'
            selec = random.choice(itens)
            with term.location(x=x_l+CAMERA_WIDTH+6, y=CAMERA_HEIGHT-1):
                print(f"Você Conseguio um {selec}")
            player.inventario.append(TODOS_OS_ITENS[f"{selec}"])
            novo_char = 'b'
            linha_antiga = mapa_art[player.y_mapa]
            mapa_art[player.y_mapa] = (
                linha_antiga[:player.x_mapa] + 
                novo_char + 
                linha_antiga[player.x_mapa + 1:]
            )
        elif caractere_atual == "P":
            def inimigos_restantes():
                return any('@' in linha for linha in mapa_art)
            if inimigos_restantes():
                with term.location(x_l+CAMERA_WIDTH+6, y=CAMERA_HEIGHT-2):
                    print("Você ainda não derrotou todos os inimigos!")
            else:
                with term.location(x_l+CAMERA_WIDTH+6, y=CAMERA_HEIGHT-2):
                    print(f"Para bens {player.nome}")
                with term.location(x_l+CAMERA_WIDTH+6, y=CAMERA_HEIGHT-1):
                    print(f"conseguimos matar esses vermes malditos")
                break
        if feedback_message:
            with term.location(0, CAMERA_HEIGHT + y_l + 4):
                print(term.red(feedback_message))
                feedback_message = ""
        with term.location(x=x_l, y=CAMERA_HEIGHT + y_l + 2):
            print(term.clear_eol + "Digite (w/s/a/d [n]):")
        with term.location(x=x_l + 21, y=CAMERA_HEIGHT + y_l + 2):
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
            player.menu(x_janela=0, y_janela=0)
            continue
        elif movi == "sair":
            exit()
        elif movi == "up":
            player.up(x=x_l+CAMERA_WIDTH+5, y=y_l,werd=CAMERA_WIDTH+2, herd=CAMERA_HEIGHT+2)
        else:
            feedback_message = f"Comando '{movi}' inválido. Use w/a/s/d."
            continue
        if 0 <= novo_y < MAP_HEIGHT and 0 <= novo_x < MAP_WIDTH:
            caractere = mapa_art[novo_y][novo_x]
            if caractere not in OBSTACULOS:
                player.x_mapa = novo_x
                player.y_mapa = novo_y
                if caractere in INTERACOES:
                    INTERACOES[caractere]()

def cutcenes(mansagem, x, y, witr, herd):
    draw_window(term, x=x, y=y, width=witr, height=herd, text_content=mansagem)

def jogo(player_j, ascii_j, x, y):
    clear()
    draw_window(term, x=x, y=y, width=52, height=11, text_content=ascii.cidade_em_caos)
    cutcenes(mansagem=dialogo.cutsine_inicil, x=x, y=y+11, witr=52, herd=8)
    input()
    clear()
    draw_window(term, x=x, y=y, width=52, height=11, text_content=ascii.cidade_em_caos)
    cutcenes(mansagem=dialogo.descricao, x=x, y=y+11, witr=52, herd=8)
    input()
    clear()
    draw_window(term, x=x, y=y, width=52, height=11, text_content=ascii.cidade_em_caos2)
    cutcenes(mansagem=dialogo.descricao2, x=x, y=y+11, witr=52, herd=8)
    input()
    menager = """Você Está no castelo de Muçumanos
Derroteos e depois ajude seus
amigo e converse com o Padre"""
    clear()
    mini_mapa(x_l=0, y_l=0, player=player_j, ascii=ascii_j, mapas_=mapas.mini_mapa_tuturial.split('\n'), camera_w=35, camera_h=15, x_p=5, y_p=1, menager=menager)

"jogo(player_j=player, ascii_j=ascii, x=10, y=0)"