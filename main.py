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
    nomeAfd1 = input("Digite o nome do arquivo do primeiro automato: ")
    leitura = LerJFLAP(nome = nomeAfd1)
    afd1 = leitura.lerAFD()
    
    nomeAfd2 = input("Digite o nome do arquivo do primeiro automato: ")
    leitura = LerJFLAP(nome = nomeAfd2)
    afd2 = leitura.lerAFD()
    
    print("\nAutomatos lidos:\n", afd1, "\n\n",afd2, "\n")

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
            automatoDestino = input("Digite o nome do arquivo em que deseja salvar o automato: ")
            salvar = SalvarJFLAP(afd= afdm, nome = automatoDestino)
            salvar.salvarAFD()
            print('Automato salvo com sucesso')
            
            
        elif x==2:
            opera.intercessao(afdm=afdm)
            print(afdm)
            automatoDestino = input("Digite o nome do arquivo em que deseja salvar o automato: ")
            salvar = SalvarJFLAP(afd= afdm, nome = automatoDestino)
            salvar.salvarAFD()
            print('Automato salvo com sucesso')
            
        elif x==3:
            opera.complemento(afdc=afd1)
            print(afd1)
            automatoDestino = input("Digite o nome do arquivo em que deseja salvar o automato: ")
            salvar = SalvarJFLAP(afd= afd1, nome = automatoDestino)
            salvar.salvarAFD()
            print('Automato salvo com sucesso')
            
            
        elif x==4:    
            opera.diferenca(afdm=afdm)
            print(afdm)
            automatoDestino = input("Digite o nome do arquivo em que deseja salvar o automato: ")
            salvar = SalvarJFLAP(afd= afdm, nome = automatoDestino)
            salvar.salvarAFD()
            print('Automato salvo com sucesso')
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
            leitura = LerJFLAP(nome = nomeMin)
            afdLido = leitura.lerAFD()
            print("\nAutomato lido: ", afdLido)
            minimizar = MinimizaAFD(afdLido)
            afdMin = minimizar.minimizaAFD()
            print("\nAutomato minimizado: ", afdMin)
            
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


    # salvar1 = SalvarJFLAP(afd = afd1, caminho = "./JFLAP/Exemplos/", nome = "teste1")
    # salvar1.salvarAFD()
    # print('automato salvo!')