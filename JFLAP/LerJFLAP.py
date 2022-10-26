import xml.etree.ElementTree as ETc
from AutomatoFD import AutomatoFD

class LerJFLAP():
    
    def __init__(self,caminho):
        self.caminho = caminho
        
    def lerAFD(self):
        root = ETc.parse(str(self.caminho)).getroot()
        # ler alfabeto
        alfabeto = ''
        for type_tag in root.findall('automaton/transition'):
            simbolo = type_tag.find('read').text
            if len(simbolo) != 1 or not simbolo in alfabeto:
                alfabeto += simbolo

        # cria afd
        afd = AutomatoFD(alfabeto)
        # insere os estados
        for type_tag in root.findall('automaton/state'):
            id = type_tag.get('id')
            inicial = type_tag.find('initial')
            final = type_tag.find('final')
            afd.criaEstado(id)

            if inicial is not None:
                afd.mudaEstadoInicial(int(id))
            if final is not None:
                afd.mudaEstadoFinal(int(id), True)

        # cria as transições
        for type_tag in root.findall('automaton/transition'):
            origem = type_tag.find('from').text
            destino = type_tag.find('to').text
            simbolo = type_tag.find('read').text
            afd.criaTransicao(origem, destino, simbolo)
            
        return afd