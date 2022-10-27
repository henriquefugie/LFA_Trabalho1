from re import I
from LFA_Trabalho1.AutomatoFD import AutomatoFD
from LFA_Trabalho1.JFLAP.LerJFLAP import LerJFLAP


class MultAFDs:

    def __init__(self, afd1: AutomatoFD, afd2: AutomatoFD):
        self.afd1 = afd1
        self.afd2 = afd2

    def multiplicaAFD(self):

        afdm=AutomatoFD(self.alfabeto)

        """Cria dicionario de Estados"""
        estados = dict()
        cont=0;
        """Cria estados"""
        for i in self.afd1.estados:
            for j in self.afd2.estados:
                estados[('afd1',i),('afd2',j)] = cont
                print(estados[cont])
                """Verifica se é Estado Inicial"""
                if i==self.afd1.inicial and j==self.afd2.inicial:
                    afdm.criaEstado(i,True)
                else:
                    afdm.criaEstado(i)    
        """Cria Transições """
        for a in self.alfabeto:
            cont=0
            while cont < estados.__len__():
                pos1=self.afd1.transicoes[(estados[cont]['afd1'],a)]
                pos2=self.afd1.transicoes[(estados[cont]['afd2'],a)]
                afdm.criaTransicao(cont,estados[(pos1,'afd1'),(pos2,'afd2')],a)
                cont+=1
            
        return afdm

