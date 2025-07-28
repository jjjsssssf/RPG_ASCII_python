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
        self.javali = r'''              _,-""""-..__
         |`,-'_. `  ` ``  `--'""".
         ;  ,'  | ``  ` `  ` ```  `.
       ,-'   ..-' ` ` `` `  `` `  ` |==.
     ,'    ^    `  `    `` `  ` `.  ;   \
    `}_,-^-   _ .  ` \ `  ` __ `   ;    #
       `"---"' `-`. ` \---""`.`.  `;
                  \\` ;       ; `. `,
                   ||`;      / / | |
                  //_;`    ,_;' ,_;"'''
        self.av = r'''[bold blue]         .-;':':'-.
        {'.'.'.'.'.}
         )        '`.
        '-. ._ ,_.-='
          `). ( `);(
          ('. .)(,'.)
           ) ( ,').(
          ( .').'(').
          .) (' ).('
           '  ) (  ).
            .'( .)'              .).'
'''
        self.sharq = r'''[bold blue] _________         .    .
(..       \_    ,  |\  /|
 \       O  \  /|  \ \/ /
  \______    \/ |   \  / 
     vvvv\    \ |   /  |
     \^^^^  ==   \_/   |
      `\_   ===    \.  |
      / /\_   \ /      |
      |/   \_  \|      /
             \________/'''
        self.lobo = r"""[bold white]        _
       / \      _-'
     _/|  \-''- _ /
__-' { |          \
    /              \
    /       "o.  |o }
    |            \ ;
                  ',
       \_         __\
         ''-_    \.//
           / '-____'
          /
        _'
      _-' """
        self.dragon = r'''[bold white]
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
        self.esqueleto = r'''[bold white]           ______
        .-"      "-.
       /            \
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`[/bold white]'''
        self.floresta = r"""
        /\ /\ /\ /\ /\ /\ /\ /\ /\
        /\ /\ /\ /\ /\ /\ /\ /\ /\
        /\ /\ /\ /\ /\ /\ /\ /\ /\
#### #  || || || || || || || || || #####
"""
        self.igreja = r'''            +
           /_\
 ,%%%______|O|
 %%%/_________\
 `%%| /\[][][]|%
___||_||______|%&,__'''
        self.cemiterio = r'''      ,-=-.       ______     _
     /  +  \     />----->  _| |_
     | ~~~ |    // -/- /  |_   _|
     |R.I.P|   //  /  /     | |
\vV,,|_____|V,//_____/VvV,v,|_|/,,,,vVv/,'''
        self.porta = r'''|Abandone Sua Esperança|
        ______
     ,-' ;  ! `-.
    / :  !  :  . \
   |_ ;   __:  ;  |
   )| .  :)(.  !  |
   |"    (##)  _  |
   |  :  ;`'  (_) (
   |  :  :  .     |
   )_ !  ,  ;  ;  |
   || .  .  :  :  |
   |" .  |  :  .  |
   |____.----.____|'''

ascii = art()

class dialogos:
    def __init__(self):
        self.inicil1 = '''Você ultimamente não esta bem está com
estranhas sensações de medo e anciedade
se sentindo perdido e vai para uma 
floresta densa'''
        self.padre = """Você vê um padre quase morto sofrendo 
com um ferimento estranho na sua bariga
você se aproxima"""
        self.padre_ora = '''Você coloca sua Cruz na cabeça do padre
e ele é iluminado com uma luz muito 
forte e seu corpo e levado para o Céu'''
        self.padre_ora_1 = '''Você Precisa do Crucifixo para Orar'''
        self.padre_mata = '''Você finaliza o padre o matando de vez
selando seu sofrimento para sempre'''
        self.cruz = '''Você se aproxima de um estranho Crucifixo
jogado no chão com um pouco de sangue
o manchando você o pega e guarda '''
        self.poram = '''Você vai para o porão e você uma
grande porta escristo 'Abandone Sua Esperança' '''

    def exibir_texto_lento(self, texto, atraso=0.05):
        for caractere in texto:
            sys.stdout.write(caractere)
            sys.stdout.flush() 
            time.sleep(atraso)
        console.print("[bold white]")

dd = dialogos()

class Item:
    def __init__(self, nome: str, tipo: str, custo_compra: int, preco_venda: int,
                 descricao: str = "", slot_equipamento: str = None, efeitos_uso: dict = None,
                 efeitos_equipamento: dict = None, usavel_em_batalha: bool = False,
                 compravel: bool = True, vendavel: bool = True): 
        self.nome = nome
        self.tipo = tipo
        self.custo_compra = custo_compra
        self.preco_venda = preco_venda
        self.descricao = descricao
        self.slot_equipamento = slot_equipamento
        self.efeitos_uso = efeitos_uso if efeitos_uso is not None else {}
        self.efeitos_equipamento = efeitos_equipamento if efeitos_equipamento is not None else {}
        self.usavel_em_batalha = usavel_em_batalha
        self.compravel = compravel
        self.vendavel = vendavel 

class Player:
    def __init__(self, nome, hp_max, str, int_stat, atk, max_mana, gold, xp_max, xp, nivel, atk_mana, x, defesa):
        self.nome = nome
        self.hpmax = hp_max
        self.hp = self.hpmax
        self.str = str
        self.defesa = defesa
        self.ini = int_stat
        self.atk = atk
        self.max_mana = max_mana
        self.mana = self.max_mana
        self.atk_mana = atk_mana
        self.gold = gold
        self.xp_max = xp_max
        self.hit_chance = 75
        self.xp = xp
        self.nivel = nivel
        self.x = x
        self.running = True
        self.itens_coletaodos = {
            "Floresta": False,
            "Padre": False,
            "Cruz": False,
            "Cemiterio": False,
            "Crucifixo": False,
        }
        self.inventario = []
        self.mana_list = []
        self.equipado = {
            "Mão Primária": None,
            'Mão Secundária': None,
            "Cabeça": None,
            "Peito": None,
            "Sacrados": None,
        }
        self.temp_atk_buff = 0
        self.temp_def_buff = 0
        self.tempo_inicio_jogo = time.time() 
        self.todos_itens = {
            "Pomada de Regeneração": Item(
                "Pomada de Regeneração", "consumivel", 50, 25,
                "Um item que pode recuperar sua vida em 30 pontos.",
                efeitos_uso={"hp": 30},
                usavel_em_batalha=True
            ),
            "Espada Curta": Item(
                "Espada Curta", "equipavel", 100, 50,
                "Uma espada básica.", "Mão Primária",
                efeitos_equipamento={"atk": 10},
                usavel_em_batalha=False 
            ),
            "Espada Longa": Item(
                "Espada Longa", "equipavel", 200, 100,
                "Uma espada pesada e poderosa.", "Mão Primária",
                efeitos_equipamento={"atk": 20, "str": 5},
                usavel_em_batalha=False 
            ),
            "Cajado Velho": Item(
                "Cajado Velho", "equipavel", 100, 50,
                "Um cajado antigo, mas útil.", "Mão Primária",
                efeitos_equipamento={"atk_mana": 10},
                usavel_em_batalha=False
            ),
            "Cajado Iniciante": Item(
                "Cajado Iniciante", "equipavel", 200, 100,
                "Um cajado bom para quem está começando na magia.", "Mão Primária",
                efeitos_equipamento={"atk_mana": 20, "ini": 5},
                usavel_em_batalha=False 
            ),
            "Escudo": Item(
                "Escudo", "equipavel", 100, 50,
                "Um escudo de madeira simples.", "Mão Secundária",
                efeitos_equipamento={"hpmax": 5, "defesa": 2},
                usavel_em_batalha=False 
            ),
            "Escudo Forte": Item(
                "Escudo Forte", "equipavel", 200, 100,
                "Um escudo resistente de metal.", "Mão Secundária",
                efeitos_equipamento={"hpmax": 15, "defesa": 5},
                usavel_em_batalha=False 
            ),
            "Anel": Item(
                "Anel", "equipavel", 100, 50,
                "Um anel mágico.", "Mão Secundária",
                efeitos_equipamento={"atk_mana": 5, "ini": 2},
                usavel_em_batalha=False
            ),
            "Colar": Item(
                "Colar", "equipavel", 200, 100,
                "Um colar encantado.", "Mão Secundária",
                efeitos_equipamento={"atk_mana": 15, "ini": 5},
                usavel_em_batalha=False 
            ),
            "Capacete": Item(
                "Capacete", "equipavel", 100, 50,
                "Um capacete de metal.", "Cabeça",
                efeitos_equipamento={"hpmax": 5, "defesa": 2},
                usavel_em_batalha=False
            ),
            "Capuz": Item(
                "Capuz", "equipavel", 100, 50,
                "Um capuz de tecido.", "Cabeça",
                efeitos_equipamento={"defesa": 2, "mana": 5},
                usavel_em_batalha=False 
            ),
            "Peitoral": Item(
                "Peitoral", "equipavel", 150, 75,
                "Uma armadura de peito resistente.", "Peito",
                efeitos_equipamento={"hpmax": 10, "defesa": 5},
                usavel_em_batalha=False 
            ),
            "Manto": Item(
                "Manto", "equipavel", 150, 75,
                "Um manto mágico.", "Peito",
                efeitos_equipamento={"defesa": 5, "mana": 10},
                usavel_em_batalha=False
            ),
            "Livro de Magias": Item(
                "Livro de Magias", "consumivel", 300, 0,
                "Um livro que aumenta sua inteligência.",
                efeitos_uso={"ini": 1},
                usavel_em_batalha=False
            ),
            "Batata": Item(
                "Batata", "consumivel", 10, 5,
                "Uma batata crua. Pode ser cozida.",
                efeitos_uso={"hp": 10},
                usavel_em_batalha=False,compravel= False
            ),
            "Batata Cozida": Item(
                "Batata Cozida", "consumivel", 15, 7,
                "Uma batata cozida que restaura vida.",
                efeitos_uso={"hp": 30},
                usavel_em_batalha=True, compravel= False
            ),
            "Caldeiram": Item(
                "Caldeiram", "ferramenta", 250, 25,
                "Um caldeirão para cozinhar alimentos.",
                usavel_em_batalha=False 
            ),
            "Água": Item(
                "Água", "consumivel", 50,25,
                "Pode tomar e recuperar suas Forças",
                efeitos_uso={"mana": 10}, usavel_em_batalha=True
            ),
            "Elixir": Item(
                "Elixir", "consumivel", 300,0,
                "Um Elixir que aumenta sua força.",
                efeitos_uso={"str": 1}, usavel_em_batalha=False
            ),
            "Ovo": Item(
                "Ovo", "consumivel", 10, 5,
                "Um Ovo cru. Pode ser Frito.",
                efeitos_uso={"hp": 5},
                usavel_em_batalha=False, compravel= False
            ),
            "Ovo Frito": Item(
                "Ovo Frito", "consumivel", 10, 5,
                "Um Ovo Frito. Pode ser consumido.",
                efeitos_uso={"hp": 20},
                usavel_em_batalha=True,compravel=False
            ),
            "Carne": Item(
                "Carne", "consumivel", 10, 5,
                "Uma carne crua. Pode ser cozida.",
                efeitos_uso={"hp": 15},
                usavel_em_batalha=False,compravel= False
            ),
            "Carne Cozida": Item(
                "Carne Cozida", "consumivel", 10, 5,
                "Uma carne cozida. Pode ser consumido.",
                efeitos_uso={"hp": 40},
                usavel_em_batalha=True,compravel=False
            ),
            "Osso Rachado": Item(
                nome="Osso Rachado", tipo="material",custo_compra=100,
                preco_venda=25, descricao="Um osso velho que pode ser usado",
                usavel_em_batalha=False,compravel=False
            ),
            "Presas de Lobo": Item(
                nome="Presas de Lobo", tipo="material",custo_compra=150,
                preco_venda=50, descricao="Uma presa de lobo forte que pode ser usado",
                compravel=False
            ),
            "Crucifixo": Item(
                nome="Crucifixo", tipo="equipavel", custo_compra= 200, preco_venda=100,
                descricao="Uma Cruz Sacrada que contem um dos Espinho da coroa de Cristo",
                slot_equipamento="Sacrados", efeitos_equipamento= {"atk_mana": 15, "ini": 5, "mana":20},
                compravel= False, vendavel=False
            ),
        }
    
    def save_game(self, filename="DEMO.json"):
        player_data = {
            "nome": self.nome,
            "hpmax": self.hpmax,
            "hp": self.hp,
            "str": self.str,
            "ini": self.ini,
            "atk": self.atk,
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
            "temp_def_buff": self.temp_def_buff,
            "x": self.x,
            "coletados": self.itens_coletaodos,
            "tempo_inicio_jogo": self.tempo_inicio_jogo,
            "defesa": self.defesa
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
                atk=player_data["atk"],
                max_mana=player_data["max_mana"],
                gold=player_data["gold"],
                xp_max=player_data["xp_max"],
                xp=player_data["xp"],
                nivel=player_data["nivel"],
                atk_mana=player_data["atk_mana"],
                x=player_data["x"],
                defesa=player_data["defesa"],
            )
            player.hp = player_data["hp"]
            player.hit_chance = player_data["hit_chance"]
            player.inventario = player_data["inventario"]
            player.mana_list = player_data["mana_list"]
            player.equipado = player_data["equipado"]
            player.itens_coletaodos = player_data["coletados"]
            player.temp_atk_buff = player_data["temp_atk_buff"]
            player.temp_def_buff = player_data["temp_def_buff"]
            if "tempo_inicio_jogo" in player_data:
                player.tempo_inicio_jogo = player_data["tempo_inicio_jogo"]
            else:
                player.tempo_inicio_jogo = time.time()
            console.print(f"[bold green]Jogo carregado com sucesso de '{filename}'![/bold green]")
            return player
        except (IOError, json.JSONDecodeError) as e:
            console.print(f"[bold red]Erro ao carregar o jogo: {e}. Iniciando novo jogo.[/bold red]")
            time.sleep(1.5)
            return None

    def _formatar_tempo(self, segundos):
        horas = int(segundos // 3600)
        minutos = int((segundos % 3600) // 60)
        segundos_restantes = int(segundos % 60)
        return f"{horas:02}:{minutos:02}:{segundos_restantes:02}"

    def adicionar_item(self, nome_do_item: str):
        if nome_do_item in self.todos_itens:
            item_a_adicionar = self.todos_itens[nome_do_item]
            self.inventario.append(item_a_adicionar)
            console.print(f"{item_a_adicionar.nome}, foi adicionado ao inventario")
            time.sleep(2)
        else:
            print(f"Erro: Item '{nome_do_item}' não encontrado nas definições do jogo.")
            time.sleep(2)

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

    def menu(self):
        while True:
            clear()
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print('[bold white][1]Status    [2]Inventario\n[3]Salvar    [4]Livro de Pesca\n[5]Aprender    [6]Magias\n[7]Sair    [8]Sair do Jogo[/bold white]') 
            console.print(f'[bold yellow]+'+'-'*45+'+')
            menu_esc = input("=>")
            if menu_esc == '1' or menu_esc == 'Status':
                self.status()
                input()
            elif menu_esc == '2' or menu_esc == 'Inventario':
                self.menu_inventario()
            elif menu_esc == '3' or menu_esc == 'Salva':
                self.save_game()
            elif menu_esc == '4' or menu_esc == 'Livro':
                self.pescar_livro()
            elif menu_esc == '5' or menu_esc == 'Aprender':
                self.aprender_magia()
            elif menu_esc == '6' or menu_esc == 'Magias':
                self.list_mana()
            elif menu_esc == '7' or menu_esc == 'Sair':
                break
            elif menu_esc == '8' or menu_esc == 'Jogo':
                exit()

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
        stra = self.str // 4
        current_atk = self.atk + self.temp_atk_buff + stra
        if roll <= self.hit_chance:
            damage = random.randint(int(current_atk - 3), int(current_atk + 3))
            damage = max(1, damage)
            enemy.take_damage(damage)
            console.print(f"[bold green]{self.nome} atacou {enemy.nome} e causou {damage} de dano![/bold green]")
        else:
            console.print(f"[bold yellow]{self.nome} errou o ataque em {enemy.nome}![/bold yellow]")
        time.sleep(1)

    def list_mana(self):
        while True:
            clear()
            console.print("\n[bold cyan]=== MENU DE MAGIAS ===[/bold cyan]")
            console.print("  [1] Ver Magias")
            console.print("  [2] Usar Magia (digite o nome da magia)")
            console.print("  [3] Sair")
            escolha = input("=> ").strip()
            if escolha == '1':
                if not self.mana_list:
                    console.print("[bold yellow]Você não possui nenhuma magia no momento.[/bold yellow]")
                else:
                    console.print("[bold magenta]--- Suas Magias ---[/bold magenta]")
                    spell_info = {
                        "Bola de Fogo": {"custo": 10, "efeito": "Causa dano mágico."},
                        "Cura": {"custo": 15, "efeito": "Restaura pontos de vida."},
                        "Espada Sacrada": {"custo": 20, "efeito": "Aumenta seu ataque temporariamente."},
                        "Dança dos Escudos": {"custo": 20, "efeito": "Aumenta sua defesa temporariamente."},
                        "Raio": {"custo": 20, "efeito": "Causa dano mágico."},
                        "Cristais de Gelo": {"custo": 15, "efeito": "Causa dano mágico."},
                        "Ira": {"custo": 15, "efeito": "Aumenta seu ataque temporariamente."},
                        "Machado Ancestral":{"custo":35,"efeito":"Aumenta seu ataque temporariamente."},
                        "Sangria": {"custo":50, "efeito": "Aumenta seu ataque em 2x mas metade de sua vida reduz"}
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
        bola_de_fogo_base_damage = self.atk_mana * 1.5
        cura_base_heal = 20
        espada_sacrada_buff_amount = 10
        danca_dos_escuados = 10
        reza = 10

        if nome_mana not in self.mana_list:
            console.print(f"[bold red]Você não possui a '{nome_mana}'.[/bold red]")
            return False
        if nome_mana == 'Cruz Sacrada':
            mana_cost = 10
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                roll = random.randint(1, 100)
                if roll <= self.hit_chance:
                    init = self.ini // 4
                    atk = bola_de_fogo_base_damage + init
                    damage = random.randint(int(atk - 3), int(atk + 3))
                    damage = max(1, damage)
                    enemy.take_damage(damage)
                    console.print(f"[bold green]{self.nome} atacou {enemy.nome} e causou {damage} de dano com Cruz Sagrada![/bold green]")
                    return True
                else:
                    console.print(f"[bold yellow]{self.nome} errou o ataque de fé em {enemy.nome}![/bold yellow]")
                    return True
            else:
                console.print("[bold red]Vontade insuficiente para usar Cruz Sagrada![/bold red]")
                return False
        
        elif nome_mana == 'Cura':
            mana_cost = 15
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                curar = self.ini // 4
                cura =  cura_base_heal + curar
                healed_amount = random.randint(int(cura - 3), int(cura + 3))
                self.hp = min(self.hpmax, self.hp + healed_amount)
                console.print(f'[bold green]Você se curou em {healed_amount}! Sua Vitalidade atual é {self.hp}/{self.hpmax}[/bold green]')
                return True
            else:
                console.print("[bold red]Vontade insuficiente para usar Cura![/bold red]")
                return False
        
        elif nome_mana == 'Espada Sacrada':
            mana_cost = 20
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                espada = self.ini // 4
                up = espada_sacrada_buff_amount + espada
                self.temp_atk_buff += int(up)
                console.print(f'[bold green]Você ativou Espada Sacrada! e sua Força aumentou em {up} para esta batalha.[/bold green]')
                return True
            else:
                console.print("[bold red]Vontade insuficiente para usar Espada Sacrada![/bold red]")
                return False
    
        elif nome_mana == 'Dança dos Escudos':
            mana_cost = 20  
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                self.temp_def_buff += danca_dos_escuados
                console.print(f'[bold green]Você ativou Dança dos Escudos! Sua DEF aumentou em {danca_dos_escuados} para esta batalha.[/bold green]')
                return True
            else:
                console.print("[bold red]Mana insuficiente para usar Dança dos Escudos![/bold red]")
                return False


        return False

    def shop(self):
        while True:
            clear()
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print('[bold cyan]Bem Vindo ao Mercado[/bold cyan]')
            console.print("   [1]Comprar")
            console.print("   [2]Vender")
            console.print("   [3]Sair")
            console.print(f'[bold yellow]+'+'-'*45+'+')
            escolha = input('=> ')
            if escolha == '3':
                break
            elif escolha == '1': # Lógica de compra
                while True:
                    clear()
                    console.print(f'[bold yellow]+'+'-'*45+'+')
                    console.print(f"[bold cyan]Ouro: {self.gold}[/bold cyan]")
                    console.print('   [1]Consumíveis:\n   [2]Equipamentos\n   [3]Ferramentas')
                    console.print(f'[bold blue]Escolha uma opção: [0 para sair][/bold blue]')
                    console.print(f'[bold yellow]+'+'-'*45+'+')
                    esc = input('=> ')
                    if esc == '0':
                        break
                    categoria_selecionada = ""
                    if esc == '1':
                        categoria_selecionada = "consumivel"
                    elif esc == '2':
                        categoria_selecionada = "equipavel"
                    elif esc == '3':
                        categoria_selecionada = "ferramenta"
                    else:
                        console.print("[bold red]Opção inválida.[/bold red]")
                        time.sleep(1)
                        continue
                    itens_na_categoria = [item for item in self.todos_itens.values()
                                          if item.tipo == categoria_selecionada and item.compravel]
                    while True:
                        clear()
                        console.print(f'[bold yellow]+'+'-'*45+'+')
                        console.print(f"[bold cyan]Ouro: {self.gold}[/bold cyan]")
                        if not itens_na_categoria:
                            console.print("[bold yellow]Não há itens nesta categoria para comprar.[/bold yellow]")
                            time.sleep(1)
                            break
                        for i, item_obj in enumerate(itens_na_categoria):
                            console.print(f"[{i+1}] {item_obj.nome}: [bold green]{item_obj.custo_compra} Ouro[/bold green]")
                        console.print(f'[bold blue]Escolha um item para comprar: [0 para sair][/bold blue]')
                        console.print(f'[bold yellow]+'+'-'*45+'+')
                        compra_escolha = input('=> ')
                        if compra_escolha == '0':
                            break
                        try:
                            indice_escolhido = int(compra_escolha) - 1
                            if 0 <= indice_escolhido < len(itens_na_categoria):
                                item_a_comprar = itens_na_categoria[indice_escolhido]
                                clear()
                                console.print(f'[bold yellow]+'+'-'*45+'+')
                                console.print(f'[bold yellow]Descrição: {item_a_comprar.descricao}\nDeseja comprar:\n [1]Sim\n [2]Não[/bold yellow]')
                                console.print(f'[bold yellow]+'+'-'*45+'+')
                                confirmar_compra = input('=> ')

                                if confirmar_compra == '1':
                                    if not item_a_comprar.compravel:
                                        console.print(f"[bold red]Este item ('{item_a_comprar.nome}') não está disponível para compra.[/bold red]")
                                        time.sleep(2)
                                        continue 
                                    if self.gold >= item_a_comprar.custo_compra:
                                        self.gold -= item_a_comprar.custo_compra
                                        self.inventario.append(item_a_comprar)
                                        console.print(f"[bold green]Você comprou {item_a_comprar.nome}![/bold green]")
                                    else:
                                        console.print("[bold red]Você não possui ouro suficiente.[/bold red]")
                                    time.sleep(1)
                                elif confirmar_compra == '2':
                                    pass
                                else:
                                    console.print("[bold red]Opção inválida.[/bold red]")
                                    time.sleep(1)
                            else:
                                console.print("[bold red]Opção inválida.[/bold red]")
                                time.sleep(1)
                        except ValueError:
                            console.print("[bold red]Por favor, digite um número válido.[/bold red]")
                            time.sleep(1)

            elif escolha == '2': # Lógica de venda
                while True:
                    clear()
                    console.print(f'[bold yellow]+'+'-'*45+'+')
                    console.print(f"[bold cyan]Ouro: {self.gold}[/bold cyan]")
                    console.print("[bold cyan]--- Seu Inventário para Venda ---[/bold cyan]")
                    itens_vendaveis_no_inventario = [item for item in self.inventario if item.vendavel]
                    if not itens_vendaveis_no_inventario:
                        console.print("[bold yellow]Você não tem itens vendáveis no seu inventário.[/bold yellow]")
                        time.sleep(1)
                        break
                    contagem_inventario = {}
                    for item_obj in itens_vendaveis_no_inventario:
                        contagem_inventario[item_obj.nome] = contagem_inventario.get(item_obj.nome, 0) + 1
                    itens_para_vender_opcoes = []
                    for i, (nome_item, count) in enumerate(contagem_inventario.items()):
                        item_original = self.todos_itens[nome_item]
                        preco_venda = item_original.preco_venda
                        itens_para_vender_opcoes.append((item_original, count, preco_venda))
                        console.print(f"   [{i+1}]{item_original.nome} (x{count}) - Vender por: [green]{preco_venda} Ouro[/green]")
                    
                    console.print(f'[bold blue]Escolha um item para vender: [0 para sair][/bold blue]')
                    console.print(f'[bold yellow]+'+'-'*45+'+')
                    escolha_venda = input('=> ')
                    if escolha_venda == '0':
                        break
                    try:
                        indice_escolhido = int(escolha_venda) - 1
                        if 0 <= indice_escolhido < len(itens_para_vender_opcoes):
                            item_a_vender_obj, quantidade_disponivel, preco_venda = itens_para_vender_opcoes[indice_escolhido]                            
                            esta_equipado = False
                            for slot, item_equipado_obj in self.equipado.items():
                                if item_equipado_obj is not None and item_equipado_obj.nome == item_a_vender_obj.nome:
                                    esta_equipado = True
                                    break
                            
                            if esta_equipado:
                                console.print(f"[bold red]Você não pode vender um item que está equipado. Desequipe '{item_a_vender_obj.nome}' primeiro.[/bold red]")
                                time.sleep(2)
                                continue 
                            clear()
                            console.print(f'[bold yellow]+'+'-'*45+'+')
                            console.print(f"[bold yellow]Deseja vender {item_a_vender_obj.nome} por {preco_venda} Ouro?\n [1]Sim\n [2]Não[/bold yellow]")
                            console.print(f'[bold yellow]+'+'-'*45+'+')
                            confirmar_venda = input('=> ')

                            if confirmar_venda == '1':

                                if not item_a_vender_obj.vendavel:
                                    console.print(f"[bold red]Este item ('{item_a_vender_obj.nome}') não pode ser vendido.[/bold red]")
                                    time.sleep(2)
                                    continue 
                                try:
                                    self.inventario.remove(item_a_vender_obj)
                                    self.gold += preco_venda
                                    console.print(f"[bold green]Você vendeu {item_a_vender_obj.nome} por {preco_venda} Ouro![/bold green]")
                                except ValueError:
                                    console.print("[bold red]Item não encontrado no inventário.[/bold red]")
                                time.sleep(1)
                            elif confirmar_venda == '2':
                                pass
                            else:
                                console.print("[bold red]Escolha inválida.[/bold red]")
                                time.sleep(1)
                        else:
                            console.print("[bold red]Escolha inválida.[/bold red]")
                            time.sleep(1)
                    except ValueError:
                        console.print("[bold red]Por favor, digite um número válido.[/bold red]")
                        time.sleep(1)
            else:
                console.print("[bold red]Opção inválida. Por favor, escolha 1 para comprar, 2 para vender ou 3 para sair.[/bold red]")
                time.sleep(1)
    
    def status(self):
        white = '[bold white]'
        tempo_decorrido = time.time() - self.tempo_inicio_jogo
        tempo_formatado = self._formatar_tempo(tempo_decorrido)
        tempo_decorrido = time.time() - self.tempo_inicio_jogo
        tempo_formatado = self._formatar_tempo(tempo_decorrido)
        console.print(f'[bold yellow]+'+'-'*45+'+')
        console.print(f"[bold cyan]Nome:{self.nome}[bold cyan]")
        console.print(f"Vitalidade:[{self.hpmax}]/[{self.hp}] Resistencia:[{self.defesa}]")
        console.print(f"Vontade:[{self.max_mana}]/[{self.mana}] Fé:[{self.atk_mana}] Razão:[{self.ini}]")
        console.print(f"Violencia:[{self.str}]    Força:[{self.atk}]")
        console.print(f"Nivel:[{self.nivel}]         xp[{self.xp_max}]/[{self.xp}]")
        console.print(f"{white}TIME:[bold yellow]{tempo_formatado}[/bold yellow]")
        console.print(f'[bold yellow]+'+'-'*45+'+')

    def info_batalha(self):
        console.print(f"[bold cyan]{self.nome} (Nível {self.nivel})[/bold cyan]")
        console.print(f"[bold green]Vitalidade:[{self.hpmax}]/[{self.hp}] | Resistencia:[{self.defesa}][/bold green]")
        console.print(f"Vontade:[{self.max_mana}]/[{self.mana}]")
        console.print(f"[bold red]Força:[{self.atk}][/bold red] | [bold cyan]Fé:[{self.atk_mana}][/bold cyan]")
        console.print(f"[bold red]Buff:[{self.temp_atk_buff}][/bold red] | [bold cyan]Buff:[{self.temp_def_buff}][/bold cyan]")

    def ops(self):
        while True:
            clear()
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print(f'[1]Menu [2]Ajuda')
            console.print(f'[3]Sair [4]EXIT')
            console.print(f'[bold yellow]+'+'-'*45+'+')
            ops = input("=>")
            if ops == '1':
                self.menu()
            elif ops == '2':
                self.ajuda()
            elif ops == '3':
                break
            elif ops == '4':
                exit()

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
                self.defesa +=1
                self.max_mana += 5
                self.mana = self.max_mana
                self.atk_mana += 3
            time.sleep(1)

    def add_xp(self, amount):
        self.xp += amount
        console.print(f"[bold blue]Você ganhou {amount} de XP![/bold blue]")
        self.up()
        time.sleep(1)

    def usar_item(self, item_obj: 'Item'): 
        if not isinstance(item_obj, Item) or item_obj not in self.inventario:
            console.print(f"[bold red]Item '{item_obj.nome if isinstance(item_obj, Item) else item_obj}' não encontrado no seu inventário.[/bold red]")
            time.sleep(1)
            return
        if item_obj.tipo == "consumivel":
            for efeito, valor in item_obj.efeitos_uso.items():
                if efeito == "hp":
                    self.hp = min(self.hpmax, self.hp + valor)
                    console.print(f"[bold green]Você usou {item_obj.nome} e recuperou {valor} HP![/bold green]")
                elif efeito == "mana":
                    self.mana = min(self.max_mana, self.mana + valor)
                    console.print(f"[bold green]Você usou {item_obj.nome} e recuperou {valor} MP![/bold green]")
                elif efeito == "ini":
                    self.ini += valor
                    console.print(f"[bold green]Você usou {item_obj.nome} e ganhou {valor} de Inteligência![/bold green]")
                elif efeito == "str":
                    self.str += valor
                    console.print(f"[bold green]Você usou {item_obj.nome} e ganhou {valor} de Força![/bold green]")
            self.inventario.remove(item_obj)
            time.sleep(1)
        elif item_obj.tipo == "equipavel":
            if item_obj.slot_equipamento:
                if self.equipado[item_obj.slot_equipamento] is None:
                    self.inventario.remove(item_obj)
                    self.equipado[item_obj.slot_equipamento] = item_obj
                    for efeito, valor in item_obj.efeitos_equipamento.items():
                        if efeito == "atk":
                            self.atk += valor
                        elif efeito == "defesa":
                            self.defesa += valor
                        elif efeito == "hpmax":
                            self.hpmax += valor
                            self.hp += valor 
                        elif efeito == "mana":
                            self.mana += valor
                        elif efeito == "atk_mana":
                            self.atk_mana += valor
                        elif efeito == "ini":
                            self.ini += valor
                        elif efeito == "str":
                            self.str += valor
                    console.print(f"[bold green]Você equipou o {item_obj.nome} no slot {item_obj.slot_equipamento}![/bold green]")
                else:
                    console.print(f"[bold yellow]Você já tem {self.equipado[item_obj.slot_equipamento].nome} equipado no slot {item_obj.slot_equipamento}. Desequipe-o primeiro.[/bold yellow]")
            else:
                console.print(f"[bold red]Este item equipável não tem um slot definido.[/bold red]")
            time.sleep(1)
        elif item_obj.tipo == "ferramenta":
            if item_obj.nome == "Caldeiram":
                while True:
                    clear()
                    console.print("[bold cyan]Caldeirão: Deseja Cozinhar?\n[1]Sim   [2]Não[/bold cyan]")
                    caldeirao_choice = input("=>")
                    if caldeirao_choice == '1':
                        console.print("[bold cyan][1]Batata Cozida\n[2]Ovo Frito\n[3]Carne Cozida[/bold cyan]")
                        coz = input("=>")
                        if coz == '1':
                            if hasattr(self, 'todos_itens'): 
                                batata_obj = self.todos_itens.get("Batata")
                                if batata_obj in self.inventario: 
                                    self.inventario.remove(batata_obj)
                                    batata_cozida_obj = self.todos_itens.get("Batata Cozida")
                                    self.inventario.append(batata_cozida_obj)
                                    console.print("[bold green]Você cozinhou uma Batata e fez uma Batata Cozida![/bold green]")
                                    time.sleep(2)
                                else:
                                    console.print("[bold yellow]Você não tem Batata para cozinhar.[/bold yellow]")
                                    time.sleep(2)
                        elif coz == '2':
                            if hasattr(self, 'todos_itens'):
                                ovo_obj = self.todos_itens.get("Ovo")
                                if ovo_obj in self.inventario:
                                    self.inventario.remove(ovo_obj)
                                    ovo_frito_obj = self.todos_itens.get("Ovo Frito")
                                    self.inventario.append(ovo_frito_obj)
                                    console.print("[bold green]Você Fritol um Ovo e fez um Ovo Frito![/bold green]")
                                    time.sleep(2)
                                else:
                                    console.print("[bold yellow]Você não tem Ovo para Fritar.[/bold yellow]")
                                    time.sleep(2)
                    elif caldeirao_choice == '2':
                        break
                    else:
                        console.print("[bold red]Opção inválida.[/bold red]")
                        time.sleep(1)
        elif item_obj.tipo == "comida":
            for efeito, valor in item_obj.efeitos_uso.items():
                if efeito == "hp":
                    self.hp = min(self.hpmax, self.hp + valor)
                    console.print(f"[bold green]Você usou {item_obj.nome} e recuperou {valor} HP![/bold green]")
            self.inventario.remove(item_obj)
            time.sleep(1)
        elif item_obj == 'material':
            if item_obj.nome == "Osso Rachado":
                console.print("[bold green]Você pode usar para fazer itens![/bold green]")
            elif item_obj.nome == "Presa de Lobo":
                console.print("[bold green]Você pode usar para fazer itens![/bold green]")

    def desequipar_item(self, slot: str):
        if slot in self.equipado and self.equipado[slot] is not None:
            item_desequipado = self.equipado[slot]
            self.inventario.append(item_desequipado)
            self.equipado[slot] = None
            for efeito, valor in item_desequipado.efeitos_equipamento.items():
                if efeito == "atk":
                    self.atk -= valor
                elif efeito == "defesa":
                    self.defesa -= valor
                elif efeito == "hpmax":
                    self.hpmax -= valor
                    self.hp = min(self.hp, self.hpmax)
                elif efeito == "mana":
                    self.mana -= valor
                elif efeito == "atk_mana":
                    self.atk_mana -= valor
                elif efeito == "ini":
                    self.ini -= valor
                elif efeito == "str":
                    self.str -= valor
            console.print(f"[bold green]Você desequipou {item_desequipado.nome} do slot {slot}.[/bold green]")
        else:
            console.print(f"[bold yellow]Não há item equipado no slot {slot}.[/bold yellow]")
        time.sleep(1)
        self.status()
    
    def menu_inventario(self):
        while True:
            clear()
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print("[bold cyan]--- SEU INVENTÁRIO ---[/bold cyan]")
            if not self.inventario and all(v is None for v in self.equipado.values()):
                console.print("[bold yellow]Seu inventário e seus slots de equipamento estão vazios.[/bold yellow]")
                time.sleep(1)
                console.print(f'[bold yellow]+'+'-'*45+'+')
                input("Pressione Enter para continuar...")
                return
            console.print("[bold blue]ITENS NO INVENTÁRIO:[/bold blue]")
            itens_agrupados = Counter(item_obj.nome for item_obj in self.inventario)
            itens_unicos_ordenados = sorted(set(self.inventario), key=lambda x: x.nome) 
            itens_listados_no_menu = []
            current_index = 0
            if self.inventario:
                for item_obj in itens_unicos_ordenados:
                    count = itens_agrupados[item_obj.nome]
                    current_index += 1
                    itens_listados_no_menu.append(item_obj) 
                    console.print(f"[{current_index}]{item_obj.nome} ({item_obj.tipo.capitalize()}) {'(' + str(count) + 'x)' if count > 1 else ''}\n{item_obj.descricao}")
            else:
                console.print("[bold yellow]Inventário (mochila) está vazio.[/bold yellow]\n")
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print("[bold blue]ITENS EQUIPADOS:[/bold blue]")
            equipados_listados = {}
            opcao_equipado_start = current_index + 1
            for slot, item_obj in self.equipado.items():
                if item_obj:
                    equipados_listados[str(opcao_equipado_start)] = (slot, item_obj)
                    console.print(f"[{opcao_equipado_start}] {slot}: {item_obj.nome}")
                    opcao_equipado_start += 1
                else:
                    console.print(f"[gray]{slot}: Vazio[/gray]")
            console.print("[bold cyan]O que você deseja fazer?[/bold cyan]")
            console.print("[1] Usar/Equipar Item do Inventário")
            console.print("[2] Desequipar Item")
            console.print("[3] Sair do Inventário")
            console.print(f'[bold yellow]+'+'-'*45+'+')
            main_choice = input('=>').strip()
            if main_choice == '3':
                break
            elif main_choice == '1':
                if not self.inventario:
                    console.print("[bold red]Seu inventário está vazio. Não há itens para usar/equipar.[/bold red]")
                    time.sleep(1.5)
                    continue
                console.print(f'[bold yellow]+'+'-'*45+'+')
                console.print("[bold blue]Qual item você deseja usar/equipar? (Digite o número)[/bold blue]")
                console.print(f'[bold yellow]+'+'-'*45+'+')
                item_choice_str = input('=>').strip()
                try:
                    chosen_index = int(item_choice_str) - 1
                    if 0 <= chosen_index < len(itens_listados_no_menu):
                        item_selecionado = itens_listados_no_menu[chosen_index]
                        self.usar_item(item_selecionado) 
                    else:
                        console.print("[bold red]Escolha inválida.[/bold red]")
                        time.sleep(1)
                except ValueError:
                    console.print("[bold red]Por favor, digite um número válido.[/bold red]")
                    time.sleep(1)
            elif main_choice == '2':
                if not any(self.equipado.values()):
                    console.print("[bold red]Você não tem nenhum item equipado para desequipar.[/bold red]")
                    time.sleep(1.5)
                    continue
                console.print(f'[bold yellow]+'+'-'*45+'+')
                console.print("[bold blue]Qual slot você deseja desequipar? (Digite o número do item equipado)[/bold blue]")
                console.print(f'[bold yellow]+'+'-'*45+'+')
                slot_choice_str = input('=>').strip()
                if slot_choice_str in equipados_listados:
                    slot_selecionado, _ = equipados_listados[slot_choice_str]
                    self.desequipar_item(slot_selecionado)
                else:
                    console.print("[bold red]Escolha inválida ou slot vazio.[/bold red]")
                    time.sleep(1)
            else:
                console.print("[bold red]Opção inválida. Por favor, escolha 1, 2 ou 3.[/bold red]")
                time.sleep(1)

class Inimigo:
    def __init__(self, nome: str, hp: int, atk: int, xp: int, gold: int, ascii_art: str, nivel: int, a1:str, a2:str, itens_drops: list[tuple[str, float]] = None):
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
        self.itens_drops = itens_drops if itens_drops is not None else []

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
        de = player.defesa // 2
        atk1 = self.atk - de
        if roll <= self.hit_chance:
            damage = random.randint(int(atk1 - 3), int(atk1 + 5))
            player.take_damage(damage)
            damage = max(1, damage)
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
    def gerar_drops(self, todos_itens: dict) -> list:
        drops_obtidos = []
        if not self.itens_drops:
            return drops_obtidos
        console.print(f"\n[bold magenta]--- Itens dropados por {self.nome} ---[/bold magenta]")
        for item_nome, chance in self.itens_drops:
            roll = random.uniform(0, 100)
            if roll <= chance:
                if item_nome in todos_itens:
                    item_obj = todos_itens[item_nome]
                    drops_obtidos.append(item_obj)
                    console.print(f"[bold green]   - {item_obj.nome} (Dropado!)[/bold green]")
                else:
                    console.print(f"[bold red]   - Erro: Item '{item_nome}' configurado para drop mas não encontrado em todos_itens.[/bold red]")
        if not drops_obtidos:
            console.print("[bold yellow]   Nenhum item foi dropado.[/bold yellow]")
        time.sleep(2)
        return drops_obtidos

def battle_system(player_obj: Player, enemy_obj: Inimigo):
    console.print("\n[bold magenta]!!! INICIANDO BATALHA !!![/bold magenta]")
    time.sleep(2)
    while player_obj.hp > 0 and enemy_obj.hp > 0:
        clear()
        enemy_obj.info()
        player_obj.info_batalha()
        console.print("[bold cyan]O que você fará?[/bold cyan]")
        console.print("[1] Atacar")
        console.print("[2] Usar Fé")
        console.print("[3] Usar Item")
        action_choice = console.input("[bold blue]Sua ação: [/bold blue]").strip()
        turn_taken = False

        if action_choice == '1':
            player_obj.attack_enemy(enemy_obj)
            turn_taken = True
        elif action_choice == '2':
            if not player_obj.mana_list:
                console.print("[bold red]Você não possui nenhuma fé para usar![/bold red]")
                time.sleep(1.5)
                continue
            
            console.print("[bold magenta]--- SUA FÉ ---[/bold magenta]")
            spell_options = {}
            for i, spell_name in enumerate(player_obj.mana_list):
                console.print(f"[{i+1}] {spell_name}")
                spell_options[str(i+1)] = spell_name
            
            magic_choice_input = console.input("[bold blue]Escolha o número da fé (ou '0' para cancelar): [/bold blue]").strip()
            
            if magic_choice_input == '0':
                console.print("[bold yellow]Ação de fé cancelada.[/bold yellow]")
                time.sleep(1)
                continue
            
            chosen_spell_name = spell_options.get(magic_choice_input)
            
            if chosen_spell_name:
                turn_taken = player_obj.usar_magias(chosen_spell_name, enemy_obj)
            else:
                console.print("[bold red]Escolha de fé inválida![/bold red]")
                time.sleep(1.5)
                continue
        elif action_choice == '3':
            usable_items_in_battle = [
                item_obj for item_obj in player_obj.inventario
                if item_obj.tipo == "consumivel" and item_obj.usavel_em_batalha
            ]
            
            if not usable_items_in_battle:
                console.print("[bold red]Seu inventário não possui itens consumíveis utilizáveis em batalha![/bold red]")
                time.sleep(1.5)
                continue
            
            console.print("[bold magenta]--- ITENS CONSUMÍVEIS ---[/bold magenta]")
            item_options = {}
            for i, item_obj in enumerate(usable_items_in_battle):
                console.print(f"   [{i+1}] {item_obj.nome} ({item_obj.descricao})")
                item_options[str(i+1)] = item_obj 
            item_choice_input = console.input("[bold blue]Escolha o número do item (ou '0' para cancelar): [/bold blue]").strip()
            if item_choice_input == '0':
                console.print("[bold yellow]Ação de item cancelada.[/bold yellow]")
                time.sleep(1)
                continue
            try:
                chosen_item_obj = item_options.get(item_choice_input)

                if chosen_item_obj:
                    turn_taken = player_obj.usar_item(chosen_item_obj) 
                    time.sleep(1)
                else:
                    console.print("[bold red]Escolha de item inválida![/bold red]")
                    time.sleep(1.5)
                    continue
            except ValueError:
                console.print("[bold red]Por favor, digite um número válido.[/bold red]")
                time.sleep(1.5)
                continue
        else:
            console.print("[bold red]Ação inválida. Tente novamente.[/bold red]")
            time.sleep(1.5)
            continue
        if enemy_obj.hp <= 0:
            console.print(f"\n[bold green]{enemy_obj.nome} foi derrotado![/bold green] ")
            player_obj.gold += enemy_obj.gold
            player_obj.add_xp(enemy_obj.xp)
            console.print(f"[bold yellow]Você ganhou {enemy_obj.gold} de ouro e {enemy_obj.xp} de XP![/bold yellow]")
            dropped_items = enemy_obj.gerar_drops(player_obj.todos_itens)
            for item in dropped_items:
                player_obj.inventario.append(item)
                console.print(f"[bold blue]Você adicionou {item.nome} ao seu inventário![/bold blue]")
            break
        if turn_taken:
            console.print(f"\n[bold yellow]--- Turno de {enemy_obj.nome} ---[/bold yellow]")
            enemy_obj.attack_player(player_obj)
            time.sleep(1.5)
    player_obj.temp_atk_buff = 0 
    player_obj.temp_def_buff = 0
    if player_obj.hp <= 0:
        console.print("\n[bold red]VOCÊ FOI DERROTADO![/bold red]")
        console.print("[bold red]Fim de Jogo.[/bold red]")
        sys.exit()
    else:
        console.print("\n[bold green]Você saiu vitorioso da batalha![/bold green]")
        console.input("\nPressione Enter para continuar...")

def encontro_aleatorio(player_obj: Player): 
    inimigo_tipos = {
        'dragao': {
            'nome': 'Dragão',
            'ascii_art': ascii.dragon,
            'a1': 'Mordida',
            'a2': 'Bola de Fogo',
            'drops': [("Espada Curta", 10.0), ("Pomada de Regeneração", 50.0)] 
        },
        'esqueleto': {
            'nome': 'Esqueleto',
            'ascii_art': ascii.esqueleto,
            'a1': 'Soco',
            'a2': 'Jogar Ossos',
            'drops': [("Osso Rachado", 70.0), ("Pomada de Regeneração", 20.0)] 
        },
        'lobo': {
            'nome': 'Lobo',
            'ascii_art': ascii.lobo,
            'a1': 'Aranhão',
            'a2': 'Mordida',
            'drops': [("Carne", 60.0), ("Pomada de Regeneração", 25.0)] 
        },
        'sharq':{
            'nome': 'Tubaram',
            'ascii_art': ascii.sharq,
            'a1': 'Caudada',
            'a2': 'Mordida',
            'drops': [("Ovo", 30.0), ("Pomada de Regeneração", 40.0)] 
        },
        'av':{
            'nome': 'Água Viva',
            'ascii_art': ascii.av,
            'a1': 'Choque',
            'a2': 'Queimar',
            'drops': [("Água", 40.0)] 
        },
        'java':{
            'nome': 'Javali',
            'ascii_art': ascii.javali,
            'a1': 'Cabeçada',
            'a2': 'Mordida',
            'drops': [("Carne", 40.0)] 
        },
    }
    selected_enemy_pool = []
    hp_range = (0, 0)
    atk_range = (0, 0)
    xp_range = (0, 0)
    gold_range = (0, 0)
    nivel_range = (0, 0)
    if play.x == 1:
        selected_enemy_pool = ['lobo', 'java']
        hp_range = (25, 50)
        atk_range = (10, 15)
        xp_range = (10, 100)
        gold_range = (0, 10)
        nivel_range = (1, 5)
    elif play.x == 3:
        selected_enemy_pool = ['esqueleto']
        hp_range = (15, 100)
        atk_range = (5, 15)
        xp_range = (50, 100)
        gold_range = (1, 10)
        nivel_range = (1, 5)
    elif play.x == 6:
        selected_enemy_pool = ['sharq', 'av', 'dragao']
        hp_range = (150, 250)
        atk_range = (20, 40)
        xp_range = (200, 350)
        gold_range = (20, 70)
        nivel_range = (5, 10)
    else:
        console.print("[bold red]Nenhum inimigo encontrado para esta área.[/bold red]")
        return None
    tipo_escolhido = random.choice(selected_enemy_pool)
    dados_inimigo = inimigo_tipos[tipo_escolhido]
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
        a2=dados_inimigo['a2'],
        itens_drops=dados_inimigo['drops']
    )
    return novo_inimigo

def mapa(play: Player):
    while play.running:
        ##Floresta
        if play.x == 1:
            clear()
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print(f'[bold green]Floresta: \n{ascii.floresta}')
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print(f'[bold cyan]Ações[/bold cyan]')
            console.print("[1]ir para Igreja  [2]ir para Cemiterio")
            console.print("[3]Explorar        [4]Andar")
            console.print(f'[bold yellow]+'+'-'*45+'+')
            acoes = input("=>")
            if acoes == '1':
                #igreja
                play.x = 2
            elif acoes == '2':
                ##cemiterio
                play.x = 3
            elif acoes == "3":
                if not play.itens_coletaodos["Floresta"]:
                    console.print("Você Explora a floresta e vê uma espada")
                    play.adicionar_item("Espada Curta")
                    play.itens_coletaodos["Floresta"] = True
                else:
                    console.print("Você já Explora a floresta e vê não vê nada de util")
                    time.sleep(1)
            elif acoes == '4':
                florest = encontro_aleatorio(play)
                battle_system(play, florest)
            elif acoes == 'ops':
                play.ops()
        ##Igreja
        elif play.x == 2:
            clear()
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print(f'[bold green]Igreja: \n{ascii.igreja}')
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print(f'[bold cyan]Ações[/bold cyan]')
            console.print("[1]ir para Floresta [2]Entrar")
            console.print(f'[bold yellow]+'+'-'*45+'+')
            acoes = input("=>")
            if acoes == '1':
                play.x = 1
            elif acoes == '2':
                play.x = 4
            elif acoes == 'ops':
                play.ops()
        ##Cemiterio
        elif play.x == 3:
            clear()
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print(f'[bold green]Cemiterio: \n{ascii.cemiterio}')
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print(f'[bold cyan]Ações[/bold cyan]')
            console.print("[1]Explorar Tumoulos [2]ir para Floresta")
            console.print(f'[bold yellow]+'+'-'*45+'+')
            acoes = input("=>")
            if acoes == '1':
                item = 50
                roll = random.randint(1, 100)
                if roll <= item:
                    if not play.itens_coletaodos["Cemiterio"]:
                        console.print(f'Você Explora um tumol')
                        itens = ['Anel', 'Escudo']
                        itens_aleatorio = random.choice(itens)
                        console.print(f'Você Explora um tumol e encontra uma {itens_aleatorio}')
                        play.adicionar_item(itens_aleatorio)
                        play.itens_coletaodos["Cemiterio"]= True
                        time.sleep(2)
                    else:
                        console.print(f"Nada encontrado")
                else:
                    esqueletp = encontro_aleatorio(play)
                    battle_system(play, esqueletp)
            elif acoes == '2':
                play.x = 1
            elif acoes == 'ops':
                play.ops()
        ##Dentro da Igreja
        elif play.x == 4:
            clear()
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print(f'[bold green]Dentro de Igreja: \n{ascii.igreja}')
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print(f'[bold cyan]Ações[/bold cyan]')
            console.print("[1]Ver Padre [2]Ver crucifixo")
            console.print("[3]Ver Porão [4]Sair da igreja")
            console.print(f'[bold yellow]+'+'-'*45+'+')
            acoes = input("=>")
            if acoes == '1':
                console.print(f'[bold yellow]+'+'-'*45+'+')
                dd.exibir_texto_lento(dd.padre, atraso=0.1)
                console.print(f"[1]Matar [2]Orar")
                console.print(f'[bold yellow]+'+'-'*45+'+')
                padre = input("=>")
                if padre == '1':
                    if not play.itens_coletaodos["Padre"]:
                        dd.exibir_texto_lento(dd.padre_mata, atraso=0.1)
                        console.print(f'[bold yellow]+'+'-'*45+'+')
                        play.str += 5
                        console.print(f'[bold yellow]Sua violencia almentou em {play.str}')
                        play.itens_coletaodos["Padre"]=True
                        input()
                    else:
                        console.print(f'[bold yellow]Já Passol por aqui')
                elif padre == '2':
                    if not play.itens_coletaodos["Padre"]:
                        if play.itens_coletaodos["Crucifixo"]:
                            dd.exibir_texto_lento(dd.padre_ora, atraso=0.1)
                            console.print(f'[bold yellow]+'+'-'*45+'+')
                            play.ini += 5
                            console.print(f'[bold yellow]Sua Razão almentou em {play.ini}')
                            play.itens_coletaodos["Padre"]=True
                            input()
                        else:
                            console.print(f'[bold cyan]{dd.padre_ora_1}[/bold cyan]')
                            console.print(f'[bold yellow]+'+'-'*45+'+')
                            input()
                    else:
                        console.print(f'[bold yellow]Já Passol por aqui')
            elif acoes == '2':
                if not play.itens_coletaodos["Crucifixo"]:
                    console.print(f'[bold yellow]+'+'-'*45+'+')
                    dd.exibir_texto_lento(dd.cruz, atraso=0.1)
                    console.print(f'[bold yellow]+'+'-'*45+'+')
                    play.adicionar_item("Crucifixo")
                    input("=>")
                    play.itens_coletaodos["Crucifixo"]=True
                else:
                    console.print(f'[bold yellow]Já Passol por aqui')
            elif acoes == '3':
                play.x = 5
            elif acoes == '4':
                play.x = 2
            elif acoes == 'ops':
                play.ops()
        ##Porão
        elif play.x == 5:
            clear()
            console.print(f'[bold yellow]+'+'-'*45+'+')
            dd.exibir_texto_lento(dd.poram, atraso=0.1)
            console.print(f'[bold yellow]+'+'-'*45+'+')
            input()
            clear()
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print(f'[bold green]Porão: \n{ascii.porta}')
            console.print(f'[bold yellow]+'+'-'*45+'+')
            console.print(f'[bold cyan]Ações[/bold cyan]')
            console.print("[1]Entrar [2]Voltar para Cima")
            console.print(f'[bold yellow]+'+'*-'*45+'+')
            acoes = input("=>")
            if acoes == '1':
                play.x = 6
            elif acoes == '2':
                play.x == 4
            elif acoes == 'ops':
                play.ops()
        ##Inferna
        elif play.x == 6:
            clear()

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
            play = Player(nome=player_name, hp_max=100, str=10, int_stat=10, atk=1000, max_mana=100, gold=10000, xp_max=100, xp=0, nivel=1, atk_mana=50, x=1, defesa=10)
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
        mapa(play)
        input()
menu()