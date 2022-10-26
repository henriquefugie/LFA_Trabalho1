from AutomatoFD import *
from JFLAP.SalvarJFLAP import SalvarJFLAP
from JFLAP.LerJFLAP import LerJFLAP

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
    
    salvar1 = SalvarJFLAP(afd = afd1, caminho = "./JFLAP/Exemplos/", nome = "testando123")
    salvar1.salvarAFD()
    print('automato salvo!')
    
    leitura = LerJFLAP(caminho = "./JFLAP/Exemplos/ComecaComAB.jff")
    afd1 = leitura.lerAFD()
    print(afd1)
    print('automato lido')
    
