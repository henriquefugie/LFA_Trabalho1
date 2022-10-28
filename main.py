from AutomatoFD import *
from Equiv_Min.EquivAFDs import EquivalenciaAFDs
from Equiv_Min.EquivAFDs import EquivalenciaAFD
from Equiv_Min.MiniAFD import MinimizaAFD
from JFLAP.SalvarJFLAP import SalvarJFLAP
from JFLAP.LerJFLAP import LerJFLAP
from Mult_Oper.Operacoes import Operacoes
from Mult_Oper.MultAFDs import MultAFDs

def copiaAFD(self):
    afdcopia = self
    return afdcopia

def menuOperacoes():
    afd2 = AutomatoFD('ab')
    afd1 = AutomatoFD('ab')

    for i in range(0, 2):
        afd2.criaEstado(i)
    afd2.mudaEstadoInicial(0)
    afd2.mudaEstadoFinal(0, True)
    afd2.criaTransicao(0, 1, 'a')
    afd2.criaTransicao(1, 0, 'a')
    afd2.criaTransicao(1, 1, 'b')
    afd2.criaTransicao(0, 0, 'b')
    
    print(afd2)

    

    for i in range(0, 4):
        afd1.criaEstado(i)
    afd1.mudaEstadoInicial(0)
    afd1.mudaEstadoFinal(2, True)
    afd1.mudaEstadoFinal(1, True)
    afd1.mudaEstadoFinal(0, True)
    afd1.criaTransicao(0, 1, 'b')
    afd1.criaTransicao(0, 0, 'a')
    afd1.criaTransicao(1, 2, 'a')
    afd1.criaTransicao(1, 1, 'b')
    afd1.criaTransicao(2, 3, 'b')
    afd1.criaTransicao(2, 0, 'a')
    afd1.criaTransicao(3, 3, 'a')
    afd1.criaTransicao(3, 3, 'b')
    print(afd1)

    while 1:
        
        opera=Operacoes(afd1=afd1,afd2=afd2)
        multi=MultAFDs(afd1=afd1,afd2=afd2)
        afdm=multi.multiplicaAFD()

        print("\n"+"="*20+"\nOPEREÇÕES\n"+"="*20+"\n1 - União\n2 - Intercessão\n"
              +"3 - Complemento\n4 - Diferença\n0 - Voltar")
        x=int(input("Digite uma opção: "))     
        print("\n"+"-"*20+"\n")

        
        if x==1:
            opera.uniao(afdm=afdm)
            print(afdm)
        elif x==2:
            opera.intercessao(afdm=afdm)
            print(afdm)
        elif x==3:
            opera.complemento(afdc=afd1)
            print(afd1)
        elif x==4:    
            opera.diferenca(afdm=afdm)
            print(afdm)
        elif x==0:
            return
        else:
            print("\nOpção inválida")    

    
if __name__ == '__main__':

    while 1: 
        print("\n"+"="*20+"\nMenu de Opções\n"+"="*20+"\n1 - Minimizar AFD\n"
              +"2 - Verificar equivalencia entre AFDs \n3 - Verificar equivalencia de estados de um AFD\n4 - Copiar Automato\n5 - Operações com AFD\n0 - Sair")
        x=int(input("Digite uma opção: "))
        print("\n"+"-"*30+"\n")

        if x==1:
            
            nomeMin = input("Digite o nome do arquivo do automato que deseja minimizar: ")
            nomeMinzado = input("Digite o nome do arquivo do automato minimizado que sera salvo: ")
            leitura = LerJFLAP(nome = nomeMin)
            afdLido = leitura.lerAFD()
            print("\nAutomato lido: ", afdLido)
            minimizar = MinimizaAFD(afdLido)
            afdMin = minimizar.minimizaAFD()
            print("\nAutomato minimizado: ", afdMin)
            salvar = SalvarJFLAP(afd= afdMin, nome = nomeMinzado)
            salvar.salvarAFD()
            print("Arquivo copiado com sucesso")
            
        elif x==2:
            
            nomeEquivAFD = input("Digite o nome do arquivo do primeiro automato para conferir a equivalencia: ")
            leitura = LerJFLAP(nome = nomeEquivAFD)
            afdLido = leitura.lerAFD()
            afdA = afdLido
            
            nomeEquivAFD = input("Digite o nome do arquivo do segundo automato para conferir a equivalencia: ")
            leitura = LerJFLAP(nome = nomeEquivAFD)
            afdLido = leitura.lerAFD()
            afdB = afdLido
            print("\nAutomatos lidos:\n", afdA, "\n\n",afdB, "\n")
            
            equivalenciaAFDs = EquivalenciaAFDs(afd1 = afdA, afd2 = afdB)
            equivalenciaAFDs.EquivalenciaEntreAFDs()
            
        elif x==3:
            
            nomeEquivAFD = input("Digite o nome do arquivo do automato que deseja verificar a equivalencia: ")
            leitura = LerJFLAP(nome = nomeEquivAFD)
            afdLido = leitura.lerAFD()
            print("\nAutomato lido: ", afdLido)
            equivalencia = EquivalenciaAFD(afdLido)
            afdEquiv = equivalencia.estadosEquiv()
            print("\nTabela de equivalencia do AFD: ")
            for (x, y) in afdEquiv.keys():
                v = afdEquiv[(x, y)]
                print("({} e {})-->{}, ".format(x, y, v))    
                
        elif x==4:
            automatoOrigem = input("Digite o nome do arquivo do automato que Copiar: ")
            automatoDestino = input("Digite o nome do arquivo que deseja salvar o automato copiado: ")
            leitura = LerJFLAP(nome = automatoOrigem)
            afdLido = leitura.lerAFD()
            afdCopiado = copiaAFD(afdLido)
            salvar = SalvarJFLAP(afd= afdCopiado, nome = automatoDestino)
            salvar.salvarAFD()
            print("Arquivo copiado com sucesso")
        elif x==5:
            menuOperacoes()
        elif x==0:
            print("\nFinalizando...")
            break
        else:
            print("\nOpção inválida")