def cria_jogada (coordenada, valor):
    if not e_coordenada(coordenada) or valor not in [1,2]:
        raise ValueError ('cria jogada: argumentos invalidos')
    else:
        return (coordenada, valor)
    

def jogada_coordenada(jogada):
    return jogada[0]


def jogada_valor(jogada):
    return jogada[1]


def e_jogada (arg):
    if isinstance(arg, (tuple)):
        if len(arg)==2 and e_coordenada(arg[0]) and arg[1] in [1,2]:
            return True
        else:
            return False
    else:
        return False


def jogadas_iguais(j1,j2):
    return j1[0]==j2[0] and j1[1]==j2[1]


def jogada_para_cadeia(jogada):
    return ( coordenada_para_cadeia(jogada[0]) + ' --> ' + str(jogada[1]) )



