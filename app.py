from classe_arts import draw_window, term, clear
from jogo import mapa_1
import random, time, string
from classe_do_jogador import jogador
from classe_do_inimigo import inimigo
from classe_arts import art_ascii
from classe_do_inventario import TODOS_OS_ITENS
ascii = art_ascii()
jj = jogador(nome="", hp_max=100, atk=15, niv=1, xp_max=100, defesa=10, gold=0, stm_max=100, intt=10, mn_max=100,d_m=20, buff=0, art_player=ascii.guerriro)
ee = inimigo(nome="", hp_max=0, atk=0, niv=0, xp=0, defesa=0, gold=0, art_ascii="",atk1="",atk2="")

def seleção_inimigo():
    if jj.niv <= 5 or jj.andar <= 5:
        hp_max = random.randint(50, 100)
        atk = random.randint(5, 15)
        niv = random.randint(1, 5)
        xp = random.randint(50, 300)
        defesa = random.randint(5, 15)
        gold = random.randint(20, 250)
    elif jj.niv >= 6 or jj.andar >= 10:
        hp_max = random.randint(200, 350)
        atk = random.randint(10, 25)
        niv = random.randint(6, 12)
        xp = random.randint(300, 600)
        defesa = random.randint(10, 25)
        gold = random.randint(50, 280)
    
    
    inimigos = [
        inimigo(nome="Esqueleto", hp_max=hp_max, atk=atk, niv=niv, xp=xp, defesa=defesa, gold=gold, art_ascii=ascii.esqueleto, atk1="Ossada", atk2="Espadada"),
        inimigo(nome="Demonio", hp_max=hp_max, atk=atk, niv=niv, xp=xp, defesa=defesa, gold=gold, art_ascii=ascii.demoni1, atk1="Tridente", atk2="Bola de Fogo"),
        inimigo(nome="Demonio", hp_max=hp_max, atk=atk, niv=niv, xp=xp, defesa=defesa, gold=gold, art_ascii=ascii.demoni0, atk1="Tridente", atk2="Bola de Fogo"),
    ]
    return random.choice(inimigos)

def batalha():
    ee = seleção_inimigo()
    with term.fullscreen():
        while True:
            print(term.clear)
            x_jogador = 30
            y_jogador = 0
            ee.status_art(x_janela=31, y_janela=0)
            jj.status_batalha_art(x_janela=0, y_janela=0)
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
                time.sleep(2)
                return True
            elif escolha == "1":
                jj.atake(ee, x_janela=0, y_janela=17)
                acao_valida = True
            elif escolha == "2":
                acao_valida = jj.menu_magias(x_menu=x_jogador+32, y_menu=7, batalha=True)
            elif escolha == "3":
                acao_valida = jj.inventario_(x_inv=x_jogador+32, y_inv=0, batalha=True)
            else:
                with term.location(x=x_jogador+32, y=7):
                    print("Escolha inválida. Tente novamente.")
                time.sleep(2)
                continue            
            if acao_valida:
                if ee.hp <= 0:
                    with term.location(x=x_jogador+32, y=7):
                        print(term.clear_eol + f"{jj.nome} venceu a batalha!")
                    time.sleep(3)
                    jj.gold += ee.gold
                    jj.xp += ee.xp
                    jj.buff = 0
                    jj.add_xp(ee.xp)
                    return True
                ee.ataque_selec(jj, x_janela=31, y_janela=17)
                with term.location(x=x_jogador+32, y=7):
                    input(">")
                if jj.hp <= 0:
                    with term.location(x=x_jogador+32, y=7):
                        print(f"{ee.nome} venceu a batalha!")
                    time.sleep(3)
                    return False

def app():
    while True:
        clear()
        magem = "[1]Novo Jogo\n[2]Load\n[3]Sair"
        draw_window(term, x=0, y=0, width=25, height=6, text_content=magem)
        with term.location(x=1, y=4):
            escolha = input(">")
        if escolha =="1":
            with term.location(x=0, y=6):
                escolha_nome = input("Qual será seu Nome: maximo de 8 caracteres\n")
            if len(escolha_nome) > 8:
                with term.location(x=0, y=7):
                    print("Nome muito extenço use apenas 8 letras")
                time.sleep(2)
            elif len(escolha_nome) < 1:
                with term.location(x=0, y=7):
                    print("Utilize uma letra no minimo")
                time.sleep(2)
            else:
                with term.location(x=0, y=7):
                    print(f"Seu nome será {escolha_nome}")
                with term.location(x=0, y=8):
                    print("Escolha sua Classe")
                with term.location(x=0, y=9):
                    print("[1]Mago\n[2]Guerreiro")
                with term.location(x=0, y=11):
                    escolha_classe = input(">")
                if escolha_classe =="1":
                    jj.nome = escolha_nome
                    jj.art_player = ascii.mago
                    menu()
                elif escolha_classe == "2":
                    jj.nome = escolha_nome
                    jj.art_player = ascii.guerriro
                    menu()
        elif escolha == "2":
            jj.load_game(filename=f"Demo.json")
        elif escolha == "3":
            exit()
        
def menu():
    while True:
        clear()
        manager = "[1]Batalhar [2]Dormir\n[3]Loja     [4]Menu  \n[5]Sair"
        draw_window(term, x=0, y=0, width=25, height=6, text_content=manager)
        with term.location(x=1, y=4):
            escolha = input(">")
        if escolha == "1":
            batalha()
        elif escolha == "2":
            jj.hospital()
        elif escolha == "3":
            clear()
            jj.gerenciar_loja(x_pos=1, y_pos=1, herd=10, x_loq=0, y_loq=0)
        elif escolha == "4":
            jj.menu(x_janela=25, y_janela=0)
        elif escolha == "5":
            app()

app()