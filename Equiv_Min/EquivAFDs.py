from AutomatoFD import AutomatoFD

class EquivalenciaAFDs():
    
    def __init__(self, afd1: AutomatoFD, afd2: AutomatoFD):
        self.afd1 = self.afd1
        self.afd2 = self.afd2
        
    def verificaEquivalencia(self):
        afd = AutomatoFD(self.alfabeto)
        """Cria dicionario de Estados"""
        estados = dict()
        cont = 0
        """Cria estados"""
        for i in self.afd1.estados:
            estados[(i,'self.afd1')] = cont
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
            for a in self.alfabeto:
                 o = estados[(i,'self.afd1')]
                 i2 = self.afd1.transicoes[(i,a)]
                 d = estados[(i2,'self.afd1')]
                 afd.criaTransicao(o,d,a)
        """Cria Transições AFD2 """
        for (i, a) in self.afd2.transicoes.keys():
            for a in self.alfabeto:
                o = estados[(i, 'afd2')]
                i2 = self.afd2.transicoes[(i, a)]
                d = estados[(i2, 'afd2')]
                afd.criaTransicao(o, d, a)
        """Verifica quais estados são equivalentes"""
        estadosEqui = afd.estadosEquivalentes()
        """Verifica se os dois estados iniciais são equivalentes"""
        x = self.afd1.inicial
        y = self.afd2.inicial
        v = estadosEqui[(x, y)]
        return v, afd, estadosEqui
        
    def equivEstados(self):
        """Retorna um dicionario com os Estados True como equivalentes e False como não Equivalentes"""
        tabelaEstEqui = dict()
        """Estados Trivialmente Não Equivalentes, serão setados como False"""
        for y in range(1, len(self.estados)):
            for x in range(0, (len(self.estados)-1)):
                if (y > x):
                        r = self.setEstadoTrivialmenteDesequivalentes(list(self.estados)[x], list(self.estados)[y]  )
                        tabelaEstEqui[list(self.estados)[x], list(self.estados)[y]] = r
                else:
                    break
        """Estados não Equivalentes"""
        """percorre o dicionario """
        roda = True
        cont = 0
        """Roda ate que não tenha feito mais nenhuma alteração"""
        while roda:
            cont = 0
            for (x, y) in tabelaEstEqui.keys():
                v = tabelaEstEqui[(x, y)]

                if(v):
                    """e verifica os estados que estão como True se não são equivalentes
                            , caso seja verdade, define como False"""
                    r = self.isEstadoEquivalente(tabelaEstEqui ,x, y)
                    tabelaEstEqui[x, y] = r
                    if(r == False):
                        cont+=1
            if(cont == 0):
                roda = False
        return tabelaEstEqui;