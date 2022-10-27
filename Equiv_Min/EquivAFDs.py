from AutomatoFD import AutomatoFD

class EquivalenciaAFDs():
    
    def __init__(self, afd1: AutomatoFD, afd2: AutomatoFD):
        self.afd1 = afd1
        self.afd2 = afd2
        
    def EquivalenciaEntreAFDs(self):
        afd = AutomatoFD(self.afd1.alfabeto)
        """Cria dicionario de Estados"""
        estados = dict()
        cont = 0
        """Cria estados"""
        for i in self.afd1.estados:
            estados[(i,'afd1')] = cont
            afd.criaEstado(cont)
            """Verifica se é Estado Inicial"""
            if (i == self.afd1.inicial):
                afd.mudaEstadoInicial(cont)
            """Verifica se é Estado Final"""
            if (self.afd1.estadoFinal(i)):
                afd.mudaEstadoFinal(cont,True)
            cont += 1
        for j in self.afd2.estados:
            estados[(j, 'afd2')] = cont
            afd.criaEstado(cont)
            """Verifica se é Estado Inicial"""
            if (j == self.afd2.inicial):
                afd.mudaEstadoInicial(cont)
            """Verifica se é Estado Final"""
            if (self.afd2.estadoFinal(j)):
                afd.mudaEstadoFinal(cont, True)
            cont += 1
        """Cria Transições AFD1 """
        for (i,a) in self.afd1.transicoes.keys():
            for a in self.afd1.alfabeto:
                 o = estados[(i,'afd1')]
                 i2 = self.afd1.transicoes[(i,a)]
                 d = estados[(i2,'afd1')]
                 afd.criaTransicao(o,d,a)
        """Cria Transições AFD2 """
        for (i, a) in self.afd2.transicoes.keys():
            for a in self.afd1.alfabeto:
                o = estados[(i, 'afd2')]
                i2 = self.afd2.transicoes[(i, a)]
                d = estados[(i2, 'afd2')]
                afd.criaTransicao(o, d, a)
        """Verifica quais estados são equivalentes"""
        estadosEqui = afd.estadosEquiv()
        """Verifica se os dois estados iniciais são equivalentes"""
        x = self.afd1.inicial
        y = self.afd2.inicial
        v = estadosEqui[(x, y)]
        return v, afd, estadosEqui
    
class EquivalenciaAFD():
    
    def __init__(self, afd: AutomatoFD):
        self.afd = afd
        
    def estadosEquiv(self):
        tabelaEstadosEquivalentes = dict()
        
        for i in range(1, len(self.afd.estados)):
            for j in range(0, (len(self.afd.estados)-1)):
                if(i > j):
                    resultado = self.estadosTrivialmenteNaoEquivalentes(list(self.afd.estados)[j], list(self.afd.estados)[i])
                    tabelaEstadosEquivalentes[list(self.afd.estados)[j], list(self.afd.estados)[i]] = resultado

                else:
                    break
        
        continua = True
        contador = 0
        
        while continua:
            contador = 0
            for(j, i) in tabelaEstadosEquivalentes.keys():
                verdade = tabelaEstadosEquivalentes[(j, i)]
                
                if verdade:
                    resultado = self.Equivalente(tabelaEstadosEquivalentes, j, i)
                    tabelaEstadosEquivalentes[j, i] = resultado
                    if(resultado == False):
                        contador += 1
            if(contador == 0):
                continua = False
        return tabelaEstadosEquivalentes
    
    def Equivalente(self, tabelaEstadosEquivalentes, j = 0, i = 0):
        for a in self.afd.alfabeto:
            x = self.afd.transicoes[(j, a)]
            y = self.afd.transicoes[(i, a)]
            if(x < y):
                valor = tabelaEstadosEquivalentes[(x, y)]
                if(valor == False):
                    return False
            elif(y < x):
                valor = tabelaEstadosEquivalentes[(y, x)]
                if(valor == False):
                    return False
        return True
    
    def estadosTrivialmenteNaoEquivalentes(self, estadoX, estadoY):
        if(self.afd.estadoFinal(estadoX) and self.afd.estadoFinal(estadoY)):
            return True
        elif(not self.afd.estadoFinal(estadoX) and not self.afd.estadoFinal(estadoY)):
            return True
        elif(self.afd.estadoFinal(estadoX) and not self.afd.estadoFinal(estadoY)):
            return False
        elif(not self.afd.estadoFinal(estadoX) and self.afd.estadoFinal(estadoY)):
            return False
        
    def equivalenciaEntreAFDs(self, afd, afd2):
        afd = AutomatoFD(self.alfabeto)
        """Cria dicionario de Estados"""
        estados = dict()
        cont = 0
        """Cria estados"""
        for i in afd.estados:
            estados[(i,'afd')] = cont
            afd.criaEstado(cont)
            """Verifica se é Estado Inicial"""
            if (i == afd.inicial):
                afd.mudaEstadoInicial(cont)
            """Verifica se é Estado Final"""
            if (afd.estadoFinal(i)):
                afd.mudaEstadoFinal(cont,True)
            cont += 1
        for j in afd2.estados:
            estados[(j, 'afd2')] = cont
            afd.criaEstado(cont)
            """Verifica se é Estado Inicial"""
            if (j == afd2.inicial):
                afd.mudaEstadoInicial(cont)
            """Verifica se é Estado Final"""
            if (afd2.estadoFinal(j)):
                afd.mudaEstadoFinal(cont, True)
            cont += 1
        """Cria Transições AFD1 """
        for (i,a) in afd.transicoes.keys():
            for a in self.alfabeto:
                 o = estados[(i,'afd')]
                 i2 = afd.transicoes[(i,a)]
                 d = estados[(i2,'afd')]
                 afd.criaTransicao(o,d,a)
        """Cria Transições AFD2 """
        for (i, a) in afd2.transicoes.keys():
            for a in self.alfabeto:
                o = estados[(i, 'afd2')]
                i2 = afd2.transicoes[(i, a)]
                d = estados[(i2, 'afd2')]
                afd.criaTransicao(o, d, a)
        """Verifica quais estados são equivalentes"""
        estadosEqui = afd.estadosEquivalentes()
        """Verifica se os dois estados iniciais são equivalentes"""
        x = afd.inicial
        y = afd2.inicial
        v = estadosEqui[(x, y)]
        return v, afd, estadosEqui