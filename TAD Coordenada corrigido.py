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
    Cria um novo tabuleiro utilizando um dicionario;
    Associado a chave "especificacao" fica o tuplo da especificacao do tabuleiro
    associado a "tab" fica outro dicionario neste caso vazio onde se guardam os
    valores das celuldas(chave usa tad Coordenada) que sejam diferentes de 0
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
    if e_tabuleiro(t) and e_coordenada(c) and v in (0,1,2):
        if v in (1,2):
            t["tab"][c]=v
        elif c in t["tab"]:
            del t[c]
    else:
        raise ValueError('tabuleiro_preenche_celula: argumentos invalidos')
    return t

def tabuleiros_iguais(t1,t2):
    return t1==t2

def e_tabuleiro(arg):
    def tab_valido(tab):        
        for i in tab:
            if not e_coordenada(i) and tab[i] not in (1,2):
                return False
        return True
    
    if isinstance(arg,dict):
        if "especificacao" in arg and "tab" in arg:
            if e_especificacao(arg["especificacao"]) and isinstance(arg["tab"],dict):
                if tab_valido(arg["tab"]):
                    return True
    return False

def escreve_tabuleiro(t):
    
    def ext_valor(v):
        """ Retorna a representacao externa do valor de uma celula"""
        ext=(" ? "," . "," X ")
        return ext[v]
    
    def max_esp(esp):
        """
        funcao auxiliar que calcula a dimensao maxima dos tuplos das
        especificacoes das linhas ou colunas
        """
        max=len(esp[0])
        for t in esp:
            if max < len(t):
                max=len(t)
        return max    

    def linha_esp(esp_l,linha):
        """
        funcao que retorna a representacao externa de uma linha da especificacao
        das colunas a primeira linha e a 0
        """
        res = ""
        for i in esp_l:
            if len(i)>linha:
                res+=" "*2 + str(i[len(i)-(linha+1)]) +" "*2
            else:
                res+=" "*5
        res +="  \n"
        return res
        
    def linha_tab(t,esp_c,linha):
        """
        retorna a representacao externa de uma linha do tabuleiro incluindo a 
        especificacao da linha do lado direito
        """
        res = ""
        coluna = 1
        dimensao = tabuleiro_dimensoes(t)
        maxcoluna = dimensao[1]
        c = cria_coordenada(linha+1,coluna)
        while coluna <= maxcoluna:
            res += "[" + ext_valor(tabuleiro_celula(t,c)) + "]"
            coluna+=1
            c = cria_coordenada(linha+1,coluna)
            
        max_c_esp = max_esp(esp_c)
        n=0
        while n<max_c_esp:
            if n<len(esp_c[linha]):
                res+= " " + str(esp_c[linha][n])
            else:
                res+=" "*2
            n+=1
        res+= "|\n"
        return res
    
    res = ""
    if e_tabuleiro(t):
        esp = tabuleiro_especificacoes(t)
        max_l_esp = max_esp(esp[1])
        while max_l_esp>0:
            res+=linha_esp(esp[1],max_l_esp-1)
            max_l_esp-=1
        dimensao = tabuleiro_dimensoes(t)
        maxlinha = dimensao[0]  
        n=0
        while n < maxlinha:
            res+= linha_tab(t,esp[0],n)
            n+=1
        print (res)   
    else:
        raise ValueError ("escreve_tabuleiro: argumento invalido")

def linha_completa(esp,linha):
    n=0
    t=()
    for i in linha:
        if i == 2:
            n+=1
        elif i==1:
            if n>0:
                t=t+(n,)
            n=0
        else:
            return False
    if n>0:
        t=t+(n,)
    return esp==t

def tabuleiro_completo(t):
    dimensoes = tabuleiro_dimensoes(t)
    n=1
    esp=tabuleiro_especificacoes(t)
    while n<= dimensoes[0]:
        if not linha_completa(esp[0][n-1],lista_tabuleiro(dimensoes[1],lambda x:tabuleiro_celula(t,cria_coordenada(n,x)))):
            return False
        n+=1
    n=1    
    while n<= dimensoes[1]:
        if not linha_completa(esp[1][n-1],lista_tabuleiro(dimensoes[0],lambda x:tabuleiro_celula(t,cria_coordenada(x,n)))):
            return False
        n+=1
    return True

def lista_tabuleiro(n,celula):
    i=1
    res=[]
    while i <= n:
        res+=[celula(i)]
        i+=1
    return res

