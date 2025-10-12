from classe_do_jogador import jogador
from classe_do_inimigo import inimigo
import time, random, os, json
from batalha import batalha, batalha_cut, seleção_inimigo
from classe_arts import draw_window,term, clear, art_ascii, Cores, mini_mapa_, dialogos, clear_region_a
from mm import tocar_musica, escolher_e_tocar_musica, parar_musica, tocando_musica
from classe_do_inventario import TODOS_OS_ITENS, Item
##ARQUIVO DO MAPA
mapas = mini_mapa_()
dialogo = dialogos()
ascii = art_ascii()
C = Cores()
player = jogador(nome="", hp_max=100, atk=150, niv=1, xp_max=100, defesa=10, gold=0, stm_max=100, intt=10, mn_max=100,d_m=20, art_player=ascii.necro, skin="@", skin_nome='')
def salvar_mapa_estado(filename, mapa_id, estado_mapa):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({
                "mapa_id": mapa_id,
                "mapa_art": estado_mapa["mapa_art"],
                "inimigos_derrotados": list(estado_mapa["inimigos_derrotados"]),
                "baus_abertos": list(estado_mapa["baus_abertos"]),
                "interacoes": estado_mapa.get("interacoes", {}),
                "obstaculos": estado_mapa["obstaculos"],
                "cores": estado_mapa.get("cores", {})
            }, f, indent=4)
        print(f"Estado do mapa salvo com sucesso.")
    except IOError as e:
        print(f"Erro ao salvar o estado do mapa: {e}")

def carregar_mapa_estado(filename):
    if not os.path.exists(filename):
        return None
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Erro ao carregar estado do mapa: {e}")
        return None

def mini_mapa(
    x_l, y_l, player, ascii, mapas_, camera_w, camera_h, x_p, y_p, menager,
    cores_custom=None, obstaculos_custom=None, mapa_anterior=None, interacoes_custom=None, quantidade_map=None,
    mapa_nome=None
):
    ESTADO_MAPAS = {}

    mapa_id = mapa_nome or id(mapas_)

    save_filename = f"save_mapa_{mapa_id}.json"

    estado_carregado = carregar_mapa_estado(save_filename)
    if estado_carregado:
        mapa_art = estado_carregado["mapa_art"]
        max_width = max(len(linha) for linha in mapa_art)

    if estado_carregado:
        ESTADO_MAPAS[mapa_id] = {
            "mapa_art": estado_carregado["mapa_art"],
            "inimigos_derrotados": set(estado_carregado["inimigos_derrotados"]),
            "baus_abertos": set(estado_carregado["baus_abertos"]),
            "interacoes": estado_carregado.get("interacoes", {}),
            "obstaculos": estado_carregado["obstaculos"],
            "cores": estado_carregado.get("cores", {})
        }
    else:
        raw_map_lines = mapas_
        max_width = max(len(l) for l in raw_map_lines if l.strip())
        mapa_art = [l.ljust(max_width) for l in raw_map_lines if l.strip()]

        ESTADO_MAPAS[mapa_id] = {
            "mapa_art": mapa_art,
            "inimigos_derrotados": set(),
            "baus_abertos": set(),
            "interacoes": {},
            "obstaculos": obstaculos_custom or ['#', '.', "H"],
            "cores": cores_custom,
        }
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

        clear()
        atualizar_camera()
        janela_mapa = [
            linha[camera_x:camera_x + CAMERA_WIDTH]
            for linha in mapa_art[camera_y:camera_y + CAMERA_HEIGHT]
        ]
        mini_mapa_render = "\n".join(janela_mapa)
        draw_window(term, x=x_l, y=y_l, width=CAMERA_WIDTH + 4, height=CAMERA_HEIGHT + 2,title=f"{mapa_nome}", text_content=mini_mapa_render)

        CORES = cores_custom or {
            "#": term.bold_magenta,
            '~': term.blue,
            '@': term.red_on_white,
            'B': term.yellow,
            'P': term.red,
            'H': term.bold_brown,
            'W': term.bold_gray,
            'V': term.bold_green,
            'M': term.bold_magenta_on_white,
            '▒': term.bold_magenta_on_blue
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
                inimigo_ = seleção_inimigo(num=1)
                batalha(player_b=player, inimigo_b=inimigo_)
                if inimigo_.hp <= 0:
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
                    x_p=7,
                    y_p=1,
                    menager="",
                    mapa_anterior={
                        "mapa": mapas_,
                        "pos": (player.x_mapa, player.y_mapa),
                        "mensagem": menager,
                        "cores": CORES,
                        "obstaculos": OBSTACULOS
                    },
                    mapa_nome="castelo_2",
                    carater_ale="@",
                    quantidade_ale=10
                )
                return

        elif mapas_ == mapas.mapa_castelo_2.split("\n"):
            if TODOS_OS_ITENS["Chave"] in player.inventario:
                if 'H' in OBSTACULOS:
                    OBSTACULOS.remove('H')
            if player.x_mapa == 6 and player.y_mapa == 1:
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
                inimigo_ = seleção_inimigo(num=1)
                batalha(player_b=player, inimigo_b=inimigo_)
                if inimigo_.hp <= 0:
                    ESTADO_MAPAS[mapa_id]["inimigos_derrotados"].add((player.x_mapa, player.y_mapa))
                    linha_antiga = mapa_art[player.y_mapa]
                    mapa_art[player.y_mapa] = linha_antiga[:player.x_mapa] + ' ' + linha_antiga[player.x_mapa + 1:]
            elif player.x_mapa == 9 and player.y_mapa == 24 or player.x_mapa == 10 and player.y_mapa == 24:
                core_custom = {
                    '#': term.blue,
                    '=': term.bold_blue,
                    '[': term.bold_magente,
                    ']': term.bold_magente,
                    'O': term.bold_white_on_brown,
                    '.': term.black,
                    'M': term.magenta
                }
                colisoes = {
                    "#", '[', ']', '=', 'O', '.'
                }
                mini_mapa(
                    x_l=0,
                    y_l=0,
                    player=player,
                    ascii=ascii,
                    mapas_=mapas.biblioteca.split('\n'),
                    camera_w=35,
                    camera_h=15,
                    x_p=12,
                    y_p=9,
                    menager="",
                    mapa_anterior={
                        "mapa": mapas_,
                        "pos": (player.x_mapa, player.y_mapa),
                        "mensagem": menager,
                        "cores": CORES,
                        "obstaculos": OBSTACULOS
                    },
                    mapa_nome="biblica",
                    carater_ale="",
                    quantidade_ale=0,
                    cores_custom=core_custom,
                    obstaculos_custom=colisoes
                )
                return
           
            elif player.x_mapa == 21 and player.y_mapa == 24 or player.x_mapa == 22 and player.y_mapa == 24:
                core_custom = {
                    '#': term.magenta,
                    '.': term.green,
                    '░': term.red,
                    '~': term.red_on_orange,
                    '^': term.orange_on_yellow,
                }
                colisoes = {
                    "#", "~", "^", '/', '\\', 'o' 
                }
                mini_mapa(
                    x_l=0,
                    y_l=0,
                    player=player,
                    ascii=ascii,
                    mapas_=mapas.boss_1.split('\n'),
                    camera_w=35,
                    camera_h=15,
                    x_p=18,
                    y_p=14,
                    menager="",
                    mapa_anterior={
                        "mapa": mapas_,
                        "pos": (player.x_mapa, player.y_mapa),
                        "mensagem": menager,
                        "cores": CORES,
                        "obstaculos": OBSTACULOS
                    },
                    mapa_nome="Suny",
                    carater_ale="",
                    quantidade_ale=0,
                    cores_custom=core_custom,
                    obstaculos_custom=colisoes
                )
                return
                
            elif player.x_mapa == 24 and player.y_mapa == 0 or player.x_mapa == 25 and player.y_mapa == 0:
                mini_mapa(
                    x_l=0,
                    y_l=0,
                    player=player,
                    ascii=ascii,
                    mapas_=mapas.taberna.split('\n'),
                    camera_w=35,
                    camera_h=15,
                    x_p=22,
                    y_p=8,
                    menager="",
                    mapa_anterior={
                        "mapa": mapas_,
                        "pos": (player.x_mapa, player.y_mapa),
                        "mensagem": menager,
                        "cores": CORES,
                        "obstaculos": OBSTACULOS
                    },
                    mapa_nome="taberna",
                    carater_ale="&",
                    quantidade_ale=5,
                )
                return
                
        elif mapas_ == mapas.biblioteca.split("\n"):
            if player.x_mapa == 12 and player.y_mapa == 8 or player.x_mapa == 13 and player.y_mapa == 8:
                mini_mapa(
                    x_l=0,
                    y_l=0,
                    player=player,
                    ascii=ascii,
                    mapas_=mapas.mapa_castelo_2.split('\n'),
                    camera_w=35,
                    camera_h=15,
                    x_p=9,
                    y_p=23,
                    menager="",
                    mapa_anterior={
                        "mapa": mapas_,
                        "pos": (player.x_mapa, player.y_mapa),
                        "mensagem": menager,
                        "cores": CORES,
                        "obstaculos": OBSTACULOS
                    },
                    mapa_nome="castelo_2",
                    carater_ale="@",
                    quantidade_ale=10
                )
                return

            if player.x_mapa == 12 and player.y_mapa == 13:
                player.aprender_magias(term, x_menu=x_l + CAMERA_WIDTH + 5, y_menu=CAMERA_HEIGHT-15, wend=camera_w+5, herd = CAMERA_HEIGHT)

        elif mapas_ == mapas.taberna.split("\n"):
            if caractere_atual == "&":
                def falas_aleatorias():
                    fala = """Por aqui todos tem medo do rei
ninguem o vio mas tem medo"""
                    fala1 = '''Se quiser comprar algo
se aproxime do vendedor'''
                    fala_ale = random.choice([fala, fala1])
                    falas(menager=fala_ale)
                falas_aleatorias()
            if player.x_mapa == 23 and player.y_mapa == 13:
                player.gerenciar_loja(x=0, y=0, largura=35)
            elif player.x_mapa == 22 and player.y_mapa == 7 or player.x_mapa == 23 and player.y_mapa == 7:
                mini_mapa(
                    x_l=0,
                    y_l=0,
                    player=player,
                    ascii=ascii,
                    mapas_=mapas.mapa_castelo_2.split('\n'),
                    camera_w=35,
                    camera_h=15,
                    x_p=24,
                    y_p=1,
                    menager="",
                    mapa_anterior={
                        "mapa": mapas_,
                        "pos": (player.x_mapa, player.y_mapa),
                        "mensagem": menager,
                        "cores": CORES,
                        "obstaculos": OBSTACULOS
                    },
                    mapa_nome="castelo_2",
                    carater_ale="@",
                    quantidade_ale=10
                )
                return

        elif mapas_ == mapas.boss_1.split("\n"):
            if player.boss['Suny'] == False:
                if player.x_mapa == 18 and player.y_mapa == 6 or player.x_mapa == 19 and player.y_mapa == 6:
                    fla = '''Suny: Como ousa a atrapalar meu sono agora
vou te matar, seu verme aldito '''
                    falas(menager=fla)
                    time.sleep(2)
                    suny = inimigo(nome='Suny', hp_max=250, atk=25, niv=5, xp=500, defesa=15, gold=600, art_ascii=ascii.suny, atk1='Mordida', atk2='Bola de Fogo')
                    batalha_cut(player_b=player, inimigo_b=suny)
                    if suny.hp <= 0:
                        fla = '''Suny: Seu maldito como pode me derrotar 
*suspiro* bem pegue essa chave e siga 
sua missão
Foi adicionado uma Chave do Dragão'''
                        falas(menager=fla)
                        player.inventario.append(TODOS_OS_ITENS['Chave do Dragão'])
                        player.boss['Suny']=True
            if player.x_mapa == 18 and player.y_mapa == 15 or player.x_mapa == 19 and player.y_mapa == 15:
                mini_mapa(
                    x_l=0,
                    y_l=0,
                    player=player,
                    ascii=ascii,
                    mapas_=mapas.mapa_castelo_2.split('\n'),
                    camera_w=35,
                    camera_h=15,
                    x_p=21,
                    y_p=23,
                    menager="",
                    mapa_anterior={
                        "mapa": mapas_,
                        "pos": (player.x_mapa, player.y_mapa),
                        "mensagem": menager,
                        "cores": CORES,
                        "obstaculos": OBSTACULOS
                    },
                    mapa_nome="castelo_2",
                    carater_ale="@",
                    quantidade_ale=10
                )
                return
                
                
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

        direcoes = {
            "w": (0, -1),
            "s": (0, 1),
            "a": (-1, 0),
            "d": (1, 0),
        }

        if movi in direcoes:
            dx, dy = direcoes[movi]
            for _ in range(quant):
                passo_x = player.x_mapa + dx
                passo_y = player.y_mapa + dy
                if 0 <= passo_x < MAP_WIDTH and 0 <= passo_y < MAP_HEIGHT:
                    caractere = mapa_art[passo_y][passo_x]
                    if caractere not in OBSTACULOS:
                        player.x_mapa = passo_x
                        player.y_mapa = passo_y
                        if caractere in INTERACOES:
                            INTERACOES[caractere]()
        else:
            if movi == "inventario":
                player.inventario_(x=x_l + CAMERA_WIDTH + 5, y=y_l, werd=CAMERA_WIDTH + 2, herd=0, batalha=False)
            elif movi == "sair":
                exit()
            elif movi == "up":
                player.up(x=x_l + CAMERA_WIDTH + 5, y=y_l, werd=CAMERA_WIDTH + 2, herd=CAMERA_HEIGHT + 2)
            elif movi == "q" and mapa_anterior:
                exit()
            elif movi == "save":
                player.save_game()
                salvar_mapa_estado(save_filename, mapa_id, ESTADO_MAPAS[mapa_id])
                feedback_message = "Jogo salvo com sucesso."
            elif movi == "load":
                estado_carregado = carregar_mapa_estado(save_filename)
                player.load_game()
                if estado_carregado:
                    mapa_art = estado_carregado["mapa_art"]
                    ESTADO_MAPAS[mapa_id]["mapa_art"] = mapa_art
                    ESTADO_MAPAS[mapa_id]["inimigos_derrotados"] = set(estado_carregado["inimigos_derrotados"])
                    ESTADO_MAPAS[mapa_id]["baus_abertos"] = set(estado_carregado["baus_abertos"])
                    ESTADO_MAPAS[mapa_id]["interacoes"] = estado_carregado.get("interacoes", {})
                    ESTADO_MAPAS[mapa_id]["obstaculos"] = estado_carregado["obstaculos"]
                    ESTADO_MAPAS[mapa_id]["cores"] = estado_carregado.get("cores", {})
            else:
                feedback_message = f"Comando '{movi}' inválido. Use w/a/s/d/inventario/up/q."
 
"""mini_mapa(
    x_l=0,
    y_l=0,
    player=player,
    ascii=ascii,
    mapas_ = mapas.mapa_castelo.split("\n"),
    x_p=10,
    y_p=3, 
    mapa_nome='catelo',
    camera_w=35,
    camera_h=15,
    carater_ale='@',
    quantidade_ale=10,
    menager=""
)
 
"""