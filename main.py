from AutomatoFD import *
from Equiv_Min.EquivAFDs import EquivalenciaAFDs
from Equiv_Min.EquivAFDs import EquivalenciaAFD
from Equiv_Min.MiniAFD import MinimizaAFD
from JFLAP.SalvarJFLAP import SalvarJFLAP
from JFLAP.LerJFLAP import LerJFLAP

def copiaAFD(self):
    afdcopia = self
    return afdcopia
    
if __name__ == '__main__':
    
    leitura2 = LerJFLAP(nome = "prefixo_ab-sufixo_ab")
    afdA = leitura2.lerAFD()
    
    leitura2 = LerJFLAP(nome = "prefixo_ab-sufixo_ab_comVazio")
    afdB = leitura2.lerAFD()
    
    minimiza = MinimizaAFD(afdA)
    afd = minimiza.minimizaAFD()
    print(afd)
    
    salva = SalvarJFLAP(afd= afd, nome= "AFDminimizado")
    salva.salvarAFD()

    minimiza = MinimizaAFD(afdB)
    afdB1 = minimiza.minimizaAFD()
    print(afdB1)
    
    salva = SalvarJFLAP(afd= afdB1, nome= "AFDminimizadocomVazio")
    salva.salvarAFD()