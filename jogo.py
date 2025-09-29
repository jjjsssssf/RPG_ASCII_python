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
    draw_window(term, x=0, y=0, width=30, height=11, text_content=ascii.vila1)
    with term.location(x=0, y=11):
        escolha = input("Você quer entrar nessa vila\n[S] [N]: ")

INTERACOES = {
    'V': vila,
}

def mini_mapa(x_l, y_l, player, ascii):
    player.x = x_l + 3
    player.y = y_l + 6
    mapa_art = [linha.rstrip() for linha in ascii.mini_mapa.split('\n') if linha]
    OBSTACULOS = ['=', '|']
    feedback_message = ""
    global thread_musica
    parar_musica()
    NOME_DO_ARQUIVO = "Menu_som_baia.mp3"
    escolher_e_tocar_musica(NOME_DO_ARQUIVO)
    while True:
        clear()
        print(term.home + term.clear)
        altura_total = len(mapa_art) + 2
        draw_window(term, x=x_l, y=y_l, width=45, height=altura_total, text_content=ascii.mini_mapa)
        with term.location(player.x, player.y):
            print(term.bold_yellow(player.skin) + term.normal)
        try:
            mapa_y_atual = player.y - (y_l + 1)
            mapa_x_atual = player.x - (x_l + 2)
            caractere_atual = mapa_art[mapa_y_atual][mapa_x_atual]
        except IndexError:
            caractere_atual = ' '
        if caractere_atual == '.':
            draw_window(term, x=0, y=0, width=30, height=8,title="Estrada" ,text_content=ascii.caminho)
        else:
            for i in range(9):
                with term.location(0, altura_total + 3 + i):
                    print(term.clear_eol)
        if caractere_atual == ".":
            barou = random.randint(1, 100)
            if barou < 25:
                batalha(player_b=player, inimigo_b=enimy)
            else:
                pass
        if caractere_atual == "~":
            draw_window(term, x=0, y=0, width=30, height=8,title="RIO" ,text_content=ascii.agua)
        if caractere_atual == "#":
            draw_window(term, x=0, y=0, width=30, height=8,title="Montanha" ,text_content=ascii.montaha)
        if caractere_atual == "V":
            draw_window(term, x=0, y=0, width=30, height=11,title="Vila" ,text_content=ascii.vila1)
        if feedback_message:
            with term.location(0, altura_total + 2):
                print(term.red(feedback_message))
                feedback_message = ""
        with term.location(31, altura_total):
            print(term.clear_eol + "Digite (w/s/a/d [n]):")
        with term.location(52, altura_total):
            entrada = input(">").strip().split()
        if not entrada:
            continue
        try:
            movi = entrada[0].lower()
            quant = int(entrada[1]) if len(entrada) > 1 else 1
        except (ValueError, IndexError):
            feedback_message = "Entrada inválida. Use: w 1 / a 3 / etc."
            continue
        novo_x_p = player.x
        novo_y_p = player.y
        if movi == "w":
            novo_y_p -= quant
        elif movi == "s":
            novo_y_p += quant
        elif movi == "a":
            novo_x_p -= quant
        elif movi == "d":
            novo_x_p += quant
        else:
            feedback_message = f"Comando '{movi}' inválido. Use w/a/s/d."
            continue
        mapa_y = novo_y_p - (y_l + 1)
        mapa_x = novo_x_p - (x_l + 2)
        if 0 <= mapa_y < len(mapa_art) and 0 <= mapa_x < len(mapa_art[mapa_y]):
            caractere_na_posicao = mapa_art[mapa_y][mapa_x]
            if caractere_na_posicao not in OBSTACULOS:
                player.x = novo_x_p
                player.y = novo_y_p                 
                if caractere_na_posicao in INTERACOES:
                    print(term.move(altura_total + 3, 0) + term.clear_eos)
                    INTERACOES[caractere_na_posicao]()

"mini_mapa(x_l=31, y_l=0, player=player, ascii=ascii)"