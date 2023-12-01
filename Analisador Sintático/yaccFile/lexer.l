%{
#include "y.tab.h"
#include <stdio.h>

// Declarações de funções
int yylex(void);
int yyerror(char *msg);
int yywrap(void);
%}

FILE *yyin; // Variável de arquivo de entrada

%%

[0-9]+      { yylval = atoi(yytext); return NUMBER; }
[-+*/()\n]  { return yytext[0]; }
[ \t]       ; // Ignora espaços em branco e tabulações
.           { yyerror("Caractere desconhecido"); }

%%

int yywrap(void) {
    return 1;
}
