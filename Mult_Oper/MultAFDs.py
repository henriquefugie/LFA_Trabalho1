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
            print('Automatos possuem alfabeto diferentes') #verifica se AFDs possuem mesmo alfabeto
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
                est['afd2']=j       #salva id dos AFDs em um dicionario
                estados.append(est.copy()) #cria um lista com o dicionario
                #dessa forma se cria uma especie de coordenada dos estados antigos no AFD resultante da multiplicação
                 
                #Verifica se é Estado Inicial
                if i==self.afd1.inicial and j==self.afd2.inicial: #caso estado seja representado pelos estados iniciais antigos
                    afdm.criaEstado(cont,True)                    #se cria o estado inicial do AFD resultante
                else:
                    afdm.criaEstado(cont)               #senão, apenas se cria um novo estado
                cont+=1    
        #Cria Transições
        for a in afdm.alfabeto:     #loop que passa por todos os caracteres do alfabeto,
                                    #criando as transições de todos os estados para tal caracter
            
            cont=0  #salva estado atual
            for e in estados:  #Passa por todos os estados fazendo a transição de cada um
                contpos=0;
                pos1=pos2=0  #guarda coordenada do destino da transição
                for v in e.values(): # V recebe id do estado de origem dos AFDs antigos
                    
                    if contpos==0:  #primeiro V recebe coordenada do estado no primeiro AFD
                        
                        pos1=self.afd1.transicoes[(v,a)]   #retorna destino do estado no primeiro AFD de acordo com caracter
                        
                        contpos+=1 #adiciona contador para mudar destino do segundo valor
                        
                    else:    #Segundo V recebe coordenada do estado segundo AFD
                        
                        pos2=self.afd2.transicoes[(v,a)]  #retorna destino do estado no segundo AFD de acordo com caracter
                        
                est['afd1']=pos1  #cria uma variavel que recebe as coordenadas de destino,
                est['afd2']=pos2  #e as formata para comparar com a lista de estados

                i=0
                while i < estados.__len__(): #passa por todos estados e encontra estado com coordenadas procurada
                    if (estados[i]==est):
                        afdm.criaTransicao(cont,i,a)  #cria transição do estado Atual para o estado destino
                        break
                    i+=1
                        
                cont+=1        
            
        return afdm     #retorna AFD resultante,  estados finais serão verificados de acordo com a operação

