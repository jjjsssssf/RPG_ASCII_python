from ast import arg
from classe_arts import draw_window, term, clear
from jogo import jogo_
import random, time, string
from classe_do_jogador import jogador
from classe_do_inimigo import inimigo
from classe_arts import art_ascii
from classe_do_inventario import TODOS_OS_ITENS
ascii = art_ascii()
jj = jogador(nome="", hp_max=100, atk=15, niv=1, xp_max=100, defesa=10, gold=0, stm_max=100, intt=10, mn_max=100,d_m=20, art_player=ascii.necro)
ee = inimigo(nome="", hp_max=0, atk=0, niv=0, xp=0, defesa=0, gold=0, art_ascii="",atk1="",atk2="")

def menu_inicial(x_l, y_l):
    global jj
    while True:
        clear()
        menu_art = ascii.titulo
        ess = "[1]Jogar\n[2]Carregar\n[3]Sair"
        num_linha = menu_art.count("\n")
        herd = num_linha
        draw_window(term, x=x_l,y=y_l, width=90, height=24, text_content=menu_art)
        draw_window(term, x=x_l+25, y=y_l+herd+1, width=25, height=6, text_content=ess)
        with term.location(x=x_l+27, y=y_l+herd+5):
            escolha = input(">")
        if escolha == "1":
            while True:
                noess = "Qual será seu Nome:\nmaximo de 8 caracteres\n"
                clear()
                num_linha_ = noess.count("\n")
                herd_ = num_linha_+ 4
                draw_window(term, x=x_l,y=y_l, width=90, height=24, text_content=menu_art)
                draw_window(term, x=x_l+25, y=y_l+herd+1, width=25, height=herd_, text_content=noess)
                with term.location(x=x_l+26, y=y_l+herd+5):
                    escolha_nome = input(">")
                if len(escolha_nome) > 8:
                    with term.location(x=x_l+26, y=y_l+herd+5):
                        print("Nome muito extenço")
                    time.sleep(2)
                elif len(escolha_nome) < 1:
                    with term.location(x=x_l+26, y=y_l+herd+5):
                        print("Utilize uma letra")
                    time.sleep(2)
                else:
                    while True:
                        clear()
                        clsee = "Escolha Sua Classe\n[1]Guerreiro\n[2]Mago\n[3]Negromante"
                        num_linha_2 = clsee.count("\n")
                        herd_2 = num_linha_2+ 4
                        draw_window(term, x=x_l,y=y_l, width=90, height=24, text_content=menu_art)
                        draw_window(term, x=x_l+25, y=y_l+herd+1, width=25, height=herd_2, text_content=clsee)
                        with term.location(x=x_l+26, y=y_l+herd+6):
                            escolha_classe = input(">")
                        if escolha_classe == "2":
                            jj = jogador(nome=escolha_nome, hp_max=100, atk=5, niv=1, xp_max=100, defesa=0, gold=0, stm_max=75, intt=5, mn_max=75, d_m=15, art_player=ascii.mago, mana_lit=[["Bola de Fogo"], ["Escudo Mágico"]])
                            jj.classe["Guerreiro"] = True
                            jj.rodar_jogo = True
                            break
                        elif escolha_classe == "1":
                            jj = jogador(nome=escolha_nome, hp_max=100, atk=15, niv=1, xp_max=100, defesa=5, gold=0, stm_max=100, intt=0, mn_max=75, d_m=10, art_player=ascii.guerriro, mana_lit=[["Cura Leve"]])
                            jj.classe["Mago"] = True
                            jj.rodar_jogo = True
                            break
                        elif escolha_classe == "3":
                            jj = jogador(nome=escolha_nome, hp_max=100, atk=10, niv=1, xp_max=100, defesa=0, gold=0, stm_max=100, intt=5, mn_max=100, d_m=15, art_player=ascii.necro, mana_lit=[["Esqueleto"]])
                            jj.classe["Negromante"] = True
                            jj.rodar_jogo = True
                            break
                        else:
                            with term.location(x=x_l+26, y=y_l+herd+6):
                                print("Digite o número correto")
                            time.sleep(2)
                    jogo_(x_l=0, y_l=0, player=jj, ascii=ascii, enimy=ee)
        elif escolha == "2":
            draw_window(term, x=x_l,y=y_l, width=90, height=24, text_content=menu_art)
            draw_window(term, x=x_l+25, y=y_l+herd+1, width=30, height=6,)
            jj.load_game(filename=f"Demo.json",x_l=x_l+26, y_l=y_l+herd+2)
            with term.location(x=x_l+26, y=y_l+herd+5):
                input(">")

        elif escolha == "3":
            exit()


menu_inicial(x_l=0, y_l=0)