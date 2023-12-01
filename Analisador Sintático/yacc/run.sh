lex lexer.l
yacc -d parser.y
gcc -DYY_MAIN lex.yy.c y.tab.c -o calculator -lm
#./calculator < input.txt

