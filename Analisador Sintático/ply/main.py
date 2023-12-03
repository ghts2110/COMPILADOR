from lexer import lexer
from parser import parser
from parser import linha


def main():
    data = """int x; // Declaracao de variavel
        float y;
        char z;
        int num1 = 42; // Atribuicao de valor
        float num2 = 3.14;
        char str1[] = "Hello, World!"
        char str2[] = "This is a string with special characters: ";
        int num3 = 3.14; // Erro de tipo"""

    lista = data.split('\n')

    for c in lista:
        linha()
        lexer.input(c)
        result = parser.parse(c, lexer=lexer)


if __name__ == "__main__":
    main()
