from AutomatoFD import *
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
        x=int(input("Digite uma opção:"))     
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
              +"2 - Vericar equivalencia entre AFDs \n3 - Operações com AFD\n0 - Sair")
        x=int(input("Digite uma opção:"))
        print("\n"+"-"*30+"\n")

        if x==1:
            #programa ai fugie
            print("minimo")
        elif x==2:
            print("equivalente")    
        elif x==3:
            menuOperacoes()
        elif x==0:
            print("\nFinalizando...")
            break
        else:
            print("\nOpção inválida")


    # salvar1 = SalvarJFLAP(afd = afd1, caminho = "./JFLAP/Exemplos/", nome = "teste1")
    # salvar1.salvarAFD()
    # print('automato salvo!')
    
    # leitura = LerJFLAP(caminho = "./JFLAP/Exemplos/ComecaComAB.jff")
    # afd1 = leitura.lerAFD()
    # print(afd1)
    # print('automato lido')
    
