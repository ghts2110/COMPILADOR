import Tokens
import Rules

if __name__ == '__main__':
    listaToken = Tokens.Token()
    listaRules = Rules.Rule()

    for i in listaRules.keys():
        for j in listaRules[i]:
            print(i + ' : ' + j)
