from classe_do_jogador import jogador
from classe_do_inimigo import inimigo
import time
from batalha import batalha, seleção_inimigo
from classe_arts import draw_window, term, clear, art_ascii
ascii = art_ascii()
player = jogador(nome="", hp_max=100, atk=15, niv=1, xp_max=100, defesa=10, gold=0, stm_max=100, intt=10, mn_max=100,d_m=20, art_player=ascii.necro)
enimy = inimigo(nome="", hp_max=0, atk=0, niv=0, xp=0, defesa=0, gold=0, art_ascii="",atk1="",atk2="")

def jogo_(x_l, y_l,player,ascii, enimy):
    player.rodar_jogo = True
    while player.rodar_jogo:
        if player.locais["Vila"] == True:
            clear()
            menu_art = ascii.vila1
            ess = "[1]Entrar\n[2]Andar\n[3]Conversar\n[4]Explorar"
            num_linha = menu_art.count("\n")+1
            herd = num_linha+2
            draw_window(term, x=x_l,y=y_l, width=36, height=herd, text_content=menu_art)
            draw_window(term, x=x_l+37, y=y_l, width=25, height=7, text_content=ess)
            with term.location(x=x_l+38, y=y_l+5):
                escolha = input(">")
            if escolha == "1":
                i = 0
                while i < 1:
                    clear()
                    draw_window(term, x=x_l,y=y_l, width=36, height=herd, text_content=menu_art)
                    ess = "[1]Mercado\n[2]Dormir\n[3]Conversar\n[4]Sair"
                    draw_window(term, x=x_l+37, y=y_l, width=25, height=7, text_content=ess)
                    with term.location(x=x_l+38, y=y_l+5):
                        escolha = input(">")
                    if escolha == "1":
                        player.gerenciar_loja(x_pos=38, y_pos=y_l+1, herd=7, x_loq=37, y_loq=y_l+0)
                    elif escolha == "2":
                        player.hospital(x_=37, y_=7)
                    elif escolha == "3":
                        pass
                    elif escolha == "4":
                        i = 1
                    elif escolha == "Menu":
                        clear()
                        player.menu(0, 0)
            elif escolha == "2":
                clear()
                menu_art = ascii.vila1
                ess = "Você Deseja Ir Para:\n[1]Moinho\n[2]Farol"
                draw_window(term, x=x_l,y=y_l, width=36, height=herd, text_content=menu_art)
                draw_window(term, x=x_l+37, y=y_l, width=25, height=7, text_content=ess) 
                with term.location(x=x_l+38, y=y_l+5):
                    escolha = input(">")
                if escolha == "1":
                    player.locais["Vila"]= None
                    player.locais["Moinho"] = True
                elif escolha == "2":
                    player.locais["Vila"]= None
                    player.locais["Farol"] = True
            elif escolha == "3":
                pass
            elif escolha == "4":
                batalha(player, enimy)
            elif escolha == "Menu":
                clear()
                player.menu(0, 0)

        elif player.locais["Farol"] == True:
            clear()
            menu_art = ascii.farol
            ess = "[1]Entrar\n[2]Andar\n[3]Placa\n[4]Explorar"
            num_linha = menu_art.count("\n")+1
            herd = num_linha+2
            draw_window(term, x=x_l,y=y_l, width=36, height=herd, text_content=menu_art)
            draw_window(term, x=x_l+37, y=y_l, width=25, height=7, text_content=ess)
            with term.location(x=x_l+38, y=y_l+5):
                escolha = input(">")
        elif player.locais["Moinho"] == True:
            clear()
            menu_art = ascii.moinho
            ess = "[1]Entrar\n[2]Andar\n[3]Conversar\n[4]Explorar"
            num_linha = menu_art.count("\n")+1
            herd = num_linha+2
            draw_window(term, x=x_l,y=y_l, width=36, height=herd, text_content=menu_art)
            draw_window(term, x=x_l+37, y=y_l, width=25, height=7, text_content=ess)
            with term.location(x=x_l+38, y=y_l+5):
                escolha = input(">")
