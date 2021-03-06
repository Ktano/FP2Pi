def cria_coordenada(linha, coluna):
    if not isinstance (linha, int) or not isinstance (coluna, int):
        raise ValueError ('cria_coordenadas: argumentos invalidos')
    elif linha<1 or coluna<1:
        raise ValueError ('cria_coordenadas: argumentos invalidos')
    else:
        return (linha, coluna)
    
def coordenada_linha(coordenada):
    return coordenada[0]

def coordenada_coluna(coordenada):
    return coordenada[1]

def e_coordenada(arg):
    if isinstance(arg, (tuple)):
        if len(arg)==2 and arg[0]>=1 and arg[1]>=1:
            return True
    return False

def coordenadas_iguais(c1, c2):
    return c1[0]==c2[0] and c1[1]==c2[1]

def coordenada_para_cadeia(coordenada):
    return  ( '(' + str(coordenada[0]) + ' : ' + str(coordenada[1]) + ')' )
    
    

