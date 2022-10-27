from AutomatoFD import *
from JFLAP.SalvarJFLAP import SalvarJFLAP
from JFLAP.LerJFLAP import LerJFLAP
from Mult_Oper.MultAFDs import MultAFDs

def copiaAFD(self):
    afdcopia = self
    return afdcopia

def menuOperacoes():
    while 1:

        print("\n=====================\nOPEREÇÕES\n====================="
             +"\n1 - União\n2 - Intercessão\n3 - Complemento\n4 - Diferença\n0 - Voltar")
        x=int(input("Digite uma opção:"))     
        print("\n---------------------\n")

        if x==1:
            for i in range(0,afd.estados.__len__()):
                print(i)
            print("uniao")
        elif x==2:
            print("intercessao")

        elif x==3:
            print("complemento")

        elif x==4:    
            print("diferença")
        elif x==0:
            return
        else:
            print("\nOpção inválida")    

    
if __name__ == '__main__':

    
    afd = AutomatoFD('ab')
    afd1 = AutomatoFD('ab')

    for i in range(0, 6):
        afd.criaEstado(i)
    afd.mudaEstadoInicial(1)
    afd.mudaEstadoFinal(4, True)
    afd.criaTransicao(1, 2, 'a')
    afd.criaTransicao(2, 1, 'a')
    afd.criaTransicao(3, 4, 'a')
    afd.criaTransicao(4, 3, 'a')
    afd.criaTransicao(1, 3, 'b')
    afd.criaTransicao(2, 1, 'b')
    afd.criaTransicao(3, 4, 'b')
    afd.criaTransicao(4, 2, 'b')
    print(afd)

    

    for i in range(0, 3):
        afd1.criaEstado(i)
    afd1.mudaEstadoInicial(0)
    afd1.mudaEstadoFinal(2, True)
    afd1.criaTransicao(0, 1, 'a')
    afd1.criaTransicao(1, 2, 'b')
    afd1.criaTransicao(2, 2, 'a')
    afd1.criaTransicao(2, 2, 'b')
    print(afd1)

    afd3=MultAFDs.multiplicaAFD()


    while 1: 
        print("\n=====================\nMenu de Opções\n====================="
             +"\n1-Minimizar AFD\n2-Operações com AFD\n0-Sair")
        x=int(input("Digite uma opção:"))
        print("\n---------------------\n")

        if x==1:
            #programa ai fugie
            print("minimo")
        elif x==2:
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
    
