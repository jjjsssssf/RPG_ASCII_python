from classe_do_jogador import jogador
import time
from classe_arts import draw_window, term, clear, art_ascii, escolhas_
art = art_ascii()

def mapa_1(player, art):
    clear()
    while player.rodar_jogo:
        clear()
        if player.locais["Vila"] == False:
            print(f"--VILA--\n{art.vila1}")
            draw_window(term, x=32, y=1, width=26, height=4)
            with term.location(33, 2):
                print(term.bold_red("[1]Andar     [2]Entrar"))
            with term.location(33, 3):
                print(term.bold_red("[3]Conversar [4]Menu"))
            with term.location(32, 5):
                escolha = input(">")
            if escolha == "1":
                i = 0
                while i < 1:
                    clear()
                    print(f"--VILA--\n{art.vila1}")
                    draw_window(term, x=32, y=1, width=26, height=4)
                    with term.location(33, 2):
                        print(term.bold_cyan("Quer ir para qual local"))
                    with term.location(33, 3):
                        print(term.bold_red("[1]Oeste [2]Sul"))
                    with term.location(33, 5):
                        local = input(">")
                    if local == "1":
                        player.locais["Vila"] = None
                        player.locais["Floresta"] = True
                    elif local == "2":
                        player.locais["Vila"] = None
                        player.locais["Caverna"] = True
                    else:
                        i = 1

            elif escolha == "2":
                player.locais["Vila"] = True
                if player.locais["Vila"] == True:
                    i = 0
                    while i < 1:
                        clear()
                        print(f"--VILA--\n{art.vila1}")
                        draw_window(term, x=32, y=1, width=26, height=4)
                        with term.location(33, 2):
                            print(term.bold_red("[1]Explorar  [2]Sair"))
                        with term.location(33, 3):
                            print(term.bold_red("[3]Conversar [4]Menu"))
                        with term.location(32, 5):
                            vila_ = input(">")
                        if vila_ == "1":
                            dentro_vila()
                        elif vila_ == "2":
                            i += 1
                            player.locais["Vila"] = False
                        elif vila_ == "3":
                            y_ = 6
                            with term.location(32, y_):
                                print(term.bold_green("Plebel: Olá senhor nossa pequena vila está cada dia"))
                            y_ += 1
                            with term.location(32, y_):
                                print(term.bold_green("mais pobre por conta do Rei ele está cobrando impostos"))
                                y_ += 1
                            with term.location(32, y_):
                                print(term.bold_green("muito altos para nossa vila nos ajude derrote o Rei"))
                                y_ += 1
                            with term.location(32, y_):
                                input(">")
                        elif vila_ == "4":
                            player.menu()
            elif escolha == "3":
                y_ = 6
                with term.location(32, y_):
                    print(term.bold_green("Andarilho: Indo ao Norte você encontrara"))
                y_ += 1
                with term.location(32, y_):
                    print(term.bold_green("aquilo que os tolos cobção mas ao Sul"))
                    y_ += 1
                with term.location(32, y_):
                    print(term.bold_green("terá aquilo que tu precisas nesse momento"))
                    y_ += 1
                with term.location(32, y_):
                    input(">")

def dentro_vila():
    i = 0
    while i < 1:
        clear()
        print(f"--VILA--\n{art.vila1}")
        draw_window(term, x=0, y=13, width=30, height=4)
        with term.location(1, 14):
            print(term.bold("[1]Mercado     [2]Dormir"))
        with term.location(1, 15):
            print(term.bold("[3]Conversar   [4]Menu"))
        with term.location(0, 17):
            escolha = input(">")
        if escolha == "1":
            player.gerenciar_loja(x_loq=32,y_loq=0, herd=7, x_pos=33, y_pos=1)
    
