import os 
import time
import random
import string
import json
def clear():
    os.system("clear")
def linhas():
    print("<<"+"="*25+">>")
def linha_inven():
    print("++"+"/"*30+"++")
def linhas_batalha():
    print("##"+"-"*25+"##")
def linhas_jogo():
    print("xX"+"="*30+"Xx")

    

class art:
    def __init__(self):
        self.esqueleto = r"""      ⣴⣾⣿⣿⣿⣿⣷⣦
      ⣿⣿⣿⣿⣿⣿⣿⣿
      ⡟⠛⠽⣿⣿⠯⠛⢻
      ⣧⣀⣀⡾⢷⣀⣀⣼
       ⡏⢽⢴⡦⡯⢹
       ⠙⢮⣙⣋⡵⠋"""
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
        self.floresta = r"""
        /\ /\ /\ /\ /\ /\ /\ /\ /\
        /\ /\ /\ /\ /\ /\ /\ /\ /\
        /\ /\ /\ /\ /\ /\ /\ /\ /\
#### #  || || || || || || || || || #####
"""

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
        self.rodar_jogo = True
        self.aleatorio = 75
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
            "Floresta":None
        }
        self.itens_coletaodos = {
            "item":None
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
        clear()
        linhas()
        print("[1]Status    [2]Inventario\n[3]Magias    [4]Save\n[5]Sair")
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
            return

    def status(self):
        linhas()
        print(f"Nome: {self.nome} Niv: [{self.niv}]")
        print(f"HP: [{self.hp_max}]/[{self.hp}]")
        print(f"ST: [{self.stm_max}]/[{self.stm}]")
        print(f"MN: [{self.mana_max}]/[{self.mana}]")
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
                if item in ("Cura", "Dança das Espada"):
                    tipo = "Suporte"
                if item in ("Bola de Fogo"):
                    tipo = "Ataque"
                print(f"[{i + 1}]{item}: {tipo}")
            linha_inven()
            print("Para usar uma magia digite o nome dela\npara sair digite sair")
            escolha = input("=>")
            if escolha == "Sair":
                return False
            if "Bola de Fogo" in self.mana_lit:
                if escolha == "Bola de Fogo":
                    if self.mana < 15:
                        print("Mana Insuficiente é nessesario 15 de mana")
                        time.sleep(3)
                    else:
                        print("Você quer usar a Magia Bola de Fogo [15/mana]\n[Sim] [Não]")
                        esc = input("=>").capitalize()
                        if esc == "Sim":
                            self.mana -= 15
                            dano_inteligente = int(self.intt // 4)
                            dano_final = dano_inteligente + self.dano_magico
                            ee.hp -= dano_final
                            print(f"{self.nome} usou Bola de Fogo em {ee.nome}\ne deu um dano de {dano_final}")
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
            if "Dança das Espadas" in self.mana_lit:
                if escolha == "Dança das Espadas":
                    if self.mana < 10:
                        print("Mana Insuficiente é nessesario 10 de mana")
                    else:
                        print("Você quer usar a Magia Dança das Espadas [10/mana]\n[Sim] [Não]")
                        esc = input("=>").capitalize()
                        if esc == "Sim":
                            print("Você Uso a Magia Dança das Espadas e seu ataque foi Buffado")
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
            if item in ("Cura", "Dança das Espada"):
                tipo = "Suporte"
            if item in ("Bola de Fogo"):
                tipo = "Ataque"
            print(f"[{i + 1}]{item}: {tipo}")
        linha_inven()

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

    def aleatorio(self):
        if jj.niv >= 1:
            nome = ["Esqueleto", "Lobo"]
            nome_ = random.choice(nome)
            nome = nome_
            self.nome = nome_
            atk_ = random.randint(5, 15)
            self.atk = atk_
            def_ = random.randint(5, 15)
            self.defesa = def_
            hp_ = random.randint(25, 150)
            self.hp = hp_
            self.hp_max = hp_
            xp_ = random.randint(1, 100)
            self.xp = xp_
            gold_ = random.randint(1, 50)
            self.gold = gold_
            niv_ = random.randint(1, 5)
            self.niv = niv_
            if nome == "Esqueleto":
                self.atk1 = "Ossada"
                self.atk2 = "Soco"
                self.art_ascii = ascii.esqueleto
            elif nome == "Lobo":
                self.atk1 = "Aranhar"
                self.atk2 = "Mordida"
                self.art_ascii = ascii.lobo

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
jj = jogador(nome="JJ", hp_max=100, atk=100, niv=1, xp_max=100, defesa=10, gold=0, stm_max=100, intt=10, mn_max=100,d_m=20, buff=0)
ascii = art()
jj = None
def batalha():
    ee.aleatorio()
    while True:
        clear()
        print("     << Batalha >>     ")
        print(f"{ee.status()}{jj.status_batalha()}")
        print("[1] Atacar      [2] Magia")
        print("[3] Inventario  [4] Sair")
        escolha = input("=>")
        acao_valida = False
        if escolha == "4":
            print("Você fugiu da batalha.")
            time.sleep(2)
            break
        elif escolha == "1":
            jj.atake()
            acao_valida = True
        elif escolha == "2":
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
            print(f"\nÉ a vez de {ee.nome}!")
            ee.ataque_selec()
            time.sleep(2)
            if jj.hp <= 0:
                print(f"{ee.nome} venceu a batalha!")
                time.sleep(3)
                break

def jogo():
    global jj
    jj.map["Vila"] = True
    while jj.rodar_jogo:
        if jj.map["Vila"] == True:
            clear()
            linhas_jogo()
            print(f"Local: Vila\n{ascii.vila}")
            linhas_jogo()
            print("[1]Andar [2]Entrar")
            escolha = input("=>").capitalize()
            if escolha == "Menu":
                jj.menu()
            elif escolha == "Andar" or escolha == "1":
                print("Digite o Local que deseja ir\n[Farol] [Floresta]")
                esc = input("=>").capitalize()
                if esc == "Farol":
                    jj.map["Farol"] = True
                    jj.map["Vila"] = None
                elif esc == "Floresta":
                    jj.map["Floresta"] = True
                    jj.map["Vila"] = None
            elif escolha == "Entrar" or escolha == "2":
                while True:
                    clear()
                    linhas_jogo()
                    print(f"Local: Vila\n{ascii.vila}")
                    linhas_jogo()
                    print("[1]Mercado [2]Hospital\n[Sair]")
                    esc = input("=>")
        elif jj.map["Floresta"] == True:
            clear()
            linhas_jogo()
            print(f"Local: Vila\n{ascii.floresta}")
            linhas_jogo()
            print("[1]Andar [2]Batalha")
            escolha = input("=>").capitalize()
            if escolha == "1":
                batalha()



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
        if initial_choice == '1':
                while True:
                    clear()
                    linhas()
                    print("Escolha um Nome para seu Personegem:\nUse apenas 8 letras")
                    linhas()
                    nome_ = input("=>")
                    if not nome_.strip():
                        print("Use letras para dar nome ao seu Personagem")
                        time.sleep(3)
                    if len(nome_) > 8:
                        print("Nome com mais de oito caracteres")
                        time.sleep(3)
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
    while True:
        clear()
        jogo()
menu()