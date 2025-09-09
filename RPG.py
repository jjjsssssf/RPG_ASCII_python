import os 
import time
import random
import string
import sys
import json
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def linhas():
    print("<<"+"="*25+">>")
def linha_inven():
    print("++"+"/"*30+"++")
def linhas_batalha():
    print("##"+"-"*25+"##")
def linhas_jogo():
    print("xX"+"="*40+"Xx")

class art:
    def __init__(self):
        self.escudo = r"""
\__________/
 |   []   |
 |   []   |
 |   []   |
 \   []   /
  \  []  /
  
"""
        self.arco = r"""   (        
    \       
     )      
##--------> 
     )      
    /       
   (     """
        self.machado = r"""  ,  /\  .  
 //`-||-'\\ 
(| -=||=- |)
 \\,-||-.// 
  `  ||  '  
     ||     
     ||     
     ||     
     ||     
     ||     
     ()     """
        self.pao = r"""  ______
 (  '   )  
  |.  '| 
  |____|"""
        self.poção = r"""     ___
    [===]
   |~~~~~|
   |_____|"""
        self.Espada = r"""         />_________________________________
[########[]_________________________________>
         \>"""
        self.cajado = r"""    /I\
    \I/
    (I)
     I
     I
     I
     I
     I
     I
     O"""

        self.asmodeus = r"""⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀
⢠⠊⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠏⡄
⠈⡐⠡⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⡘⠄⠃
⠀⠐⣧⡐⢄⣴⠾⡟⠛⠛⢻⡳⣦⡀⠊⣜⠎⠀
⠀⠀⠘⣧⢆⡯⠀⠀⠀⠀⠀⠀⢜⡠⣹⠏⠀⠀
⠀⠀⢘⡙⡞⡇⠀⠀⠀⠀⠀⠀⢀⠑⠏⣵⠀⠀
⠀⠀⢰⡓⡄⠃⠀⢀⠀⠀⡀⠀⠈⢢⠇⡆⠀⠀
⠀⠀⠈⢰⠘⢍⣉⡹⡆⠀⣯⣉⡉⠅⡎⡇⠀⠀
⠀⠀⠈⡎⠣⠤⢒⠂⠀⠀⠁⣲⡤⠔⢱⠁⠀⠀
⠀⠀⠀⠑⣔⡴⣆⡝⠤⠤⢪⣵⣇⢢⠞⠀⠀⠀
⠀⠀⠀⠀⠈⢻⢿⡘⣓⣒⠏⡿⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢏⠚⠋⠉⠛⣱⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠉⠁⠀⠀⠀⠀⠀⠀        """
        self.esqueleto = r"""      ⣴⣾⣿⣿⣿⣿⣷⣦
      ⣿⣿⣿⣿⣿⣿⣿⣿
      ⡟⠛⠽⣿⣿⠯⠛⢻
      ⣧⣀⣀⡾⢷⣀⣀⣼
       ⡏⢽⢴⡦⡯⢹
       ⠙⢮⣙⣋⡵⠋"""
        self.minus = r""" ⠀⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⡟⣴⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣬⣿⣯⡇⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠿⣿⢿⣷⣟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⡇⠀⠈⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣇⠀⣀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⡛⠛⠛⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣠⣿⠼⠳⢯⣀⣀⠀        """
        self.lobo = r"""             _     ___
            #_~`--'__ `===-,
            `.`.     `#.,//
            ,_\_\     ## #\
            `__.__    `####\
                 ~~\ ,###'~
                    \##'"""
        self.vila = r"""  ~         ~~          __
       _T      .,,.    ~--~ ^^
 ^^   // \                    ~
      ][O]    ^^      ,-~ ~
   /''-I_I         _II____
__/_  /   \ ______/ ''   /'\_,__
  | II--'''' \,--:--..,_/,.-{ },
; '/__\,.--';|   |[] .-.| O{ _ }
:' |  | []  -|   ''--:.;[,.'\,/
'  |[]|,.--'' '',   ''-,.    |
  ..    ..-''    ;       ''. '        """
        self.farol = r""" . _  .    .__  .  .  __,--'                 
  (_)    ' /__\ __,--'                       
'  .  ' . '| o|'                             
          [IIII]`--.__                       
           |  |       `--.__                 
           | :|             `--.__           
           |  |                   `--.__     
._,,.-,.__.'__`.___.,.,.-..,_.,.,.,-._..`--.."""
        self.floresta = r"""
        /\ /\ /\ /\ /\ /\ /\ /\ /\
        /\ /\ /\ /\ /\ /\ /\ /\ /\
        /\ /\ /\ /\ /\ /\ /\ /\ /\
#### #  || || || || || || || || || #####
"""
        self.texto1 = r"""Contra Todo Mal Conjurado do Inferno 
todos Pecados e Perversidade da Humanidade
Nós enviaremos a eles você o unico que 
pode os Matar e os Punir"""
        self.missão_1 = r"""Vá até o centro de controle dos demonios
e mate o primeiro sacerdote infernal
o Nome dele é Asmodeus """
        self.texto2 = f"""Adam: vá na fortalesa de
Asmodeus e mate todos por lá e pegue
seu broche de imortalidade"""
        self.npc_1_vila = r"""Campones: Olá Viajante, estamos com um grande
problema, demônios estão atacando nossa vila
pode nos ajudar?"""
        self.demoni0 = r'''   ,    ,    /\   /\
  /( /\ )\  _\ \_/ /_
  |\_||_/| < \_   _/ >
  \______/  \|0   0|/
    _\/_   _(_  ^  _)_
   ( () ) /`\|V"""V|/`\
     {}   \  \_____/  /
     ()   /\   )=(   /\
    {}  /  \_/\=/\_/  \        '''
        self.demoni1 = r"""              v
        (__)v | v
        /\/\\_|_/
       _\__/  |
      /  \/`\<`)
      \ (  |\_/
      /)))-(  |
     / /^ ^ \ |
    /  )^/\^( |
    )_//`__>> |
      #   #`  |"""

    def exibir_texto_lento(self, texto, atraso=0.05):
        for caractere in texto:
            sys.stdout.write(caractere)
            sys.stdout.flush() 
            time.sleep(atraso)
        print("")
ascii = art()

class jogador:
    def __init__(self, nome, hp_max, atk, niv, xp_max, defesa, gold, stm_max, intt, mn_max, d_m, buff):
        self.nome = nome
        self.hp_max = hp_max
        self.hp = self.hp_max
        self.mana_max = mn_max
        self.mana = self.mana_max
        self.stm_max = stm_max
        self.stm = self.stm_max
        self.atk = atk
        self.intt = intt
        self.niv = niv
        self.xp_max = xp_max
        self.dano_magico = d_m
        self.xp = 100
        self.buff = buff
        self.defesa = defesa
        self.gold = gold
        self.rodar_jogo = False
        self.aleatorio = 75
        self.andar = 0
        self.inventario = ["Espada","Poção de Cura"]
        self.mana_lit = ["Cura", "Bola de Fogo", "Dança das Espada"]
        self.equipa = {
            "m_pri":None,
            "m_seg":None,
            "c_cap":None,
            "p_pet":None
        }
        self.map = {
            "Vila":None,
            "Farol":None,
            "Floresta":None,
        }
        self.itens_coletaodos = {
            "item_1":False,
            "item_2":False,
            "Farol":False,
            "Dentro_Farol":False,
        }
        self.missoes = {
           "Asmodeus":False,
           "Missão_1":None
        }
    
    def save_game(self, filename=f"Demo.json"):
        player_data = {
            "nome": self.nome,
            "hp_max": self.hp_max,
            "hp": self.hp,
            "atk": self.atk,
            "niv": self.niv,
            "xp_max": self.xp_max,
            "defesa": self.defesa,
            "gold": self.gold,
            "stm_max": self.stm_max,
            "stm": self.stm,
            "intt": self.intt,
            "mn_max": self.mana_max,
            "mana": self.mana,
            "d_m": self.dano_magico,
            "buff": self.buff,
            "xp": self.xp,
            "aleatorio": self.aleatorio,
            "inventario": self.inventario,
            "mana_lit": self.mana_lit,
            "equipa": self.equipa,
            "map": self.map,
            "itens_coletaodos": self.itens_coletaodos,
            "rodar": self.rodar_jogo
        }
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(player_data, f, indent=4)
            print(f"Jogo salvo com sucesso em '{filename}'!")
        except IOError as e:
            print(f"Erro ao salvar o jogo: {e}")
        time.sleep(1.5)

    @classmethod
    def load_game(cls, filename=f"Demo.json"):
        if not os.path.exists(filename):
            print(f"Nenhum arquivo de salvamento encontrado em '{filename}'. Iniciando novo jogo.")
            time.sleep(1.5)
            return None
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                player_data = json.load(f)
            player = cls(
                nome=player_data["nome"],
                hp_max=player_data["hp_max"],
                atk=player_data["atk"],
                niv=player_data["niv"],
                xp_max=player_data["xp_max"],
                defesa=player_data["defesa"],
                gold=player_data["gold"],
                stm_max=player_data["stm_max"],
                intt=player_data["intt"],
                mn_max=player_data["mn_max"],
                d_m=player_data["d_m"],
                buff=player_data["buff"]
            )
            player.hp = player_data["hp"]
            player.aleatorio = player_data["aleatorio"]
            player.inventario = player_data["inventario"]
            player.mana_lit = player_data["mana_lit"]
            player.equipa = player_data["equipa"]
            player.itens_coletaodos = player_data["itens_coletaodos"]
            player.map = player_data["map"]
            player.xp = player_data["xp"]
            player.mana = player_data["mana"]
            player.stm = player_data["stm"]
            player.rodar_jogo = player_data["rodar"]
            print(f"Jogo carregado com sucesso de '{filename}'!")
            return player
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Erro ao carregar o jogo: {e}. Iniciando novo jogo.")
            time.sleep(1.5)
            return None
    
    def menu(self):
        while True:
            clear()
            linhas()
            print("[1]Status    [2]Inventario\n[3]Magias    [4]Save\n[5][Missões  [6]Sair")
            linhas()
            escolha = input("=>")
            if escolha == "1":
                self.status()
            elif escolha == "2":
                self.inventario_()
            elif escolha == "3":
                self.magias_()
            elif escolha == "4":
                self.save_game(filename=f"{jj.nome}.json")
            elif escolha == "5":
                self.miss()
            elif escolha == "6":
                break
           
    def dormir(self):
        if self.hp > self.hp_max or self.stm > self.stm_max or self.mana > self.mana_max:
            print("Você dormil essa noite")
            self.hp = self.hp_max
            self.stm = self.stm_max
            self.mana = self.mana_max
            time.sleep(3)
        else:
            print("Você não precisa dormir")
        
    def miss(self):
        clear()
        if self.missoes["Asmodeus"] == False:
            linhas()
            print(ascii.missão_1)
            linhas()
            input()
            return
        if self.missoes["Missão_1"] == False:
            linhas()
            print("Derrote o Grande Demonio que atormenta a vila")
            linhas()
            input()
            return

    def status(self):
        linhas()
        print(f"Nome: {self.nome} Niv: [{self.niv}]")
        print(f"HP: [{self.hp_max}]/[{self.hp}]")
        print(f"ST: [{self.stm_max}]/[{self.stm}]")
        print(f"EN: [{self.mana_max}]/[{self.mana}]")
        print(f"ATK: [{self.atk}] DEF:[{self.defesa}]")
        print(f"Gold: [{self.gold}]")
        print(f"XP: [{self.xp_max}]/[{self.xp}]")
        linhas()
    
    def status_batalha(self):
        linhas_batalha()
        print(f"Nome: {self.nome} Niv: [{self.niv}]")
        print(f"HP:[{self.hp_max}]/[{self.hp}] ST:[{self.stm_max}]/[{self.stm}]")
        print(f"MN: [{self.mana_max}]/[{self.mana}] MA:[{self.dano_magico}]")
        print(f"ATK: [{self.atk}] DEF:[{self.defesa}]")
        print(f"Buff: [{self.buff}]")
        linhas_batalha()

    def add_xp(self):
        while True:
            if self.xp >= self.xp_max:
                print(f"Você subiu de nível!{self.niv}")            
                xp_remaining = self.xp - self.xp_max
                self.xp_max = int(self.xp_max * 1.2)
                self.xp = xp_remaining
                self.niv += 1
                self.hp_max += 10
                self.stm_max += 10
                self.mana_max += 10
                self.atk += 5
                self.dano_magico += 5
                self.defesa += 5
                self.hp = self.hp_max
                self.stm = self.stm_max
                self.mana = self.mana_max
                time.sleep(1)
            else:
                break

    def mana_(self):
        while True:
            clear()
            linha_inven()
            if not self.mana_lit:
                print("Não tem nada")
                input("=>")
                return False
            for i, item in enumerate(self.mana_lit):
                tipo = ""
                if item in ("Cura", "Fúria"):
                    tipo = "Suporte"
                if item in ("Lança Divina"):
                    tipo = "Ataque"
                print(f"[{i + 1}]{item}: {tipo}")
            linha_inven()
            print("Para usar uma magia digite o nome dela\npara sair digite sair")
            escolha = input("=>")
            if escolha == "Sair":
                return False
            if "Lança Divina" in self.mana_lit:
                if escolha == "Lança Divina":
                    if self.mana < 15:
                        print("Mana Insuficiente é nessesario 15 de mana")
                        time.sleep(3)
                    else:
                        print("Você quer usar a Magia Lança Divina [15/mana]\n[Sim] [Não]")
                        esc = input("=>").capitalize()
                        if esc == "Sim":
                            self.mana -= 15
                            dano_inteligente = int(self.intt // 4)
                            dano_final = dano_inteligente + self.dano_magico
                            ee.hp -= dano_final
                            print(f"{self.nome} usou Lança Divina em {ee.nome}\ne deu um dano de {dano_final}")
                            time.sleep(3)
                            return True  
                        elif esc == "Não":
                            pass
            if "Cura" in self.mana_lit:
                if escolha == "Cura":
                    if self.mana < 10:
                        print("Mana Insuficiente é nessesario 10 de mana")
                    else:
                        print("Você quer usar a Magia Cura [10/mana]\n[Sim] [Não]")
                        esc = input("=>").capitalize()
                        if esc == "Sim":
                            if self.hp >= self.hp_max:
                                self.mana -= 10
                                cura_inteligente = int(self.intt // 4)
                                cura_final = cura_inteligente + self.dano_magico
                                self.hp += cura_final
                                print(f"{self.nome} usou a Magia Cura e curou {cura_final}")
                                time.sleep(3)
                                return True  
                        elif esc == "Não":
                            pass
            if "Fúria" in self.mana_lit:
                if escolha == "Fúria":
                    if self.mana < 10:
                        print("Mana Insuficiente é nessesario 10 de mana")
                    else:
                        print("Você quer usar a Magia Fúria [10/mana]\n[Sim] [Não]")
                        esc = input("=>").capitalize()
                        if esc == "Sim":
                            print("Você Uso a Magia Fúria e seu ataque foi Buffado")
                            self.buff += 5
                            self.mana -= 10
                            time.sleep(3)
                            return True
                        elif esc == "Não":
                            pass

    def magias_(self):
        clear()
        linha_inven()
        if not self.mana_lit:
            print("Não tem nada")
            input("=>")
            return False
        for i, item in enumerate(self.mana_lit):
            tipo = ""
            if item in ("Cura", "Fúria"):
                tipo = "Suporte"
            if item in ("Granada"):
                tipo = "Ataque"
            print(f"[{i + 1}]{item}: {tipo}")
        linha_inven()

    def inventario_(self):
        while True:
            clear()
            linha_inven()
            contagem_itens = {}
            for item in self.inventario:
                contagem_itens[item] = contagem_itens.get(item, 0) + 1
            if not self.inventario:
                print("Não tem nada")
                input("=>")
                return
            for item, quantidade in contagem_itens.items():
                estado = ""
                tipo = ""
                if item in ("Poção", "Cura", "Pão"):
                    tipo = "Consumivel"
                if item in ("Espada", "Cajado", "Arco"):
                    tipo = "Equipavel"
                if self.equipa.get("m_pri") == item:
                    estado = "[Arma]"
                elif self.equipa.get("m_seg") == item:
                    estado = "[Suporte]"
                elif self.equipa.get("c_cap") == item:
                    estado = "[Cabeça]"
                elif self.equipa.get("p_pet") == item:
                    estado = "[Peitoral]"
                print(f"{item}: {tipo}/(x{quantidade}){estado}")
            linha_inven()
            print("Para usar um item digite o nome dele\npara sair digite sair")
            escolha = input("=>")
            if escolha == "Sair":
                print("Saindo do Inventario:")
                time.sleep(2)
                break
            if "Espada" in self.inventario:
                if escolha == "Espada":
                    print("Oque Você Deseja Fazer com a Espada")
                    print("[1]Equipar [2]Desequipar")
                    esc = input("=>")
                    if esc == "1":
                        if not self.equipa["m_pri"]:
                            print("Você Equipou uma Arma")
                            self.equipa["m_pri"] = "Espada"
                            self.atk += 10
                            time.sleep(2)
                        else:
                            print("Já tem alguma arma equipada")
                            time.sleep(2)
                    elif esc == "2":
                        if self.equipa["m_pri"]:
                            print("Desequipando Arma")
                            time.sleep(2)
                            self.equipa["m_pri"] = None
                            self.atk -= 10
                        else:
                            print("Não ah Nada equipado")
                            time.sleep(2)
            if "Poção de Cura" in self.inventario:
                if escolha == "Poção de Cura":
                    print("Você quer utilizar a Poção?")
                    print("[1]Sim [2]Não")
                    esc = input("=>")
                    if esc == "1":
                        if self.hp >= self.hp_max:
                            print("Você Não Pode Usar Seu HP em 100%")
                            time.sleep(2)
                        elif self.hp < self.hp_max:
                            print("Você Bebeu uma Poção")
                            self.hp += 20
                            self.inventario.remove("Poção")
                            if self.hp > self.hp_max:
                                self.hp = self.hp_max
                            time.sleep(2)
            if "Peitoral de Ferro" in self.inventario:
                if esc == "Peitoral de Ferro":
                    print("Oque Você Deseja Fazer com o Peitoral de Ferro")
                    print("[1]Equipar [2]Desequipar")
                    esc = input("=>")
                    if esc == "1":
                        if not self.equipa["p_pet"]:
                            print("Você Equipou um Peito")
                            self.equipa["p_pet"] = "Peitoral de Ferro"
                            self.defesa += 20
                            time.sleep(2)
                        else:
                            print("Já tem algum peito equipada")
                            time.sleep(2)
                    elif esc == "2":
                        if self.equipa["p_pet"]:
                            print("Desequipando Peito")
                            time.sleep(2)
                            self.equipa["p_pet"] = None
                            self.defesa -= 20
                        else:
                            print("Não ah Nada equipado")
                            time.sleep(2)
            if "Capacete de Colro" in self.inventario:
                if esc == "Capacete de Colro":
                    print("Oque Você Deseja Fazer com o Capacete de Colro")
                    print("[1]Equipar [2]Desequipar")
                    esc = input("=>")
                    if esc == "1":
                        if not self.equipa["c_cap"]:
                            print("Você Equipou um Capacete")
                            self.equipa["c_cap"] = "Capacete de Colro"
                            self.defesa += 10
                            time.sleep(2)
                        else:
                            print("Já tem algum capacete equipada")
                            time.sleep(2)
                    elif esc == "2":
                        if self.equipa["c_cap"]:
                            print("Desequipando Capacete")
                            time.sleep(2)
                            self.equipa["c_cap"] = None
                            self.dafesa -= 10
                        else:
                            print("Não ah Nada equipado")
                            time.sleep(2)
            if "Escudo" in self.inventario:
                if esc == "Escudo":
                    print("Oque Você Deseja Fazer com o Escudo")
                    print("[1]Equipar [2]Desequipar")
                    esc = input("=>")
                    if esc == "1":
                        if not self.equipa["m_seg"]:
                            print("Você Equipou um Escudo")
                            self.equipa["m_seg"] = "Escudo"
                            self.atk += 5
                            self.defesa += 5
                            time.sleep(2)
                        else:
                            print("Já tem algum suporte equipada")
                            time.sleep(2)
                    elif esc == "2":
                        if self.equipa["m_seg"]:
                            print("Desequipando Suporte")
                            time.sleep(2)
                            self.equipa["m_seg"] = None
                            self.atk -= 5
                            self.defesa -= 5
                        else:
                            print("Não ah Nada equipado")
                            time.sleep(2)

    def inventario_b(self):
        while True:
            clear()
            linha_inven()
            contagem_itens = {}
            for item in self.inventario:
                contagem_itens[item] = contagem_itens.get(item, 0) + 1
            if not self.inventario:
                print("Não tem nada")
                input("=>")
                return
            for item, quantidade in contagem_itens.items():
                estado = ""
                tipo = ""
                if item in ("Poção de Cura", "Cura", "Pão"):
                    tipo = "Consumivel em Batalha"
                if item in ("Espada", "Cajado", "Arco"):
                    tipo = "Não Utilizavel em Batalha"
                if self.equipa.get("m_pri") == item:
                    estado = "[Arma]"
                elif self.equipa.get("m_seg") == item:
                    estado = "[Suporte]"
                elif self.equipa.get("c_cap") == item:
                    estado = "[Cabeça]"
                elif self.equipa.get("p_pet") == item:
                    estado = "[Peitoral]"
                print(f"{item}:\n{tipo}/(x{quantidade}){estado}")
            linha_inven()
            print("Para usar um item digite o nome dele\npara sair digite sair")
            escolha = input("=>")
            if escolha == "Sair":
                print("Saindo do Inventario:")
                time.sleep(2)
                return False
            if "Poção de Cura" in self.inventario:
                if escolha == "Poção de Cura":
                    print("Você quer utilizar a Poção?")
                    print("[1]Sim [2]Não")
                    esc = input("=>")
                    if esc == "1":
                        if self.hp >= self.hp_max:
                            print("Você Não Pode Usar Seu HP em 100%")
                            time.sleep(2)
                            return False
                        elif self.hp < self.hp_max:
                            print("Você Bebeu uma Poção")
                            self.hp += 20
                            self.inventario.remove("Poção")
                            if self.hp > self.hp_max:
                                self.hp = self.hp_max
                                return True
                            time.sleep(2)
                    elif esc == "2":
                        pass
    
    def atake(self):
        atak_aleatorio = random.randint(1, 100)
        if self.stm >= 10:
            if self.aleatorio > atak_aleatorio:
                self.stm -= 10
                dano_ale = random.randint(int(self.atk - 3), int(self.atk + 3))
                meno_defsa = ee.defesa // 4
                dano_final = int(self.buff + dano_ale - meno_defsa)
                print(f"{self.nome} deu um dano de {dano_final} em {ee.nome}")
                ee.hp -= dano_final
                time.sleep(2)
            else:
                print(f"{self.nome} errou o ataque")
                time.sleep(2)
        else:
            print(f"Você não contem ST suficiente")
            time.sleep(2)

class inimigo:
    def __init__(self, nome, hp_max, atk, niv, xp, defesa, gold, art_ascii, atk1, atk2):
        self.nome = nome
        self.hp_max = hp_max
        self.hp = self.hp_max
        self.art_ascii = art_ascii
        self.atk = atk
        self.niv = niv
        self.xp = xp
        self.defesa = defesa
        self.gold = gold
        self.atk1 = atk1
        self.atk2 = atk2
        self.aleatorio_ = 50

    def status(self):
        print(f"{self.art_ascii}")
        linhas_batalha()
        print(f"Nome: {self.nome} Niv: [{self.niv}]")
        print(f"HP: [{self.hp_max}]/[{self.hp}]")
        print(f"ATK: [{self.atk}] DEF:[{self.defesa}]")
        print(f"Com: [{self.atk1}]/[{self.atk2}]")
        linhas_batalha()

    def ataque_1(self):
        atak_aleatorio = random.randint(1, 100)
        if self.aleatorio_ > atak_aleatorio:
            dano_ale = random.randint(int(self.atk - 3), int(self.atk + 3))
            meno_defsa = jj.defesa // 4
            dano_final = int(dano_ale - meno_defsa)
            print(f"{self.nome} usou {self.atk1} de {dano_final} em {jj.nome}")
            jj.hp -= dano_final
            time.sleep(2)
        else:
            print(f"{self.nome} errou o ataque")
            time.sleep(2)

    def ataque_2(self):
        atak_aleatorio = random.randint(1, 100)
        if self.aleatorio_ > atak_aleatorio:
            dano_ale = random.randint(int(self.atk - 3), int(self.atk + 3))
            meno_defsa = jj.defesa // 4
            dano_final = int(1.5 * dano_ale - meno_defsa)
            print(f"{self.nome} usou {self.atk2} de {dano_final} em {jj.nome}")
            jj.hp -= dano_final
            time.sleep(2)
        else:
            print(f"{self.nome} errou o ataque")
            time.sleep(2)

    def ataque_selec(self):
        atk = ["atk1", "atk2"]
        atk_ = random.choice(atk)
        atk = atk_
        if atk == "atk1":
            self.ataque_1()
        elif atk == "atk2":
            self.ataque_2()

ee = inimigo(nome="", hp_max=0, atk=0, niv=0, xp=0, defesa=0, gold=0, art_ascii="",atk1="",atk2="")
jj = jogador(nome="JJ", hp_max=1000, atk=1000, niv=1, xp_max=100, defesa=10, gold=10000, stm_max=100, intt=10, mn_max=100,d_m=20, buff=0)

def seleção_inimigo():
    if jj.niv <= 5 or jj.andar <= 5:
        hp_max = random.randint(50, 150)
        atk = random.randint(5, 20)
        niv = random.randint(1, 5)
        xp = random.randint(150, 300)
        defesa = random.randint(5, 20)
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
    global ee
    ee = seleção_inimigo()
    while True:
        clear()
        print("     << Batalha >>     ")
        print(f"{ee.status()}")
        print(f"{jj.status_batalha()}")
        print("[1] Atacar      [2] Execução")
        print("[3] Inventario  [4] Magias\n[5] Fugir")
        escolha = input("=>")
        acao_valida = False
        if escolha == "5":
            print("Você fugiu da batalha.")
            time.sleep(2)
            break
        elif escolha == "1":
            jj.atake()
            acao_valida = True
        elif escolha == "2":
            if ee.hp <= ee.hp_max * 0.2:
                print(f"{jj.nome} executou {ee.nome}!")
                xp_extra = ee.xp * 0.5
                dinheiro_extra = ee.gold * 0.5
                dinheiro = ee.gold + int(dinheiro_extra)
                xp = ee.xp + int(xp_extra)
                jj.gold += dinheiro
                jj.xp += xp
                ee.hp = 0
                time.sleep(3)
                acao_valida = True
            else:
                print(f"{ee.nome} ainda está forte demais para")
                time.sleep(3)
        elif escolha == "4":
            if jj.mana_():
                acao_valida = True
        elif escolha == "3":
            if jj.inventario_b():
                acao_valida = True
        else:
            print("Escolha inválida. Tente novamente.")
            time.sleep(2)
            continue            
        if acao_valida:
            if ee.hp <= 0:
                print(f"{jj.nome} venceu a batalha!")
                time.sleep(3)
                dinheiro = ee.gold
                xp = ee.xp
                jj.gold += dinheiro
                jj.xp += xp
                jj.buff = 0
                jj.add_xp()
                break
            print(f"É a vez de {ee.nome}!")
            ee.ataque_selec()
            time.sleep(2)
            if jj.hp <= 0:
                print(f"{ee.nome} venceu a batalha!")
                time.sleep(3)
                break

def batalha_boss(ee: inimigo):
    while True:
        clear()
        print("     << Batalha >>     ")
        print(f"{ee.status()}")
        print(f"{jj.status_batalha()}")
        print("[1] Atacar      [2] Execução")
        print("[3] Inventario  [4] Magias")
        escolha = input("=>")
        acao_valida = False
        if escolha == "1":
            jj.atake()
            acao_valida = True
        elif escolha == "2":
            if ee.hp <= ee.hp_max * 0.2:
                print(f"{jj.nome} executou {ee.nome}!")
                xp_extra = ee.xp * 0.5
                dinheiro_extra = ee.gold * 0.5
                dinheiro = ee.gold + int(dinheiro_extra)
                xp = ee.xp + int(xp_extra)
                jj.gold += dinheiro
                jj.xp += xp
                ee.hp = 0
                time.sleep(3)
                acao_valida = True
            else:
                print(f"{ee.nome} ainda está forte demais para")
                print(f"{ee.nome} ri da sua tentativa de execução")
                time.sleep(3)
        elif escolha == "4":
            if jj.mana_():
                acao_valida = True
        elif escolha == "3":
            if jj.inventario_b():
                acao_valida = True
        else:
            print("Escolha inválida. Tente novamente.")
            time.sleep(2)
            continue            
        if acao_valida:
            if ee.hp <= 0:
                print(f"{jj.nome} venceu a batalha!")
                time.sleep(3)
                dinheiro = ee.gold
                xp = ee.xp
                jj.gold += dinheiro
                jj.xp += xp
                jj.buff = 0
                jj.add_xp()
                break
            print(f"É a vez de {ee.nome}!")
            ee.ataque_selec()
            time.sleep(2)
            if jj.hp <= 0:
                print(f"{ee.nome} venceu a batalha!")
                time.sleep(3)
                break

def mercado(jj=jj):
    while True:
        clear()
        linhas()
        print("Bem-vindo ao Mercado!")
        print("[1]Comprar \n[2]Vender \n[3]Sair")
        linhas()
        escolha = input("=>")
        if escolha == "Menu":
            jj.menu()   
        if escolha == "1":
            while True:
                item_precos = {
                    "Poção de Cura": 100,
                    "Espada": 250,
                    "Capacete de Colro": 200,
                    "Peitoral de Ferro": 300,
                    "Escudo": 300,
                }
                clear()
                linhas()
                print("Itens Disponíveis para Compra:")
                for item, preco in item_precos.items():
                    print(f"{item}: {preco} Gold")
                linhas()
                print(f"Seu Gold: {jj.gold}")
                print("Digite o nome do item que deseja comprar ou 'Sair' para voltar:")
                escolha_compra = input("=>").strip()
                if escolha_compra.lower() == "sair":
                    break
                elif escolha_compra in item_precos:
                    preco_item = item_precos[escolha_compra]
                    if jj.gold >= preco_item:
                        jj.gold -= preco_item
                        jj.inventario.append(escolha_compra)
                        print(f"Você comprou {escolha_compra} por {preco_item} Gold.")
                    else:
                        print("Gold insuficiente para essa compra.")
                else:
                    print("Item inválido. Tente novamente.")
                time.sleep(2)
        elif escolha == "2":
            while True:
                item_precos_venda = {
                    "Poção de Cura": 50,
                    "Espada": 125,
                    "Capacete de Colro": 100,
                    "Peitoral de Ferro": 150,
                    "Escudo": 150,
                }
                clear()
                linhas()
                print("Itens Disponíveis para Venda:")
                contagem_itens = {}
                for item in jj.inventario:
                    contagem_itens[item] = contagem_itens.get(item, 0) + 1
                for item, quantidade in contagem_itens.items():
                    preco = item_precos_venda.get(item, 0)
                    if preco > 0:
                        print(f"{item} (x{quantidade}): {preco} Gold cada")
                linhas()
                print(f"Seu Gold: {jj.gold}")
                print("Digite o nome do item que deseja vender ou 'Sair' para voltar:")
                escolha_venda = input("=>").strip()
                if escolha_venda.lower() == "sair":
                    break
                elif escolha_venda in item_precos_venda and escolha_venda in jj.inventario:
                    preco_item = item_precos_venda[escolha_venda]
                    jj.gold += preco_item
                    jj.inventario.remove(escolha_venda)
                    print(f"Você vendeu {escolha_venda} por {preco_item} Gold.")
                else:
                    print("Item inválido ou não disponível para venda. Tente novamente.")
                time.sleep(2)   
        elif escolha == "3":
            print("Saindo do Mercado...")
            time.sleep(2)
            return 

def jogo():
    #clear()
    #linhas_jogo()
    #ascii.exibir_texto_lento(ascii.texto1, atraso=0.05)
    #linhas_jogo()
    #input("=>")
    #clear()
    #linhas_jogo()
    #ascii.exibir_texto_lento(ascii.texto2, atraso=0.05)
    #linhas_jogo()
    #input("=>")
    jj.rodar_jogo = True
    jj.map["Farol"] = True
    while jj.rodar_jogo:
        if jj.map["Vila"] == True:
            clear()
            linhas_jogo()
            print(f"Local: Vila{ascii.vila}")
            print("[Entrar] [Andar]\n[Conversar] [Explorar]")
            linhas_jogo()
            escolha = input("=>").capitalize()
            if escolha == "Menu":
                jj.menu()
            elif escolha == "Sair":
                exit()
            elif escolha == "Entrar":
                while True:
                    clear()
                    linhas_jogo()
                    print(f"Local: Vila{ascii.vila}")
                    print("[Mercado] [Dormir]\n[Conversar] [Sair]")
                    linhas_jogo()
                    esc = input("=>").capitalize()
                    if esc == "Menu":
                        jj.menu()
                    elif esc == "Mercados":
                        mercado(jj)
                    elif esc == "Dormir":
                        jj.dormir()
                    elif esc == "Conversar":
                        linhas_jogo()
                        ascii.exibir_texto_lento(ascii.npc_1_vila, atraso=0.05)
                        linhas_jogo()
                        jj.missoes['Missão_1'] = False
                    elif esc == "Sair":
                        print("Saindo da Vila...")
                        time.sleep(2)
                        break
            elif escolha == "Andar":
                print("Qual local você deseja ir?\n[Farol] [Floresta]")
                escolha = input("=>").capitalize()
                if escolha == "Farol":
                    jj.map["Vila"] = None
                    jj.map["Farol"] = True
                elif escolha == "Floresta": 
                    jj.map["Vila"] = None
                    jj.map["Floresta"] = True
            elif escolha == "Conversar":
                if jj.itens_coletaodos["item_2"] == False:
                    linhas_jogo()
                    print("Viajante: Olá, Rapaz os demonios estão indo para o farol")
                    print("Viajante: Se você for lá, tome cuidado")
                    print("Viajante: Aqui estás um Pão para te ajudar")
                    input("=>")
                    linhas_jogo()
                    jj.inventario.append("Pão")
                    jj.itens_coletaodos["item_2"] = True
                else:
                    print("Você não tem mais nada para conversar")
                    time.sleep(3)             
            elif escolha == "Explorar":
                if jj.itens_coletaodos["item_1"] == False:
                    print("Você encontrou uma Espada!")
                    jj.inventario.append("Espada")
                    jj.itens_coletaodos["item_1"] = True
                    time.sleep(3)
                else:
                    print("Você não encontrou nada")
                    time.sleep(3)
        elif jj.map["Farol"] == True:
            clear()
            linhas_jogo()
            print(f"Local: Farol{ascii.farol}")
            print("[Entrar] [Andar]\n[Ler] [Observar]")
            linhas_jogo()
            escolha = input("=>").capitalize()
            if escolha == "Menu":
                jj.menu()
            elif escolha == "Sair":
                exit()
            elif escolha == "Entrar":
                jj.map["Farol"] = None
                jj.map["Dentro_Farol"] = True
            elif escolha == "Andar":
                print("Qual local você deseja ir?\n[Vila] [Floresta]")
                escolha = input("=>").capitalize()
                if escolha == "Vila":
                    jj.map["Farol"] = None
                    jj.map["Vila"] = True
                elif escolha == "Floresta": 
                    jj.map["Farol"] = None
                    jj.map["Floresta"] = True
            elif escolha == "Ler":
                linhas_jogo()
                placa = """Placa: Cuidado com os Demonios que estão no Farol!"""
                ascii.exibir_texto_lento(placa, atraso=0.2)
                linhas_jogo()
                input("=>")
            elif escolha == "Observar":
                linhas_jogo()
                observação = """Você observa o farol, notando que está em ruínas e parece abandonado há muito tempo.\nTriste pensar que um lugar que antes guiava os navegantes agora está tomado por criaturas sombrias."""
                ascii.exibir_texto_lento(observação, atraso=0.2)
                linhas_jogo()
                input("=>")
        elif jj.map["Dentro_Farol"] == True:
            jj.andar = 9
            while True:
                clear()
                linhas_jogo()
                print(f"Andar: {jj.andar}")
                print(f"Local: Farol{ascii.farol}")
                print("[Subir] [Sair]\n[Dormir] [Explorar]")
                linhas_jogo()
                esc = input("=>").capitalize()
                if esc == "Menu":
                    jj.menu()
                elif esc == "Subir":
                    batalha_aleatoria = random.randint(1, 100)
                    if batalha_aleatoria <= 50:
                        batalha()
                        if jj.hp >= 1:
                            print("Você subiou um andar do farol com sucesso")
                            time.sleep(3)
                            jj.andar += 1
                            jj.itens_coletaodos["Farol"] = False
                        if jj.andar > 10:
                            print("Você já está no ultimo andar do farol")
                            time.sleep(3)
                            jj.andar = 10

                        if jj.andar == 5:
                            clear()
                            fala_de_adam = '''Adam: O Senhor está a alguns andares abaixo, de Asmodeus
Eu estou detectando um estranha presença de um poder muito grande
pelo visto é o campeão do Asmodeus o nome dele é Minus'''
                            linhas_jogo()
                            ascii.exibir_texto_lento(fala_de_adam, atraso=0.05)
                            linhas_jogo()
                            input("=>")
                            clear()
                            fala_de_minus = f'''Minus: Então você é o campeão que foi enviado para
deter todo inferno hahaha, pesei que fosse mais alto
{jj.nome}: ...
Minus: Vamos ver se você é forte o suficiente para me derrotar'''
                            linhas_jogo()
                            ascii.exibir_texto_lento(fala_de_minus, atraso=0.05)
                            linhas_jogo()
                            input("=>")
                            boss_minus = inimigo(nome="Minus", hp_max=500, atk=35, niv=15, xp=1000, defesa=30, gold=1000, art_ascii=ascii.minus, atk1="Corte Sombrio", atk2="Explosão das Trevas")
                            batalha_boss(boss_minus)
                            if jj.hp >= 1:
                                clear()
                                fala_de_adam_vitoria = f'''Adam: Minus derrotada a porta para o proximo andar está aberta'''
                                linhas_jogo()
                                ascii.exibir_texto_lento(fala_de_adam_vitoria, atraso=0.01)
                                linhas_jogo()
                                input("=>")
                                jj.andar += 1
                                jj.itens_coletaodos["Farol"] = False
                        if jj.andar == 10:
                            fala_de_adam_final = f'''Adam: Senhor {jj.nome} você chegou ao andar de asmodeus
eu estou detectando uma presença dele ele está muito perto'''
                            clear()
                            linhas_jogo()
                            ascii.exibir_texto_lento(fala_de_adam_final, atraso=0.01)
                            linhas_jogo()
                            input("=>")
                            asmodeus = inimigo(nome="Asmodeus", hp_max=1000, atk=50, niv=20, xp=2000, defesa=50, gold=5000, art_ascii=ascii.asmodeus, atk1="Chamas do Inferno", atk2="Golpe do Abismo")
                            batalha_boss(asmodeus)
                            
                    else:
                        print("Você subiu um andar do farol com sucesso")
                        time.sleep(3)
                        jj.andar += 1
                elif esc == "Sair":
                    print("Saindo do Farol...")
                    time.sleep(2)
                    break
                elif esc == "Dormir":
                    jj.dormir()
                elif esc == "Explorar":
                    if jj.itens_coletaodos["Farol"] == True:
                        print("Você já explorou esse andar")
                        time.sleep(3)
                    else:
                        item_aleatorio = random.randint(1, 100)
                        if item_aleatorio <= 30:
                            item_coletaveis = ["Poção de Cura", "Cura", "Pão"]
                            item_encontrado = random.choice(item_coletaveis)
                            print(f"Você encontrou um(a) {item_encontrado}!")
                            jj.inventario.append(item_encontrado)
                            time.sleep(3)
                        else:
                            print("Você não encontrou nada.")
                            time.sleep(3)

jogo()

jj = None

def menu():
    global jj
    while jj is None:
        clear()
        print(("<<" + "#" * 15 + ">>"))
        print("[1] Novo Jogo")
        print("[2] Carregar Jogo")
        print("[3] Sair")
        print("<<" + "#" * 15 + ">>")
        initial_choice = input("Escolha uma opção: ")
        nome_aceito = False
        if initial_choice == '1':
                while True:
                    clear()
                    linhas()
                    print("Escolha um Nome para seu Personegem:\nUse apenas 8 letras")
                    linhas()
                    nome_ = input("=>")
                    if not nome_.strip() or len(nome_) > 8:
                        print("Use letras para dar nome ao seu Personagem")
                        time.sleep(3)
                    else:
                        nome_aceito = True
                    
                    if nome_aceito == True:
                        jj = jogador(nome=nome_, hp_max=100, atk=100, niv=1, xp_max=100, defesa=10, gold=0, stm_max=100, intt=10, mn_max=100, d_m=20, buff=0)
                        print(f"Bem-vindo, {jj.nome}")
                        jj.save_game(filename=f"{jj.nome}.json")
                        time.sleep(1.5)
                        break
        elif initial_choice == '2':
            player_name_to_load = input("Qual o Save que deseja carregar\n(digite o nome do personagem) ")
            file_to_load = f"{player_name_to_load}.json"
            loaded_player = jogador.load_game(filename=file_to_load)
            if loaded_player:
                jj = loaded_player
                print(f"Bem-vindo de volta, {jj.nome}!")
            else:
                print("Não foi possível carregar o jogo. Por favor, tente novamente ou inicie um Novo Jogo.")
                time.sleep(2)
        elif initial_choice == '3':
            print("Saindo do jogo... Até mais!")
            exit()
        else:
            print("Opção inválida. Por favor, escolha novamente.")
            time.sleep(1.5)
        clear()
        jj.rodar_jogo = True
        jogo()
        

