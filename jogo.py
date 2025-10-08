from classe_do_jogador import jogador
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

ESTADO_MAPAS = {}

def mini_mapa(
    x_l, y_l, player,ascii, mapas_, camera_w, camera_h, x_p, y_p, menager,
    cores_custom=None, obstaculos_custom=None, mapa_anterior=None, interacoes_custom=None, quantidade_map=None,
    mapa_nome=None 
):
    raw_map_lines = mapas_
    max_width = max(len(l) for l in raw_map_lines if l.strip())
    mapa_id = mapa_nome or id(mapas_)
    if mapa_id not in ESTADO_MAPAS:
        mapa_art = [l.ljust(max_width) for l in raw_map_lines if l.strip()]
        quantidade_caracteres = quantidade_map or {'@': player.niv + 5}

        posicoes_vazias = [
            (y, x)
            for y, linha in enumerate(mapa_art)
            for x, char in enumerate(linha)
            if char == ' '
        ]
        posicoes_disponiveis = posicoes_vazias.copy()

        for caractere, quantidade in quantidade_caracteres.items():
            if len(posicoes_disponiveis) == 0:
                break
            escolhidas = random.sample(posicoes_disponiveis, min(quantidade, len(posicoes_disponiveis)))        
            for y, x in escolhidas:
                linha_antiga = mapa_art[y]
                mapa_art[y] = linha_antiga[:x] + caractere + linha_antiga[x+1:]
                posicoes_disponiveis.remove((y, x))

        ESTADO_MAPAS[mapa_id] = {
            "mapa_art": mapa_art,
            "inimigos_derrotados": set(),
            "baus_abertos": set(),
            "interacoes": {},
            "obstaculos": obstaculos_custom or ['#', '.', "H"],
            "cores": cores_custom,
        }
    else:
        mapa_art = ESTADO_MAPAS[mapa_id]["mapa_art"]

    player.x_mapa = x_p
    player.y_mapa = y_p
    OBSTACULOS = obstaculos_custom or ESTADO_MAPAS[mapa_id]["obstaculos"]
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
        def bau():
            pos = (player.x_mapa, player.y_mapa)
            if pos in ESTADO_MAPAS[mapa_id]["baus_abertos"]:
                return
            ESTADO_MAPAS[mapa_id]["baus_abertos"].add(pos)

            with term.location(x=x_l+CAMERA_WIDTH+6, y=CAMERA_HEIGHT-2):
                print("Você Encontrou um Bau")
            itens = ['Espada', 'Escudo', 'Suco', 'Poção de Cura']
            selec = random.choice(itens)
            with term.location(x=x_l+CAMERA_WIDTH+6, y=CAMERA_HEIGHT-1):
                print(f"Você Conseguio um {selec}")
                player.inventario.append(TODOS_OS_ITENS[f"{selec}"])
                novo_char = 'b'
                linha_antiga = mapa_art[player.y_mapa]
                mapa_art[player.y_mapa] = linha_antiga[:player.x_mapa] + novo_char + linha_antiga[player.x_mapa + 1:]

        def falas(menager):
            clear_region_a(x=x_l + CAMERA_WIDTH + 6, start_y=y_l, end_y=y_l, width=CAMERA_WIDTH + 5)
            draw_window(term, x=x_l + CAMERA_WIDTH + 5, y=y_l, width=CAMERA_WIDTH + 5, height=CAMERA_HEIGHT + 2, text_content=menager)
            input("")

        clear()
        atualizar_camera()
        janela_mapa = [
            linha[camera_x:camera_x + CAMERA_WIDTH]
            for linha in mapa_art[camera_y:camera_y + CAMERA_HEIGHT]
        ]
        mini_mapa_render = "\n".join(janela_mapa)
        draw_window(term, x=x_l, y=y_l, width=CAMERA_WIDTH + 4, height=CAMERA_HEIGHT + 2, text_content=mini_mapa_render)

        CORES = cores_custom or {
            "#": term.bold_magenta,
            '~': term.blue,
            '@': term.blue,
            'B': term.yellow,
            'P': term.red,
            'H': term.bold_brown,
            'W': term.bold_gray,
            'V': term.bold_green,
            'M': term.bold_magenta_on_white
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

        if mapas_ == mapas.mapa_castelo.split("\n"):
            if caractere_atual == "B":
                bau()
            elif caractere_atual == "@":
                inimigo = seleção_inimigo(num=1)
                batalha(player_b=player, inimigo_b=inimigo)
                if inimigo.hp <= 0:
                    ESTADO_MAPAS[mapa_id]["inimigos_derrotados"].add((player.x_mapa, player.y_mapa))
                    linha_antiga = mapa_art[player.y_mapa]
                    mapa_art[player.y_mapa] = linha_antiga[:player.x_mapa] + ' ' + linha_antiga[player.x_mapa + 1:]

            elif caractere_atual == "P":
                if TODOS_OS_ITENS["Chave"] in player.inventario:
                    text= 'Vá para o porta a chave ira abri-la'
                else:
                    text= 'Está Aqui Rapaz uma Chave'
                    player.inventario.append(TODOS_OS_ITENS["Chave"])
                    falas(menager=text)
            if TODOS_OS_ITENS["Chave"] in player.inventario:
                if 'H' in OBSTACULOS:
                    OBSTACULOS.remove('H')

            if caractere_atual == "W":
                mini_mapa(
                    x_l=0,
                    y_l=0,
                    player=player,
                    ascii=ascii,
                    mapas_=mapas.mapa_castelo_2.split('\n'),
                    camera_w=35,
                    camera_h=15,
                    x_p=6,
                    y_p=1,
                    menager="",
                    mapa_anterior={
                        "mapa": mapas_,
                        "pos": (player.x_mapa, player.y_mapa),
                        "mensagem": menager,
                        "cores": CORES,
                        "obstaculos": OBSTACULOS
                    },
                    mapa_nome="castelo_2"  
                )
                return

        elif mapas_ == mapas.mapa_castelo_2.split("\n"):
            if TODOS_OS_ITENS["Chave"] in player.inventario:
                if 'H' in OBSTACULOS:
                    OBSTACULOS.remove('H')
            if player.x_mapa == 5 and player.y_mapa == 1:
                mini_mapa(
                    x_l=0,
                    y_l=0,
                    player=player,
                    ascii=ascii,
                    mapas_=mapas.mapa_castelo.split('\n'),
                    camera_w=35,
                    camera_h=15,
                    x_p=26,
                    y_p=12,
                    menager="",
                    mapa_anterior={
                        "mapa": mapas_,
                        "pos": (player.x_mapa, player.y_mapa),
                        "mensagem": menager,
                        "cores": CORES,
                        "obstaculos": OBSTACULOS
                    },
                    mapa_nome="castelo_1"
                )
                return
            if caractere_atual == "B":
                bau()
            elif caractere_atual == "@":
                inimigo = seleção_inimigo(num=1)
                batalha(player_b=player, inimigo_b=inimigo)
                if inimigo.hp <= 0:
                    ESTADO_MAPAS[mapa_id]["inimigos_derrotados"].add((player.x_mapa, player.y_mapa))
                    linha_antiga = mapa_art[player.y_mapa]
                    mapa_art[player.y_mapa] = linha_antiga[:player.x_mapa] + ' ' + linha_antiga[player.x_mapa + 1:]
            elif caractere_atual == "M":
                player.aprender_magias(term, x_menu=x_l + CAMERA_WIDTH + 5, y_menu=CAMERA_HEIGHT-15, wend=camera_w+5, herd = CAMERA_HEIGHT)


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
            continue
        elif movi == "sair":
            exit()
        elif movi == "up":
            player.up(x=x_l + CAMERA_WIDTH + 5, y=y_l, werd=CAMERA_WIDTH + 2, herd=CAMERA_HEIGHT + 2)
            continue
        elif movi == "q" and mapa_anterior:
            exit()
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


mini_mapa(
                x_l=0,
                y_l=0,
                player=player,
                ascii=ascii,
                mapas_=mapas.mapa_castelo_2.split('\n'),
                camera_w=35,
                camera_h=15,
                x_p=5,
                y_p=3,
                menager="",)