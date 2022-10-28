from AutomatoFD import AutomatoFD

class Operacoes():
    
    def __init__(self, afd1: AutomatoFD, afd2: AutomatoFD):
        self.afd1 = afd1
        self.afd2 = afd2
    
    def uniao(self,afdm: AutomatoFD):
        cont=0
        for i in self.afd1.estados:     #passa pela combinação de todos os estados
            for j in self.afd2.estados:
                if (self.afd1.estadoFinal(int(i)) or self.afd2.estadoFinal(int(j))): #quando qualquer um dos estados são finais
                    afdm.mudaEstadoFinal(cont, True)    #estado do AFD equivalente à combinação vira estado final 
                cont+=1 
   

    def intercessao(self,afdm: AutomatoFD):
        cont=0
        for i in self.afd1.estados:         #passa pela combinação de todos os estados
            for j in self.afd2.estados:
                if (self.afd1.estadoFinal(i) and self.afd2.estadoFinal(j)): #quando ambos são finais
                    afdm.mudaEstadoFinal(cont, True)    #estado do AFD equivalente à combinação vira estado final 
                cont+=1
       

    def complemento(self,afdc: AutomatoFD):
        for i in afdc.estados:    #passa por todos estadoos de um AFD
            if(afdc.estadoFinal(i)):            #se estado é final
                afdc.mudaEstadoFinal(i, False)  #estado passa a não ser final
            else:                               #se não era final
                afdc.mudaEstadoFinal(i, True)   #estado passa a ser final

    def diferenca(self,afdm: AutomatoFD):
        cont=0
        for i in self.afd1.estados:          #passa pela combinação de todos os estados
            for j in self.afd2.estados:                                           #se estado do primeiro AFD for final
                if (self.afd1.estadoFinal(i) and not self.afd2.estadoFinal(j)):   #e estado do segundo AFD não for final
                    afdm.mudaEstadoFinal(cont, True)    #estado do AFD equivalente à combinação vira estado final 
                cont+=1 