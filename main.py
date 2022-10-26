from AutomatoFD import *
from JFLAP.SalvarJFLAP import SalvarJFLAP
from JFLAP.LerJFLAP import LerJFLAP

if __name__ == '__main__':

    afd = AutomatoFD('ab')

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
    
    salvar1 = SalvarJFLAP(afd = afd, caminho = "./JFLAP/Exemplos/", nome = "automatoteste")
    salvar1.salvarAFD()
    print('automato salvo!')
    
    leitura = LerJFLAP(caminho = "./JFLAP/Exemplos/ComecaComAB.jff")
    afd = leitura.lerAFD()
    print(afd)
    print('automato lido')
    
