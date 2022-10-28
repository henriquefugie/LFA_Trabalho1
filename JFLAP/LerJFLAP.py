import xml.etree.ElementTree as ETc
from AutomatoFD import AutomatoFD

class LerJFLAP():
    
    def __init__(self,nome):
        self.nome = nome
        
    def lerAFD(self):
        root = ETc.parse(str("./JFLAP/Exemplos/"+self.nome+".jff")).getroot()
        alfabeto = ''
        #cria um loop que verifica se a letra encontrada no read, onde no jflap são as transições, está presente no alfabeto, caso não esteja, ele adiciona
        for type_tag in root.findall('automaton/transition'):
            simbolo = type_tag.find('read').text
            if len(simbolo) != 1 or not simbolo in alfabeto:
                alfabeto += simbolo

        #cria o afd recolhendo os estados, atravez do state e recebe tambem o id do estado classificando tambem se ele é final ou inicial ou não através da tag initial ou final
        alfabetoOrd=''
        alfabetoOrd=sorted(alfabeto)
        novoAlfabeto = ''.join(alfabetoOrd)
        afd = AutomatoFD(novoAlfabeto)
        for type_tag in root.findall('automaton/state'):
            id = type_tag.get('id')
            inicial = type_tag.find('initial')
            final = type_tag.find('final')
            afd.criaEstado(id)

            if inicial is not None:
                afd.mudaEstadoInicial(int(id))
            if final is not None:
                afd.mudaEstadoFinal(int(id), True)

        #recebe as transicoes procurando em todas as tags transition e recebem ao rigem da transicao, como o destino e o simbolo que ele vai receber
        for type_tag in root.findall('automaton/transition'):
            origem = type_tag.find('from').text
            destino = type_tag.find('to').text
            simbolo = type_tag.find('read').text
            afd.criaTransicao(origem, destino, simbolo)
            
        return afd