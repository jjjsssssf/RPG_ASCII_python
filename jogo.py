from classe_do_jogador import jogador
from classe_do_inimigo import inimigo
import time, random, os
from batalha import batalha
from classe_arts import draw_window,term, clear, art_ascii, Cores, mini_mapa_, dialogos
from mm import tocar_musica, escolher_e_tocar_musica, parar_musica, tocando_musica
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

def mini_mapa(x_l, y_l, player, ascii, mapas_, camera_w, camera_h):
    raw_map_lines = mapas_
    max_width = max(len(l) for l in raw_map_lines if l.strip())
    mapa_art = [l.ljust(max_width) for l in raw_map_lines if l.strip()]
    player.x_mapa = 3
    player.y_mapa = 4
    OBSTACULOS = ['=', '|', " ", "║", "_", "-"]
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
            'X': term.bold_white_on_red,
            '@': C.VERMELHO_CLARO,
            ';': C.VERDE,
            '`': C.AMARELO,
            '.': C.VERDE,
            '~': C.AZUL,
            '#': C.CINZA_ESCURO,
            'v': f"{C.FUNDO_BRANCO+C.CIANO}",
            '*': C.AMARELO,
            '^': C.VERDE,
            '&': C.CINZA_CLARO,
            ':': f"{C.AMARELO+C.BRILHO}",
            '"': C.BRILHO
        }
        draw_window(term, x=x_l, y=y_l, width=CAMERA_WIDTH + 4, height=CAMERA_HEIGHT + 2)
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
        if caractere_atual == '.':
            draw_window(term, x=x_l, y=y_l - 8, width=30, height=8, title="Estrada", text_content=ascii.caminho)
            if random.randint(1, 100) < 25:
                batalha(player_b=player, inimigo_b=enimy)
                escolher_e_tocar_musica("music_back.mp3")
        elif caractere_atual == '~':
            draw_window(term, x=x_l, y=y_l - 8, width=31, height=8, title="Lago", text_content=ascii.agua)
        elif caractere_atual == '#':
            draw_window(term, x=x_l, y=y_l - 8, width=31, height=8, title="Montanha", text_content=ascii.montaha)
        elif caractere_atual == 'v':
            draw_window(term, x=x_l, y=y_l - 8, width=31, height=8, title="Vila", text_content=ascii.vila1)
        elif caractere_atual == '*':
            draw_window(term, x=x_l, y=y_l - 8, width=31, height=8, title="Deserto", text_content=ascii.deserto)
        elif caractere_atual == '^':
            draw_window(term, x=x_l, y=y_l - 8, width=31, height=8, title="Floreta", text_content=ascii.floresta)
        elif caractere_atual == '&':
            draw_window(term, x=x_l, y=y_l - 8, width=31, height=8, title="Topo da Montanha", text_content=ascii.montaha)
        elif caractere_atual == ':':
            draw_window(term, x=x_l, y=y_l - 8, width=31, height=8, title="Praia", text_content=ascii.praia)
        elif caractere_atual == '`':
            draw_window(term, x=x_l, y=y_l - 8, width=31, height=8, title="Caminho", text_content=ascii.caminho2)
        elif caractere_atual == '"':
            draw_window(term, x=x_l, y=y_l - 8, width=31, height=8, title="Floresta de Neve", text_content=ascii.neve)
        elif caractere_atual == ';':
            def matar():
                with term.location(x=10, y=0):
                    print("Você deseja matar esse inocente? (S/N)")
                with term.location(x=10, y=1):
                    esc = input(">").strip().upper()
                if esc == "S":
                    novo_char = "X"
                    linha_antiga = mapa_art[player.y_mapa]
                    mapa_art[player.y_mapa] = (
                        linha_antiga[:player.x_mapa] + 
                        novo_char + 
                        linha_antiga[player.x_mapa + 1:]
                    )
                    with term.location(x=10, y=2):
                        print("Você matou o inocente...")
                else:
                    with term.location(x=10, y=2):
                        print("Você poupou o inocente.")
            matar()
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
            player.menu(x_janela=0, y_janela=8)
            continue
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

def jogo():
    clear()
    draw_window(term, x=10, y=0, width=52, height=11, text_content=ascii.cidade_em_caos)
    cutcenes(mansagem=dialogo.cutsine_inicil, x=10, y=11, witr=52, herd=8)
    input()
    clear()
    draw_window(term, x=10, y=0, width=52, height=11, text_content=ascii.cidade_em_caos)
    cutcenes(mansagem=dialogo.descricao, x=10, y=11, witr=52, herd=8)
    input()
    clear()
    draw_window(term, x=10, y=0, width=52, height=11, text_content=ascii.cidade_em_caos2)
    cutcenes(mansagem=dialogo.descricao2, x=10, y=11, witr=52, herd=8)
    input()
    mini_mapa(x_l=0, y_l=8, player=player, ascii=ascii, mapas_=mapas.mini_mapa_tuturial.split('\n'), camera_w=30, camera_h=8)

    

jogo()