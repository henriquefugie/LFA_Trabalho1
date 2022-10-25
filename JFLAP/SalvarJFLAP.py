import xml.etree.cElementTree as ETc
from AutomatoFD import AutomatoFD

class SalvarJFLAP(AutomatoFD):
    
    def __init__(self, afd : AutomatoFD, caminho, nome):
        self.afd1 = afd
        self.caminho1 = caminho
        self.nome1 = nome

    def salvarAFD(self):
        
        arquivo = open(self.nome1 + ".jff", "w")
        print(self.afd1)
        print('testando')
        root = ETc.Element("structure")
        ETc.SubElement(root, "type").text = "fa"
        doc = ETc.SubElement(root, "automaton")
        for e in self.afd1.estados:
            sub =  ETc.SubElement(doc, "state", id=str(e), name=str(e+1))
            if e == self.afd1.inicial:
                ETc.SubElement(sub,"initial")
            if self.afd1.estadoFinal(int(e)):
                ETc.SubElement(sub, "final")
        for (e, a) in self.afd1.transicoes.keys():
            tran = ETc.SubElement(doc, "transition")
            d = self.afd1.transicoes[(e, a)]
            ETc.SubElement(tran, "from").text = str(e)
            ETc.SubElement(tran, "to").text = str(d)
            ETc.SubElement(tran, "read").text = str(a)
        tree = ETc.ElementTree(root)

        tree.write("{}.jff".format(self.caminho) ,encoding='utf8', method='xml', short_empty_elements=True)