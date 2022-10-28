import xml.etree.ElementTree as ETc
from AutomatoFD import AutomatoFD

#código copiado para apenas arrumar a endentacao do arquivo .jff para melhorar a visualizacao do arquivo
def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
            
class SalvarJFLAP():
    
    def __init__(self, afd : AutomatoFD, nome):
        self.afd = afd
        self.nome = nome
        
    def salvarAFD(self):
        
        #separa o arquivo jff em estrutura, classifica em automato finito e faz o subelemento automaton
        root = ETc.Element("structure")
        ETc.SubElement(root, "type").text = "fa"
        doc = ETc.SubElement(root, "automaton")
        
        #constroe no arquivo.jff os estados presentes no automato
        for origem in self.afd.estados:
            sub =  ETc.SubElement(doc, "state", id=str(origem), name=str(origem))
            #condições que verificam se o estado que ele está salvando é final ou inicial ou nada
            if origem == self.afd.inicial:
                ETc.SubElement(sub,"initial")
            if self.afd.estadoFinal(int(origem)):
                ETc.SubElement(sub,"final")
                
        #constroe no arquivo.jff as transições presentes no automato
        for (origem, simbolo) in self.afd.transicoes.keys():
                    transicao = ETc.SubElement(doc, "transition")
                    destino = self.afd.transicoes[(origem, simbolo)]
                    ETc.SubElement(transicao, "from").text = str(origem)
                    ETc.SubElement(transicao, "to").text = str(destino)
                    ETc.SubElement(transicao, "read").text = str(simbolo)
        indent(root)
        tree = ETc.ElementTree(root)
        
        #adiciona a parte de cima do xml, onde tem a versão do xml, o encoding e o caminho do arquivo junto com o nome
        tree.write("{}.jff".format("./JFLAP/Exemplos/"+self.nome), encoding="UTF-8", method="xml", xml_declaration=True)