#Grupo:8 Joao Loureiro n 182607 , Pedro Caetano n 56564
#############################################################################

#TAD coordenada

def cria_coordenada(linha, coluna):
    """
    CONSTRUTOR
    
    Cria uma nova coordenada a partir de dois inteiros
    (correspondentes a uma linha e a uma coluna)
    com as especificacoes apresentadas na funcao
    
    Sendo o TAD coordenada um tipo imutavel, o mais logico
    para a representacao interna seria usar um tuplo 
    (i.e ao inves de uma lista) pois tambem estes sao imutaveis 
    """
    if not isinstance (linha, int) or not isinstance (coluna, int):
        raise ValueError ('cria_coordenadas: argumentos invalidos')
    elif linha<1 or coluna<1:
        raise ValueError ('cria_coordenada: argumentos invalidos')
    else:
        return (linha, coluna)
    
def coordenada_linha(coordenada):
    """
    SELECTOR
    
    Devolve a linha respectiva
    """
    return coordenada[0]

def coordenada_coluna(coordenada):
    """
    SELECTOR
    
    Devolve a coluna respectiva
    """
    return coordenada[1]

def e_coordenada(arg):
    """
    RECONHECEDOR
    
    Verifica se o argumento inserido
    e do tipo coordenada
    """
    if isinstance(arg, (tuple)):
        if len(arg)==2 and arg[0]>=1 and arg[1]>=1:
            return True
        else:
            return False
    else:
        return False

def coordenadas_iguais(c1, c2):
    """
    TESTE
    
    Recebe dois elementos do tipo coordenada 
    e verifica se sao iguais ou nao
    """
    return c1[0]==c2[0] and c1[1]==c2[1]

def coordenada_para_cadeia(coordenada):
    """
    TRANSFORMADOR DE SAIDA
    
    Devolve uma representacao externa do tipo coordenada
    """
    return  ( '(' + str(coordenada[0]) + ' : ' + str(coordenada[1]) + ')' )

    
#############################################################################

#TAD tabuleiro

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
    valores das celulas(chave usa tad Coordenada) que sejam diferentes de 0
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
        dim = tabuleiro_dimensoes(t)
        if coordenada_linha(c) <= dim[0] and coordenada_coluna(c)<=dim[1]:
            if c in t['tab']:
                return t['tab'][c]
            else:
                return 0
    
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
        ext=(" ? "," . "," x ")
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


#############################################################################

#TAD Jogada

def cria_jogada (coordenada, valor):
    """
    CONSTRUTOR
    
    Recebe como argumentos um elemento do tipo coordenada 
    e um inteiro 1 ou 2 (referente a uma celula: se o inteiro
    for 1 a celula corresponde a uma celula em branco; se o 
    inteiro for dois corresponde a uma caixa)
    
    Optou-se por um tuplo, com o tuplo correspondente 
    ao tipo coordenada no indice 0 e o valor no indice 1
    """
    if not e_coordenada(coordenada) or valor not in [1,2]:
        raise ValueError ('cria_jogada: argumentos invalidos')
    else:
        return (coordenada, valor)
    
def jogada_coordenada(jogada):
    """
    SELECTOR
    
    Recebe um argumento do tipo jogada e devolve a coordenada 
    """
    return jogada[0]

def jogada_valor(jogada):
    """
    SELECTOR
    
    Recebe um argumento do tipo jogada e devolve o valor 
    """
    return jogada[1]

def e_jogada (arg):
    """
    RECONHECEDOR
    
    Verifica se o argumento inserido e do tipo jogada 
    """
    if isinstance(arg, (tuple)):
        if len(arg)==2 and e_coordenada(arg[0]) and arg[1] in [1,2]:
            return True
        else:
            return False
    else:
        return False

def jogadas_iguais(j1,j2):
    """
    TESTE
    
    Recebe dois argumentos do tipo jogada 
    e verifica se as jogadas sao iguais
    """
    return j1[0]==j2[0] and j1[1]==j2[1]

def jogada_para_cadeia(jogada):
    """
    TRANSFORMADOR DE SAIDA
    
    Recebe uma jogada e devolve uma representacao externa para o tipo
    """
    return ( coordenada_para_cadeia(jogada[0]) + ' --> ' + str(jogada[1]) )


#############################################################################

#Funcao le_tabuleiro

def le_tabuleiro(fich_cc):
    """
    Recebe como argumento uma string correspondente ao nome de um ficheiro
    (tuplo de tuplos que contem as especificacaoes do jogo)
     e devolvende o conteudo do ficheiro 
    """
    fich=open(fich_cc,'r')
    tuplo_res=eval(fich.read())   #a leitura do ficheiro devolve uma string, sendo necessario devolver o tuplo
    fich.close()                    
    return tuplo_res


#############################################################################

#Funcao pede_jogada
    
def pede_jogada(tabuleiro):  
    dimensao_lin=(tabuleiro_dimensoes(tabuleiro))[0]
    dimensao_col=(tabuleiro_dimensoes(tabuleiro))[1]
    possibilidades_lin=range(1,dimensao_lin+1)
    possibilidades_col=range(1,dimensao_col+1)
    print('Introduza a jogada')
    pede_coordenada=input('- coordenada entre (1 : 1) e (' + str(dimensao_lin) + ' : ' + str(dimensao_col) + ')' + ' >> ')
    pede_valor=eval(input('- valor' + ' >> '))
    
    def jogada_valida(coord,val):
        coord_linha=eval(coord[1])
        coord_coluna=eval(coord[5])
        if coord_linha not in possibilidades_lin or coord_coluna not in possibilidades_col or val not in [1,2]:
            return False
        else:
            return cria_jogada((coord_linha, coord_coluna), val)
    
    return jogada_valida(pede_coordenada, pede_valor)


#############################################################################

#Funcao jogo_picross e funcao auxiliar celulas_vazias

def jogo_picross(ficheiro):           #????????????????????????????????????
    fich_tuplo=le_tabuleiro(ficheiro)
    tabuleiro_para_jogar=cria_tabuleiro(fich_tuplo)
    print ("JOGO PICROSS")
    escreve_tabuleiro(tabuleiro_para_jogar)
    while celulas_vazias(tabuleiro_para_jogar) == True:    #enquanto houver celulas vazias...
        jogada=pede_jogada(tabuleiro_para_jogar)
        if jogada != False:
            tabuleiro_para_jogar=tabuleiro_preenche_celula(tabuleiro_para_jogar, jogada[0], jogada[1])
            escreve_tabuleiro(tabuleiro_para_jogar)
        else:
            print('Jogada invalida.')
        
    if tabuleiro_completo(tabuleiro_para_jogar):
        print ("JOGO: Parabens, encontrou a solucao!")
        return True
    else:
        print ("JOGO: O tabuleiro nao esta correto!")
        return False

def celulas_vazias(tabuleiro):
    
    def celulas_vazias_aux(tabuleiro, possibilidades_lin, possibilidades_col):
        tuplo_controlo=()
        for posslin in range(1,possibilidades_lin+1):
            for posscol in range(1,possibilidades_col+1):
                val_celula=tabuleiro_celula(tabuleiro, cria_coordenada (posslin, posscol) )
                if val_celula == 0:
                    tuplo_controlo+=cria_coordenada (posslin, posscol)
        return tuplo_controlo
    
    dim = tabuleiro_dimensoes(tabuleiro)
    if celulas_vazias_aux(tabuleiro,dim[0],dim[1]) != () :
        return True
    else:
        return False
