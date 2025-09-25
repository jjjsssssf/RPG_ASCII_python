from classe_arts import draw_window, term, clear
import random, time, string
from classe_do_jogador import jogador
from classe_do_inimigo import inimigo
from classe_arts import art_ascii
ascii = art_ascii()
player_b = jogador(nome="", hp_max=100, atk=15, niv=1, xp_max=100, defesa=10, gold=0, stm_max=100, intt=10, mn_max=100,d_m=20, art_player=ascii.necro)
inimigo_b = inimigo(nome="", hp_max=0, atk=0, niv=0, xp=0, defesa=0, gold=0, art_ascii="",atk1="",atk2="")

def seleção_inimigo():
    if player_b.niv <= 5 or player_b.andar <= 5:
        hp_max = random.randint(50, 100)
        atk = random.randint(5, 15)
        niv = random.randint(1, 5)
        xp = random.randint(50, 300)
        defesa = random.randint(5, 15)
        gold = random.randint(20, 250)
    elif player_b.niv >= 6 or player_b.andar >= 10:
        hp_max = random.randint(200, 350)
        atk = random.randint(10, 25)
        niv = random.randint(6, 12)
        xp = random.randint(300, 600)
        defesa = random.randint(10, 25)
        gold = random.randint(50, 280)
    
    
    inimigos = [
        inimigo(nome="Lobo", hp_max=hp_max, atk=atk, niv=niv, xp=xp, defesa=defesa, gold=gold, art_ascii=ascii.lobo, atk1="Tridente", atk2="Bola de Fogo"),
        inimigo(nome="Lobo", hp_max=hp_max, atk=atk, niv=niv, xp=xp, defesa=defesa, gold=gold, art_ascii=ascii.lobo1, atk1="Tridente", atk2="Bola de Fogo"),
        inimigo(nome="Esqueleto", hp_max=hp_max, atk=atk, niv=niv, xp=xp, defesa=defesa, gold=gold, art_ascii=ascii.esqueleto, atk1="Ossada", atk2="Espadada"),
        inimigo(nome="Demonio", hp_max=hp_max, atk=atk, niv=niv, xp=xp, defesa=defesa, gold=gold, art_ascii=ascii.demoni1, atk1="Tridente", atk2="Bola de Fogo"),
        inimigo(nome="Demonio", hp_max=hp_max, atk=atk, niv=niv, xp=xp, defesa=defesa, gold=gold, art_ascii=ascii.demoni0, atk1="Tridente", atk2="Bola de Fogo"),
    ]
    return random.choice(inimigos)

def batalha(player_b, inimigo_b):
    inimigo_b = seleção_inimigo()
    with term.fullscreen():
        while True:
            print(term.clear)
            x_jogador = 30
            y_jogador = 0
            inimigo_b.status_art(x_janela=31, y_janela=0)
            player_b.status_batalha_art(x_janela=0, y_janela=0)
            acoes = "[1]Atacar\n[2]Magias\n[3]Inventario\n[4]Fugir\n"
            acoes_text= acoes.count('\n')+1
            herd = acoes_text + 2
            draw_window(term, x=x_jogador+32, y=0, width=25, height=herd, title="Ações",text_content=acoes)
            with term.location(x=x_jogador+33, y=5):
                escolha = input(">")
            acao_valida = False
            if escolha == "4":
                with term.location(x=x_jogador+32, y=7):
                    print(term.bold_red("Você fugiu da batalha."))
                    player_b.buff_atk = 0
                    player_b.buff_def = 0
                time.sleep(2)
                return True
            elif escolha == "1":
                player_b.atake(inimigo_b, x_janela=0, y_janela=17)
                acao_valida = True
            elif escolha == "2":
                acao_valida = player_b.menu_magias(x_menu=x_jogador+32, y_menu=7, batalha=True, alvo=inimigo_b)
            elif escolha == "3":
                acao_valida = player_b.inventario_(x_inv=x_jogador+32, y_inv=0, batalha=True)
            else:
                with term.location(x=x_jogador+32, y=7):
                    print("Escolha inválida. Tente novamente.")
                time.sleep(2)
                continue            
            if acao_valida:
                if inimigo_b.hp <= 0:
                    with term.location(x=x_jogador+32, y=7):
                        print(term.clear_eol + f"{player_b.nome} venceu a batalha!")
                    time.sleep(3)
                    player_b.gold += inimigo_b.gold
                    player_b.xp += inimigo_b.xp
                    player_b.buff_atk = 0
                    player_b.buff_def = 0
                    player_b.add_xp(inimigo_b.xp)
                    return True
                inimigo_b.ataque_selec(player_b, x_janela=31, y_janela=17)
                with term.location(x=x_jogador+32, y=7):
                    input(">")
                if player_b.hp <= 0:
                    with term.location(x=x_jogador+32, y=7):
                        print(f"{inimigo_b.nome} venceu a batalha!")
                    time.sleep(3)
                    return False
                
