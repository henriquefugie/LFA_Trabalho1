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
    
    leitura = LerJFLAP(nome = "AutomatoParaMinimizar")
    afdparamin = leitura.lerAFD()

    minimiza = MinimizaAFD(afdparamin)
    afdAmin = minimiza.minimizaAFD()
    print(afdAmin)
    
    salva = SalvarJFLAP(afd= afdAmin, nome= "AutomatoMinimizado")
    salva.salvarAFD()
    
    leitura = LerJFLAP(nome = "AutomatoA")
    afdA = leitura.lerAFD()
    print(afdA)
    
    leitura = LerJFLAP(nome = "AutomatoB")
    afdB = leitura.lerAFD()
    print(afdB)
    
    equivalencia = EquivalenciaAFD(afd = afdA)
    tabelaEstEquivalentes = equivalencia.estadosEquiv()
    print("Tabela dos estados equivalentes")
    for (x, y) in tabelaEstEquivalentes.keys():
        v = tabelaEstEquivalentes[(x, y)]
        print("({} e {})-->{}, ".format(x, y, v))
        
    equivalenciaAFDs = EquivalenciaAFDs(afd1 = afdA, afd2 = afdB)
    equivalenciaAFDs.EquivalenciaEntreAFDs()