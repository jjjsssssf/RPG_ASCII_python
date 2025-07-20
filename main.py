import os
import json
import sys
from rich.console import Console
from rich.text import Text
import time
import random
from collections import Counter

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
console = Console()

class art:
    def __init__(self):
        self.lobo = r"""[bold white]        _
       / \      _-'
     _/|  \-''- _ /
__-' { |          \
    /             \
    /       "o.  |o }
    |            \ ;
                  ',
       \_         __\
         ''-_    \.//
           / '-____'
          /
        _'
      _-' """
        self.dragon = '''[bold white]
                  ______________                               
            ,===:'.,            `-._                           
          `:.`---.__         `-._                       
              `:.     `--.         `.                     
                 \.        `.         `.                   
         (,,(,    \.         `.   ____,-`.,                
      (,'     `/   \.   ,--.___`.'                         
  ,  ,'  ,--.  `,   \.;'         `                         
   `{D, {    \  :    \;                                    
     V,,'    /  /    //                                    
     j;;    /  ,' ,-//.    ,---.      ,                    
     \;'   /  ,' /  _  \  /  _  \   ,'/                    
           \   `'  / \  `'  / \  `.' /                     
            `.___,'   `.__,'   `.__,'         
'''
        self.esqueleto = '''[bold white]           ______
        .-"      "-.
       /            \\
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`[/bold white]'''
        self.vila = r"""
~         ~~          __        
       _T      .,,.    ~--~ ^^  
 ^^   // \                    ~ 
      ][O]    ^^      ,-~ ~     
   /''-I_I         _II____      
__/_  /   \ ______/ ''   /'\_,__
  | II--'''' \,--:--..,_/,.-{ },
; '/__\,.--';|   |[] .-.| O{ _ }
:' |  | []  -|   ''--:.;[,.'\,/ 
'  |[]|,.--'' '',   ''-,.    |  
  ..    ..-''    ;       ''. '  
"""
        self.floresta = r"""
        /\ /\ /\ /\ /\ /\ /\ /\ /\
        /\ /\ /\ /\ /\ /\ /\ /\ /\
        /\ /\ /\ /\ /\ /\ /\ /\ /\
#### #  || || || || || || || || || #####
"""
        self.rio= r'''[bold #8B4513]              |    |    |                 
             )_)  )_)  )_)              
            )___))___))___)\            
           )____)____)_____)\\
         _____|____|____|____\\\__[/bold #8B4513]
[bold blue]---------[bold #8B4513]\                   /[/bold #8B4513]---------
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^[/bold blue]'''
        self.campos = r'''                 ,-_                  (`  ).    
                 |-_'-,              (     ).   
                 |-_'-'           _(        '`. 
        _        |-_'/        .=(`(      .     )
       /;-,_     |-_'        (     (.__.:-`-_.' 
      /-.-;,-,___|'          `(       ) )       
     /;-;-;-;_;_/|\_ _ _ _ _   ` __.:'   )      
        x_( __`|_P_|`-;-;-;,|        `--'       
        |\ \    _||   `-;-;-'                   
        | \`   -_|.      '-'                    
        | /   /-_| `                            
        |/   ,'-_|  \                           
        /____|'-_|___\                          
 _..,____]__|_\-_'|_[___,.._                    
'                          ``'--,..,.           '''


ascii = art()


class Player:
    def __init__(self, nome, hp_max, str, int_stat, con, atk, max_mana, gold, xp_max, xp, nivel, atk_mana, x, y):
        self.nome = nome
        self.hpmax = hp_max
        self.hp = self.hpmax
        self.str = str
        self.ini = int_stat
        self.atk = atk
        self.con = con
        self.max_mana = max_mana
        self.mana = self.max_mana
        self.atk_mana = atk_mana
        self.gold = gold
        self.xp_max = xp_max
        self.hit_chance = 75
        self.xp = xp
        self.nivel = nivel
        self.x = x
        self.y = y
        self.running = True
        self.inventario = []
        self.mana_list = []
        self.peixes = {
            'Tilapia': False,
            'Carpa': False,
            'Bagre': False,
            'Camaram': False
        }
        self.equipado = {
            "Mão Primária": None,
            'Mão Secundária': None,
            "Cabeça": None,
            "Peito": None
        }
        self.temp_atk_buff = 0
        self.current_location = "Vila" 
        self.itens = {
            "Espada Curta": False,
            "Campos1": False
        }
        self.tic = {
            "Barco":False
        }

    def save_game(self, filename="DEMO.json"):
        player_data = {
            "nome": self.nome,
            "hpmax": self.hpmax,
            "hp": self.hp,
            "str": self.str,
            "ini": self.ini,
            "atk": self.atk,
            "con": self.con,
            "max_mana": self.max_mana,
            "mana": self.mana,
            "atk_mana": self.atk_mana,
            "gold": self.gold,
            "xp_max": self.xp_max,
            "hit_chance": self.hit_chance,
            "xp": self.xp,
            "nivel": self.nivel,
            "inventario": self.inventario,
            "mana_list": self.mana_list,
            "equipado": self.equipado,
            "temp_atk_buff": self.temp_atk_buff,
            "x": self.x,
            "y": self.y,
            "itens": self.itens,
            "peixes": self.peixes,
            "tic": self.tic
        }
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(player_data, f, indent=4)
            console.print(f"[bold green]Jogo salvo com sucesso em '{filename}'![/bold green]")
        except IOError as e:
            console.print(f"[bold red]Erro ao salvar o jogo: {e}[/bold red]")
        time.sleep(1.5)

    @classmethod
    def load_game(cls, filename="DEMO.json"):
        if not os.path.exists(filename):
            console.print(f"[bold yellow]Nenhum arquivo de salvamento encontrado em '{filename}'. Iniciando novo jogo.[/bold yellow]")
            time.sleep(1.5)
            return None
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                player_data = json.load(f)
            player = cls(
                nome=player_data["nome"],
                hp_max=player_data["hpmax"],
                str=player_data["str"], 
                int_stat=player_data["ini"],
                con=player_data["con"],
                atk=player_data["atk"],
                max_mana=player_data["max_mana"],
                gold=player_data["gold"],
                xp_max=player_data["xp_max"],
                xp=player_data["xp"],
                nivel=player_data["nivel"],
                atk_mana=player_data["atk_mana"],
                x=player_data["x"],
                y=player_data["y"]
            )
            player.hp = player_data["hp"]
            player.hit_chance = player_data["hit_chance"]
            player.inventario = player_data["inventario"]
            player.mana_list = player_data["mana_list"]
            player.equipado = player_data["equipado"]
            player.itens = player_data["itens"]
            player.peixes = player_data["peixes"]
            player.tic = player_data["tic"]
            player.temp_atk_buff = player_data["temp_atk_buff"]
            console.print(f"[bold green]Jogo carregado com sucesso de '{filename}'![/bold green]")
            return player
        except (IOError, json.JSONDecodeError) as e:
            console.print(f"[bold red]Erro ao carregar o jogo: {e}. Iniciando novo jogo.[/bold red]")
            time.sleep(1.5)
            return None

    def mapa(self):
        while self.running:
            ##VILA
            if self.x == 1 and self.y == 1:
                clear()
                console.print(f'[bold yellow]+'+'-'*45+'+')
                console.print('[bold yellow]Local: Vila[/bold yellow]')
                console.print(f"[bold yellow]{ascii.vila}[/bold yellow]")
                console.print('[bold yellow]Ações:\nir Descansar\nir para o Mercado[/bold yellow]')
                console.print(f'[bold yellow]+'+'-'*45+'+')
                console.print('[bold yellow]Locais:\nir para a Floresta\nir para o Campo[/bold yellow]')
                console.print(f'[bold yellow]+'+'-'*45+'+')
                user = input("=>")
                if user == '1' or user == 'Descansar':
                    self.visitar_hospital()
                elif user == '2' or user == 'Mercado':
                    self.shop()
                elif user == '3'or user =='Floresta':
                    self.x = 2
                    self.y = 2
                elif user == '4' or user == 'Campo':
                    self.x = 1
                    self.y = 2
                elif user == 'Sair':
                    self.running = False
                elif user== 'Ajudar':
                    self.ajuda()
                elif user == 'Menu':
                    self.menu()
            ##CAMPOS
            elif self.x == 1 and self.y == 2:
                clear()
                console.print(f'[bold yellow]+'+'-'*45+'+')
                console.print('[bold yellow]Local: Campos[/bold yellow]')
                console.print(f"[bold white]{ascii.campos}[/bold white]")
                console.print('[bold yellow]Ações:\nir Converar\nir Andar[/bold yellow]')
                console.print(f'[bold yellow]+'+'-'*45+'+')
                console.print('[bold yellow]Locais:\nir para Vila[/bold yellow]')
                console.print(f'[bold yellow]+'+'-'*45+'+')
                user = input("=>")
                if user == '1' or user == 'conversar':
                    if not self.itens['Campos1']:
                        console.print(f'[bold yellow]+'+'-'*45+'+')
                        console.print('Fazendeioro: Olá Rapaz Oque Você deseja?')
                        console.print(f'{self.nome}: ...')
                        console.print('Fazendeioro: Bem eu tenho um Capacete comigo\neu não estou o usando')
                        console.print(f'{self.nome}: Obrigado Senhor.')
                        console.print('Fazendeioro: Não a de quer Rapaz, até mais')
                        console.print('Você conseguio um Capacete')
                        console.print(f'[bold yellow]+'+'-'*45+'+')
                        self.inventario.append('Capacete')
                        self.itens['Campos1'] = True
                        input()
                    else:
                        console.print(f'[bold yellow]+'+'-'*45+'+')
                        console.print('Fazendeioro: Olá Rapaz Oque Você Está Bem?')
                        console.print(f'{self.nome}: Estou senhor')
                        console.print('Fazendeioro: Você pode me ajudar eu tenho alguns tracados?')
                        console.print(f'[bold yellow]+'+'-'*45+'+')
                        console.print("SIM / NÃO")
                        esc = input('=>')
                        if esc == 'SIM':
                            if self.gold <= 10:
                                self.mana -= 10
                                self.gold += 10
                                console.print(f'[bold yellow]+'+'-'*45+'+')
                                console.print("Após um longo dia de trabalho você finalmente termina")
                                console.print("O Fazendeiro te deu 10 moedas")
                                console.print(f"Sua Estamina Diminuio em {self.max_mana}/{self.mana}\nMoedas: {self.gold}")
                                console.print(f'[bold yellow]+'+'-'*45+'+')
                                input()
                            else:
                                self.mana -= 10
                                console.print("Após um longo dia de trabalho você finalmente termina")
                                console.print(f"Sua Estamina Diminuio em {self.max_mana}/{self.mana}\nMoedas: {self.gold}")
                                input()
                        elif esc == 'NÂO':
                            console.print(f'[bold yellow]+'+'-'*45+'+')
                            console.print('Fazendeioro: Tudo Bem Você Deve Estar Ocupado?')
                            console.print(f'[bold yellow]+'+'-'*45+'+')
                            input()
                elif user == '2' or user == 'Andar':
                    console.print('Você observa o lindo Campos')
                    time.sleep(2)
                elif user == '3' or user == 'Vila':
                    self.x = 1
                    self.y = 1
                elif user == 'Sair':
                    self.running = False
                elif user== 'Ajudar':
                    self.ajuda()
                elif user == 'Menu':
                    self.menu()
            ##FLORESTA
            elif self.x == 2 and self.y == 2:
                clear()
                console.print(f'[bold yellow]+'+'-'*45+'+')
                console.print('[bold green]Local: Floresta[/bold green]')
                console.print(f"[bold green]{ascii.floresta}[/bold green]")
                console.print('[bold green]Ações:\nir Explorar\nir Andar[/bold green]')
                console.print(f'[bold yellow]+'+'-'*45+'+')
                console.print('[bold green]Locais:\nir para Vila\nir para o Rio[/bold green]')
                console.print(f'[bold yellow]+'+'-'*45+'+')
                user = input("=>")
                if user == '1' or user == 'Explorar':
                    enie = encontro_aleatorio() 
                    battle_system(play, enie)
                elif user == '2' or user == 'Andar':
                    if not self.itens['Espada Curta']:
                        console.print('[bold yellow]Você Pegol uma Espada Curta[/bold yellow]')
                        time.sleep(2)
                        self.inventario.append('Espada Curta')
                        self.itens['Espada Curta'] = True
                    else:
                        console.print('[bold yellow]Você Já passol por aqui não a mais nada[/bold yellow]')
                        time.sleep(2)
                elif user == '3' or user == 'Vila':
                    self.x = 1
                    self.y = 1
                elif user == '4' or user == 'Rio':
                    self.x = 3
                    self.y = 3
                elif user == 'Sair':
                    self.running = False
                elif user== 'Ajudar':
                    self.ajuda()
                elif user == 'Menu':
                    self.menu()
            ##RIO
            elif self.x == 3 and self.y == 3:
                clear()
                console.print(f'[bold yellow]+'+'-'*45+'+')
                console.print('[bold blue]Local: Rio[/bold blue]')
                console.print(f"{ascii.rio}")
                console.print('[bold blue]Ações:\nir Pescar\nir Observar[/bold blue]')
                console.print(f'[bold yellow]+'+'-'*45+'+')
                console.print('[bold blue]Locais:\nir para Floresta\nir para o Barco[/bold blue]')
                console.print(f'[bold yellow]+'+'-'*45+'+')
                user = input("=>")
                if user == '1' or user == 'Pescar':
                    if "Vara de Pescar" in self.inventario:
                        console.print('Você jogol a Isca')
                        time.sleep(2)
                        chanse = random.randint(1, 10)
                        if chanse <= 5:
                            peixe = ['Tilapia', 'Carpa']
                            peixe_ads = random.choice(peixe)
                            if peixe_ads == 'Tilapia':
                                self.peixes['Tilapia']=True
                                console.print('[bold blue]Você consegui pegar uma Tilapia[/bold blue]')
                                time.sleep(2)
                            elif peixe_ads == 'Carpa':
                                self.peixes['Carpa']=True
                                console.print('[bold blue]Você consegui pegar uma Carpa[/bold blue]')
                                time.sleep(2)
                        else:
                            console.print("[bold red]Sem sorte Tente de novo[/bold red]")
                            time.sleep(2)
                    else:
                        console.print("[bold red]Você Não Tem uma Vara de pesca[/bold red]")
                elif user == '2' or user == 'Observar':
                    console.print('[bold blue]Você começa a observar a costa do mar[/bold blue]')
                    time.sleep(3)
                elif user == '3' or user == 'Floresta':
                    self.x = 2
                    self.y = 2
                elif user == '4' or user == 'Barco':
                    self.x = 3
                    self.y = 1
                elif user == 'Sair':
                    self.running = False
                elif user== 'Ajudar':
                    self.ajuda()
                elif user == 'Menu':
                    self.menu()
            ##BARCO
            elif self.x == 3 and self.y == 1:
                clear()
                console.print(f'[bold yellow]+'+'-'*45+'+')
                console.print('[bold blue]Local: Barco[/bold blue]')
                console.print(f"{ascii.rio}")
                console.print('[bold blue]Ações:\nir Conversar\nir Entrar[/bold blue]')
                console.print(f'[bold yellow]+'+'-'*45+'+')
                console.print('[bold blue]Locais:\nir para Rio[/bold blue]')
                console.print(f'[bold yellow]+'+'-'*45+'+')
                user = input("=>")
                if user == '1' or user == 'Conversar':
                    if self.tic["Barco"]==False:
                        console.print('[bold blue]Atendente: Você deseja entrar?\n[SIM]    [NÂO][/bold blue]')
                        cov = input('=>')
                        if cov == 'SIM':
                            if self.gold <= 99:
                                console.print('[bold red]Você não possui dinheiro suficiente[/bold red]')
                                time.sleep(2)
                            else:
                                self.golg -= 100
                                console.print('[bold blue]Atendente: Aqui está seu tiquet[/bold blue]')
                                time.sleep(2)
                                self.tic['Barco']=True
                        elif cov == 'NÂO':
                            pass
                    elif self.tic['Barco']==True:
                        console.print('[bold blue]Atendente: Já te deu seu tiquet então entre[/bold blue]')
                        time.sleep(2)
                elif user == '2' or user =='Entrar':
                    if self.tic["Barco"]==False:
                        console.print('[bold red]Segurança: Você não possui um tiquet[/bold red]')
                        time.sleep(2)
                    elif self.tic['Barco']==True:
                        console.print('[bold blue]Segurança: Entre[/bold blue]')
                        time.sleep(2)
                elif user == '3' or user =='Rio':
                    self.x = 3
                    self.y = 3
                elif user == 'Sair':
                    self.running = False
                elif user== 'Ajudar':
                    self.ajuda()
                elif user == 'Menu':
                    self.menu()
            

    def ajuda(self):
        while True:
            clear()
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print("[bold blue]Ajuda: [/bold blue]")
            console.print("[bold blue]Para Sair Digite:Sair[/bold blue]")
            console.print("[bold blue]Para Ajuda Digite: Ajuda[/bold blue]")
            console.print("[bold blue]Para fazer Ações no Jodo Digite:\n[Numero]ou\nNome da Ação[/bold blue]")
            console.print(f'[bold yellow]+'+'-'*45+'+')
            input('=>')
            break

    def pescar_livro(self):
        if self.peixes['Tilapia']== False:
            console.print('[bold red]Você Não Pescol Uma Tilapia[/bold red]')
        elif self.peixes['Tilapia']== True:
            console.print('[bold blue]Você Já Pescol Uma Tilapia[/bold blue]')
        if self.peixes['Carpa']== False:
            console.print('[bold red]Você Não Pescol Uma Carpa[/bold red]')
        elif self.peixes['Carpa']== True:
            console.print('[bold blue]Você Já Pescol Uma Carpa[/bold blue]')
        if self.peixes['Bagre']== False:
            console.print('[bold red]Você Não Pescol Um Bagre[/bold red]')
        elif self.peixes['Bagre']== True:
            console.print('[bold blue]Você Já Pescol Um Bagre[/bold blue]')
        if self.peixes['Camaram']== False:
            console.print('[bold red]Você Não Pescol Um Camaram[/bold red]')
        elif self.peixes['Camaram']== True:
            console.print('[bold blue]Você Já Pescol Um Camaram[/bold blue]')
        input()

    def menu(self):
        while True:
            clear()
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print('[bold white][1]Status    [2]Inventario\n[3]Salvar    [4]Livro de Pesca\n[5]Magias   [6]Sair[/bold white]') 
            console.print(f'[bold yellow]+'+'-'*45+'+')
            menu_esc = input("=>")
            if menu_esc == '1' or menu_esc == 'Status':
                self.status()
                input()
            elif menu_esc == '2' or menu_esc == 'Inventario':
                self.exibir_menu_inventario()
            elif menu_esc == '3' or menu_esc == 'Salva':
                self.save_game()
            elif menu_esc == '4' or menu_esc == 'Livro':
                self.pescar_livro()
            elif menu_esc == '5' or menu_esc == 'Magias':
                self.list_mana()
            elif menu_esc == '6' or menu_esc == 'Sair':
                break

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        console.print(f"[bold red]{self.nome} recebeu {damage} de dano![/bold red]")
        time.sleep(1)

    def visitar_hospital(self):
        if self.hp == self.hpmax and self.mana == self.max_mana: 
            console.print(f"[bold yellow]{self.nome}: Está Bem![/bold yellow]")
        else:
            self.hp = self.hpmax
            self.mana = self.max_mana
            console.print(f"[bold yellow]{self.nome} foi recuperado\nVida atual: {self.hp}/{self.hpmax}\nEstamina atual: {self.mana}/{self.max_mana}[/bold yellow]")
        input()

    def attack_enemy(self, enemy):
        roll = random.randint(1, 100)
        current_atk = self.atk + self.temp_atk_buff 
        if roll <= self.hit_chance:
            damage = random.randint(current_atk - 3, current_atk + 3)
            enemy.take_damage(damage)
            console.print(f"[bold green]{self.nome} atacou {enemy.nome} e causou {damage} de dano![/bold green]")
        else:
            console.print(f"[bold yellow]{self.nome} errou o ataque em {enemy.nome}![/bold yellow]")
        time.sleep(1)

    def list_mana(self):
        while True:
            console.print("\n[bold cyan]=== MENU DE MAGIAS ===[/bold cyan]")
            console.print("  [1] Ver Magias")
            console.print("  [2] Usar Magia (digite o nome da magia)")
            console.print("  [3] Sair")
            escolha = input("=> ").strip()
            if escolha == '1':
                if not self.mana_list:
                    console.print("[bold yellow]Você não possui nenhuma magia no momento.[/bold yellow] 😥")
                else:
                    console.print("[bold magenta]--- Suas Magias ---[/bold magenta]")
                    spell_info = {
                        "Bola de Fogo": {"custo": 10, "efeito": "Causa dano mágico."},
                        "Cura": {"custo": 15, "efeito": "Restaura pontos de vida."},
                        "Espada Sacrada": {"custo": 20, "efeito": "Aumenta seu ataque temporariamente."} # UPDATED: Description
                    }
                    for i, magia_nome in enumerate(self.mana_list):
                        info = spell_info.get(magia_nome, {"custo": "N/A", "efeito": "Descrição não disponível."})
                        console.print(f"  [cyan]{i + 1}.[/cyan] [bold]{magia_nome}[/bold] (Custo: [green]{info['custo']}[/green] Mana, Efeito: [blue]{info['efeito']}[/blue])")
                    console.print("[bold magenta]---------------------[/bold magenta]")
                time.sleep(1.5)
            elif escolha == '2':
                if not self.mana_list:
                    console.print("[bold yellow]Você não possui nenhuma magia para usar.[/bold yellow]")
                    time.sleep(1.5)
                    continue
                
                magia_escolhida = input("Digite o nome da magia que deseja usar: ").strip()
                
                if magia_escolhida in self.mana_list:
                    console.print(f"[bold green]Você escolheu usar '{magia_escolhida}'.[/bold green]")
                    console.print("Esta magia só pode ser usada em combate contra um inimigo ou para se curar.")
                else:
                    console.print("[bold red]Magia não encontrada ou você não a possui.[/bold red]")
                time.sleep(1.5)
            elif escolha == '3':
                console.print("[bold green]Saindo do Menu de Magias.[/bold green]")
                time.sleep(1)
                break
            else:
                console.print("[bold red]Opção inválida. Por favor, escolha novamente.[/bold red]")
                time.sleep(1.5)

    def usar_magias(self, nome_mana, enemy):
        bola_de_fogo_base_damage = self.atk_mana * 2.0
        cura_base_heal = 20
        espada_sacrada_buff_amount = 10
        
        if nome_mana not in self.mana_list:
            console.print(f"[bold red]Você não possui a magia '{nome_mana}'.[/bold red]")
            return False

        if nome_mana == 'Bola de Fogo':
            mana_cost = 10
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                roll = random.randint(1, 100)
                if roll <= self.hit_chance:
                    damage = random.randint(int(bola_de_fogo_base_damage - 3), int(bola_de_fogo_base_damage + 3))
                    enemy.take_damage(damage)
                    console.print(f"[bold green]{self.nome} atacou {enemy.nome} e causou {damage} de dano com Bola de Fogo![/bold green]")
                    return True
                else:
                    console.print(f"[bold yellow]{self.nome} errou o ataque mágico em {enemy.nome}![/bold yellow]")
                    return True
            else:
                console.print("[bold red]Mana insuficiente para usar Bola de Fogo![/bold red]")
                return False
        
        elif nome_mana == 'Cura':
            mana_cost = 15
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                healed_amount = random.randint(cura_base_heal - 5, cura_base_heal + 5)
                self.hp = min(self.hpmax, self.hp + healed_amount)
                console.print(f'[bold green]Você se curou em {healed_amount} HP! Seu HP atual é {self.hp}/{self.hpmax}[/bold green]')
                return True
            else:
                console.print("[bold red]Mana insuficiente para usar Cura![/bold red]")
                return False
        
        elif nome_mana == 'Espada Sacrada':
            mana_cost = 20
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                self.temp_atk_buff += espada_sacrada_buff_amount
                console.print(f'[bold green]Você ativou Espada Sacrada! Seu ATK aumentou em {espada_sacrada_buff_amount} para esta batalha.[/bold green]')
                return True
            else:
                console.print("[bold red]Mana insuficiente para usar Espada Sacrada![/bold red]")
                return False
        
        return False

    def aprender_magia(self):
        while True:
            clear()
            console.print(f'[bold blue]Você precisa de INT para aprender magias novas[/bold blue]')
            console.print(f'[bold white]INTELIGêNCIA:{self.ini}[/bold white]')
            console.print(f'[bold white][0]Sair\n[1]Cura\n[2]Espada Sacrada\n[3]Bola de Fogo[/bold white]')
            escolha = input('=>')
            if escolha == '0':
                break
            elif escolha == '1':
                if self.ini >= 10:
                    if 'Cura' in self.mana_list:
                        console.print(f'[bold yellow]Você já possui a Magia Cura.[/bold yellow]')
                        time.sleep(1)
                    else:
                        console.print(f'[bold white]Você aprendeu a Magia Cura[/bold white]')
                        self.mana_list.append('Cura')
                        time.sleep(1)
                elif self.ini < 10:
                    console.print('Você não possui inteligência')
                    time.sleep(1)

            elif escolha == '2':
                if self.ini >= 15:
                    if 'Espada Sacrada' in self.mana_list:
                        console.print(f'[bold yellow]Você já possui a Magia Espada Sacrada.[/bold yellow]')
                        time.sleep(1)
                    else:
                        console.print(f'[bold white]Você aprendeu a Magia Espada Sacrada[/bold white]')
                        self.mana_list.append('Espada Sacrada')
                        time.sleep(1)
                elif self.ini < 15:
                    console.print('Você não possui inteligência')
                    time.sleep(1)
                    
            elif escolha == '3':
                if self.ini >= 20:
                    if 'Bola de Fogo' in self.mana_list:
                        console.print(f'[bold yellow]Você já possui a Magia Bola de Fogo.[/bold yellow]')
                        time.sleep(1)
                    else:
                        console.print(f'[bold white]Você aprendeu a Magia Bola de Fogo[/bold white]')
                        self.mana_list.append('Bola de Fogo')
                        time.sleep(1)
                elif self.ini < 20:
                    console.print('Você não possui inteligência')
                    time.sleep(1)

    def shop(self):
        while True:
            clear()
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print('[bold cyan]Bem Vindo ao Mercado[/bold cyan]')
            console.print("[bold cyan]  Mercado  [/bold cyan]")
            console.print("  [1]Comprar")
            console.print("  [2]Sair")
            console.print(f'[bold yellow]+'+'-'*45+'+')
            escolha = input('')
            if escolha == '2':
                break
            elif escolha == '1':
                while True:
                    clear()
                    console.print(f'[bold yellow]+'+'-'*45+'+')
                    console.print(f"[bold cyan]Gold:{self.gold} Itens[/bold cyan]")
                    console.print('  [1]Consumiveis:\n  [2]Equipar')
                    console.print(f'[bold blue]Escolha uma opção: [0 para sair][/bold blue]')
                    console.print(f'[bold yellow]+'+'-'*45+'+')
                    esc = input('=>')
                    if esc == '0':
                        break
                    elif esc == '1':
                        while True:
                            clear()
                            console.print(f'[bold yellow]+'+'-'*45+'+')
                            console.print(f"[bold cyan]Gold:{self.gold}[/bold cyan]")
                            console.print('  [1]Pomada de Regeneração:[50]')
                            console.print(f'[bold blue]Escolha uma opção: [0 para sair][/bold blue]')
                            console.print(f'[bold yellow]+'+'-'*45+'+')
                            consumivel = input('=>')
                            if consumivel == '1':
                                while True:
                                    clear()
                                    console.print(f'[bold yellow]+'+'-'*45+'+')
                                    console.print('[bold yellow]Descrição: Um item que pode recuperar sua vida\nem 30 pontos\nDeseja comprar:\n [1]Sim\n [2]Nâo[/bold yellow]')
                                    console.print(f'[bold yellow]+'+'-'*45+'+')
                                    pomada = input('=>')
                                    cons = 50
                                    if pomada == '1':
                                        if self.gold >= cons:
                                            self.gold -= cons
                                            self.inventario.append('Pomada de Regeneração')
                                            console.print("[bold yellow]Você compro uma Pomada de Regeneração[/bold yellow]")
                                            time.sleep(1)
                                        elif self.gold < cons:
                                            console.print("[bold yellow]Você não possui dinheiro suficiente[/bold yellow]")
                                            time.sleep(1)
                                    elif pomada == '2':
                                        break
                    elif esc == '2':
                        while True:
                            clear()
                            console.print(f'[bold yellow]+'+'-'*45+'+')
                            console.print(f"[bold cyan]Gold:{self.gold} Itens[/bold cyan]")
                            console.print('  [1]Espada Curta:[100]\n  [2]Capacete:[100]\n  [3]Capuz:[100]\n  [4]Peitoral:[150]\n  [5]Manto:[150]')
                            console.print(f'[bold blue]Escolha uma opção: [0 para sair][/bold blue]')
                            console.print(f'[bold yellow]+'+'-'*45+'+')
                            equipaveis = input('=>')
                            if equipaveis == '1':
                                while True:
                                    clear()
                                    console.print(f'[bold yellow]+'+'-'*45+'+')
                                    console.print('[bold yellow]Descrição: Espada Curta um Item que pode ser equipado\naumenta seu ataque em 10\nDeseja comprar:\n [1]Sim\n [2]Nâo[/bold yellow]')
                                    espada_curta = input('=>')
                                    console.print(f'[bold yellow]+'+'-'*45+'+')
                                    cons = 100
                                    if espada_curta == '1':
                                        if self.gold >= cons:
                                            self.gold -= cons
                                            self.inventario.append('Espada Curta')
                                            console.print("[bold yellow]Você compro uma Espada Curta[/bold yellow]")
                                            time.sleep(1)
                                        elif self.gold < cons:
                                            console.print("[bold yellow]Você não possui dinheiro suficiente[/bold yellow]")
                                            time.sleep(1)
                                    elif espada_curta == '1':
                                        break
                            elif equipaveis == '2':
                                while True:
                                    clear()
                                    console.print(f'[bold yellow]+'+'-'*45+'+')
                                    console.print('[bold yellow]Descrição: Capacete um Item que pode ser equipado\naumenta seu HP em 5\nDeseja comprar:\n [1]Sim\n [2]Nâo[/bold yellow]')
                                    capacete = input('=>')
                                    console.print(f'[bold yellow]+'+'-'*45+'+')
                                    cons = 100
                                    if capacete == '1':
                                        if self.gold >= cons:
                                            self.gold -= cons
                                            self.inventario.append('Capacete')
                                            console.print("[bold yellow]Você compro um Capacete[/bold yellow]")
                                            time.sleep(1)
                                        elif self.gold < cons:
                                            console.print("[bold yellow]Você não possui dinheiro suficiente[/bold yellow]")
                                            time.sleep(1)
                                    elif capacete == '2':
                                        break
                            elif equipaveis == '3':
                                while True:
                                    clear()
                                    console.print(f'[bold yellow]+'+'-'*45+'+')
                                    console.print('[bold yellow]Descrição: Capuz um Item que pode ser equipado\naumenta seu HP em 2.5 e Mana em 5\nDeseja comprar:\n [1]Sim\n [2]Nâo[/bold yellow]')
                                    console.print(f'[bold yellow]+'+'-'*45+'+')
                                    capuz = input('=>')
                                    cons = 100
                                    if capuz == '1':
                                        if self.gold >= cons:
                                            self.gold -= cons
                                            self.inventario.append('Capuz')
                                            console.print("[bold yellow]Você compro um Capuz[/bold yellow]")
                                            time.sleep(1)
                                        elif self.gold < cons:
                                            console.print("[bold yellow]Você não possui dinheiro suficiente[/bold yellow]")
                                            time.sleep(1)
                                    elif capuz == '2':
                                        break
                            elif equipaveis == '4':
                                while True:
                                    clear()
                                    console.print(f'[bold yellow]+'+'-'*45+'+')
                                    console.print('[bold yellow]Descrição: Peitoral um Item que pode ser equipado\naumenta seu HP em 10\nDeseja comprar:\n [1]Sim\n [2]Nâo[/bold yellow]')
                                    console.print(f'[bold yellow]+'+'-'*45+'+')
                                    peitoral = input('=>')
                                    cons = 150
                                    if peitoral == '1':
                                        if self.gold >= cons:
                                            self.gold -= cons
                                            self.inventario.append('Peitoral')
                                            console.print("[bold yellow]Você compro um Peitoral[/bold yellow]")
                                            time.sleep(1)
                                        elif self.gold < cons:
                                            console.print("[bold yellow]Você não possui dinheiro suficiente[/bold yellow]")
                                            time.sleep(1)
                                    elif peitoral == '2':
                                        break
                            elif equipaveis == '5':
                                while True:
                                    clear()
                                    console.print(f'[bold yellow]+'+'-'*45+'+')
                                    console.print('[bold yellow]Descrição: Manto um Item que pode ser equipado\naumenta seu HP em 5 Mana em 10\nDeseja comprar:\n [1]Sim\n [2]Nâo[/bold yellow]')
                                    console.print(f'[bold yellow]+'+'-'*45+'+')
                                    manto = input('=>')
                                    cons = 150
                                    if manto == '1':
                                        if self.gold >= cons:
                                            self.gold -= cons
                                            self.inventario.append('Manto')
                                            console.print("[bold yellow]Você compro um Peitoral[/bold yellow]")
                                            time.sleep(1)
                                        elif self.gold < cons:
                                            console.print("[bold yellow]Você não possui dinheiro suficiente[/bold yellow]")
                                            time.sleep(1)
                                    elif manto == '2':
                                        break

    def status(self):
        console.print(f'[bold white]+'+'-'*45+'+')
        console.print(f'[bold green]HP[{self.hp}/{self.hpmax}][/bold green][bold red]  ATK[{self.atk}][/bold red][bold blue]  MA[{self.atk_mana}]  MP[{self.mana}/{self.max_mana}][/bold blue]')
        console.print(f'[bold white]STR[{self.str}]    INT[{self.ini}]  CON[{self.con}][/bold white]')
        console.print(f'[bold yellow]GOLD[{self.gold}][/bold yellow]')
        console.print(f'[bold green]XP[/bold green][bold white][{self.xp}/{self.xp_max}][/bold white]')
        console.print(f'[bold white]NIVEL[{self.nivel}][/bold white]')
        console.print(f'[bold white]+'+'-'*45+'+')

    def info_batalha(self):
        console.print(f"[bold white]{self.nome} (Nível {self.nivel})[/bold white]")
        console.print(f"  [bold green]HP: {self.hp}/{self.hpmax}[/bold green]")
        console.print(f"  [bold blue]MP: {self.mana}/{self.max_mana}[/bold blue]")
        console.print(f"  [bold red]ATK: {self.atk + self.temp_atk_buff}[/bold red] | [bold cyan]MA: {self.atk_mana}[/bold cyan]") # MODIFIED: Show effective ATK
        console.print(f"  [bold yellow]Buff ATK: {self.temp_atk_buff}[/bold yellow]") # Added for clarity

    def up(self):
        if self.xp >= self.xp_max:
            while self.xp >= self.xp_max:
                self.nivel += 1
                self.xp -= self.xp_max
                self.xp_max = int(self.xp_max * 1.5)
                console.print(f"\n[bold magenta]PARABÉNS! Você alcançou o Nível {self.nivel}![/bold magenta]")
                self.hpmax += 10
                self.hp = self.hpmax
                self.atk += 2
                self.str += 1
                self.ini += 1
                self.con += 1
                self.max_mana += 5
                self.mana = self.max_mana
            time.sleep(1)

    def add_xp(self, amount):
        self.xp += amount
        console.print(f"[bold blue]Você ganhou {amount} de XP![/bold blue]")
        self.up()
        time.sleep(1)

    def usar_item(self, item_nome: str):
        if item_nome == "Pomada de Regeneração":
            if "Pomada de Regeneração" in self.inventario:
                self.hp = min(self.hpmax, self.hp + 30)
                self.inventario.remove("Pomada de Regeneração")
                console.print("[bold green]Você usou uma Pomada de Regeneração e recuperou HP![/bold green]")
            else:
                console.print("[bold red]Você não tem Pomadas de Regeneração no seu inventário.[/bold red]")
        elif item_nome == "Vara de Pescar":
            if "Vara de Pescar" in self.inventario:
                console.print("[bold green]Você pode a usar em Rios[/bold green]")
            else:
                console.print("[bold red]Você não tem Vara de Pescar no seu inventário.[/bold red]")
        elif item_nome in ["Capacete", "Escudo", 'Capuz', 'Peitoral', 'Cajado', 'Espada Curta','Espada Longa','Anel','Escudo Forte','Manto']:
            if item_nome in self.inventario:
                target_slot = None
                if item_nome == "Capacete" or item_nome == "Capuz":
                    target_slot = "Cabeça"
                elif item_nome == 'Cajado'or item_nome == 'Espada Curta'or item_nome == 'Espada Longa':
                    target_slot = 'Mão Primária'
                elif item_nome == "Escudo" or item_nome == 'Anel' or item_nome == 'Escudo Forte':
                    target_slot = "Mão Secundária"
                elif item_nome == "Peitoral" or item_nome == 'Manto':
                    target_slot = "Peito"
                if target_slot:
                    if self.equipado[target_slot] is None:
                        self.inventario.remove(item_nome)
                        self.equipado[target_slot] = item_nome
                        if item_nome == 'Espada Curta': self.atk += 10
                        if item_nome == 'Cajado': self.atk_mana += 10
                        if item_nome == "Capacete": self.hpmax += 5
                        if item_nome == "Peitoral": self.hpmax += 10
                        if item_nome == 'Espada Longa': self.atk += 20
                        if item_nome == "Escudo": self.hpmax *= 1.2
                        if item_nome == "Anel": self.atk_mana *= 1.2 
                        if item_nome == "Escudo Forte": self.hpmax *= 1.5
                        if item_nome == "Manto": self.hpmax += 5; self.mana += 10
                        if item_nome == "Capuz": self.hpmax += 2.5; self.mana += 5


                        console.print(f"[bold green]Você equipou o {item_nome} no slot {target_slot}![/bold green]")
                    else:
                        console.print(f"[bold yellow]Você já tem {self.equipado[target_slot]} equipado no slot {target_slot}. Desequipe-o primeiro.[/bold yellow]")
                else:
                    console.print(f"[bold red]Não sei onde equipar '{item_nome}'.[/bold red]")
            else:
                console.print(f"[bold red]Você não tem {item_nome} no seu inventário.[/bold red]")
        else:
            console.print(f"[bold red]Item '{item_nome}' não reconhecido ou não pode ser usado diretamente.[/bold red]")
        self.status()

    def desequipar_item(self, item_nome: str):
        slot_desequipado = None
        for slot, item in self.equipado.items():
            if item == item_nome:
                slot_desequipado = slot
                break
        if slot_desequipado:
            self.inventario.append(item_nome)
            self.equipado[slot_desequipado] = None
            if item_nome == "Espada Curta": self.atk -= 10
            if item_nome == "Cajado": self.atk_mana -= 10
            if item_nome == "Capacete": self.hpmax -= 5
            if item_nome == "Peitoral": self.hpmax -= 10
            if item_nome == "Escudo": self.atk -= 5 ; self.hpmax -= 5
            if item_nome == 'Espada Longa': self.atk -= 20
            if item_nome == "Escudo": self.hpmax /= 1.2
            if item_nome == "Anel": self.atk_mana /= 1.2 
            if item_nome == "Escudo Forte": self.hpmax /= 1.5
            console.print(f"[bold green]Você desequipou o {item_nome} do slot {slot_desequipado}.[/bold green]")
        else:
            console.print(f"[bold red]Você não tem {item_nome} equipado.[/bold red]")
        self.status()

    def mostrar_inventario(self):
        console.print("\n[bold magenta]---------- SEU INVENTÁRIO ----------[/bold magenta]")
        all_items_current = list(self.inventario) + [item for item in self.equipado.values() if item is not None]
        todos_os_itens_unicos = sorted(list(set(all_items_current)))

        if not todos_os_itens_unicos:
            console.print("[italic red]  (Seu inventário e equipamentos estão vazios)[/italic red]")
        else:
            itens_por_slot = {item: slot for slot, item in self.equipado.items() if item is not None}
            contagem_no_inventario = Counter(self.inventario)

            for item_nome in todos_os_itens_unicos:
                status_equipado = ""
                if item_nome in itens_por_slot:
                    slot_info = itens_por_slot[item_nome]
                    status_equipado = f" [bold green](Equipado: {slot_info})[/bold green]"
                
                quantidade_em_inventario = contagem_no_inventario.get(item_nome, 0)
                
                quantidade_str = ""
                if quantidade_em_inventario > 1 and item_nome not in itens_por_slot:
                    quantidade_str = f" x{quantidade_em_inventario}"
                elif quantidade_em_inventario >= 1 and item_nome not in itens_por_slot:
                    quantidade_str = ""
                
                if item_nome in itens_por_slot and quantidade_em_inventario > 0:
                    console.print(f"  [bold cyan]{item_nome}[/bold cyan] x{quantidade_em_inventario}{status_equipado}")
                elif item_nome in itens_por_slot and quantidade_em_inventario == 0:
                    console.print(f"  [bold cyan]{item_nome}[/bold cyan]{status_equipado}")
                elif item_nome not in itens_por_slot and quantidade_em_inventario > 0:
                    console.print(f"  [bold cyan]{item_nome}[/bold cyan]{quantidade_str}")
        console.print("[bold magenta]------------------------------------[/bold magenta]")

    def exibir_menu_inventario(self):
        while True:
            clear()
            self.mostrar_inventario()
            console.print("\n[bold magenta]O que deseja fazer com seu inventário?[/bold magenta]")
            console.print("[1] Usar/Equipar Item do Inventário")
            console.print("[2] Desequipar Item")
            console.print("[3] Sair do Inventário")
            choice = console.input("[bold blue]Escolha uma opção: [/bold blue]")
            if choice == '1':
                clear()
                itens_para_interagir = list(set(self.inventario))
                if not itens_para_interagir:
                    console.print("[bold yellow]Seu inventário está vazio. Você não tem itens para usar ou equipar.[/bold yellow]")
                    time.sleep(1.5)
                    continue
                console.print("[bold magenta]Itens no Inventário para USAR/EQUIPAR:[/bold magenta]")
                for i, item_name in enumerate(itens_para_interagir):
                    console.print(f"[{i+1}] {item_name}")
                item_choice = console.input("[bold blue]Escolha o número do item (ou '0' para cancelar): [/bold blue]")
                try:
                    item_index = int(item_choice) - 1
                    if 0 <= item_index < len(itens_para_interagir):
                        self.usar_item(itens_para_interagir[item_index])
                        time.sleep(1.5)
                    elif item_index == -1:
                        console.print("[bold yellow]Ação cancelada.[/bold yellow]")
                        time.sleep(1.5)
                    else:
                        console.print("[bold red]Escolha inválida de item![/bold red]")
                        time.sleep(1.5)
                except ValueError:
                    console.print("[bold red]Entrada inválida![/bold red]")
                    time.sleep(1.5)
            elif choice == '2':
                clear()
                equipped_items_list = [item for item in self.equipado.values() if item is not None]
                if not equipped_items_list:
                    console.print("[bold yellow]Você não tem itens equipados para desequipar.[/bold yellow]")
                    time.sleep(1.5)
                    continue
                console.print("\n[bold magenta]Itens Equipados para DESEQUIPAR:[/bold magenta]")
                for i, item_name in enumerate(equipped_items_list):
                    console.print(f"[{i+1}] {item_name}")
                item_choice = console.input("[bold blue]Escolha o número do item (ou '0' para cancelar): [/bold blue]")
                try:
                    item_index = int(item_choice) - 1
                    if 0 <= item_index < len(equipped_items_list):
                        self.desequipar_item(equipped_items_list[item_index])
                        time.sleep(1.5)
                    elif item_index == -1:
                        console.print("[bold yellow]Ação cancelada.[/bold yellow]")
                        time.sleep(1.5)
                    else:
                        console.print("[bold red]Escolha inválida de item![/bold red]")
                        time.sleep(1.5)
                except ValueError:
                    console.print("[bold red]Entrada inválida![/bold red]")
                    time.sleep(1.5)
            elif choice == '3':
                console.print("[bold yellow]Saindo do Inventário...[/bold yellow]")
                time.sleep(1)
                break
            else:
                console.print("[bold red]Opção inválida. Por favor, escolha novamente.[/bold red]")
                time.sleep(1.5)

class Inimigo:
    def __init__(self, nome: str, hp: int, atk: int, xp: int, gold: int, ascii_art: str, nivel: int, a1:str, a2:str):
        self.ascii = ascii_art
        self.nome = nome
        self.hp = hp
        self.atk = atk
        self.a1 = a1 
        self.a2 = a2 
        self.hp_max = hp
        self.hit_chance = 50
        self.nivel = nivel
        self.xp = xp
        self.gold = gold

    def info(self):
        console.print(f'[bold yellow]+'+'-'*45+'+')
        console.print(f'{self.ascii}')
        console.print(f'[bold yellow]+'+'-'*45+'+')
        console.print(f'[bold white]{self.nome} (Nível {self.nivel})[/bold white]')
        console.print(f'HP: [bold green]{self.hp}[/bold green] | ATK: [bold red]{self.atk}[/bold red]')
        console.print(f'[bold white]Atk:1[{self.a1}]/Atk:2[{self.a2}][/bold white]') 
        console.print(f'[bold yellow]+'+'-'*45+'+')

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        console.print(f"[bold red]{self.nome} recebeu {damage} de dano![/bold red]")

    def atake_a1(self, player):
        roll = random.randint(1, 100)
        if roll <= self.hit_chance:
            damage = random.randint(self.atk - 2, self.atk + 2)
            player.take_damage(damage)
            console.print(f"[bold red]{self.nome} usou {self.a1} em {player.nome} e causou {damage} de dano![/bold red]")
        else:
            console.print(f"[bold yellow]{self.nome} errou o ataque com {self.a1} em {player.nome}![/bold yellow]")

    def atake_a2(self, player):
        roll = random.randint(1, 100)
        a2_damage_modifier = 1.5
        if roll <= (self.hit_chance - 10):
            damage = random.randint(int(self.atk * a2_damage_modifier) - 3, int(self.atk * a2_damage_modifier) + 3)
            player.take_damage(damage)
            console.print(f"[bold red]{self.nome} usou {self.a2} em {player.nome} e causou {damage} de dano![/bold red]")
        else:
            console.print(f"[bold yellow]{self.nome} errou o ataque com {self.a2} em {player.nome}![/bold yellow]")

    def attack_player(self, player):
        choice = random.choice([self.a1, self.a2])
        if choice == self.a1:
            self.atake_a1(player)
        else: 
            self.atake_a2(player)

def battle_system(player_obj: Player, enemy_obj: Inimigo):
    console.print("\n[bold magenta]!!! INICIANDO BATALHA !!![/bold magenta]")
    time.sleep(2)

    while player_obj.hp > 0 and enemy_obj.hp > 0:
        clear()
        enemy_obj.info()
        player_obj.info_batalha()
        console.print("[bold cyan]O que você fará?[/bold cyan]")
        console.print("  [1] Atacar")
        console.print("  [2] Usar Magia")
        console.print("  [3] Usar Item")
        action_choice = console.input("[bold blue]Sua ação: [/bold blue]").strip()
        turn_taken = False
        if action_choice == '1':
            player_obj.attack_enemy(enemy_obj)
            turn_taken = True
        elif action_choice == '2':
            if not player_obj.mana_list:
                console.print("[bold red]Você não possui nenhuma magia para usar![/bold red]")
                time.sleep(1.5)
                continue
            
            console.print("[bold magenta]--- SUAS MAGIAS ---[/bold magenta]")
            spell_options = {}
            for i, spell_name in enumerate(player_obj.mana_list):
                console.print(f"  [{i+1}] {spell_name}")
                spell_options[str(i+1)] = spell_name
            
            magic_choice_input = console.input("[bold blue]Escolha o número da magia (ou '0' para cancelar): [/bold blue]").strip()
            
            if magic_choice_input == '0':
                console.print("[bold yellow]Ação de magia cancelada.[/bold yellow]")
                time.sleep(1)
                continue
            
            chosen_spell_name = spell_options.get(magic_choice_input)
            
            if chosen_spell_name:
                turn_taken = player_obj.usar_magias(chosen_spell_name, enemy_obj)
            else:
                console.print("[bold red]Escolha de magia inválida![/bold red]")
                time.sleep(1.5)
                continue
        elif action_choice == '3':
            
            if not player_obj.inventario:
                console.print("[bold red]Seu inventário está vazio. Não há itens para usar![/bold red]")
                time.sleep(1.5)
                continue
            
            console.print("[bold magenta]--- ITENS DO INVENTÁRIO ---[/bold magenta]")
            usable_items = [item for item in player_obj.inventario if item == "Pomada de Regeneração"]
            
            if not usable_items:
                console.print("[bold yellow]Você não tem itens utilizáveis em batalha.[/bold yellow]")
                time.sleep(1.5)
                continue
            
            item_options = {}
            for i, item_name in enumerate(usable_items):
                console.print(f"  [{i+1}] {item_name}")
                item_options[str(i+1)] = item_name
            
            item_choice_input = console.input("[bold blue]Escolha o número do item (ou '0' para cancelar): [/bold blue]").strip()

            if item_choice_input == '0':
                console.print("[bold yellow]Ação de item cancelada.[/bold yellow]")
                time.sleep(1)
                continue
            
            chosen_item_name = item_options.get(item_choice_input)

            if chosen_item_name:
                player_obj.usar_item(chosen_item_name)
                turn_taken = True
                time.sleep(1)
            else:
                console.print("[bold red]Escolha de item inválida![/bold red]")
                time.sleep(1.5)
                continue
        else:
            console.print("[bold red]Ação inválida. Tente novamente.[/bold red]")
            time.sleep(1.5)
            continue

        if enemy_obj.hp <= 0:
            console.print(f"\n[bold green]{enemy_obj.nome} foi derrotado![/bold green] 🎉")
            player_obj.gold += enemy_obj.gold
            player_obj.add_xp(enemy_obj.xp)
            console.print(f"[bold yellow]Você ganhou {enemy_obj.gold} de ouro e {enemy_obj.xp} de XP![/bold yellow]")
            break

        if turn_taken:
            console.print(f"\n[bold yellow]--- Turno de {enemy_obj.nome} ---[/bold yellow]")
            enemy_obj.attack_player(player_obj)
            time.sleep(1.5)
        else:
            pass
    player_obj.temp_atk_buff = 0 
    if player_obj.hp <= 0:
        console.print("\n[bold red]VOCÊ FOI DERROTADO![/bold red] 💀")
        console.print("[bold red]Fim de Jogo.[/bold red]")
        sys.exit()
    else:
        console.print("\n[bold green]Você saiu vitorioso da batalha![/bold green] 🏆")
        console.input("\nPressione Enter para continuar...")

def encontro_aleatorio():

    inimigo_tipos = {
        'dragao': {
            'nome': 'Dragão',
            'ascii_art': ascii.dragon,
            'a1': 'Mordida',
            'a2': 'Bola de Fogo',
        },
        'esqueleto': {
            'nome': 'Esqueleto',
            'ascii_art': ascii.esqueleto, 
            'a1': 'Soco',
            'a2': 'Jogar Ossos',
        },
        'lobo': {
            'nome': 'Lobo',
            'ascii_art': ascii.lobo, 
            'a1': 'Aranhão',
            'a2': 'Mordida',
        }
    }
    if 1 <= play.nivel <= 5:
        hp_range = (50, 100)
        atk_range = (10, 25)
        xp_range = (100, 250)
        gold_range = (1, 15)
        nivel_range = (1, 5)
        tipo_escolhido = random.choice(list(inimigo_tipos.keys()))
        dados_inimigo = inimigo_tipos['esqueleto'or'lobo']
        hp_aleatorio = random.randint(*hp_range)
        atk_aleatorio = random.randint(*atk_range)
        xp_aleatorio = random.randint(*xp_range)
        gold_aleatorio = random.randint(*gold_range)
        nivel_aleatorio = random.randint(*nivel_range)
        novo_inimigo = Inimigo(
            nome=dados_inimigo['nome'],
            hp=hp_aleatorio,
            atk=atk_aleatorio,
            xp=xp_aleatorio,
            gold=gold_aleatorio,
            ascii_art=dados_inimigo['ascii_art'],
            nivel=nivel_aleatorio,
            a1=dados_inimigo['a1'],
            a2=dados_inimigo['a2']
        )
    
    elif 6 <= play.nivel <= 10:
        hp_range = (125, 200)
        atk_range = (15, 25)
        xp_range = (125, 400)
        gold_range = (100, 150)
        nivel_range = (5, 10)
        tipo_escolhido = random.choice(list(inimigo_tipos.keys()))
        dados_inimigo = inimigo_tipos['esqueleto'or'lobo']
        hp_aleatorio = random.randint(*hp_range)
        atk_aleatorio = random.randint(*atk_range)
        xp_aleatorio = random.randint(*xp_range)
        gold_aleatorio = random.randint(*gold_range)
        nivel_aleatorio = random.randint(*nivel_range)
        novo_inimigo = Inimigo(
            nome=dados_inimigo['nome'],
            hp=hp_aleatorio,
            atk=atk_aleatorio,
            xp=xp_aleatorio,
            gold=gold_aleatorio,
            ascii_art=dados_inimigo['ascii_art'],
            nivel=nivel_aleatorio,
            a1=dados_inimigo['a1'],
            a2=dados_inimigo['a2']
        )
    
    return novo_inimigo

play = None
def menu():
    global play
    while play is None:
        clear()
        console.print("[bold cyan]BEM-VINDO AO JOGO![/bold cyan]")
        console.print("[1] Novo Jogo")
        console.print("[2] Carregar Jogo")
        console.print("[3] Sair")
        initial_choice = console.input("[bold blue]Escolha uma opção: [/bold blue]")
        if initial_choice == '1':
            player_name = console.input("Qual o nome do seu herói? ")
            play = Player(nome=player_name, hp_max=100, str=10, int_stat=10, con=10, atk=10, max_mana=50, gold=0, xp_max=100, xp=0, nivel=1, atk_mana=10, x=1, y=1)
            console.print(f"[bold green]Bem-vindo, {play.nome}![/bold green]")
            time.sleep(1.5)
        elif initial_choice == '2':
            loaded_player = Player.load_game() 
            if loaded_player:
                play = loaded_player 
            else:
                console.print("[bold yellow]Não foi possível carregar o jogo. Por favor, tente novamente ou inicie um Novo Jogo.[/bold yellow]")
                time.sleep(2)
        elif initial_choice == '3':
            console.print("[bold yellow]Saindo do jogo... Até mais![/bold yellow]")
            sys.exit()
        else:
            console.print("[bold red]Opção inválida. Por favor, escolha novamente.[/bold red]")
            time.sleep(1.5)
    while True:
        clear()
        play.inventario.append('Vara de Pescar')
        play.mapa()
menu()