from blessed import Terminal
import curses
from curses import wrapper
import os
term = Terminal()
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def linhas():
    print(term.bold_white("<<"+"="*25+">>"))
def linha_inven():
    print(term.bold_blue("<<")+term.bold_white("="*30)+term.bold_blue(">>"))
def linhas_batalha():
    print(term.bold_white("##"+"-"*25+"##"))
def linhas_jogo():
    print(term.bold_white("xX"+"="*40+"Xx"))

def draw_window(term, x, y, width, height, title='', text_content='', bg_color='default'):
    if bg_color == 'default':
        bg_style = ''
    else:
        bg_style = getattr(term, f'on_{bg_color}', '')
    border_style = bg_style + term.white_on_default 
    title_style = bg_style + term.bold_on_default
    text_style = bg_style + term.on_default
    with term.location(x, y):
        print(border_style + '╔' + '═' * (width - 2) + '╗' + term.normal)
    for i in range(1, height - 1):
        with term.location(x, y + i):
            print(text_style + '║' + ' ' * (width - 2) + '║' + term.normal)
    with term.location(x, y + height - 1):
        print(border_style + '╚' + '═' * (width - 2) + '╝' + term.normal)
    if title:
        title_x = x + (width - len(title)) // 2
        with term.location(title_x, y):
            print(title_style + ' ' + title + ' ' + term.normal)
    if text_content:
        lines = text_content.split('\n')
        for i, line in enumerate(lines):
            if i < height - 2:
                with term.location(x + 2, y + i + 1):
                    print(text_style + line[:width - 4] + term.normal)


def escolhas_(esc, esc1, esc2, esc3, y_pos, x_pos):
    with term.location(x_pos, y_pos):
        print(term.bold("xX"+"="*25+"Xx"))
    y_pos += 1
    with term.location(x_pos, y_pos):
        print(term.bold(f"| {esc}  {esc1} |"))
    y_pos += 1
    with term.location(x_pos, y_pos):
        print(term.bold(f"| {esc2}  {esc3} |"))
    y_pos += 1
    with term.location(x_pos, y_pos):
        print(term.bold("xX"+"="*25+"Xx"))
    y_pos += 1

class art_ascii:
    def __init__(self):
        self.titulo = r"""                        ╔╦╗┬ ┬┌─┐  ╦  ┌─┐┌─┐┌┬┐
                         ║ ├─┤├┤   ║  ├─┤└─┐ │
                         ╩ ┴ ┴└─┘  ╩═╝┴ ┴└─┘ ┴
                        ╔═╗┬─┐┬ ┬┌─┐┌─┐┌┬┐┌─┐
                        ║  ├┬┘│ │└─┐├─┤ ││├┤
                        ╚═╝┴└─└─┘└─┘┴ ┴─┴┘└─┘
"""
        self.linha = "xX"+"="*30+"Xx"
        self.necro = r""" (\.   \      ,/)
  \(   |\     )/
  //\  | \   /\\
 (/ /\_#oo#_/\ \)
  \/\__####__/\/
       \##/
       /##\
      /####\
      \~~~~/
.,.,.,,.,,.,.,.,..,,.,.
"""
        self.mago = r"""         ,/   *
      _,'/_   |
      `(")' ,'/
   _ _,-H-./ /
   \_\_\.   /
     )" |  (
  __/   H   \__
  \    /|\    /
   `--'|||`--'
      ==^=="""
        self.esqueleto = r"""            .-.
           (o.o)
            |=|
           __|__
         //.=|=.\\
        // .=|=. \\
        \\ .=|=. //
         \\(_=_)//
          (:| |:)
           || ||
           () ()
           || ||
           || ||
          ==' '==
"""
        self.demoni0 = r'''   ,    ,    /\   /\
  /( /\ )\  _\ \_/ /_
  |\_||_/| < \_   _/ >
  \______/  \|0   0|/
    _\/_   _(_  ^  _)_
   ( () ) /`\|V"""V|/`\
     {}   \  \_____/  /
     ()   /\   )=(   /\
     {}  /  \_/\=/\_/  \ 
'''
        self.demoni1 = r"""            v
      (__)v | v
      /\/\\_|_/
     _\__/  |
    /  \/`\<`)
    \ (  |\_/
   /)))-(  |
  / /^ ^ \ |
 /  )^/\^( |
 )_//`__>> |
   #   #`  | 
"""
        self.vila1 = r"""
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
  ..    ..-''    ;       ''. '  """
        self.farol = r""" . _  .    .__  .  .  __,--'                 
  (_)    ' /__\ __,--'                       
'  .  ' . '| o|'                             
          [IIII]`--.__                       
           |  |       `--.__                 
           | :|             `--.__           
           |  |                   `--.__     
._,,.-,.__.'__`.___.,.,.-..,_.,.,.,-._..`--..
"""
        self.vila_map = r"""
 [CASA_01]===.-.-.-.-.-.-[HOSPITAL]
 ..,.,.,. [PRAÇA] ;; [CASA_02].....
 .,.,[MERCADO]####[CASA_03].,.,..,,
 [SAIDA]..,,.,,.,.,.,.[FERREIRO],,.
 """
        self.guerriro = r"""                 /
          ,~~   /
      _  <=)  _/_
     /I\.="==.{>
     \I/-\T/-'
         /_\
        // \\_
       _I    / 
============================
"""
        self.moinho = r"""                 ,-_                  (`  ).    
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
'                          ``'--,..,.           
"""
        self.lobo = r"""
             _/|
            =/_/
           _/ |
      (   /  ,|
       \_/^\/||__
    _/~  `""~`"` \_
 __/  -'/  `-._ `\_\__
/     /-'`  `\   \  \-.\
"""
        self.lobo1 = r"""
         _     ___
        #_~`--'__ `===-,
        `.`.     `#.,//
        ,_\_\     ## #\
        `__.__    `####\
             ~~\ ,###'~
                \##'

"""
art = art_ascii()
