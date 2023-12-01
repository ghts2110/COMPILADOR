%{
#include <stdio.h>
#include "y.tab.h"
extern char *yytext;  // Adicione esta linha para declarar externamente yytext
%}

%token ADD SUB MUL DIV NUMBER LPAREN RPAREN

%%

expression: 
    expression ADD term
    | expression SUB term
    | term
    ;

term:
    term MUL factor
    | term DIV factor
    | factor
    ;

factor:
    NUMBER
    | LPAREN expression RPAREN
    ;

%%

int main() {
    yyparse();
    return 0;
}

int yyerror(const char *s) {
    fprintf(stderr, "Erro de análise: %s\n", s);
    fprintf(stderr, "Último token lido: %s\n", yytext);
    return 0;
}

int yywrap(void) {
    return 1;
}
