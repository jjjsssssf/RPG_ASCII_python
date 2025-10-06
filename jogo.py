from classe_do_jogador import jogador
from classe_do_inimigo import inimigo
import time, random, os
from batalha import batalha, batalha_cut, seleção_inimigo
from classe_arts import draw_window,term, clear, art_ascii, Cores, mini_mapa_, dialogos, clear_region_a
from mm import tocar_musica, escolher_e_tocar_musica, parar_musica, tocando_musica
from classe_do_inventario import TODOS_OS_ITENS, Item
mapas = mini_mapa_()
dialogo = dialogos()
ascii = art_ascii()
C = Cores()
player = jogador(nome="", hp_max=100, atk=15, niv=1, xp_max=100, defesa=10, gold=0, stm_max=100, intt=10, mn_max=100,d_m=20, art_player=ascii.necro, skin="@")
enimy = inimigo(nome="", hp_max=0, atk=0, niv=0, xp=0, defesa=0, gold=0, art_ascii="",atk1="",atk2="")

def mini_mapa(
    x_l, y_l, player,ascii, mapas_, camera_w, camera_h, x_p, y_p, menager,
    cores_custom=None, obstaculos_custom=None, mapa_anterior=None, interacoes_custom=None 
):
    raw_map_lines = mapas_
    max_width = max(len(l) for l in raw_map_lines if l.strip())
    mapa_art = [l.ljust(max_width) for l in raw_map_lines if l.strip()]

    player.x_mapa = x_p
    player.y_mapa = y_p

    OBSTACULOS = obstaculos_custom or ['#', '═', '╗', '║','╝','♠','│', '─', '┌', '└', '┐', '┘',"╔",'╚','╗']
    INTERACOES = interacoes_custom or {}
    feedback_message = ""

    MAP_WIDTH = max_width
    MAP_HEIGHT = len(mapa_art)
    CAMERA_WIDTH = camera_w
    CAMERA_HEIGHT = camera_h

    camera_x = max(0, player.x_mapa - CAMERA_WIDTH // 2)
    camera_y = max(0, player.y_mapa - CAMERA_HEIGHT // 2)

    def atualizar_camera():
        nonlocal camera_x, camera_y
        camera_x = max(0, min(MAP_WIDTH - CAMERA_WIDTH, player.x_mapa - CAMERA_WIDTH // 2))
        camera_y = max(0, min(MAP_HEIGHT - CAMERA_HEIGHT, player.y_mapa - CAMERA_HEIGHT // 2))

    while True:
        clear()
        atualizar_camera()

        janela_mapa = [
            linha[camera_x:camera_x + CAMERA_WIDTH]
            for linha in mapa_art[camera_y:camera_y + CAMERA_HEIGHT]
        ]
        mini_mapa_render = "\n".join(janela_mapa)
        draw_window(term, x=x_l, y=y_l, width=CAMERA_WIDTH + 4, height=CAMERA_HEIGHT + 2, text_content=mini_mapa_render)
        CORES = cores_custom or {
            '╫': term.bold_white_on_orange,
            '♠': term.bold_green_on_black,
            'B': term.bold_white_on_brown,
            'P': term.blue,
            'F': term.red,
            '†': term.bold_yellow,
            '╚': term.bold_magenta_on_black,
            '═': term.bold_magenta_on_black,
            '║': term.bold_magenta_on_black,
            '╝': term.bold_magenta_on_black,
            "╔": term.bold_magenta_on_black,
            '╚': term.bold_magenta_on_black,
            '╗': term.bold_magenta_on_black,
            '│': term.bold_magenta_on_black,
            '─': term.bold_magenta_on_black,
            '┌':term.bold_magenta_on_black,
            '└':term.bold_magenta_on_black,
            '┐':term.bold_magenta_on_black,
            '┘': term.bold_magenta_on_black,

        }

        draw_window(term, x=x_l + CAMERA_WIDTH + 5, y=y_l, width=CAMERA_WIDTH + 5, height=CAMERA_HEIGHT + 2, text_content=menager)
        player.barra_de_vida(x_l + CAMERA_WIDTH + 6, y_l=CAMERA_HEIGHT-14)

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
        if caractere_atual == "B":
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
        if caractere_atual == "╫":
            ale = random.randint(1, 100)
            if ale <=10:
                with term.location(x=x_l+CAMERA_WIDTH+6, y=CAMERA_HEIGHT-1):
                    input("Você esbarou um inimigo")
                batalha(player_b=player, inimigo_b=seleção_inimigo(), numero=1)
            else:
                pass
        if caractere_atual == "†":
            player.hospital(x_=x_l+CAMERA_WIDTH+6, y_=CAMERA_HEIGHT-1)
            novo_char = '╫'
            linha_antiga = mapa_art[player.y_mapa]
            mapa_art[player.y_mapa] = (
                linha_antiga[:player.x_mapa] + 
                novo_char + 
                linha_antiga[player.x_mapa + 1:]
            )
        if caractere_atual == "V":
            with term.location(x=x_l+CAMERA_WIDTH+6, y=CAMERA_HEIGHT-5):
                print("Você que compara alguma coisa")
            with term.location(x=x_l+CAMERA_WIDTH+6, y=CAMERA_HEIGHT-4):
                escolha = input("[S] [N]: ")
                if escolha == "S":
                    player.gerenciar_loja(x=0, y=0, largura=35)

            

        if feedback_message:
            with term.location(0, CAMERA_HEIGHT + y_l + 4):
                print(term.red(feedback_message))
                feedback_message = ""
        with term.location(x=x_l, y=CAMERA_HEIGHT + y_l + 2):
            print(term.clear_eol + "Digite (w/s/a/d [n]:")
        with term.location(x=x_l + 21, y=CAMERA_HEIGHT + y_l + 2):
            entrada = input(">").strip().split()
        if not entrada:
            continue
        try:
            movi = entrada[0].lower()
            quant = int(entrada[1]) if len(entrada) > 1 else 1
        except (ValueError, IndexError):
            quant = 1
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
        elif movi == "inventario":
            player.inventario_(x=x_l + CAMERA_WIDTH + 5, y=y_l, werd=CAMERA_WIDTH + 2, herd=0, batalha=False)
        elif movi == "sair":
            exit()
        elif movi == "up":
            player.up(x=x_l + CAMERA_WIDTH + 5, y=y_l, werd=CAMERA_WIDTH + 2, herd=CAMERA_HEIGHT + 2)
        elif movi == "q" and mapa_anterior:
            mini_mapa(
                x_l=0,
                y_l=0,
                player=player,
                ascii=ascii,
                mapas_=mapa_anterior["mapa"],
                camera_w=35,
                camera_h=15,
                x_p=mapa_anterior["pos"][0]+1,
                y_p=mapa_anterior["pos"][1],
                menager=mapa_anterior["mensagem"],
                cores_custom=mapa_anterior["cores"],
                obstaculos_custom=mapa_anterior["obstaculos"],
                mapa_anterior=None,
                interacoes_custom=None
            )
            return
        else:
            feedback_message = f"Comando '{movi}' inválido. Use w/a/s/d/inventario/up/q."
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
    menager = """"""
    clear()
    mini_mapa(x_l=0, y_l=0, player=player_j, ascii=ascii_j, mapas_=mapas.mapa_castelo.split('\n'), camera_w=35, camera_h=15, x_p=1, y_p=1, menager=menager)
              
jogo(player_j=player, ascii_j=ascii, x=10, y=0)