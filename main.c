#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
void clear(){
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}
typedef struct{
    char nome[50];
    int hp_max;
    int hp;
    int atk;
}player;
void status(player* p) {
    printf("Nome: %s\n", p->nome);
    printf("HP: [%d]/[%d]", p->hp_max, p->hp);
    printf("\nATK: [%d]", p->atk);
    
}
void inicil(player* p){
    while (true){
        clear();
        printf("###################\n");
        printf("### < 1.Jogar > ###\n");
        printf("### < 2.Sair  > ###\n");
        printf("###################\n");
        printf("=>");
        char esc;
        scanf(" %c", &esc);
        if (esc == '1') {
            printf("Qual será seu nome: ");
            scanf("%s", p->nome);
            break;
        }
        else if (esc == '2'){
            printf("SAIR");
            break;
        }
        else{
            printf("ERRO");
        }
    }
}

void jogo(player*p){
    while (true){
        clear();
        printf("~         ~~          __\n");
        printf("       _T      .,,.    ~--~ ^^\n");
        printf(" ^^   // \\                    ~\n");
        printf("      ][O]    ^^      ,-~ ~\n");
        printf("   /''-I_I         _II____\n");
        printf("__/_  /   \\ ______/ ''   /'\\,__\n");
        printf("  | II--'''' \\,--:--..,_/,.-{ },\n");
        printf("; '/__\\,.-';|   |[] .-.| O{ _ }\n");
        printf(":' |  | []  -|   ''--:.;[,.'\\,/\n");
        printf("'  |[]|,.--'' '',   ''-,.    |\n");
        printf("  ..    ..-''    ;       ''. '\n");
        printf("\n");
        printf("[1]Andar\n");
        printf("[2]Ver Status\n");
        printf("[3]Voltar ao Menu Principal\n");
        printf("[4]Sair do Jogo\n");
        printf("=> ");
        
        char esc;
        scanf(" %c", &esc);
        if (esc == '1'){
            clear();
            printf("Você está andando por uma floresta densa. Não há nada por perto...\n");
            printf("Pressione Enter para continuar...");
            getchar();
            getchar(); 
        }
        else if (esc == '2'){
            clear();
            status(p);
            printf("\n\nPressione Enter para continuar...");
            getchar();
            getchar();
        }
        else if (esc == '3'){
            return;
        }
        else if (esc == '4'){
            printf("Saindo do jogo...\n");
            exit(0);
        }
        else {
            printf("Opção inválida. Tente novamente.\n");
            printf("Pressione Enter para continuar...");
            getchar();
            getchar();
        }
    }
}

int main(){
    player jj;
    jj.hp_max = 100; 
    jj.hp = jj.hp_max;
    jj.atk = 10;
    inicil(&jj);
    jogo(&jj);
    

    return 0;
}