flex lexer.l
yacc -d parser.y
gcc lex.yy.c y.tab.c -o calculator
