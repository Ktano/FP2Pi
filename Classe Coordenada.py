class coordenada:
    
    def cria_coordenada (self, linha, coluna):
        if not isinstance (linha, int) or not isinstance (coluna, int):
            raise ValueError ('cria_coordenadas: argumentos invalidos')
        elif linha<0 or coluna<0:
            raise ValueError ('cria_coordenadas: argumentos invalidos')
        else:
            self.linha=linha
            self.coluna=coluna
            
    
    def coordenada_linha(self):
        return self.linha
    
    def coordenada_coluna(self):
        return self.coluna
    
    def e_coordenada(arg):
        return isinstance(arg, coordenada)
    
    def coordenadas_iguais(self, outro):
        return self.linha==outro.coordenada_linha() and self.coluna==outro.coordenada_coluna()
    
    def coordenada_para_cadeia(self):
        print ('\'' + '(' + str(self.linha) + ' : ' + str(self.coluna) + ')' + '\'')

#TAD Tabuleiro Picross

def cria_tabuleiro(t):
    if isinstance(t,tuple):
        return {'especificacao':t,'tab':{}}

    

def tabuleiro_especificacoes(t):
    return t['especificacao']