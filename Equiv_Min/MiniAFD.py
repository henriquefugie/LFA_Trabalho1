from itertools import count
from AutomatoFD import AutomatoFD
from Equiv_Min.EquivAFDs import EquivalenciaAFD

class MinimizaAFD():
    
    def __init__(self, afd: AutomatoFD):
         self.afd = afd
        
    def minimizaAFD(self):
        
        #para fazer o processo de minimizacao, o automato, ele precisa ser um afd, ele não pode ter estados inacessiveis e o automato deve ser completo
        self.removerEstadosInacessiveis()
        
        equivalente = EquivalenciaAFD(self.afd)
        estadosEqui = equivalente.estadosEquiv()
        for (x, y) in estadosEqui.keys():
            v = estadosEqui[(x, y)]
            
            #ele vai receber os estados equivalentes que estão em True e caso seja True, ele vai eliminar um dos estados, no caso o da direita
            if(v):
                
                #este for é utilizado para percorrer as transicoes e recebe o destino da transicao, caso o destino seja igual ao estado que sera eliminado, ele vai alterar o destino para o outro estado equivalente
                for (e, a) in  self.afd.transicoes.keys():
                    d =  self.afd.transicoes[(e, a)]
                    if(d == y):
                         self.afd.transicoes[(e, a)] = x
                         
                #Este for é utilizado para remover as transicoes que estavam ligadas ao estado que foi eliminado e no final elimina o estado
                for a in  self.afd.alfabeto:
                  del self.afd.transicoes[(y,a)]
                
                self.afd.estados.remove(y)
        
        #por o automato minimizado
        return self.afd
    
    def removerEstadosInacessiveis(self):
        
        #armazena os estados totais na variavel y e atraves de outra variavel x, ele percorre por todas as variaveis
        y = len(self.afd.estados)
        for x in range(y):
            count = 0
            
            #atraves deste for que percorre todas as transicoes, ele verifica se possui algum destino ou origem igual ao estado que esta sendo analisado no momento
            for (i,a) in self.afd.transicoes.keys():
                d = self.afd.transicoes[(i, a)]
                
                #caso possua algum estado com o valor igual, é adicionado um ao contador
                if(x == d or x == i):
                    count +=1
                
            #o contador é utilizado para verificar se o estado possui alguma transicao, saindo dele ou chegando nele, caso nao tenha, o estado é eliminado
            if(count == 0):
                  self.afd.estados.remove(x)                  