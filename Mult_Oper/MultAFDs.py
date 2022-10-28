from asyncio.windows_events import NULL
from re import I
from AutomatoFD import AutomatoFD
from JFLAP.LerJFLAP import LerJFLAP


class MultAFDs:

    def __init__(self, afd1: AutomatoFD, afd2: AutomatoFD):
        self.afd1 = afd1
        self.afd2 = afd2

    def multiplicaAFD(self):
        
        if(self.afd1.alfabeto!=self.afd2.alfabeto):
            print('Automatos possuem alfabeto diferentes')
            return NULL

        afdm=AutomatoFD(self.afd1.alfabeto)

        #Cria dicionario de Estados
        est=dict()
        estados = list()
        #Cria estados
        cont=0
        for i in self.afd1.estados:
            for j in self.afd2.estados:
                est['afd1']=i
                est['afd2']=j
                estados.append(est.copy())
                #Verifica se é Estado Inicial
                if i==self.afd1.inicial and j==self.afd2.inicial:
                    afdm.criaEstado(cont,True)
                else:
                    afdm.criaEstado(cont)
                cont+=1    
        #Cria Transições
        for a in afdm.alfabeto:
            cont=0;
            for e in estados:
                contpos=0;
                pos1=pos2=0
                for v in e.values(): 
                    
                    if contpos==0:
                        pos1=self.afd1.transicoes[(v,a)]
                        contpos+=1
                    else:    
                        pos2=self.afd2.transicoes[(v,a)]
                est['afd1']=pos1
                est['afd2']=pos2

                i=0
                while i < estados.__len__():
                    if (estados[i]==est):
                        afdm.criaTransicao(cont,i,a)
                        break
                    i+=1    
                cont+=1        
            
        return afdm

