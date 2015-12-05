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
    
    
#TAD Tabuleiro Picross

def e_especificacao(t):
    """funcao auxiliar que verifica se o argumento e uma especificacao valida"""
    def e_esp_LC(t):
        """ Verifica se o tuplo corresponde a uma especificacao valida para
        linhas ou colunas"""
        for a in t:
            if isinstance(a,tuple):
                for i in a:
                    if not isinstance(i,int):
                        return False
            else:
                return False
        return True
        
    if not isinstance(t,tuple):
        return False
    elif len(t)!=2:
        return False
    elif not e_esp_LC(t[0]) or not e_esp_LC(t[1]):
        return False
    else:
        return True
    

            

def cria_tabuleiro(t):
    """
    Cria um novo tabuleiro
    """
    if e_especificacao(t):
        return {'especificacao':t,'tab':{}}
    else:
        raise ValueError('cria_tabuleiro: argumentos invalidos')

    

def tabuleiro_especificacoes(t):
    """"
    Devolve a especificacao do tabuleiro
    """
    return t['especificacao']

def tabuleiro_dimensoes(t):
    """
    Devolve um tuplo com as dimensoes do tabuleiro (linhas,colunas)
    """
    esp=tabuleiro_especificacoes(t)
    return (len(esp[0]),len(esp[1]))

def tabuleiro_celula(t,c):
    """
    Devolve o valor da celula correspondente a coordenada c do tabuleiro t
    """
    if e_tabuleiro(t) and e_coordenada(c):
        if c in t['tab']:
            return t['tab'][c]
        else:
            return 0
    else:
        raise ValueError('tabuleiro_celula: argumentos invalidos')
    
def tabuleiro_preenche_celula(t,c,v):
    if e_tabuleiro[t] and e_coordenada[c] and v in (0,1,2):
        if v in (1,2):
            t[tab][c]=v
        elif c in t[tab]:
            del t[c]
    else:
        raise ValueError('tabuleiro_preenche_celula: argumentos invalidos')
    return t

def e_tabuleiro(arg):
    def tab_valido(tab):        
        for i in tab:
            if not e_coordenada(i) and tab[i] not in (1,2):
                return False
        return true
    
    if isinstance(arg,dict):
        if "especificacao" in arg and "tab" in arg:
            if e_especificacao(arg["especificacao"]) and isinstance(arg["tab"],dict):
                if tab_valido(arg["tab"]):
                    return True
    return False

def escreve_tabuleiro(t):
    def ext_valor(v):
        """ Retorna a representacao externa do valor de uma celula"""
        ext=("  "," . "," X ")
        return ext[v]
    def max_esp(esp):
        """
        funcao auxiliar que calcula a dimensao maxima dos tuplos das
        especificacoes das linhas ou colunas
        """
        max=len(t[0])
        for t in esp:
            if max < len(t):
                max=t
        return max
    
    str = ""
    if e_tabuleiro(t):
        
    else:
        raise ValueError ("escreve_tabuleiro: argumento invalido")