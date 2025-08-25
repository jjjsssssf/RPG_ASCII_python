import os
import time
import random
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def linhas():
    print("X","="*25,"X")
def linhas_2():
    print("<"+"-="*25+">")

class arts:
    def __init__(self):
        self.fazenda = r"""
                   x
        .-. _______|
        |=|/     /  \
        | |_____|_""_|
  |=|=|=|_|_[X]_|____|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ """
        self.farol = r""" . _  .    .__  .  .  __,--'                 
  (_)    ' /__\ __,--'                       
'  .  ' . '| o|'                             
          [IIII]`--.__                       
           |  |       `--.__                 
           | :|             `--.__           
           |  |                   `--.__     
._,,.-,.__.'__`.___.,.,.-..,_.,.,.,-._..`--.."""
        self.livro = r"""         ,..........   ..........,         
     ,..,'          '.'          ',..,     
    ,' ,'            :            ', ',    
   ,' ,'             :             ', ',   
  ,' ,'              :              ', ',  
 ,' ,'............., : ,.............', ', 
,'  '............   '.'   ............'  ',
 '''''''''''''''''';''';'''''''''''''''''' 
                    '''                     """
        self.cigarro = r'''                   (  )/  
                    )(/
 ________________  ( /)
()__)____________)))))   '''

class jogador:
    def __init__(self):
        self.nome = "JJ"
        self.hp_max = 100
        self.hp = self.hp_max
        self.stm_max = 50
        self.stm = self.stm_max
        self.san_max = 100
        self.san = self.san_max
        self.atk = 10
        self.x = 1
        self.y = 1
        self.jogo = True
        self.dfs = 10
        self.dias = 0
        self.crit = 500
        self.gold = 0
        self.xp_max = 100
        self.xp = 0
        self.nivel = 1
        self.equipados = {
            "Peitoral":None,
            "Arma":None,
            "Protetor":None
        }
        self.comidas = ["Ovo Cru"]
        self.inventario = ["Peitoral","Camisa","Espada","Escudo","Cura"]
    
    def fumar(self):
        if self.hp < 15:
            print("Você não pode fumar")
            time.sleep(2)
        else:
            clear()
            linhas_2()
            print(ascii.cigarro)
            print("Você descide fumar e apenas vê os barcos")
            linhas_2()
            time.sleep(5)
            self.hp -= 15
            self.san += 5
            if self.san > self.san_max:
                self.san = self.san_max

    def ler(self):
        clear()
        linhas_2()
        print(ascii.livro)
        print("Você começou a ler o livro")
        linhas_2()
        time.sleep(5)
        self.san += 10
        if self.san > self.san_max:
            self.san = self.san_max
        
    def dormir(self):
        print("Você descide dormir e se deita na cama")
        self.hp = self.hp_max
        self.stm = self.stm_max
        self.san = self.san_max
        time.sleep(2)

    def cozinhar(self):
        while True:
            clear()
            linhas()
            if not self.comidas:
                print("Inventário Vazio")
                time.sleep(1)
                return
            print("     <=== Comidas ===>")
            for i, item in enumerate(self.comidas):
                print(f"[{i + 1}] {item}")
            linhas()
            print("[1]Cozinhar [2]Sair")
            escolha = input("=>").capitalize()
            if escolha == "Sair":
                print("saindo do fogão")
                time.sleep(2)
                break
            elif escolha == "Cozinhar":
                linhas_2()
                print("Escolhar um comida crua para cozinhar")
                print("[1]Ovo Frito [2]Carne Grelhada\n[3]Arroz cozido")
                linhas_2()
                print("Digite o número da comida")
                linhas_2()
                cozinhar = input("=>").capitalize()
                if cozinhar == "1":
                    if "Ovo Cru" in self.comidas:
                        print("Fritando o Ovo...")
                        time.sleep(3)
                        print("Ovo frito pronto")
                        self.inventario.append("Ovo Frito")
                    else:
                        print("Você não tem Ovo cru")
                        time.sleep(2)

    def menu(self):
        clear()
        linhas()
        print(f"Nome: {self.nome} Dias: [{self.dias}]")
        print(f"HP:  [{self.hp_max}]/[{self.hp}]")
        print(f"STM: [{self.stm_max}]/[{self.stm}]")
        print(f"ATK: [{self.atk}] DEF: [{self.dfs}]")
        print(f"Dinheiro: [{self.gold}]")
        print(f"Nivel: [{self.nivel}] XP:[{self.xp_max}]/[{self.xp}]")
        linhas()
        print("[1] Inventario /[2] sair")
        esc = input("=>")
        if esc == "1":
            self.usar_inventario()

    def add_xp(self):
        while True:
            if self.xp >= self.xp_max:
                print(f"Você subiu de nível!{self.nivel}")            
                xp_remaining = self.xp - self.xp_max
                self.xp_max = int(self.xp_max * 1.2)
                self.xp = xp_remaining
                self.nivel += 1
                self.hp_max += 10
                self.stm_max += 10
                self.atk += 5
                self.dfs += 5
                self.hp += 10 
                self.stm += 10
                time.sleep(1)
            else:
                break

    def atake(self):
        atak_aleatorio = random.randint(1, 100)
        if self.stm >= 10:
            if self.crit > atak_aleatorio:
                self.stm -= 10
                dano_ale = random.randint(int(self.atk - 3), int(self.atk + 3))
                meno_defsa = ii.dfs // 4
                dano_final = dano_ale - meno_defsa
                print(f"{self.nome} deu um dano de {dano_final}")
                ii.hp -= dano_final
                time.sleep(2)
            else:
                print(f"{self.nome} errou o ataque")
                time.sleep(2)
        else:
            print(f"Você não contem STM suficiente")
            time.sleep(2)

    def menu_batalha(self):
        print(f"Nome: {self.nome} Nivel: [{self.nivel}]")
        print(f"HP: [{self.hp_max}]/[{self.hp}]")
        print(f"STM: [{self.stm_max}]/[{self.stm}]")
        print(f"ATK: [{self.atk}]")
        print(f"DEF: [{self.dfs}]")

    def usar_inventario(self):
        while True:
            clear()
            linhas()
            if not self.inventario:
                print("Inventário Vazio")
                time.sleep(1)
                return
            print("--- Inventário ---")
            for i, item in enumerate(self.inventario):
                status = ""
                if item == self.equipados["Peitoral"]:
                    status = "(Equipado)"
                elif item == self.equipados["Arma"]:
                    status = "(Equipado)"
                elif item == self.equipados["Protetor"]:
                    status = "(Equipado)"
                print(f"[{i + 1}] {item} {status}")
            linhas()
            escolha = input("=>").capitalize()
            if escolha == "Sair":
                self.menu()
            elif escolha == "Peitoral":
                if "Peitoral" in self.inventario:
                    print("Você quer equipar ou desequipar o Peitoral?")
                    esc = input("=>").capitalize()
                    if esc == "Equipar":
                        if not self.equipados["Peitoral"]:
                            print("Você está equipando o Peitoral")
                            self.equipados["Peitoral"] = "Peitoral"
                            self.hp_max += 10
                            time.sleep(1)
                        else:
                            print(f"Você já tem um item equipado: {self.equipados['Peitoral']}!")
                            time.sleep(1)
                    elif esc == "Desequipar":
                        if self.equipados["Peitoral"] == "Peitoral":
                            print("Você Desequipou seu Peitoral")
                            self.equipados["Peitoral"] = None
                            self.hp_max -= 10
                            time.sleep(1.5)
                        else:
                            print("Não há Peitoral equipado.")
                            time.sleep(1)

            elif escolha == "Camisa":
                if "Camisa" in self.inventario:
                    print("Você quer equipar ou desequipar a Camisa?")
                    esc = input("=>").capitalize()
                    if esc == "Equipar":
                        if not self.equipados["Peitoral"]:
                            print("Você está equipando a Camisa")
                            self.equipados["Peitoral"] = "Camisa"
                            self.hp_max = 5
                            time.sleep(1)
                        else:
                            print(f"Você já tem um item equipado: {self.equipados['Peitoral']}!")
                            time.sleep(1)
                    elif esc == "Desequipar":
                        if self.equipados["Peitoral"] == "Camisa":
                            print("Você Desequipou a Camisa")
                            self.equipados["Peitoral"] = None
                            self.hp_max -= 5
                            time.sleep(1)
                        else:
                            print("Não há Camisa equipada.")
                            time.sleep(1)    

            elif escolha == "Espada":
                if "Espada" in self.inventario:
                    print("Você quer equipar ou desequipar a Espada?")
                    esc = input("=>").capitalize()
                    if esc == "Equipar":
                        if not self.equipados["Arma"]:
                            print("Você está equipando a Espada")
                            self.equipados["Arma"] = "Espada"
                            self.atk += 10
                            time.sleep(1)
                        else:
                            print(f"Você já tem um item equipado: {self.equipados['Arma']}!")
                            time.sleep(1)
                    elif esc == "Desequipar":
                        if self.equipados["Arma"] == "Espada":
                            print("Você Desequipou a Espada")
                            self.equipados["Arma"] = None
                            self.atk -= 10
                            time.sleep(1)
                        else:
                            print("Não há Espada equipada.")
                            time.sleep(1)

            elif escolha == "Escudo":
                if "Escudo" in self.inventario:
                    print("Você quer equipar ou desequipar o Escudo?")
                    esc = input("=>").capitalize()
                    if esc == "Equipar":
                        if not self.equipados["Protetor"]:
                            print("Você está equipando o Escudo")
                            self.equipados["Protetor"] = "Escudo"
                            self.dfs += 5
                            time.sleep(1)
                        else:
                            print(f"Você já tem um item equipado: {self.equipados['Arma']}!")
                            time.sleep(1)
                    elif esc == "Desequipar":
                        if self.equipados["Protetor"] == "Escudo":
                            print("Você Desequipou o Escudo")
                            self.equipados["Protetor"] = None
                            self.dfs -= 5
                            time.sleep(1)
                        else:
                            print("Não há Escudo equipada.")
                            time.sleep(1)

            elif escolha == "Cura":
                if "Cura" in self.inventario:
                    print("Você que usar a Cura? (Sim/Não)")
                    esc = input("=>").capitalize()
                    if esc == "Sim":
                        if self.hp == self.hp_max:
                            print("Sua vida está completa não presisa se curar")
                            time.sleep(1.5)
                        else:
                            print("Você usou a Cura e recuperou sua vida")
                            self.inventario.remove("Cura")
                            self.hp += 20
                            time.sleep(1.5)
                            if self.hp > self.hp_max:
                                self.hp = self.hp_max
                        
                    elif esc == "Não":
                        return

            elif escolha == "Ovo frito":
                if "Ovo Frito" in self.inventario:
                    print("Você quer Comer o Ovo Frito? (Sim/Não)")
                    esc = input("=>").capitalize()
                    if esc == "Sim":
                        if self.hp == self.hp_max:
                            print("Sua vida está completa não presisa comer")
                            time.sleep(1.5)
                        else:
                            print("Você comeu o Ovo Frito e recuperou sua vida")
                            self.inventario.remove("Ovo Frito")
                            self.hp += 20
                            time.sleep(1.5)
                            if self.hp > self.hp_max:
                                self.hp = self.hp_max
                    elif esc == "Não":
                        return

class inimigo:
    def __init__(self, nome, hp, atk, dfs, nivel, gold, xp):
        self.nome = nome
        self.gold = gold
        self.hp_max = hp
        self.hp = self.hp_max
        self.atk = atk
        self.dfs = dfs
        self.crit = 50
        self.xp = xp
        self.nivel = nivel
    def atake(self):
        atak_aleatorio = random.randint(1, 100)
        if self.crit > atak_aleatorio:
            dano_ale = random.randint(int(self.atk - 3), int(self.atk + 3))
            meno_defsa = pp.dfs // 4
            dano_final = dano_ale - meno_defsa
            print(f"{self.nome} deu um dano de {dano_final}")
            time.sleep(2)
            pp.hp -= dano_final
        else:
            print(f"{self.nome} errou o ataque")
            time.sleep(2)
    def menu_batalha(self):
        print(f"Nome: {self.nome} Nivel: [{self.nivel}]")
        print(f"HP: [{self.hp_max}]/[{self.hp}]")
        print(f"ATK: [{self.atk}]")
        print(f"DEF: [{self.dfs}]")

ascii = arts()
pp = jogador()
ii = inimigo(nome="aa", hp=100, atk=5, dfs=10, nivel=2, gold=10, xp=100)
def batalha():
    while True:
        clear()
        print("     <=== Batalha ===>")
        pp.menu_batalha()
        print("<-=-=-=-=-=-=-=-=-=-=-=-=->")
        ii.menu_batalha()
        print("<-=-=-=-=-=-=-=-=-=-=-=-=->")
        print("[1]Atacar")
        print("[2]Sair")
        esc = input("=>").capitalize()
        if esc == "Atacar" or esc == "1":
            pp.atake()
            if ii.hp <= 0:
                print(f"{pp.nome} ganhou a batalhas")
                pp.gold += ii.gold
                pp.xp += ii.xp
                pp.add_xp()
                print(f"Você ganhou {ii.gold} de dinheiro")
                time.sleep(3)
            ii.atake()
            if pp.hp <= 0:
                print(f"Você perdeu")
                time.sleep(2)
                exit()
        elif esc == "Sair" or esc == "2":
            print("Saindo da Batalha")
            time.sleep(2)
            break
        else:
            print("Erro de Digitação")
            time.sleep(2)

def jogo():
    while pp.jogo:
        if pp.x == 1 and pp.y == 1:
            clear()
            linhas_2()
            print("Local: Farol")
            print(f"{ascii.farol}")
            linhas_2()
            print("[1]Andar  [2]Entrar")
            print("[3]Observar")
            linhas_2()
            esc = input("=>").capitalize()
            if esc == "Menu":
                pp.menu()
            elif esc == "Andar" or esc == "1":
                print("Ir para Floresta ou Vila:")
                andar = input("=>").capitalize()
                if andar == "Floresta":
                    pp.x = 1
                    pp.y = 2
                elif andar == "Vila":
                    pp.x = 2
                    pp.y = 1
                else:
                    pass
            elif esc == "Entra" or esc == "2":
                while True:
                    clear()
                    linhas_2()
                    print("Local: Dentro do Farol")
                    print(f"{ascii.farol}")
                    linhas_2()
                    print("[1]Dormir [2]Cozinhar")
                    print("[3]Ler    [4]Fumar\n[5]Sair")
                    linhas_2()
                    esc = input("=>").capitalize()
                    if esc == "Menu":
                        pp.menu()
                    elif esc == "Dormir" or esc == "1":
                        pp.dormir()
                    elif esc == "Cozinhar" or esc == "2":
                        pp.cozinhar()
                    elif esc == "Ler" or esc == "3":
                        pp.ler()
                    elif esc == "Fumer" or esc == "4":
                        pp.fumar()
                    elif esc == "Sair" or esc == "5":
                        print("Você Saio do Farol")
                        time.sleep(2)
                        break

jogo()