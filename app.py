from jogo import mini_mapa, jogo
from classe_arts import draw_window, term, clear
import random, time, string
from classe_do_jogador import jogador
from classe_do_inimigo import inimigo
from classe_arts import art_ascii, Cores
from mm import tocar_musica, escolher_e_tocar_musica, parar_musica, tocando_musica
from classe_do_inventario import TODOS_OS_ITENS
ascii = art_ascii()
C = Cores()
jj = jogador(nome="", hp_max=100, atk=15, niv=1, xp_max=100, defesa=10, gold=0, stm_max=100, intt=10, mn_max=100,d_m=20, art_player=ascii.necro, skin="0")
ee = inimigo(nome="", hp_max=0, atk=0, niv=0, xp=0, defesa=0, gold=0, art_ascii="",atk1="",atk2="")
thread_musica = None

def menu_inicial(x_l, y_l):
    NOME_DO_ARQUIVO = "Title_.mp3"
    escolher_e_tocar_musica(NOME_DO_ARQUIVO)
    while True:
        clear()
        menu_art = ascii.titulo
        opcoes = "[1] Jogar\n[2] Carregar\n[3] Sair"
        herd = menu_art.count("\n")
        draw_window(term, x=x_l, y=y_l, width=90, height=24, text_content=menu_art)
        draw_window(term, x=x_l+25, y=y_l+herd+1, width=25, height=6, text_content=opcoes)
        with term.location(x=x_l+27, y=y_l+herd+5):
            escolha = input(">")
        if escolha == "1":
            nome = solicitar_nome(x_l, y_l, menu_art)
            skin, caractere, cor_final = escolher_personagem(x_l, y_l)
            jj = jogador(
                nome=nome,
                hp_max=50,
                atk=10,
                niv=1,
                xp_max=100,
                defesa=0,
                gold=0,
                stm_max=100,
                intt=0,
                mn_max=50,
                d_m=15,
                art_player=skin,
                skin=cor_final
            )
            jogo(player_j=jj, ascii_j=ascii, x=10, y=0)

        elif escolha == "2":
            draw_window(term, x=x_l, y=y_l, width=90, height=24, text_content=menu_art)
            draw_window(term, x=x_l+25, y=y_l+herd+1, width=30, height=6)
            jj.load_game(filename="Demo.json", x_l=x_l+26, y_l=y_l+herd+2)
            with term.location(x=x_l+26, y=y_l+herd+5):
                input(">")

        elif escolha == "3":
            exit()

def solicitar_nome(x_l, y_l, menu_art):
    while True:
        clear()
        prompt = "Qual será seu Nome:\n(max 8 caracteres)"
        num_linhas = prompt.count("\n") + 4
        draw_window(term, x=x_l, y=y_l, width=90, height=24, text_content=menu_art)
        draw_window(term, x=x_l+25, y=y_l+num_linhas+2, width=27, height=num_linhas, text_content=prompt)

        with term.location(x=x_l+26, y=y_l+num_linhas+5):
            nome = input(">")

        if len(nome) > 8:
            mostrar_mensagem(x_l+26, y_l+num_linhas+5, "Nome muito extenso")
        elif len(nome) < 1:
            mostrar_mensagem(x_l+26, y_l+num_linhas+5, "Digite pelo menos 1 letra")
        else:
            return nome

def escolher_personagem(x_l, y_l):
    personagens = {
        "1": ascii.necro,
        "2": ascii.guerriro,
        "3": ascii.mago
    }
    while True:
        clear()
        draw_window(term, x=x_l, y=y_l, width=90, height=24)
        draw_window(term, x=x_l+2, y=y_l+1, width=25, height=11, title="1", text_content=ascii.necro)
        draw_window(term, x=x_l+32, y=y_l+1, width=25, height=11, title="2", text_content=ascii.guerriro)
        draw_window(term, x=x_l+64, y=y_l+1, width=25, height=11, title="3", text_content=ascii.mago)

        with term.location(x=x_l+2, y=y_l+12):
            escolha = input("Escolha uma Skin: ")

        if escolha in personagens:
            skin = personagens[escolha]
            caractere = solicitar_caractere(x_l, y_l)
            cor_final = escolher_cor(caractere, x_l, y_l)
            return skin, caractere, cor_final

def solicitar_caractere(x_l, y_l):
    while True:
        with term.location(x=x_l+2, y=y_l+13):
            print("Escolha um caractere do seu personagem: ")
        with term.location(x=x_l+2, y=y_l+14):
            caractere = input(">")
        if len(caractere) == 1:
            return caractere
        else:
            with term.location(x=x_l+2, y=y_l+15):
                print("Use apenas UM caractere")
            time.sleep(2)

def escolher_cor(caractere, x_l, y_l):
    cores = {
        "1": C.AZUL,
        "2": C.AMARELO,
        "3": C.VERDE,
        "4": C.VERMELHO
    }
    while True:
        with term.location(x=x_l+2, y=y_l+15):
            print("Escolha um Cor: ")
        with term.location(x=x_l+2, y=y_l+16):
            print(f"{C.AZUL}[1]Azul {C.AMARELO}[2]Amarelo {C.VERDE}[3]Verde {C.VERMELHO}[4]Vermelho")
        with term.location(x=x_l+2, y=y_l+17):
            escolha = input(">")
        if escolha in cores:
            return f"{cores[escolha]}{caractere}{C.RESET}"

def mostrar_mensagem(x, y, mensagem):
    with term.location(x, y):
        print(mensagem)
    time.sleep(2)

menu_inicial(x_l=0, y_l=0)