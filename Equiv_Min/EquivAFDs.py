from AutomatoFD import AutomatoFD

class EquivalenciaAFDs():
    
    def __init__(self, afd1: AutomatoFD, afd2: AutomatoFD):
        self.afd1 = afd1
        self.afd2 = afd2
        
    def EquivalenciaEntreAFDs(self):
        
        #antes de tudo, é necessário verificar se os alfabetos dos dois AFs são iguais, caso não, ele não consegue executar
        if(self.afd1.alfabeto != self.afd2.alfabeto):
            print("Os automatos possuem alfabetos diferentes")
            return
        #Neste ponto do código ele vai criar um novo afd que vai armazenar todos os estados e transicoes do dois automatos
        afd = AutomatoFD(self.afd1.alfabeto)
        estados = dict()
        cont = 0
        
        #Aqui ele percorre o primeiro e o segundo autmato para armazenar os estados e as transicoes no afd criado
        for i in self.afd1.estados:
            estados[(i,'afd1')] = cont
            afd.criaEstado(cont)
            
            #verifica se os estados são inicias ou finais
            if (i == self.afd1.inicial):
                afd.mudaEstadoInicial(cont)
            if (self.afd1.estadoFinal(i)):
                afd.mudaEstadoFinal(cont,True)
            cont += 1
            
        for j in self.afd2.estados:
            estados[(j, 'afd2')] = cont
            afd.criaEstado(cont)
            
            #verifica se os estados são inicias ou finais
            if (j == self.afd2.inicial):
                afd.mudaEstadoInicial(cont)
            if (self.afd2.estadoFinal(j)):
                afd.mudaEstadoFinal(cont, True)
            cont += 1

        #verifica as transicoes do primeiro automato
        for (i,a) in self.afd1.transicoes.keys():
            for a in self.afd1.alfabeto:
                 o = estados[(i,'afd1')]
                 i2 = self.afd1.transicoes[(i,a)]
                 d = estados[(i2,'afd1')]
                 afd.criaTransicao(o,d,a)
                 
        #verifica as transicoes do segundo automato
        for (i, a) in self.afd2.transicoes.keys():
            for a in self.afd2.alfabeto:
                o = estados[(i, 'afd2')]
                i2 = self.afd2.transicoes[(i, a)]
                d = estados[(i2, 'afd2')]
                afd.criaTransicao(o, d, a)
        
        #aqui ele verifica se os estados do afd gerado sao equivalentes
        equivalente = EquivalenciaAFD(afd)
        estadosEqui = equivalente.estadosEquiv()
        
        #neste ponto, ele verifica se na tabela, os estados inicias dos dois autmatos são equivalentes ou não, se sim são equivalentes, se não, não
        x = self.afd1.inicial
        y = (len(self.afd1.estados))
        v = estadosEqui[(x, y)]
        
        if(v):
            print("Os AFDs sao equivalentes")
        else:
            print("Os AFDs NAO sao equivalentes")
    
class EquivalenciaAFD():
    
    def __init__(self, afd: AutomatoFD):
        self.afd = afd
        
    def estadosEquiv(self):
        
        #aqui ele vai criar a matriz que armazena se os estados sao equivalentes ou não, onde False seria não equivalente e True equivalente
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
        
        #aqui ele verifica os valores colocados na matriz,caso o valor seja armazenado como True, ele faz uma segunda verificacao
        while continua:
            contador = 0
            for(j, i) in tabelaEstadosEquivalentes.keys():
                valor = tabelaEstadosEquivalentes[(j, i)]
                
                if valor:
                    resultado = self.Equivalente(tabelaEstadosEquivalentes, j, i)
                    tabelaEstadosEquivalentes[j, i] = resultado
                    if(resultado == False):
                        contador += 1
            if(contador == 0):
                continua = False
        return tabelaEstadosEquivalentes
    
    #Esta funcao verifica se os True são realmente equivalentes, caso não, ele define como False
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
    
    # esta funcao ja elimina da tabela os casos onde um estado é inicial ou final e classifica na tabela como False para os diferentes e True para os que são inicias e finais simultaneamente
    def estadosTrivialmenteNaoEquivalentes(self, estadoX, estadoY):
        if(self.afd.estadoFinal(estadoX) and self.afd.estadoFinal(estadoY)):
            return True
        elif(not self.afd.estadoFinal(estadoX) and not self.afd.estadoFinal(estadoY)):
            return True
        elif(self.afd.estadoFinal(estadoX) and not self.afd.estadoFinal(estadoY)):
            return False
        elif(not self.afd.estadoFinal(estadoX) and self.afd.estadoFinal(estadoY)):
            return False