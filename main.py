from AutomatoFD import *
from Equiv_Min.EquivAFDs import EquivalenciaAFDs
from Equiv_Min.EquivAFDs import EquivalenciaAFD
from JFLAP.SalvarJFLAP import SalvarJFLAP
from JFLAP.LerJFLAP import LerJFLAP

def copiaAFD(self):
    afdcopia = self
    return afdcopia
    
if __name__ == '__main__':
    
    leitura2 = LerJFLAP(caminho = "./JFLAP/Exemplos/AutomatoA.jff")
    afdA = leitura2.lerAFD()
    print(afdA)
    
    leitura2 = LerJFLAP(caminho = "./JFLAP/Exemplos/AutomatoB.jff")
    afdB = leitura2.lerAFD()
    print(afdB)
    
    # equivalencia = EquivalenciaAFD(afdA)
    # tabelaEstEqui = equivalencia.estadosEquiv()
    # for (x, y) in tabelaEstEqui.keys():
    #     v = tabelaEstEqui[(x, y)]
    #     print("({} e {})-->{}, \n".format(x, y, v))
    
    equivalenciaAFDs = EquivalenciaAFDs(afdA, afdB)
    
    v, afd, estadosEqui = equivalenciaAFDs.EquivalenciaEntreAFDs()
    if(v):
        print("Os AFDs são equivalentes!!")
    else:
        print("Os AFDs NÂO são equivalentes!!")
    
