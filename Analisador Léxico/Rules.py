def Rule():
    listRules = {'Programa': [], 'Declaração': [], 'DeclaracaoVariavel': [], 'Tipo': [], 'DeclaracaoFuncao': [],
                 'Parametros': [], 'Bloco': [], 'Comentário': [], 'Expressões': [], 'Atribuicao': [],
                 'EstruturaControle': [], 'DeclaracaoEstrutura': [], 'Array': [], 'Expressao': [],
                 'ExpressaoLogica': [], 'ExpressaoRelacional': [], 'ExpressaoAritmetica': [],
                 'ExpressaoMultiplicativa': [], 'ExpressaoUnaria': [], 'ExpressaoPostfix': [], 'Argumentos': [],
                 'Primaria': []}

    listRules['Programa'].append('Declaracao')

    listRules['Declaração'].append('DeclaracaoVariavel')
    listRules['Declaração'].append('DeclaracaoFuncao')
    listRules['Declaração'].append('DeclaracaoEstrutura')
    listRules['Declaração'].append('Comentario')

    listRules['DeclaracaoVariavel'].append('Tipo ID')
    listRules['DeclaracaoVariavel'].append('Tipo ID = Expressao')

    listRules['Tipo'].append('int')
    listRules['Tipo'].append('float')
    listRules['Tipo'].append('double')
    listRules['Tipo'].append('char')
    listRules['Tipo'].append('boolean')

    listRules['DeclaracaoFuncao'].append('Tipo ID ( Parametros ) Bloco')

    listRules['Parametros'].append('Parametro')
    listRules['Parametros'].append('Parametro, Parametros')
    listRules['Parametros'].append('Tipo ID')
    listRules['Parametros'].append('Tipo ID []')
    listRules['Parametros'].append('Tipo ... ID')

    listRules['Bloco'].append('{ Declaracao }')

    listRules['Comentário'].append('// Qualquer texto até o final da linha')
    listRules['Comentário'].append('/* Qualquer texto até */')

    listRules['Expressões'].append('Atribuicao')

    listRules['Atribuicao'].append('D = Expressao')
    listRules['Atribuicao'].append('ID += Expressao')
    listRules['Atribuicao'].append('ID -= Expressao')
    listRules['Atribuicao'].append('ID *= Expressao')
    listRules['Atribuicao'].append('ID /= Expressao')
    listRules['Atribuicao'].append('D %= Expressao')
    listRules['Atribuicao'].append('ID &&= Expressao')
    listRules['Atribuicao'].append(' ID ||= Expressao')
    listRules['Atribuicao'].append('ID = ID')
    listRules['Atribuicao'].append('ID += ID')
    listRules['Atribuicao'].append('ID -= ID')
    listRules['Atribuicao'].append('ID *= ID')
    listRules['Atribuicao'].append('ID /= ID')
    listRules['Atribuicao'].append('D %= ID')
    listRules['Atribuicao'].append('ID &&= ID')
    listRules['Atribuicao'].append('ID ||= ID')

    listRules['EstruturaControle'].append('if ( Expressao ) Bloco')
    listRules['EstruturaControle'].append('if ( Expressao ) Bloco else Bloco')
    listRules['EstruturaControle'].append('while ( Expressao ) Bloco')
    listRules['EstruturaControle'].append('for ( Expressao ; Expressao ; Expressao ) Bloco')
    listRules['EstruturaControle'].append('switch ( Expressao ) CaseLista')
    listRules['EstruturaControle'].append('CaseDecl')
    listRules['EstruturaControle'].append('case Expressao : Bloco')
    listRules['EstruturaControle'].append('break ;')
    listRules['EstruturaControle'].append('continue ;')
    listRules['EstruturaControle'].append('return Expressao ;')

    listRules['DeclaracaoEstrutura'].append('struct ID { DeclaracaoVariavel }')

    listRules['Array'].append('ID [ Expressao ]')
    listRules['Array'].append('ID [ ]')
    listRules['Array'].append('{ ExpressaoLista }')

    listRules['Expressao'].append('ExpressaoLogica')

    listRules['ExpressaoLogica'].append('ExpressaoRelacional')
    listRules['ExpressaoLogica'].append('ExpressaoLogica && ExpressaoRelacional')
    listRules['ExpressaoLogica'].append('ExpressaoLogica || ExpressaoRelacional')
    listRules['ExpressaoLogica'].append('! ExpressaoRelacional')

    listRules['ExpressaoRelacional'].append('ExpressaoAritmetica')
    listRules['ExpressaoRelacional'].append('ExpressaoAritmetica > ExpressaoAritmetica')
    listRules['ExpressaoRelacional'].append('ExpressaoAritmetica >= ExpressaoAritmetica')
    listRules['ExpressaoRelacional'].append('ExpressaoAritmetica < ExpressaoAritmetica')
    listRules['ExpressaoRelacional'].append('ExpressaoAritmetica <= ExpressaoAritmetica')
    listRules['ExpressaoRelacional'].append('ExpressaoAritmetica != ExpressaoAritmetica')
    listRules['ExpressaoRelacional'].append('ExpressaoAritmetica == ExpressaoAritmetica')

    listRules['ExpressaoAritmetica'].append('ExpressaoMultiplicativa')
    listRules['ExpressaoAritmetica'].append('ExpressaoAritmetica + ExpressaoMultiplicativa')
    listRules['ExpressaoAritmetica'].append('ExpressaoAritmetica - ExpressaoMultiplicativa')

    listRules['ExpressaoMultiplicativa'].append('ExpressaoUnaria')
    listRules['ExpressaoMultiplicativa'].append('ExpressaoMultiplicativa * ExpressaoUnaria')
    listRules['ExpressaoMultiplicativa'].append('ExpressaoMultiplicativa / ExpressaoUnaria')
    listRules['ExpressaoMultiplicativa'].append('ExpressaoMultiplicativa % ExpressaoUnaria')

    listRules['ExpressaoUnaria'].append('ExpressaoPostfix')
    listRules['ExpressaoUnaria'].append('-ExpressaoUnaria')
    listRules['ExpressaoUnaria'].append('++ ExpressaoPostfix')
    listRules['ExpressaoUnaria'].append('-- ExpressaoPostfix')

    listRules['ExpressaoPostfix'].append('Primaria')
    listRules['ExpressaoPostfix'].append('Primaria [ Expressao ]')
    listRules['ExpressaoPostfix'].append('Primaria ( Argumentos )')
    listRules['ExpressaoPostfix'].append('Primaria . ID')
    listRules['ExpressaoPostfix'].append('Primaria -> ID')

    listRules['Argumentos'].append('ExpressaoLista')
    listRules['Argumentos'].append('vazio')

    listRules['Primaria'].append('ID')
    listRules['Primaria'].append('NUM_INT')
    listRules['Primaria'].append('NUM_DEC')
    listRules['Primaria'].append('TEXTO')
    listRules['Primaria'].append('( Expressao )')

    return listRules
