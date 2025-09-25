import random, os, time, json
from classe_arts import draw_window, term, linha_inven, linhas, linhas_batalha, clear, art_ascii
from classe_do_inventario import Item, TODOS_OS_ITENS, magias, TODAS_AS_MAGIAS
from collections import defaultdict
art= art_ascii()
class jogador:
    def __init__(self, nome, hp_max, atk, niv, xp_max, defesa, gold, stm_max, intt, mn_max, d_m,art_player,mana_lit=None):
        self.nome = nome
        self.hp_max = hp_max
        self.hp = self.hp_max
        self.mana_max = mn_max
        self.mana = self.mana_max
        self.stm_max = stm_max
        self.stm = self.stm_max
        self.atk = atk
        self.buff_atk = 0
        self.buff_def = 0
        self.intt = intt
        self.niv = niv
        self.xp_max = xp_max
        self.dano_magico = d_m
        self.xp = 100
        self.defesa = defesa
        self.gold = gold
        self.rodar_jogo = False
        self.aleatorio = 75
        self.andar = 0
        self.art_player = art_player
        self.classe= {
            "Guerreiro":None,
            "Mago":None,
            "Negromante":None
        }
        self.inventario = [TODOS_OS_ITENS["Poção de Cura"], TODOS_OS_ITENS["Elixir"], TODOS_OS_ITENS["Poção de Cura"],TODOS_OS_ITENS["Crucifixo"]]
        self.locais = {
            "Vila": True,
            "Farol":None,
            "Moinho":None,
            "Caverna":None,
            "Mar":None,
            "Deserto":None,
            "Montanha":None
        }
        self.mana_lit = mana_lit if mana_lit is not None else []
        self.equipa = {
            "m_pri": None,
            "m_seg": None,
            "c_cap": None,
            "p_pet": None,
            "s_crad": None,
        }
        self.itens_coletaodos = {
            "item_1": True,
            "item_2": False,
            "Farol": False,
            "Dentro_Farol": False,
        }
    
    def save_game(self, filename="Demo.json", x_l=int, y_l =int):
        inventario_nomes = [item.nome for item in self.inventario]
        equipa_nomes = {slot: item.nome if item else None for slot, item in self.equipa.items()}
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
            "xp": self.xp,
            "aleatorio": self.aleatorio,
            "inventario": inventario_nomes,
            "mana_lit": self.mana_lit,
            "equipa": equipa_nomes,
            "itens_coletaodos": self.itens_coletaodos,
            "rodar": self.rodar_jogo,
            "classes": self.classe,
        }
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(player_data, f, indent=4)
            with term.location(x=x_l, y=y_l):
                print(f"Jogo salvo com sucesso em")
            with term.location(x=x_l, y=y_l+1):
                print(f"'{filename}'")            
        except IOError as e:
            with term.location(x=x_l, y=y_l):
                print(f"Erro ao salvar o jogo: {e}")

    @classmethod
    def load_game(cls, filename="Demo.json", x_l=int, y_l =int):
        if not os.path.exists(filename):
            with term.location(x=x_l, y=y_l):
                print(f"Nenhum arquivo de salvamento")
            with term.location(x=x_l, y=y_l+1):
                print(f"encontrado em '{filename}'.")
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
            )
            player.inventario = [TODOS_OS_ITENS[nome] for nome in player_data["inventario"]]
            player.equipa = {slot: TODOS_OS_ITENS[nome] if nome else None for slot, nome in player_data["equipa"].items()}
            
            player.hp = player_data["hp"]
            player.aleatorio = player_data["aleatorio"]
            player.mana_lit = player_data["mana_lit"]
            player.itens_coletaodos = player_data["itens_coletaodos"]
            player.xp = player_data["xp"]
            player.mana = player_data["mana"]
            player.stm = player_data["stm"]
            player.rodar_jogo = player_data["rodar"]
            player.classe = player_data["classes"]
            print(f"Jogo carregado com sucesso de '{filename}'!")
            return player
        except (IOError, json.JSONDecodeError, KeyError) as e:
            with term.location(x=x_l, y=y_l):
                print(f"Erro ao carregar o jogo: {e}.")
            return None
    
    def menu(self, x_janela, y_janela):
        menu = "[1]Status [2]Inventario\n[3]Magias [4]Save\n[5]Sair   [6]Sair do jogo"
        herd = 6
        draw_window(term, x=x_janela, y=y_janela, width=30,height=herd, text_content=menu)
        with term.location(x=x_janela+1, y=herd-2):
            escolha = input(">")
        if escolha == "1":
            self.status(x_janela=x_janela, y_janela=y_janela+6)
        elif escolha == "2":
            clear()
            self.inventario_(x_inv=0, y_inv=0, batalha=False)
        elif escolha == "3":
            clear()
            self.menu_magias(x_menu=0, y_menu=0, batalha=False, alvo=None)
        elif escolha == "4":
            self.save_game(filename=f"Demo.json")
        elif escolha == "5":
            return False
        elif escolha == "6":
            exit()

    def status(self, x_janela, y_janela):
        manager = ""
        if self.classe["Mago"] == True:
            manager = "Mago"
        elif self.classe["Guerreiro"] == True:
            manager = "Guerreiro"
        elif self.classe["Negromante"] == True:
            manager = "Necromante"
        else:
            manager = "Null"
        draw_window(term, x=x_janela, y=y_janela, width=31, height=8)
        with term.location(x=x_janela+1, y=y_janela+1):
            print(f"Nome: [{term.italic_gray(str(self.nome))}] Nivel: [{term.yellow(str(self.niv))}]") 
        with term.location(x=x_janela+1, y=y_janela+2):
            print(f"HP: [{term.bold_green(str(self.hp_max))}/{term.green(str(self.hp))}] MP: [{term.bold_blue(str(self.stm_max))}/{term.blue(str(self.stm))}]")
        with term.location(x=x_janela+1, y=y_janela+3):
            print(f"MG: [{term.bold_magenta(str(self.mana_max))}/{term.magenta(str(self.mana))}] MA: [{term.bold_purple(str(self.dano_magico+3))}-{term.purple(str(self.dano_magico-3))}]")
        with term.location(x=x_janela+1, y=y_janela+4):
            print(f"AT: [{term.bold_red(str(self.atk))}-{term.red(str(self.buff_atk))}] DF: [{term.bold_cyan(str(self.defesa))}-{term.cyan(str(self.buff_def))}]")
        with term.location(x=x_janela+1, y=y_janela+5):
            print(f"AT: [{term.bold_blue(str(self.intt))}] Classe: [{term.bold_cyan(str(manager))}]")
        self.status_art(x_janela=x_janela+32, y_janela=y_janela)
        with term.location(x=x_janela+1, y=y_janela+6):
            input(">")
    def status_art(self ,x_janela, y_janela):
        art_player = self.art_player
        draw_window(term, x=x_janela, y=y_janela, width=31, height=11, text_content=art_player)

    def status_batalha_art(self, x_janela, y_janela):
        art_player = self.art_player
        draw_window(term, x=x_janela, y=y_janela, width=31, height=11, text_content=art_player)
        self.status_batalha(x_janela=x_janela, y_janela=y_janela+11)

    def status_batalha(self, x_janela, y_janela):
        draw_window(term, x=x_janela, y=y_janela, width=31, height=6)
        with term.location(x=x_janela+1, y=y_janela+1):
            print(f"HP: [{term.bold_green(str(self.hp_max))}/{term.green(str(self.hp))}] MP: [{term.bold_blue(str(self.stm_max))}/{term.blue(str(self.stm))}]")
        with term.location(x=x_janela+1, y=y_janela+2):
            print(f"MG: [{term.bold_magenta(str(self.mana_max))}/{term.magenta(str(self.mana))}] MA: [{term.bold_purple(str(self.dano_magico+3))}-{term.purple(str(self.dano_magico-3))}]")
        with term.location(x=x_janela+1, y=y_janela+3):
            print(f"AT: [{term.bold_red(str(self.atk))}-{term.red(str(self.buff_atk))}] DF: [{term.bold_cyan(str(self.defesa))}-{term.cyan(str(self.buff_def))}]")
        with term.location(x=x_janela+1, y=y_janela+4):
            print(f"Nivel: [{term.yellow(str(self.niv))}]")
             
    def add_xp(self, xp_ganho):
        self.xp += xp_ganho
        while self.xp >= self.xp_max:
            print(term.bold_white("Você subiu de nível!"))
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
        print(f"Você ganhou {xp_ganho} de XP. Total: {self.xp}/{self.xp_max}")
        time.sleep(2)

    def menu_magias(self, x_menu, y_menu, batalha, alvo):
        text_content = ""
        nome_das_magias = [sublist[0] for sublist in self.mana_lit]

        if not self.mana_lit:
            text_content = "Você não conhece nenhuma magia."
        else:
            for nome_magia in nome_das_magias:
                magia_obj = TODAS_AS_MAGIAS.get(nome_magia)
                if magia_obj:
                    text_content += f"{magia_obj.nome} (Custo: {magia_obj.mana_gasta} Mana)\n"
        
        text_content += "Para usar uma magia, digite o nome dela.\nPara sair, digite 'sair'."
        num_linhas_texto = text_content.count('\n') + 1
        herd = num_linhas_texto + 3
        draw_window(term, x_menu, y_menu, width=45, height=herd, title="Livro de Magias", text_content=text_content)
        x_input = x_menu + 2
        y_input = y_menu + herd - 2
        
        with term.location(x_input, y_input):
            escolha = input(">")
        
        if escolha.lower() == "sair":
            return False
            
        if escolha in nome_das_magias:
            magia_escolhida = TODAS_AS_MAGIAS[escolha]
            if magia_escolhida.batalhas and not batalha:
                feedback_message = "Você só pode usar esta magia em batalha!"
                draw_window(term, x=x_menu, y=y_menu + herd, width=len(feedback_message) + 5, height=5, text_content=feedback_message)
                time.sleep(2)
                return False
            else:
                return self.usar_magia(magia_escolhida, x_menu, y_menu + herd, alvo=alvo)
        else:
            feedback_message = "Magia inválida ou não conhecida."
            draw_window(term, x=x_menu, y=y_menu + herd, width=len(feedback_message) + 5, height=5, text_content=feedback_message)
            time.sleep(2)
            return False

    def usar_magia(self, magia, x_janela, y_janela, alvo):
        text_content = ""
        sucesso = False       
        if self.mana < magia.mana_gasta:
            text_content = "Mana insuficiente!"
            sucesso = False
        else:
            self.mana -= magia.mana_gasta            
            if magia.tipo == "Cura":
                self.hp += magia.bonus_hp
                if self.hp > self.hp_max:
                    self.hp = self.hp_max
                text_content = f"Você usou {magia.nome} e curou {magia.bonus_hp} de HP."
                sucesso = True
            elif magia.tipo == "Ataque":
                div = self.intt // 4
                soma = self.dano_magico + div
                dano = soma + magia.bonus_atk
                alvo.hp -= dano
                text_content = f"Você lançou {magia.nome} e causou {dano} de dano."
                sucesso = True
            elif magia.tipo == "Defesa":
                self.buff_def += magia.bonus_def
                text_content = f"Você usou {magia.nome} e sua defesa aumentou em {magia.bonus_def}."
                sucesso = True
            elif magia.tipo == "Ajuda":
                self.atk += magia.bonus_atk
                text_content = f"Você usou {magia.nome} e seu ataque aumentou em {magia.bonus_atk}."
                sucesso = True
            elif magia.tipo == "Necro":
                self.buff_atk += magia.bonus_atk
                text_content = f"Você envocou um {magia.nome} ajudando na batalha {self.atk}."
                sucesso = True
        herd = 3
        draw_window(term, x_janela, y_janela, width=len(text_content) + 5, height=herd, text_content=text_content)
        time.sleep(2)
        return sucesso

    def atake(self, alvo, x_janela, y_janela):
        atak_aleatorio = random.randint(1, 100)
        if self.stm >= 10:
            if self.aleatorio > atak_aleatorio:
                self.stm -= 10
                dano_ale = random.randint(int(self.atk - 3), int(self.atk + 3))
                meno_defsa = alvo.defesa // 4
                dano_final = int(self.buff_atk + dano_ale - meno_defsa)
                mensagem = f"{str(self.nome)} deu um dano de {str(dano_final)}\nno {str(alvo.nome)}"
                alvo.hp -= dano_final
                time.sleep(1)
            else:
                mensagem = f"{self.nome} errou o ataque"
                time.sleep(1)
        else:
            mensagem = "Você não tem ST suficiente"
            time.sleep(1)
        herd = 4
        draw_window(term, x_janela, y_janela, width=len(mensagem)-5, height=herd, text_content=mensagem)

    def inventario_(self, x_inv, y_inv, batalha):
        text_content = ""
        contagem_itens = defaultdict(int)
        for item_obj in self.inventario:
            contagem_itens[item_obj.nome] += 1
        if not self.inventario:
            text_content = "Não tem nada no inventário."
        else:
            for item_nome, quantidade in contagem_itens.items():
                item_obj = TODOS_OS_ITENS[item_nome]
                estado = ""
                if item_obj.slot_equip and self.equipa.get(item_obj.slot_equip) and self.equipa[item_obj.slot_equip].nome == item_obj.nome:
                    estado = "[Equipado]"
                text_content += f"{item_obj.nome} (x{quantidade}) {estado}\n"
        text_content += "Para usar/equipar um item, digite o nome dele.\nPara sair, digite 'sair'."
        num_linhas_texto = text_content.count('\n')+1
        herd = num_linhas_texto + 3
        draw_window(term, x_inv, y_inv, width=45, height=herd, title="Inventário", text_content=text_content)
        x_input = x_inv + 2
        y_input = y_inv + herd - 2
        y_acao = y_inv
        with term.location(x_input, y_input):
            escolha = input(">")
        if escolha.lower() == "sair":
            return False
        if batalha == True:
            if escolha in TODOS_OS_ITENS and escolha in contagem_itens:
                item_escolhido = TODOS_OS_ITENS[escolha]
                if item_escolhido.tipo == "Consumivel":
                    return self.usar_consumivel(item_escolhido, x_inv, y_inv + herd)
                elif item_escolhido.tipo == "Equipavel":
                    mensagem = "Você Não Pode usar um\nequipavel em batalha"
                    draw_window(term, x=x_inv, y=y_acao+herd, width=25, height=4,text_content=mensagem)
                    time.sleep(4)
        elif batalha == False:
            if escolha in TODOS_OS_ITENS and escolha in contagem_itens:
                item_escolhido = TODOS_OS_ITENS[escolha]
                if item_escolhido.tipo == "Consumivel":
                    self.usar_consumivel(item_escolhido, x_inv, y_acao+herd)
                elif item_escolhido.tipo == "Equipavel":
                    self.gerenciar_equipavel(item_escolhido, x_inv, y_acao+herd)             
        else:
            return False

    def usar_consumivel(self, item, x_janela, y_janela):
        text_content = ""
        sucesso = False
        if item.nome == "Poção de Cura":
            if self.hp >= self.hp_max:
                text_content = "Seu HP já está no máximo!"
                sucesso = False
            else:
                text_content = "Você bebeu uma poção de cura."
                self.hp += item.bonus_hp
                if self.hp > self.hp_max:
                    self.hp = self.hp_max
                self.inventario.remove(item)
                sucesso = True
        elif item.nome == "Elixir":
            if self.mana >= self.mana_max:
                text_content = "Sua Mana já está no máximo!"
                sucesso = False
            else:
                text_content = "Você bebeu um elixir."
                self.mana += item.bonus_mana
                if self.mana > self.mana_max:
                    self.mana = self.mana_max
                self.inventario.remove(item)
                sucesso = True
        herd = 3
        draw_window(term, x_janela+1, y_janela, width=len(text_content) + 5, height=herd, text_content=text_content)
        time.sleep(2)
        return sucesso

    def gerenciar_equipavel(self, item, x_janela, y_janela):
        text_content = "O que deseja fazer com o item?\n[1]Equipar\n[2]Desequipar"
        herd = 6
        draw_window(term, x_janela, y_janela, width=35, height=herd, title=item.nome, text_content=text_content)
        with term.location(x_janela + 2, y_janela + herd - 2):
            esc = input(">")
        feedback_message = ""
        if esc == "1":
            if not self.equipa.get(item.slot_equip):
                self.equipa[item.slot_equip] = item
                self.atk += item.bonus_atk
                self.defesa += item.bonus_def
                self.dano_magico += item.bonus_atk_mana
                feedback_message = f"Você equipou {item.nome}."
            else:
                feedback_message = "Já tem algo equipado nesse slot!"
        elif esc == "2":
            if self.equipa.get(item.slot_equip) and self.equipa[item.slot_equip].nome == item.nome:
                self.equipa[item.slot_equip] = None
                self.atk -= item.bonus_atk
                self.defesa -= item.bonus_def
                self.dano_magico -= item.bonus_atk_mana
                feedback_message = f"Desequipando {item.nome}."
            else:
                feedback_message = "Este item não está equipado."
        else:
            feedback_message = "Opção inválida."
        
        feedback_herd = 5
        draw_window(term, x_janela, y_janela + herd, width=len(feedback_message) + 5, height=feedback_herd, text_content=feedback_message)
        time.sleep(2)
        draw_window(term, x_janela, y_janela + herd, width=len(feedback_message) + 5, height=feedback_herd, text_content=" " * len(feedback_message))

    def gerenciar_loja(self, x_pos, y_pos, herd, x_loq, y_loq):
        draw_window(term, x_loq, y_loq, width=25, height=herd, title="Loja")
        with term.location(x=x_pos, y=y_pos):
            print("Gold: ["+term.bold_yellow(f"{self.gold}")+"]")
        with term.location(x=x_pos, y=y_pos+1):
            print("[1] Comprar itens")
        with term.location(x=x_pos, y=y_pos+2):
            print("[2] Vender itens")
        with term.location(x=x_pos, y=y_pos+3):
            print("[3] Sair da loja")
        with term.location(x=x_pos, y=y_pos+4):
            escolha = input("> ")
        if escolha == "1":
            self.comprar_itens(x_m=x_pos+26, y_m=y_pos, herd=7, x_l =x_loq+25, y_l=y_loq)
        elif escolha == "2":
            self.vender_itens(x_l=x_loq+0, y_l=y_loq +7)
        elif escolha == "3":
            with term.location(x=x_pos, y=y_pos):
                print("Saindo da loja")
            time.sleep(1)
            return
        else:
            return

    def comprar_itens(self, x_m, y_m, herd, x_l, y_l):
        draw_window(term, x_l, y_l, width=25, height= herd, title="Comprar")
        with term.location(x=x_m, y=y_m):
            print("Gold: ["+term.bold_yellow(f"{self.gold}")+"]")
        with term.location(x=x_m, y=y_m+1):
            print("[1] Itens Equipáveis")
        with term.location(x=x_m, y=y_m+2):
            print("[2] Itens Consumíveis")
        with term.location(x=x_m, y=y_m+3):
            print("[3] Voltar")
        with term.location(x=x_m, y=y_m+4):
            escolha_tipo = input(">")
            if escolha_tipo == "1":
                self.exibir_itens_por_tipo("Equipavel", x_l-25, y_l=7-y_l)
            elif escolha_tipo == "2":
                self.exibir_itens_por_tipo("Consumivel", x_l-25, y_l=7-y_l)
            elif escolha_tipo == "3":
                return
            else:
                with term.location(x=x_m, y=y_m):
                    print("Opção inválida.")
                time.sleep(2)

    def exibir_itens_por_tipo(self, tipo, x_l, y_l):
        itens_disponiveis = [item for item in TODOS_OS_ITENS.values() if item.tipo == tipo and item.comprável]
        text_content ="Gold: ["+term.bold_yellow(f"{self.gold}")+"]\n"
        if not itens_disponiveis:
            text_content += f"Nenhum item do tipo '{tipo}' disponível."
        else:
            for i, item_obj in enumerate(itens_disponiveis, 1):
                text_content += f"[{i}] {item_obj.nome}-[{item_obj.preco}]\n"
        text_content += "[0] Voltar"
        num_linhas_texto = text_content.count('\n') + 1
        herd = num_linhas_texto + 3
        draw_window(term, x_l, y_l, width=35, height=herd, title=f"Comprar {tipo.capitalize()}", text_content=text_content)
        with term.location(x_l +1, y_l + herd - 2):
            try:
                escolha_item = int(input(">"))
                if escolha_item == 0:
                    return
                item_selecionado = itens_disponiveis[escolha_item - 1]
                if self.gold >= item_selecionado.preco:
                    self.gold -= item_selecionado.preco
                    self.inventario.append(item_selecionado)
                    with term.location(x_l + 2, y_l + herd):
                        print(f"Você comprou {item_selecionado.nome}.")
                else:
                    with term.location(x_l + 2, y_l + herd):
                        print("Dinheiro insuficiente.")
            except (ValueError, IndexError):
                with term.location(x_l + 2, y_l + herd):
                    print("Opção inválida.")
            
            time.sleep(2)
    
    def vender_itens(self, x_l, y_l):
        while True:
            itens_vendaveis = [item for item in self.inventario if item.vendivel]
            text_content ="Gold: ["+term.bold_yellow(f"{self.gold}")+"]\n"
            if not itens_vendaveis:
                text_content += "Você não tem nenhum item vendável."
                herd = 5
            else:
                contagem_itens = defaultdict(int)
                for item_obj in itens_vendaveis:
                    contagem_itens[item_obj.nome] += 1
                itens_unicos = list(contagem_itens.keys())
                for i, item_nome in enumerate(itens_unicos, 1):
                    item_obj = TODOS_OS_ITENS[item_nome]
                    quantidade = contagem_itens[item_nome]
                    preco_venda = item_obj.preco // 2
                    text_content += f"[{i}] {item_nome} (x{quantidade})-[{preco_venda}]\n"
                text_content += "[0] Voltar"
                num_linhas_texto = text_content.count('\n') + 1
                herd = num_linhas_texto + 3
            draw_window(term, x_l, y_l, width=40, height=herd, title="Vender Itens", text_content=text_content)
            with term.location(x_l + 2, y_l + herd - 2):
                try:
                    escolha = int(input(">"))
                    if escolha == 0:
                        return
                    item_nome_selecionado = itens_unicos[escolha - 1]
                    item_vendido = TODOS_OS_ITENS[item_nome_selecionado]
                    preco_venda = item_vendido.preco // 2
                    self.gold += preco_venda
                    self.inventario.remove(item_vendido)                    
                    with term.location(x_l + 2, y_l + herd):
                        print(f"Você vendeu {item_vendido.nome} por {preco_venda} moedas.")
                except (ValueError, IndexError):
                    with term.location(x_l + 2, y_l + herd):
                        print("Opção inválida.")
                time.sleep(2)
                with term.location(x_l + 2, y_l + herd):
                    print(" " * 30)

    def hospital(self, x_, y_):
        with term.location(x=x_, y=y_):
            print("Você dormil essa noite")
        self.hp = self.hp_max
        self.stm = self.stm_max
        self.mana = self.mana_max
        time.sleep(3)

    def mapa(self):
        with term.location(32, 2):
            print(term.bold_gray("+=Mapa=============================+"))
        with term.location(33, 3):
            print(term.italic_yellow_on_black("[CAVERNA]") + term.bold_green("."*19) + term.italic_magenta("[VILA]"))
        with term.location(33, 4):
            print(term.bold_gray(":::::::::")+term.bold_green("....")+term.italic_green_on_black("[FLORETA]")+term.bold_green("###........."))
        with term.location(33, 5):
            print(term.italic_white("[MONTANHA]")+term.bold_green("........................"))
        with term.location(33, 6):
            print(term.bold_gray(":::::::::")+term.bold_green(".............")+term.bold_yellow("************"))
        with term.location(33, 7):
            print(term.italic_red("[FAROL]")+term.bold_green("............")+term.italic_yellow("**[DESERTO]****"))
        with term.location(33, 8):
            print(term.bold_cyan("~~~~~~~~~~~~~~~~~~")+term.bold_yellow("****************"))
        with term.location(33, 9):
            print(term.bold_cyan("~~~")+term.italic_cyan("[MAR]")+term.bold_cyan("~~~~~~~~~~~~~~~~~~~~~~~~~~"))
        with term.location(32, 10):
            print(term.bold_gray("+==================================+"))

    def ver_mapa(self):
        local = ""
        if self.locais["Vila"] == True:
            local = "Vila"
        elif self.locais["Farol"] == True:
            local = "Farol"
        elif self.locais["Caverna"] == True:
            local = "Caverna"
        elif self.locais["Montanha"] == True:
            local = "Montanha"
        elif self.locais["Floresta"] == True:
            local = "Floresta"
        elif self.locais["Mar"] == True:
            local = "Mar"
        elif self.locais["Deserto"] == True:
            local = "Deserto"
        
        if self.itens_coletaodos["item_1"]== True:
            clear()
            self.mapa()
            with term.location(32, 11):
                print(f"Você está na: {local}")
            with term.location(32, 12):
                input(">")
        else:
            print("Você não tem um Mapa")

    def escolha_(self, x_l , y_l):
        menu = "Escolha seu Nome:\n"
        draw_window(term, x=x_l, y=y_l, width=30, height=6, text_content=menu)
        with term.location(x=x_l+2, y=y_l+2):
            escolha_nome = input(">")
        if len(escolha_nome) > 8:
            with term.location(x=x_l+1, y=y_l+3):
                print("Nome muito extenço use")
            with term.location(x=x_l+1, y=y_l+4):
                print("apenas 8 letras")
            time.sleep(2)
        elif len(escolha_nome) < 1:
            with term.location(x=x_l+1, y=y_l+3):
                print("Utilize uma letra no minimo")
            time.sleep(2)
        else:
            text = "[1]Mago\n[2]Guerreiro\n[3]Negromante"
            draw_window(term, x=x_l+30, y=y_l,width=18,height=6, text_content=text)
            with term.location(x=x_l+31, y=y_l+4):
                escolha_classe = input(">")
            if escolha_classe == "1":
                self.nome = escolha_classe



if __name__ == "__main__":
    jj = jogador(nome="JJ", hp_max=100, atk=10, niv=1, xp_max=100, defesa=10, gold=0, stm_max=100, intt=10, mn_max=100,d_m=20, art_player=art.guerriro)
    jj.gerenciar_loja(x_pos=1, y_pos=1, herd=7, x_loq=0, y_loq=0)