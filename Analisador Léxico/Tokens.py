reservedWords = ["int", "float", "char", "boolean", "void", "if", "else", "for", "while",
                 "scanf", "println", "main", "return"]

Operators = ["=", "+", "-", "*", "/", "%", "&&", "||", "!", "&", "|"]

comparison = [">", ">=", "<", "<=", "!=", "=="]

Symbols = ["(", ")", "[", "]", "{", "}", ",", ";"]

listaToken = []
listIdentifiers = []

npt = '/Users/gabriel/Documents/COMPILADORES/input.txt '

nome_arquivo = 'input.txt'


def Token():
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            linhas = [linha.strip() for linha in linhas]
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    for s in linhas:
        index = 0
        while len(s) != 0:
            c = str(s[0])
            s = s[1:]

            if c.isnumeric():
                while len(s) != 0 and (s[0].isnumeric() or s[0] == '.'):
                    c += str(s[0])
                    s = s[1:]

                if '.' in c:
                    listaToken.append({"type ": "Num_float", "value": c})
                else:
                    listaToken.append({"type ": "Num_int", "value": c})

                index += 1
            elif c in Symbols:
                listaToken.append({"type ": "Symbols", "value": c})
            elif c in comparison or (len(s) > 0 and (c + s[0] == "==" or c + s[0] == "!=")):
                if c + s[0] == "==" or c + s[0] == "!=":
                    c = c + s[0]
                    s = s[1:]
                if (c == '>' and s[0] == '=') or (c == '<' and s[0] == '='):
                    c = c + s[0]
                    s = s[1:]

                listaToken.append({"type ": "Comparison operators", "value": c})
            elif len(s) > 1 and c == '/' and s[0] == '/':
                c = c + s
                s = ""
                listaToken.append({"type ": "Comments", "value": c})
            elif c in Operators:
                if c == '&' or c == '|' and c == s[0]:
                    c = c + s[0]
                    s = s[1:]

                listaToken.append({"type ": "Operators", "value": c})
            elif c == "'":
                while s[0] != "'":
                    c = c + s[0]
                    s = s[1:]
                c = c + s[0]
                s = s[1:]

                listaToken.append({"type ": "Char", "value": c})
            elif c == '"':
                while s[0] != '"':
                    c = c + s[0]
                    s = s[1:]
                c = c + s[0]
                s = s[1:]

                listaToken.append({"type ": "String", "value": c})
            elif c != " " and c != "\t":
                while (len(s) > 0 and (s[0] not in Operators) and (s[0] not in comparison) and
                       (s[0] not in Symbols) and len(s) > 0 and s[0] != " "):
                    c = c + s[0]
                    s = s[1:]

                if c in reservedWords:
                    listaToken.append({"type ": "Reserved Words", "value": c})
                else:
                    if c in listIdentifiers:
                        listaToken.append({"type ": "(id, " + str(listIdentifiers.index(c)) + ")", "value": c})
                    else:
                        listIdentifiers.append(c)
                        listaToken.append({"type ": "(id, " + str(listIdentifiers.index(c)) + ")", "value": c})

    return listaToken




