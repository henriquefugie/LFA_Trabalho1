from AutomatoFD import AutomatoFD

class Operacoes():
    
    def __init__(self, afd1: AutomatoFD, afd2: AutomatoFD):
        self.afd1 = afd1
        self.afd2 = afd2
    
    def uniao(self,afdm: AutomatoFD):
        cont=0
        for i in self.afd1.estados:
            for j in self.afd2.estados:
                if (self.afd1.estadoFinal(i) or self.afd2.estadoFinal(j)):
                    afdm.mudaEstadoFinal(cont, True)
                cont+=1 
   

    def intercessao(self,afdm: AutomatoFD):
        cont=0
        for i in self.afd1.estados:
            for j in self.afd2.estados:
                if (self.afd1.estadoFinal(i) and self.afd2.estadoFinal(j)):
                    afdm.mudaEstadoFinal(cont, True)
                cont+=1
       

    def complemento(afdc: AutomatoFD):
        for i in afdc.estados:
            if(afdc.estadoFinal(i)):
                afdc.mudaEstadoFinal(cont, False)
            else:
                afdc.mudaEstadoFinal(cont, True)

    def diferenca(afdm: AutomatoFD):
        for i in self.afd1.estados:
            for j in self.afd2.estados:
                if (self.afd1.estadoFinal(i) and not self.afd2.estadoFinal(j)):
                    afdm.mudaEstadoFinal(cont, True)
                cont+=1 